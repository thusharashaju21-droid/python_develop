cibil_score=int(input("Enter cibil score"))
if cibil_score>=800 and cibil_score<=850:
    print("Excellent")
elif cibil_score>=740 and cibil_score<800:
    print("Ver Good")
elif cibil_score>=670 and cibil_score<740:
    print("Good")
elif cibil_score>=500 and cibil_score<670:
    print("Fair") 
else:
    print("Poor")               