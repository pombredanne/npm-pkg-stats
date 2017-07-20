import time

def getLocalTime():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
