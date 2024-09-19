# #Exception handling(controlling the crash control)
# x=1/0
# print(x)#code will terminate cox of error and doesnot go to 2nd line so unable to detect  2nd line error
# print(y)
# # try:
# #    print(x)
# # except :
# #      print("Something went wrong")
# #we wrote name error by knowing the type of the error
# #if i dont know the error type then we simply put same in try 
# #first find the error type name and then give solution
# print(y)
# x=1/0
# print(x)
#error get detected sequece wise
try:
    x=1/0 # error coming by expression 1/0
    print(y)
except ZeroDivisionError:
    print("Zero division error")
except NameError:
    print("y is not defined ")
# find the error line 1st step
#as well as the type of error
# put the error line in try
#and put the error in except
#print the error in words 
a=int(input("Enter the integer value:"))
aa=str(a)
#exception handling 
try:
    x= aa+1
except TypeError:
    print("Hola concatenate str not i")


