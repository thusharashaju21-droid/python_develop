def is_randsome_note(note,maganize):
  
  for alpha in note:

    if alpha not in maganize.lower():

        print(False)

        break

  else:
      
      print(True)

is_randsome_note("hen","cHicken")      
is_randsome_note("hen","chicken")      
