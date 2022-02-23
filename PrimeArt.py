import turtle

turtle.shape('turtle')
def prime(s):
     flag = False
     for i in range(2,s):
          num = s % i
          if num == 0:
               flag = True
               break
     if flag == False:
          return 1
     else:
          return 0

num = 2
while True:
     turtle.forward(5)
     if prime(num) == 1:
          turtle.right(num%360)
          print(num)
     num += 1
