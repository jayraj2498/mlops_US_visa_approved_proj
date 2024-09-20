import logging
import os
from datetime import datetime

LOG_FILENAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILENAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)







# import logging
# import os
# from datetime import datetime

# # Set log file name with timestamp
# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# # Set logs directory to the "logs" folder inside your current working directory
# log_dir = "logs"
# logs_path = os.path.join(log_dir, LOG_FILE)

# # Create directory if it doesn't exist
# os.makedirs(log_dir, exist_ok=True)

# # Print log path
# print(f"Logs will be saved at: {logs_path}")

# # Configure logging
# logging.basicConfig(
#     filename=logs_path,
#     format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
#     level=logging.DEBUG,
# )

# # Log a test message
# logging.info("This is a test log message to verify logging setup.")






# # %(asctime)s ] = time 
# # %(name)s-= name of the file  
# # %(levelname)s = wherther information is bug level logger 
# # %(message)s = msg of the log 