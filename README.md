# mlops_US_visa_approved_proj 

# MLOps Production-Ready Machine Learning Project



## 📚 Tools and Resources

Tools Used in the Project
Anaconda – Environment management
VS Code – Code editor
Git – Version control
Whimsical – Flowchart creation
Evidently AI – MLOps monitoring tool
MongoDB – Database
Kaggle – Dataset source
Docker – Containerization
GitHub Actions – CI/CD pipeline
AWS – Cloud deployment (EC2, ECR)

## 🚀 Git Commands
```bash
git add .
git commit -m "Updated"
git push origin main



# Create and activate environment
conda create -n visa python=3.8 -y
conda activate visa

# Install dependencies
pip install -r requirements.txt


export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net"
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> 


AWS CI/CD Deployment with GitHub Actions
Steps:
Login to AWS Console.

Create IAM User with:

EC2 Access (Virtual Machine)
ECR Access (Elastic Container Registry)
Deployment Process:

Build Docker image.
Push Docker image to ECR.
Launch EC2 instance.
Pull and run Docker image in EC2.
Required Policies:
AmazonEC2ContainerRegistryFullAccess
AmazonEC2FullAccess
Docker Setup on EC2: 


sudo apt-get update -y
sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker






Configure EC2 as Self-Hosted Runner:
GitHub:
Settings > Actions > Runners > New Self-Hosted Runner
Follow on-screen commands.
GitHub Secrets Setup:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO 




## 🚀 Project Setup Instructions

### 1. Flowchart Creation
- Used **Whimsical** to design the project flowchart.  

### 2. Initial Project Structure
- **Template Setup**: Created `template.py` to define the skeleton of the project.
- **Dependencies**: Listed all required packages in `requirements.txt`.  
  - Using `-e .` to install the project as a package (`us_visa`).  

### 3. Python Environment Setup
```bash
conda create -n visa python=3.11 -y
conda activate visa




Created a MongoDB project and cluster (Cluster0).
Set username & password: jayraj#$%959354.
Allowed public IP access: Allow from Anywhere.
Connection String:
plaintext
Copy code
mongodb+srv://jayraj24*&*:jayraj2_*98@cluster0.a78lp.mongodb.net/?retryWrites=true& 






## Data Ingestion Process

A. **Data Ingestion**: Getting data from MongoDB  
In this project, we used modular coding to connect to MongoDB and fetch data. Initially, we did this through a notebook, but later transitioned it into modular coding for better maintainability and scalability.

### Steps to Connect MongoDB:
1. **MongoDB Connection**:  
   With the help of the connection string, we connect to MongoDB, fetch the required data, and proceed with the data ingestion pipeline.

2. **Flowchart**:  
   The flow of data ingestion can be understood by looking at the `data_ingestion.png` flowchart. It visually explains how data flows through various stages of the ingestion process.

3. **Helper Constants**:  
   Constants are used to define paths and parameters. These include:
   - `data_ingestion_dir`
   - `feature_store_file_path`
   - `training_file_path`
   - `testing_file_path`
   - `train_test_split_ratio`
   - `collection_name`

   These constants are crucial as they define the local machine paths where the data will be stored after ingestion.

4. **Artifact Generation**:  
   Artifacts refer to the generated outputs after executing the data ingestion process:
   - `feature_store`: `usvisa.csv`
   - `ingested`: `train.csv` and `test.csv`

### 1. **Constant Variables**:
   Constant variables are set to easily update values throughout the codebase. If we need to change the database name or paths, we only need to change them in the constants file.

   Example constants in the **Data Ingestion Pipeline**:
   - `MONGODB_URL_KEY = "MONGODB_URL"` (Connection string set as an environment variable for security)

   For environment variable management:
   - In Windows, create a system environment variable for MongoDB URL using the `os` package to load the variable.

### 2. **Entity Folder**:

