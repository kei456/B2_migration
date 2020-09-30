print("Good morning")

num=1
print(num)

string_A="hello"

print(string_A)
print(type(string_A))

a=["apple","sss","banana"]
print(a[0])

b=[["aaa","bbb"],["cccc","dddd"]]
print(b[0][0])

x=10
y=2

print(x<y)
print(x==10 or y==1)
print(x==10 and y==2)

age=22

if age >= 20:
  print("Adult")
elif age==0:
  print("baby")
else:
    print("child")

print()

for i in range(5):
  if i==3:
    break
  elif i==1:
    continue
  print(i)

print()

arr=[2,4,6,8,10]
for i in arr:
  print(i)

def say_hello():
  print("hello ww")

say_hello()

def say_anything(word):
  print(word)
  #print("2222")

say=say_anything
say("heeee")
say_anything("hehehe")

print()

class Student:

  def __init__(self,name): #アンダーバーふたつずつ
    self.name=name

  def avg(self,math,english): #引数が必ずひとついる
    print((math+english)/2)

a001 = Student("tanaka")
a001.avg(80,70)
a001.name="sato"
print(a001.name)

a002 = Student("sato")
print(a002.name)

class Student2:
  
  def __init__(self,name): #アンダーバーふたつずつ
    self.name=name

  def calculate_avg(self,date): #引数が必ずひとついる
    sum = 0

    for num in date:
      sum += num
    
    avg = sum/len(date)
    return avg
  def jedge(self,avg):

    if(avg >=60):
      result="passed"
    else:
      result="failed"
    
    return result

b001=Student2("sss")
date1=[60,70,80,20]
print(b001.jedge(b001.calculate_avg(date1)))

avg = b001.calculate_avg(date1)
result = b001.jedge(avg)

print(avg)
print(b001.name+":"+result)


