# Custom Derocators and Exception handling
import time

def makeerror():
    start = time.time()
    try:
        time.sleep(1)
        return 1/0
    except ZeroDivisionError:
        print("There is a Error")
    finally:
        print(f'Function took {time.time() - start} seconds to execute')

    

def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print("There was a type error")
        except ZeroDivisionError:
            print("There was a Zero division error")
        except Exception:
            print('There was some sort of error!')
        
    return wrapper

@handleException
def causerror():
    return 1/0 



@handleException
def raiserror(n):
    if n == 0:
        raise Exception()
    print(n)
    

if __name__=="__main__":
    makeerror()
    
    causerror()

    raiserror(0)