#### Config Entity:
   The **config_entity** manipulates constants (like file paths) to ensure data is processed correctly. It ensures proper paths are set for storing data, and after the data ingestion process, we obtain:
   - `train.csv`
   - `test.csv`

#### Artifact Entity:
   After data ingestion, we generate artifacts (`train.csv` and `test.csv`), which serve as input for the next component, Data Validation. This process helps in ensuring the data is valid and correctly formatted.

   **Artifact flow**: Data from the data ingestion component is passed as input to other components (data validation, data transformation, model training, etc.).

   Configuration for MongoDB connection is written in `mongo_db_connection.py`. This separation ensures better maintainability and readability, instead of keeping all logic in one file.

### 3. **Component Folder**:
   In this folder, we define classes and methods to carry out the data ingestion process:
   - **DataIngestionConfig**: Initializes paths and other necessary constants for ingestion.
   - **export_data_into_feature_store()**: Saves the data as `usvisa.csv` in the feature store folder.
   - **split_data_as_train_test()**: Splits data into training and testing sets, and saves them as `train.csv` and `test.csv`.
   - **initiate_data_ingestion()**: Initializes the data ingestion process and returns the artifact that can be passed to the next pipeline stage.

### 4. **Pipeline**:
   There are two pipelines: **Training Pipeline** and **Prediction Pipeline**. In this project, we use the **Training Pipeline**.

   The pipeline initializes all methods within the data ingestion component, which automates the entire process.

   **DataIngestionArtifact** is used to store paths for `train.csv` and `test.csv`. The training pipeline calls the `initiate_data_ingestion()` function, which returns the artifact, making the process seamless.

   The final step inside the pipeline is the `run_pipeline()` function, which executes all components of the pipeline in a structured manner.

### 5. **Main File**:
   The main file serves as the entry point for running the entire pipeline. It will trigger the components and initiate the workflow.

---

### Final Output:
- **Artifact Folder**:
  - The artifact folder is created with a timestamp folder inside it, containing subfolders:
    - **Data_Ingestion Folder**:
      - `feature_store`: Contains `usvisa.csv`
      - `ingested`: Contains `train.csv` and `test.csv`






# Data Validation Pipeline

This section outlines the Data Validation step in the pipeline, which ensures the integrity of the data before proceeding to Data Transformation.

## Overview

The **Data Validation** module performs the following key tasks:
1. **Column Validation**:
   - Checks if all required columns (numerical, categorical, and other necessary columns) are present in the dataset.
   - If any required columns are missing, a validation error is raised.
   
2. **Data Drift Detection**:
   - If the columns are valid, it checks for **data drift**, which occurs when the distribution of the data changes over time.
   - If data drift is detected, a validation error is raised.
   - If no drift is detected, a report is generated in `.yml` format.

The output of this validation step is the `DataValidationArtifact`, which includes the validation status and details for the next steps in the pipeline.

## Data Validation Output

The following details are captured in the **Data Validation Artifact**:
- **validation_status**: `True` or `False`, indicating if the data is valid.
- **message**: A message indicating whether data drift was detected or not.
- **valid_train_file_path**: Path to the valid training file.
- **valid_test_file_path**: Path to the valid test file.
- **invalid_train_file_path**: Path to the invalid training file.
- **invalid_test_file_path**: Path to the invalid test file.
- **drift_report_file_path**: Path to the drift report (in `.yml` format).

This artifact is passed to the **Data Transformation** step for further processing.

## Workflow

### 1. **Constant Configuration**:
   - The constants related to data validation are stored in the `constant.py` file.
   - Example entries:
     - Columns to validate (numerical, categorical, drop columns).
     - Paths for the output validation files.

### 2. **Schema Definition** (`schema.yml`):
   - The `schema.yml` file defines the columns, data types, and transformations to apply.
   - Example:
     ```yaml
     columns:
       - case_id
       - continent
       - education_of_employee
       - ...
     num_features: [no_of_employees, prevailing_wage]
     categorical_columns: [continent, education_of_employee]
     ```

