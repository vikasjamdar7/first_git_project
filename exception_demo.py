import traceback
from logging_demo import logger


class MyClass1:
    a = 10
    def __init__(self, mylist):
        try:
            raise KeyError()
            raise AttributeError("this is attr error")
            print(mylist[10])
            print("MyClass1 object created...")
            print("a===", self.a)
            try:
                self.a = 20
                self.l = mylist
            except AttributeError as e:
                print(e)
            print("a===", self.a)
            print("sum of list==", sum(self.l))
        except (IndexError,AttributeError) as e:
            print("We catched list index error")
            print(e)
            print(traceback.format_exc())
            logger.critical(traceback.format_exc())
        except Exception as e:
            print(traceback.format_exc())
        else:
            print("else block executed in init")
        finally:
            print("this will execute whether\
                    exception occur or not!!")


    def function1(self):
        try:
            print(12 / 0)
            #print("v==",v)
            result = sum(self.l)
            return result

        except NameError as e:
            print("We catched Name error")
            print(e)
            logger.critical(traceback.format_exc())

        except Exception as e:
            print("We catched any general error")
            print(e)
            print(traceback.format_exc())
            logger.critical(traceback.format_exc())

        else:
            print("else block executed in function")
        finally:
            print('finally executed in fuction')


if __name__ == "__main__":
    try:
        mylist = eval(input("Enter a list:"))
        obj1 = MyClass1(mylist)
        res = obj1.function1()
        print("sum of list==", res)
    except:
        print(traceback.format_exc())
