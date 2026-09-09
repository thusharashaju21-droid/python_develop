note="hen"
magnize="chicken"
for alpha in note:
    if alpha not in magnize:
        print("not ransom")
        break
else:
    print("ransom")    