### 3. **Entity**:
   - Define the `DataValidationArtifact` class to store the validation results.
   - Example:
     ```python
     class DataValidationArtifact:
         validation_status: bool
         message: str
         drift_report_file_path: str
     ```

### 4. **Component** (`data_validation.py`):
   - Methods to implement the validation logic:
     - `validate_number_of_columns()`: Validates the number of columns in the dataframe.
     - `is_column_exist(df: DataFrame)`: Checks if the required columns (both numerical and categorical) exist in the dataframe.
     - `detect_dataset_drift(reference_df: DataFrame, current_df: DataFrame)`: Detects data drift between the reference and current datasets. The output is saved in JSON format.

   - Main validation function:
     ```python
     def initiate_data_validation() -> DataValidationArtifact:
         # Calls all validation methods and returns the DataValidationArtifact
     ```

### 5. **Pipeline Integration**:
   - The **Data Ingestion Artifact** is passed as input to the **Data Validation** component.
   - Example pipeline integration:
     ```python
     data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
     ```

### 6. **Final Output**:
   - The artifact is saved in a timestamped folder inside the `data_validation` folder.
   - Final folder structure:
     ```
     Artifact Folder/
     ├── Timestamp Folder/
     │   └── data_validation/
     │       └── drift_report/
     │           └── report.yml
     ```

## Next Steps

Once the Data Validation step completes, the next task in the pipeline is **Data Transformation**, where feature engineering and transformations will be applied.

---

## Example File Structure




# Data Transformation Pipeline

The **Data Transformation** step in the pipeline applies necessary transformations to the data to make it ready for model training. This process involves feature engineering, scaling, encoding, handling imbalances, and saving the preprocessed data for later use.

## Overview

In the **Data Transformation** step, the following tasks are performed:

1. **Feature Engineering**:
   - We perform various transformations like **One-Hot Encoding**, **Ordinal Encoding**, **Standard Scaler**, **Power Transformer**, etc., as part of feature engineering.

2. **Imbalance Handling**:
   - The data is passed through **SMOTEEN** (Synthetic Minority Over-sampling Technique with Edited Nearest Neighbors) to handle class imbalance.

3. **Saving Preprocessed Data**:
   - After preprocessing, the data is saved in `.npy` (NumPy format) for both train and test datasets.
   - The preprocessing pipeline (transformations applied on the data) is saved as a **Pickle file** (`preprocessing.pkl`), which allows for consistent preprocessing of test data, the same way as the train data.

4. **Artifact Creation**:
   - The processed data and Pickle file are saved under a timestamped folder inside the `data_transformation` artifact directory.
   
## Data Transformation Output

After the transformation, the following outputs are generated:

- **Transformed Data**:
  - `train.npy` - The transformed training data (in NumPy format).
  - `test.npy` - The transformed test data (in NumPy format).
  
- **Transformed Objects**:
  - `preprocessing.pkl` - The Pickle file that contains the transformations applied to the data (including encoders and scalers).

These outputs are passed to the **Model Training** component for the next stage of the pipeline.

## Workflow

### 1. **Constant Configuration**:
   - Update the constants related to data transformation, such as file paths.
   - Example:
     - Create directories for transformed data and Pickle file in the `artifact` folder:
       ```
       artifact/
       ├── Timestamp Folder/
       │   └── data_transformation/
       │       ├── transformed/
       │       │   ├── train.npy
       │       │   └── test.npy
       │       └── transformed_object/
       │           └── preprocessing.pkl
       ```

### 2. **Entity**:
   - The **config entity** defines paths for the transformation constants.
   - The **artifact entity** holds the paths for the transformed data and the `preprocessing.pkl` file, which will be used in the next pipeline stage (Model Training).

