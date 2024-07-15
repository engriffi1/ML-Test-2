import sys
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_no=exc_tb.tb_lineno
    error_msg=str(error)

    error_message=f"Error occured in python script name {file_name}, line number {line_no}, and error message {error_msg}"

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_message_detail=error_message)

    def __str__(self):
        return self.error_message
    

    # if __name__=="__main__":
    #     try:
    #         a=1/0
    #     except Exception as e:
    #         logging.info("Divide by Zero Error...")
    #         raise CustomException(e,sys)
        



