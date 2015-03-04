import time

def in_future(offset):
    return int(round(time.time() * 1000 + offset))