### 3. **Component** (`data_transformation.py`):
   - The main class **DataTransformation** handles the following tasks:
     1. **Target Value Mapping**: The target column (`'certified' or 'denied'`) is mapped to numeric values for model compatibility.
     2. **Preprocessing**: The transformations like **One-Hot Encoding**, **Ordinal Encoding**, **Scaling**, etc., are applied to both the train and test datasets.
     3. **SMOTEEN**: Applied to handle class imbalance by creating synthetic examples of the minority class.
     4. **Saving Transformed Data**: The transformed data is saved in `.npy` format, and the preprocessing pipeline is saved as a `preprocessing.pkl` file.

   Example:
   ```python
   from us_visa.entity.estimator import TargetValueMapping
   from sklearn.preprocessing import OneHotEncoder, StandardScaler
   from imblearn.combine import SMOTEENN
   import pickle

   class DataTransformation:
       def __init__(self, config):
           # Initialize the paths and other parameters
           pass

       def target_value_mapping(self, df):
           # Apply target mapping
           pass

       def preprocess_data(self, df):
           # Apply encoding, scaling, transformations
           pass

       def handle_imbalance(self, df):
           # Apply SMOTEEN for imbalance
           pass

       def save_transformed_data(self, df_train, df_test):
           # Save transformed data as .npy files
           pass

       def save_preprocessing_object(self, preprocess_pipeline):
           # Save preprocessing object as pickle file
           pass

       def initiate_data_transformation(self, data_validation_artifact):
           # Perform all data transformation tasks
           pass




artifact/
├── Timestamp Folder/
│   └── data_transformation/
│       ├── transformed/
│       │   ├── train.npy
│       │   └── test.npy
│       └── transformed_object/
│           └── preprocessing.pkl






# Model Trainer Pipeline

The **Model Trainer** step in the pipeline automates model training, hyperparameter tuning, and evaluation of classification models. It focuses on selecting the best model based on performance metrics and ensuring the model is ready for production deployment.

## Overview

In the **Model Trainer** step, the following tasks are performed:

1. **Model Training**:
   - The step automates model training using multiple classification models. It performs **hyperparameter tuning** to improve model performance using the `neuromf` library.

2. **Model Evaluation**:
   - The model is evaluated using classification metrics such as **F1-score**, **Precision**, and **Recall**.
   - If the trained model performs better than the current production model, it is promoted to the evaluation model.

3. **Saving the Trained Model**:
   - The trained model is saved as `model.pkl` under the `trained_model` folder inside the `model_trainer` artifact directory.

4. **Model Configuration**:
   - The configuration for the model is saved in the `model.yaml` file. This includes hyperparameters, expected accuracy, and file paths for input and output.

## Data Flow

The **Model Trainer** component receives data from the previous step (Data Transformation) and processes it as follows:

- The preprocessed data (`train.npy` and `test.npy`) and preprocessing pipeline are loaded.
- Hyperparameter tuning is performed to select the best classification model.
- The trained model is saved as `model.pkl`, and classification evaluation metrics are computed.

## Final Output

After training, the following files are saved under the `artifact/` folder:





### **Classification Metrics** (e.g., F1-score, Precision, Recall) are saved as well for evaluation purposes.

---

## Workflow

### 1. **Constant Configuration**:
   - Update constants related to model training, such as file paths and expected accuracy.
   - Example:
     - Create directories for the trained model and model evaluation metrics in the `artifact` folder:
       ```
       artifact/
       ├── Timestamp Folder/
       │   └── model_trainer/
       │       └── trained_model/
       │           └── model.pkl
       ```

### 2. **Entity**:
   - **Config Entity**:
     - This entity stores paths for configuration files such as `trained_model_file_path`, `expected_accuracy`, and `model_config_file_path`.
   - **Artifact Entity**:
     - The artifact stores paths for the trained model (`model.pkl`) and classification metrics (e.g., F1-score, Precision, Recall).

   Example:
   ```python
   class ModelTrainerArtifact:
       trained_model_path: str
       classification_metrics_path: str





