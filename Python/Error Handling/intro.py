"""
error handling 
 - logical  error
 - syntax error
 -  run time error

=====(block)
 try
 except
 finally

 =====(keywords)
 raise  - create custom error 
 assert - debugging(test check)

 
try: -double of code (error)
   (doubtful code)

except: -error handle
   (handling code)

finally: - close files
   (clean up processing)   

"""

num1=int(input("Enter a number"))

num2=int(input("Enter a number"))

try:

    result=num1 /num2

except Exception as e:

    print(e)

print("okkkeiiiii")
print("byyeeeeei")
         