# python3
# wait_return.py
# codeing: UTF-8
import threading

class waitReturn:

    flag = True
    def __init__ (self): 
        def wait_input():
            global flag
            input()
            flag = False

        th = threading.Thread(target=wait_input)
        th.start()

    def is_true(self):
        global flag
        return flag

    def is_false(self):
        global flag
        return not flag



        