# US Visa Model Evaluation & Deployment

## Overview

This project is designed to evaluate and push machine learning models into AWS S3 storage for production deployment. The system evaluates a trained model, compares its performance against the production model, and pushes it to the S3 bucket if it meets the accuracy criteria. It automates the process of model evaluation, comparison, and deployment in a cloud environment.

## Project Workflow

1. **Model Evaluation**:
   - The trained model (`model.pkl`) is evaluated against the test dataset (`test.csv`).
   - The model's performance metrics such as accuracy, F1 score, precision, and recall are calculated.
   - If the accuracy exceeds a predefined threshold, the model is considered accepted.

2. **Model Pusher**:
   - If the new model's performance is better than the previous model in production, the new model is pushed to the AWS S3 bucket for use in production.

3. **AWS Integration**:
   - AWS credentials and configuration are set up to connect to the S3 bucket where models are stored.
   - The model is pushed to and pulled from S3 using `boto3`.

## File Structure




# US Visa Model Pusher to Production (Amazon S3)

## Overview

The Model Pusher component is responsible for pushing the final evaluated machine learning model to the cloud storage (Amazon S3) for production use. Once the model passes evaluation, it is uploaded to an S3 bucket, making it available for use in final prediction pipelines.

## File Structure Updates for Model Pusher

### 1. **Constants**
   - The Model Pusher does not require any new constants. The logic for pushing the model will rely on the configuration and artifact files defined in the entity and component sections.

### 2. **Entity**
   
#### **Config Entity:**
- **`USvisaPredictorConfig`**: 
  - Stores the configuration for the model file path and S3 bucket name.

#### **Artifact Entity:**
- **`ModelPusherArtifact`**: 
  - Contains the information regarding the bucket name and the S3 path where the model is uploaded.

### 3. **Component**
   
#### **`model_pusher.py`**:
   - This component contains the functionality to upload the final model to the Amazon S3 bucket.
   - The code will handle the connection to AWS and upload the `model.pkl` to the specified S3 bucket.

### 4. **Pipeline**

In the pipeline, we need to check whether the model has been accepted. If it has been accepted based on the evaluation metrics, we proceed with the model pushing process. Otherwise, the model will not be pushed.

### 5. **Final Production Model**
Once the model is pushed to the S3 bucket, it is now available for production usage. When performing predictions in the production environment, the model from S3 will be fetched and used to make predictions.

## Setup Instructions for Model Pusher

### 1. Install `boto3`
The `boto3` library is required to interact with AWS S3. Install it via:

```bash
pip install boto3




# US Visa Prediction Pipeline

## Overview

The Prediction Pipeline allows users to input data, which will be processed and used for making predictions based on the final trained model. This pipeline is the core functionality that enables the deployment of the model for real-time use. The user will pass data (with respect to various input columns), and the pipeline will predict the outcome using the model stored in Amazon S3.

## File Structure Updates for Prediction Pipeline

### 1. **Constants**

The following constants are updated for the prediction service configuration:

- **`APP_HOST`**: The host address for the web application.
- **`APP_PORT`**: The port number for the web application.

### 2. **Config Entity**

In the `config_entity.py`, we define the following configuration:

#### **`USvisaPredictorConfig`**:
- **`model_file_path`**: Specifies the path to the model file (e.g., `model.pkl`).
- **`model_bucket_name`**: The name of the S3 bucket where the model is stored.

```python
@dataclass
class USvisaPredictorConfig:
    model_file_path: str = MODEL_FILE_NAME
    model_bucket_name: str = MODEL_BUCKET_NAME




# US Visa Prediction Web Application (Frontend)

## Overview

The User App is the frontend interface of the US Visa Prediction system. We use FastAPI to serve the application, allowing users to input data via an HTML form and view predictions generated by the machine learning model. The web application consists of an HTML interface for user input and a backend powered by FastAPI to handle the prediction logic.

