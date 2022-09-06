"""
Chapter 1
Python Advanced(1) - Python Variable Scope
Keyword - scope, global, nonlocal, locals, globals...

전역변수는 주로 변하지 않는 고정 값에 사용
지역변수는 사용 이유: 지역변수는 함수 내에 로직 해결에 국한, 소멸주기: 함수 실행 해제 시
전역변수를 지역내에서 수정되는 것은 권장 x
"""

# Ex1
a = 10 # Global variable

def foo():
  # Read global variable
  print('Ex1 > ', a)
  
foo()

# Read global variable
print('Ex1 > ', a)

# Ex2
b = 20

def bar():
  b = 30 # Local variable
  print('Ex2 > ', b) # Read local variable
  
bar() # 30

print('Ex2 > ', b) # Read global variable

# Ex3
c = 40

def foobar():
  c = c + 10
  print('Ex3 > ', c)
  
foobar() # UnboundLocalError

# Ex4
d = 50

def barfoo():
  global d # not recommend
  d = 60
  d += 100
  print('Ex4 > ', d) # 160

print('Ex4 > ', d) # 160

# Ex5 (Important)
def outer():
  e = 70
  def inner():
    nonlocal e
    e += 10
    print('Ex5 > ', e) # without nonlocal -> UnboundLocalError
  return inner

in_test = outer() # Closure

in_test() # 80
in_test() # 90

# Ex6
def func(var):
  x = 10
  def printer():
    print('Ex6 > ', "Printer Func Inner")
  print("Func Inner", locals()) # 지역 전체 출력
  
func("Hi")

# Ex7
print('Ex7 > ', globals()) # 전역 전체 출력
test_variable = 100 # == globals()["test_variable"] = 100
print('Ex7 > ', globals())

# Ex8(지역 -> 전역 변수 생성)
for i in range(1, 10):
  for k in range(1, 10):
    globals()['plus_{}_{}'.format(i, k)] = i + k
    
# print(globals())
print("Ex 8 >", plus_5_5)
print("Ex 8 >", plus_9_9)
