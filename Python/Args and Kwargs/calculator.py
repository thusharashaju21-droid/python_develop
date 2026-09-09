def calculator(*args,**kwargs):

  if kwargs.get("operation")=="+":

    return sum(args)

  elif kwargs.get("operation")=="*":

    result=1

    for num in args:

      result=result*num

      return result

print(calculator(10,20,30,40,operation="+"))
print(calculator(10,20,30,40,operation="*"))


    
