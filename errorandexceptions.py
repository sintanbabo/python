print('='*60)
print('errorandexceptions')
print('='*60)

import time

class CustomException(Exception):
    className = None
    functionName = None
    errorNumber = None
    statusCode = None
    message = None

    def __init__(self,className,functionName,errorNumber, statusCode, message):
        self.className = className
        self.functionName = functionName
        self.errorNumber = errorNumber
        self.statusCode = statusCode
        self.message = message
        super().__init__(f'ClassName: {self.className}, FunctionName: {self.functionName}, ErrorNumber: {self.errorNumber}, StatusCode: {self.statusCode}, Message: {self.message}')

def causeError():
    functionName = 'causeError()'
    start = time.time()
    try:
        try:
            pass
        except Exception as e:
            errorNumber = 10100
            raise CustomException('',functionName,errorNumber,'E',e.args)
        
        try:
            1/0
        except Exception as e:
            errorNumber = 10200
            raise CustomException('',functionName,errorNumber,'E',e.args)

    except Exception as e:
        raise e
    finally:
        print(f'{functionName} took {time.time() - start} seconds to execute')


def callCauseError():
    functionName = 'callCauseError()'
    start = time.time()
    try:
        return causeError()
    except Exception as e:
        errorNumber = 10100
        raise CustomException('',functionName,errorNumber,'E',e.args)
    finally:
        print(f'{functionName} took {time.time() - start} seconds to execute')

try:
    callCauseError()
except Exception as e:
    print(e)
    
