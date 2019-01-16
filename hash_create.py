import hashlib
import sys
import threading
import time

def hash():

    f=open('nc.exe','rb')
    data=f.read()
    f.close()

    sys.stdout=open('hash_result.txt','w')

    print("SHA-1: " + hashlib.sha1(data).hexdigest())
    print(time.ctime())

    threading.Timer(5,hash).start()

hash()




