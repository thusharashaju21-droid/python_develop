wishes=("good morng","good night","good evening")
fw=open("Python\File Operation\greetings.txt","w")
for m in wishes:
  fw.write(m+"\n")