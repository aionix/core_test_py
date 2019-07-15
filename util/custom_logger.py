import inspect
import logging
import os
from datetime import datetime

log_folder_exists = False
testRunDirectoryGlobal = "undefined"

# Get testRunDirectoryGlobal
def getLogDir():
    global testRunDirectoryGlobal
    return testRunDirectoryGlobal

# Logger for selenium work
def customLogger(logLevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    global log_folder_exists
    global testRunDirectoryGlobal

    # Save date and time
    current_time = datetime.now().strftime('%y_%m_%d_%I%M%S')
    # Root folder of all logs and reports
    logsDirectory = "../logs/"

    if log_folder_exists is False:
        # Root folder name for specific test run results
        testRunDirectory = "snc_smoke_" + current_time + "/"
        testRunDirectoryGlobal = testRunDirectory
        log_folder_exists = True
    else:
        testRunDirectory = testRunDirectoryGlobal

    # Way to testRunDir
    testRunLocation = logsDirectory + testRunDirectory
    # Current directory
    currentDirectory = os.path.dirname(__file__)
    # Location where exactly to put this log file
    destinationDirectory = os.path.join(currentDirectory, testRunLocation)
    # In case if destination does not exist - create it
    if not os.path.exists(destinationDirectory):
        os.makedirs(destinationDirectory)

    fileHandler = logging.FileHandler(destinationDirectory + "automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger

# Logger for k2 server output
def k2Logger(logLevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    global log_folder_exists
    global testRunDirectoryGlobal

    # Save date and time
    current_time = datetime.now().strftime('%y_%m_%d_%I%M%S')
    # Root folder of all logs and reports
    logsDirectory = "../logs/"

    if log_folder_exists is False:
        # Root folder name for specific test run results
        testRunDirectory = "snc_smoke_" + current_time + "/"
        testRunDirectoryGlobal = testRunDirectory
        log_folder_exists = True
    else:
        testRunDirectory = testRunDirectoryGlobal

    # Way to testRunDir
    testRunLocation = logsDirectory + testRunDirectory
    # Current directory
    currentDirectory = os.path.dirname(__file__)
    # Location where exactly to put this log file
    destinationDirectory = os.path.join(currentDirectory, testRunLocation)
    # In case if destination does not exist - create it
    if not os.path.exists(destinationDirectory):
        os.makedirs(destinationDirectory)

    fileHandler = logging.FileHandler(destinationDirectory + "k2_server.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