## Folder Structure

The application follows a basic structure with two primary folders:

### 1. **`templates/`** - Contains HTML files for the frontend.
- **`usvisa.html`**: The HTML form where users will input data for the prediction.

### 2. **`static/`** - Contains static files like CSS, JavaScript, etc.
- **`css/`**:
  - **`style.css`**: The CSS file for styling the HTML form.

### 3. **`app.py`** - The FastAPI application that serves the backend and frontend.
- This file contains the FastAPI server that handles routing and connects the HTML form to the prediction pipeline.

## FastAPI Setup

### 1. Install FastAPI and Uvicorn

First, you need to install the FastAPI and Uvicorn packages. Uvicorn is an ASGI server used to serve the FastAPI application.

```bash
pip install fastapi uvicorn





# Deployment (CICD) for US Visa Prediction Model

## Overview

This section describes the Continuous Integration and Continuous Deployment (CICD) pipeline for deploying the US Visa Prediction model. We use AWS, GitHub Actions, and Docker for automating the deployment process. Every time we commit code to GitHub, the changes are automatically reflected in the cloud environment.

## CICD Tools Used

1. **GitHub Actions**: For automating the CICD pipeline with a `.yaml` file.
2. **Genkings**: For manual setup of certain tasks.
3. **Circle CI**: For manual setup of other tasks.

## AWS Services Used

- **Amazon EC2**: A virtual machine to host the environment.
- **Amazon ECR (Elastic Container Registry)**: For storing Docker images.
- **GitHub Actions**: For automating the deployment from GitHub to AWS.

## Steps for Setting Up CICD Pipeline

### Step 1: Create IAM User in AWS
1. Go to AWS Console and create an IAM user with the following permissions:
   - `AmazonEC2ContainerRegistryFullAccess`
   - `AmazonEC2FullAccess`
   
2. Save the access key and download the `.csv` file containing the credentials.

### Step 2: Create an ECR Repository
1. In AWS Console, go to **Amazon ECR** and create a new repository to store Docker images.
2. Copy the repository URI, e.g., `975049952288.dkr.ecr.ap-south-1.amazonaws.com/visa`.

### Step 3: Create an EC2 Instance
1. Launch a new EC2 instance with the following details:
   - Name: `visa-machine`
   - OS: Ubuntu
   - Instance type: `t2-large`
   - Key pair: `visa`
   - Storage: 30 GB
   - Allow HTTP traffic
   
2. Once the EC2 instance is created, click on the instance ID, then click **Connect** to access the terminal.

3. Set up the EC2 instance:
   ```bash
   sudo apt-get update -y
   sudo apt-get upgrade
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker ubuntu






# Running the Project Inside AWS Cloud (EC2)

## Accessing EC2 Instance
1. Go to your **AWS EC2 Instances** dashboard.
2. Copy the **Public IP address** of your EC2 instance.

> **Note:** The application by default runs on port `8080`. If you try to access the instance directly, it might not work due to security settings.

## Fixing Port Mapping
To allow traffic on port `8080`, follow these steps:
1. In the **EC2 Console**, navigate to **Security Groups**.
2. Select the security group associated with your instance.
3. Click **Edit inbound rules**.
4. Add a new rule:
   - Choose **Custom TCP Rule**.
   - Set the **Port Range** to `8080`.
   - Set the **Source** to `0.0.0.0/0` (for public access).
5. Save the rules.

## Accessing the Application
1. Copy the **Public IP address** again.
2. Append `:8080` to the IP address.
   - Example URL: `http://your_public_ip:8080`
3. Now, you should be able to access your application running on the EC2 instance.

## Cleanup
Once the application has been successfully executed and you no longer need the resources:
1. **Delete all resources** from AWS (EC2, Security Groups, etc.) to avoid any further charges.

---

Thank you for using this guide!
