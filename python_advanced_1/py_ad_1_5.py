"""
Chapter 1
Python Advanced(1) - Context Manager(2)
Keyword - Contextlib, __enter__, __exit__

"""
"""
Contextlib - Measure execution(타이머) 제작

"""
# Ex1
# Use Class
import time


class ExecuteTimer():
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic()
        return self._start

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print("Logging exception {}".format((exc_type, exc_value, exc_traceback)))
        else:
            print('{} : {}s'.format(self._msg, time.monotonic() - self._start))
        return True


with ExecuteTimer("Start! job") as v:
    print('Received start monotonic : {}'.format(v))
    # Execute job
    for i in range(1000000):
        pass
    raise Exception('Raise! Exception!')  # 강제로 발생
