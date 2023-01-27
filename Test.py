#def convert(seconds):
#    seconds = seconds %(100*31536000)
#    year =seconds // 31536000
#    seconds %= 31536000
#    mounth =seconds // 2592000
#    seconds %= 2592000
#    day =seconds // 86400
#    seconds %= 86400
#    hour = seconds // 3600
#    seconds %= 3600
#    minute = seconds // 60
#    seconds %= 60
#    return"{}:{}:{}:{}:{}:{}".format(year,mounth,day,hour, minute, seconds)
#n=int(input("enter the second s:"))

#print(convert(n))
#__________
#from math import *
#print(sqrt(9))
#num1 =float(input("enter first num : "))
#num2 =input("")
#num3 =float(input("enter second num : "))
#if num2 == "+":
#   print(num1 + num3)
#elif num2 == "-":
#     print(num1 - num3)
#elif num2 == "*":
#     print(num1 * num3)
#elif num2 == "/":
#     print(num1 / num3)
#elif num2 == "**":
#     print(num1 ** num3)
#elif num2 == "√":
#     print(sqrt(num1))  
#elif num2 == "√√":
#     print(sqrt(num3))   
#else:
#     print("error")
#_______
#print("تانيمخت ةبعل")    
    
#sacourd_word="code mode"
#guess =""
#guess_count =0
#guess_leimt=3
#loser = False 
#while guess != sacourd_word and not loser:
#     if guess_count < guess_leimt:
#        guess= input("enter guess:")
#        guess_count +=1
#     else:
#          loser =True 
            
      
#if loser :
#   print("you lose")
#else:
#     print(" you win")
    
   #________ 
       
#def convert(year):
#    year = year %(31536000*19)
#    sounds =year*31536000
#    return"{}".format(sounds)
#n=float(input("you"))
#print(convert(n))
#______   
    
#def convert(minutes):
#    minutes = minutes %(60*60)
#    hour =minutes//60
#    minutes %= 60    
#    return "{}:{}".format(hour, minutes)
#y=int(input("enter minutes:"))



#print(convert(y))
#_______

#p=int(input("enter : "))
#n=0    
#while n<p: 
   
#         t =input("is you need again: ")
#         if t=="3":
#            n+=1      
#            def pluse(x,y):
#                return x + y
#            def subtract(x, y):
#                return x - y
#            def multiply(x, y):
#                return x * y
#            def divide(x, y):
#                return x / y
#            def os(x,y):
#                return x**y
#            print("Select operation.") 
#            print("1.+")
#            print("2.-")
#            print("3.*")
#            print("4./")
#            print("5.**")
     
            
#            choice = input("Enter choice(1/2/3/4/5): ")
#            if choice in ('1', '2', '3', '4','5'):
#               num1 = float(input("Enter first number: "))
#               num2 = float(input("Enter second number: "))
#               if choice == '1':
#                  print(num1, "+", num2, "=", pluse(num1, num2))
#               elif choice == '2':
#                     print(num1, "-", num2, "=", subtract(num1, num2))
#               elif choice == '3':
#                    print(num1, "*", num2, "=", multiply(num1, num2))
#               elif choice == '4':
#                    print(num1, "/", num2, "=", divide(num1, num2))
#               elif choice == '5':
#                    print(num1,"**",num2,"=",os(num1,num2))
                   
#               else:
#                    print("Invalid Input")
#            else:
#               print("error") 
#               pass         
#         else : 
#             print("ok")
#             break;

#________

#n=0

#while n < 10:
       
#      n+=1
      
#      if n % 2==0  :
#         print("{} is number two". format(n))
         
         
#      else:
#          print("{} is number one". format(n))
          
#______

#n=0
#while n <=3:
#      i=input("is you need two true or false :") 
      
#      if i == "true" :
#        n+=1
#        t=int(input("enter the range one"))
#        y=int(input("enter the range two"))     
#        import string
#        from random import *
#        characters = string.ascii_letters + string.punctuation  + string.digits
#        password =  "".join(choice(characters) for x in range(randint(t, y)))

#        print(password)
       
       
#      else:        
#           print('ok')
#           break

    
from math import*


try :
    n=0
    l=int(input("enter the try's number"))
    while n<l :
      print('yes or no')
      m=input("is need again : ")
      if m=="yes":
          n+=1
          def plus (x,y):
              return x+y
          def Subtract (x,y):
              return x-y
          def multiply (x,y):
              return x*y 
          def divide (x,y):
              return x/y 
          def os (x,y):
              return x**y 
          def sprt(x):
              return sqrt(x)
          print("Select operation.")
          print("1.+")
          print("2.-")
          print("3.×")
          print("4.÷")
          print("5.**")
          print("6.√")
          t=input("enter operation :")
          if t == "1":
             num1=float(input('enter the one nember : '))
             num2=float(input('enter the two nember : '))
             print(num1," + ",num2," = ",plus(num1,num2))
          elif t=="2":
               num1=float(input('enter the one nember : '))
               num2=float(input('enter the two nember : '))
               print(num1," - ",num2," = ",Subtract(num1,num2))
          elif t=="3":
               num1=float(input('enter the one nember : '))
               num2=float(input('enter the two nember : '))
               print(num1," × ",num2," = ",multiply(num1,num2))
          elif t=="4":
               num1=float(input('enter the one nember : '))
               num2=float(input('enter the two nember : '))
               print(num1," ÷ ",num2," = ",divide(num1,num2))
          elif t=="5":
               num1=float(input('enter the one nember : '))
               num2=float(input('enter the two nember : '))
               print(num1," ** ",num2," = ",os(num1,num2))
          elif t=="6":
               num1=float(input('enter the one nember : '))
               print(" √ ",num1," = ",sqrt(num1))
          else:
               print("error")
        
        
        
        
      else:     
           print('ok')
           break;
     

                
except ValueError as err :
       print(err)          
