import boto3

from us_visa.configuration.aws_connection import S3Client
from io import StringIO
from typing import Union, List
import os, sys
from us_visa.logger import logging
# from boto3.resources.factory import Bucket

from mypy_boto3_s3.service_resource import Bucket
from us_visa.exception import USvisaException
from botocore.exceptions import ClientError
from pandas import DataFrame, read_csv
import pickle


class SimpleStorageService:

    def __init__(self):
        s3_client = S3Client()
        self.s3_resource = s3_client.s3_resource
        self.s3_client = s3_client.s3_client

    def s3_key_path_available(self, bucket_name: str, s3_key: str) -> bool:
        try:
            bucket = self.get_bucket(bucket_name)
            file_objects = [file_object for file_object in bucket.objects.filter(Prefix=s3_key)]
            return len(file_objects) > 0
        except Exception as e:
            raise USvisaException(e, sys)

    @staticmethod
    def read_object(object_name: str, decode: bool = True, make_readable: bool = False) -> Union[StringIO, str]:
        """
        Reads the S3 object content.

        :param object_name: The S3 object name (key).
        :param decode: If True, decodes the object bytes to a string.
        :param make_readable: If True, returns the content as a readable StringIO object.
        :return: The content of the S3 object.
        """
        logging.info("Entered the read_object method of S3Operations class")
        try:
            func = lambda: object_name.get()["Body"].read().decode() if decode else object_name.get()["Body"].read()
            content = func()
            return StringIO(content) if make_readable else content
        except Exception as e:
            raise USvisaException(e, sys) from e



    def get_bucket(self, bucket_name: str) -> Bucket:
        """
        Returns the S3 bucket object.

        :param bucket_name: The name of the S3 bucket.
        :return: The bucket object.
        """
        logging.info("Entered the get_bucket method of S3Operations class")
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            logging.info("Exited the get_bucket method of S3Operations class")
            return bucket
        except Exception as e:
            raise USvisaException(e, sys) from e

    def get_file_object(self, filename: str, bucket_name: str) -> Union[List[object], object]:
        """
        Returns the S3 file object(s) from the bucket.

        :param filename: The file name or prefix in S3.
        :param bucket_name: The name of the S3 bucket.
        :return: S3 object(s).
        """
        logging.info("Entered the get_file_object method of S3Operations class")
        try:
            bucket = self.get_bucket(bucket_name)
            file_objects = [file_object for file_object in bucket.objects.filter(Prefix=filename)]
            return file_objects[0] if len(file_objects) == 1 else file_objects
        except Exception as e:
            raise USvisaException(e, sys) from e

    def load_model(self, model_name: str, bucket_name: str, model_dir: str = None) -> object:
        """
        Loads a model from S3.

        :param model_name: The name of the model file in S3.
        :param bucket_name: The name of the S3 bucket.
        :param model_dir: The directory in S3 where the model is stored.
        :return: The loaded model object.
        """
        logging.info("Entered the load_model method of S3Operations class")
        try:
            model_file = model_name if model_dir is None else f"{model_dir}/{model_name}"
            file_object = self.get_file_object(model_file, bucket_name)
            model_obj = self.read_object(file_object, decode=False)
            model = pickle.loads(model_obj)
            logging.info("Exited the load_model method of S3Operations class")
            return model
        except Exception as e:
            raise USvisaException(e, sys) from e

    def create_folder(self, folder_name: str, bucket_name: str) -> None:
        """
        Creates a folder in an S3 bucket.

        :param folder_name: The name of the folder to create.
        :param bucket_name: The name of the S3 bucket.
        """
        logging.info("Entered the create_folder method of S3Operations class")
        try:
            self.s3_resource.Object(bucket_name, folder_name).load()
        except ClientError as e:
            if e.response["Error"]["Code"] == "404":
                folder_obj = folder_name + "/"
                self.s3_client.put_object(Bucket=bucket_name, Key=folder_obj)
            logging.info("Exited the create_folder method of S3Operations class")

    def upload_file(self, from_filename: str, to_filename: str, bucket_name: str, remove: bool = True):
        """
        Uploads a file to an S3 bucket.

        :param from_filename: The local filename to upload.
        :param to_filename: The S3 key (destination filename).
        :param bucket_name: The name of the S3 bucket.
        :param remove: If True, deletes the local file after upload.
        """
        logging.info("Entered the upload_file method of S3Operations class")
        try:
            logging.info(f"Uploading {from_filename} to {to_filename} in {bucket_name} bucket")
            self.s3_resource.meta.client.upload_file(from_filename, bucket_name, to_filename)
            if remove:
                os.remove(from_filename)
                logging.info(f"Deleted local file {from_filename}")
            logging.info("Exited the upload_file method of S3Operations class")
        except Exception as e:
            raise USvisaException(e, sys) from e

    def upload_df_as_csv(self, data_frame: DataFrame, local_filename: str, bucket_filename: str, bucket_name: str) -> None:
        """
        Uploads a DataFrame as a CSV to an S3 bucket.

        :param data_frame: The DataFrame to upload.
        :param local_filename: The local file to create before upload.
        :param bucket_filename: The destination file in S3.
        :param bucket_name: The name of the S3 bucket.
        """
        logging.info("Entered the upload_df_as_csv method of S3Operations class")
        try:
            data_frame.to_csv(local_filename, index=False)
            self.upload_file(local_filename, bucket_filename, bucket_name)
            logging.info("Exited the upload_df_as_csv method of S3Operations class")
        except Exception as e:
            raise USvisaException(e, sys) from e

    def get_df_from_object(self, object_: object) -> DataFrame:
        """
        Converts an S3 object to a pandas DataFrame.

        :param object_: The S3 object to convert.
        :return: The DataFrame.
        """
        logging.info("Entered the get_df_from_object method of S3Operations class")
        try:
            content = self.read_object(object_, make_readable=True)
            df = read_csv(content, na_values="na")
            logging.info("Exited the get_df_from_object method of S3Operations class")
            return df
        except Exception as e:
            raise USvisaException(e, sys) from e

    def read_csv(self, filename: str, bucket_name: str) -> DataFrame:
        """
        Reads a CSV file from an S3 bucket into a pandas DataFrame.

        :param filename: The name of the file in S3.
        :param bucket_name: The name of the S3 bucket.
        :return: The pandas DataFrame.
        """
        logging.info("Entered the read_csv method of S3Operations class")
        try:
            csv_obj = self.get_file_object(filename, bucket_name)
            df = self.get_df_from_object(csv_obj)
            logging.info("Exited the read_csv method of S3Operations class")
            return df
        except Exception as e:
            raise USvisaException(e, sys) from e
