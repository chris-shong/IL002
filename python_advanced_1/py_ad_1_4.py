"""
Chapter 1
Python Advanced(1) - Context Manager(1)
Keyword - Contextlib, __enter__, __exit__, exception

"""
"""
Context manager: 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할
가장 대표적인 구문: with

"""

# Ex1
file = open('./testfile.txt', 'w')
try:
    file.write('Context Manager Test1\nContextlib Test1.')
finally:
    file.close()

# Ex2
with open('./testfile2.txt', 'w') as f:
    f.write('Context Manager Test\nContextlib Test2.')

# Ex3
# Use Class -> Context Manager with exception handling
class MyFileWriter():
    def __init__(self, file_name, method):
        print('MyFileWriter started: __init__')
        self.file_obj = open(file_name, method)

    def __enter__(self):
        print('MyFileWriter started: __enter__')
        return self.file_obj

    def __exit__(self, exc_type, value, trace_back):
        print('MyFileWriter started: __exit__')
        if exc_type:
            print('Logging exception {}'.format((exc_type, value, trace_back)))
        self.file_obj.close()

with MyFileWriter('./testfile3.txt', 'w') as f:
    f.write('Context Manager Test\nContextlib Test3.')

