print('='*60)
print('handlingexception')
print('='*60)

import time

def handleException(func):
    start = time.time()

    def wrapper(*args):
        try:
            func(*args)
        except Exception as e:
            raise e
        finally:
            print(f'Function took {time.time() - start} seconds to execute')
    return wrapper

def causeError():
    name = 'causeError()'
    start = time.time()
    try:
        return 1/0
    except Exception as e:
        errorNumber = 10100
        raise Exception(f'{name}  {errorNumber}  {e.args}')
    finally:
        print(f'Function took {time.time() - start} seconds to execute')


def callCauseError():
    name = 'callCauseError()'
    start = time.time()
    try:
        return causeError()
    except Exception as e:
        errorNumber = 10100
        raise Exception(f'{name}  {errorNumber}  {e.args}')
    finally:
        print(f'Function took {time.time() - start} seconds to execute')

try:
    callCauseError()
except Exception as e:
    print(e)
    
