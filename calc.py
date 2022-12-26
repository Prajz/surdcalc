import random
import time
import numpy as np
import triwq as nothing


list_two = []
list_three = []
list_five = []
list_seven = []
list_eleven = []

for i in range(1,9):
      q = 0
      while q < 200:
            n = (i ** 2) * 2
            list_two.append(n)
            q = n

for i in range(1,9):
      q = 0
      while q < 200:
            n = (i ** 2) * 3
            list_three.append(n)
            q = n

for i in range(1,9):
      q = 0
      while q < 200:
            n = (i ** 2) * 5
            list_five.append(n)
            q = n

for i in range(1,9):
      q = 0
      while q < 200:
            n = (i ** 2) * 7
            list_seven.append(n)
            q = n

for i in range(1,9):
      q = 0
      while q < 200:
            n = (i ** 2) * 11
            list_eleven.append(n)
            q = n

a = 0
b = 0
c = 0
d = 0

def randomas():
  global a,b,c,d
  a = random.randint(1,20)
  c = random.randint(1,20)
  #ensures that the surds can be simplifed so the answer can be a single surd
  e = random.randint(1,5)
  if e == 1:
    b = random.choice(list_two)
    d = random.choice(list_two)
  if e == 2:
    b = random.choice(list_three)
    d = random.choice(list_three)
  if e == 3:
    b = random.choice(list_five)
    d = random.choice(list_five)
  if e == 4:
    b = random.choice(list_seven)
    d = random.choice(list_seven)
  if e == 5:
    b = random.choice(list_eleven)
    d = random.choice(list_eleven)


def add(a,b,c,d):
  num1 = a * np.sqrt(b)
  num2 = c * np.sqrt(d)
  time.sleep(1)
  print ("Find the simplified answer to the following 2 surds added together")
  time.sleep(1)
  print("the numbers are " + str(a) + "sqrt(" + str(b) + ") and " + str(c) + "sqrt(" + str(d) + ")")
  ans = num1 + num2
  time.sleep(1)
  x = input("Enter integer x: ")
  time.sleep(1)
  y = input("Enter integer y: ")
  time.sleep(1)
  yans = int(x) * np.sqrt(int(y))
  yans = yans
  if (yans == ans):
    if (verifysimp(int(y))):
      print("simplify")
      time.sleep(1)
      add(a,b,c,d)
      #try again if not verified
    else:
      print("good")
  else:
    print("try again")
    time.sleep(1)
    add(a,b,c,d)
    #try again if not correct
  
def subtract(a,b,c,d):
  time.sleep(1)
  num1 = a * np.sqrt(b)
  num2 = c * np.sqrt(d)
  ans = num1 - num2
  ans = abs(ans)
  print("Find the difference between the following two surds")
  time.sleep(1)
  print("the numbers are " + str(a) + "sqrt(" + str(b) + ") and " + str(c) + "sqrt(" + str(d) + ")")
  time.sleep(1)
  x = input("Enter integer x: ")
  time.sleep(1)
  y = input("Enter integer y: ")
  time.sleep(1)
  yans = int(x) * np.sqrt(int(y))
  if (yans == ans):
    if (verifysimp(int(y))):
      print("simplify")
      subtract(a,b,c,d)
    else:
      print("good")
  else:
    print("try again")
    time.sleep(1)
    subtract(a,b,c,d)
    #try again if not correct
    
def verifysimp(yanss):
  if (yanss % 4 == 0) or (yanss % 9 == 0) or (yanss % 25 == 0) or (yanss % 49 == 0) or (yanss % 121 == 0) or (yanss % 169 == 0) or (yanss % 289 ==0) or (yanss % 361 == 0):
    return True
  else:
    return False
    
def randomis():
  global a,b,c,d 
  a = random.randint(1,20)
  b = random.randint(1,20)
  c = random.randint(1,20)
  d = random.randint(1,20)
  
def finda(b, c):
  a = np.sqrt((c**2) - (b**2))
  print("FIND a")
  time.sleep(1)
  yansi = input("Enter integer x: ")
  time.sleep(1)
  yanss = input("Enter integer y: ")
  yanss = int(yanss)
  yansi = int(yansi)
  if (int(yansi) * np.sqrt(int(yanss)) == a):
    if (verifysimp(yanss)):
        time.sleep(1)
        print("simplfy")
        finda(b, c)
    else:
      print("good")
  else:
    print("Try again")
    finda(b, c)

def findc(a, b):
  c = np.sqrt(a**2 + b**2)
  print("FIND C")
  time.sleep(1)
  yansi = input("Enter integer x: ")
  time.sleep(1)
  yanss = input("Enter integer y: ")
  yanss = int(yanss)
  yansi = int(yansi)
  if (int(yansi)* np.sqrt(int(yanss)) == c):
    if (verifysimp(yanss)): 
        time.sleep(1)
        print("simplfy")
        findc(a, b)
    else:
        print("good job")
  else:
    print("Try again")
    findc(a, b)

def rand():
  ar = random.randint(0,1)
  br = random.randint(0,1)
  cr = random.randint(0,1)
  if (ar == 1):
    if (br == 1):
      #c = 0
      return False
    if ( cr == 1):
      #b = 0
      return True
    if (cr != 1):
      rand()
  if (cr == 1):
    if (ar == 1):
      #b = 0
      return True
    if (br == 1):
      #a = 0
      return True
    if (br != 1):
      rand()
  if (br == 1):
    if (ar ==1):
      #c = 0
      return False
    if (cr ==1):
      #a=0
      return True
    if (cr != 1):
      rand()
  if (ar != 1 or br != 1 or cr != 1):
    rand()


print("welcome to surds calculator")
time.sleep(1)
print("first part is pythagoras")
time.sleep(1)
print("second part is addition and subtraction")
time.sleep(1)
print("you will get your key at the end so make sure to finish it")
time.sleep(1)
print("you will get two numbers and their variables")
time.sleep(1)
print("find the missing one in simplest surd form x ROOT y where both x and y are integers")
time.sleep(2)
print("Are you ready?")

y = input("Type y for yes and n for no: ")
if y == "y":
  print("good")
elif y == "n":
  print("ok i dont care get ready")
else:
  print("i said y or n. ur so clever")
time.sleep(1)
print("if it's a whole number enter 1 for integer b")
time.sleep(1)
print("if it's just a surd with nothing at the front enter 1 for integer a")
time.sleep(1)

for t in range(0,60):
  time.sleep(1)
  print("this is question " + str(t+1))
  time.sleep(1)
  if rand():
    randomis()
    a = 0
    #c = random.randint(1,20)
    #b = random.randint(1,20)
    
    while (int(c) <= int(b)):
      b = random.randint(1,20)
      c = random.randint(1,20)
    print("b = " + str(b))
    time.sleep(1)
    print("c = " + str(c))
    time.sleep(1)
    finda(b, c)
  else:
    randomis()
    c = 0
    print("a = " + str(a))
    time.sleep(1)
    print("b = " + str(b))
    time.sleep(1)
    findc(a, b)

time.sleep(1)
print("well done part 1 is finished")
time.sleep(1)
print("now it's time for addition/subtraction")
time.sleep(1)
print("you will get two surds and give them in same format as before")

for t in range(0,60):
  print("this is question " + str(t+1) + "a")
  time.sleep(1)
  randomas()
  add(a,b,c,d)
  time.sleep(1)
  print("this is question " + str(t+1) + "b")
  subtract(a,b,c,d)
  time.sleep(1)
  

nothing.a()
