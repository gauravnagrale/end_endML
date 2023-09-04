import logging
import sys

def error_message(error,error_details:sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_messgae = "Error occured in python Script name [{0}], line number [{1}], error_message[{2}]".format(
    file_name, exc_tb.tb_lineno, str(error))
    return error_messgae

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super.__init__(error_message)
        self.error_message = error_message(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logging.INFO("Divisible by 0")
        raise CustomException(e, sys)