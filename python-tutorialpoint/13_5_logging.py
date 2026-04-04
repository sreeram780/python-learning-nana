# Benefits of Logging
#   Debugging − Helps identify and diagnose issues by capturing relevant information during program execution.
#   Monitoring − Provides insights into the application's behavior and performance.
#   Auditing − Keeps a record of important events and actions for security purposes.
#   Troubleshooting − Facilitates tracking of program flow and variable values to understand unexpected behavior.

# Components of Python Logging
#   Logger − It is the main entry point that you use to emit log messages. Each logger instance is named and can be configured independently.
#   Handler − It determines where log messages are sent. Handlers send log messages to different destinations such as the console, files, sockets, etc.
#   Formatter − It specifies the layout of log messages. Formatters define the structure of log records by specifying which information to include (e.g., timestamp, log level, message).
#   Logger Level − It defines the severity level of log messages. Messages below this level are ignored. Common levels include DEBUG, INFO, WARNING, ERROR, and CRITICAL.
#   Filter − It is the optional components that provide finer control over which log records are processed and emitted by a handler.

# log levels
#   DEBUG − Detailed information, typically useful only for debugging purposes. These messages are used to trace the flow of the program and are usually not seen in production environments.
#   INFO − Confirmation that things are working as expected. These messages provide general information about the progress of the application.
#   WARNING − Indicates potential issues that do not prevent the program from running but might require attention. These messages can be used to alert developers about unexpected situations.
#   ERROR − Indicates a more serious problem that prevents a specific function or operation from completing successfully. These messages highlight errors that need immediate attention but do not necessarily terminate the application.
#   CRITICAL − The most severe level, indicating a critical error that may lead to the termination of the program. These messages are reserved for critical failures that require immediate intervention.

import logging
# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage
def calculate_sum(a, b):
   logging.debug(f"Calculating sum of {a} and {b}")
   result = a + b
   logging.info(f"Sum calculated successfully: {result}")
   return result

# Main program
if __name__ == "__main__":
   logging.info("Starting the program")
   result = calculate_sum(10, 20)
   logging.info("Program completed")


import logging
# Create logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)  # Set global log level

# Create console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(console_handler)

# Example usage
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# Types of Logging Handlers
#   StreamHandler − Sends log messages to streams such as sys. stdout or sys.stderr. Useful for displaying log messages in the console or command line interface.
#   FileHandler − Writes log messages to a specified file on the file system. Useful for persistent logging and archiving of log data.
#   RotatingFileHandler − Similar to FileHandler but automatically rotates log files based on size or time intervals. Helps manage log file sizes and prevent them from growing too large.
#   SMTPHandler − Sends log messages as emails to designated recipients via SMTP. Useful for alerting administrators or developers about critical issues.
#   SysLogHandler − Sends log messages to the system log on Unix-like systems (e.g., syslog). Allows integration with system-wide logging facilities.
#   MemoryHandler − Buffers log messages in memory and sends them to a target handler after reaching a certain buffer size or timeout. Useful for batching and managing bursts of log messages.
#   HTTPHandler − Sends log messages to a web server via HTTP or HTTPS. Enables logging messages to a remote server or logging service.