try:

   fr=open("Python\\Error Handling\\eywords.txt")
   
   for line in fr:

    print(line)

except Exception as e:

    print(e)

finally:    

    print("db commit")
