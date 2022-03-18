import sys
import os
import random
import time
import datetime
import subprocess
q = "Enter digit number generates password."
c = "Do you Continue[Y/N]?"
s = "Enter times generates passwords."
b = "It will finish after digit number seconds you specify."
p = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","t","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
dt_now = datetime.datetime.now()
dt_now = str(dt_now)
print("Password List")
print(dt_now)
print(q)
x=input()
print(s)
y=input()
for k in range(int(y)):
  sys.stdout.write("\n")
  for i in range(int(x)):
    sys.stdout.write(random.choice(p))
print("\n"+c)
answer=input()
print("\n")
while answer == "Y":
    for j in range(1):
        print(q)
        x=input()
        print(s)
        y=input()
        for k in range(int(y)):
          sys.stdout.write("\n")
          for i in range(int(x)):
            sys.stdout.write(random.choice(p))
        sys.stdout.write("\n"+c)
        sys.stdout.write("\n")
        answer=input()
if answer == "N":
    sys.stdout.write("\n"+b)
    sys.stdout.write("\n")
    a=input()
    time.sleep(int(a))
