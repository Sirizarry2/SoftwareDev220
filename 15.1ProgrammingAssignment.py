##15.1

import multiprocessing
import os
import time
from datetime import datetime

def whoami(num):
    print("Process %s says: %s" % (os.getpid(),num ), "time is", datetime.utcnow())
   
    

if __name__ == "__main__":
    whoami("Main Process")
    
    for n in range(2):
        p = multiprocessing.Process(target=whoami, args=("I'm process %s" % n,))
        time.sleep(1)
        p.start()