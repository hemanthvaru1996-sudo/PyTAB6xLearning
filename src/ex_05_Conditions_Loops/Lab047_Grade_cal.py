score=int(input("enter the score\n"))
if score>=101 or score<=-1:
    print("You are a super man !!! you can't get a grade")
else:
    if score>=90 and score<=100: # if 90 < score < 100
        print("The Grade is A")
    elif score>=80 and score<=89:
        print("The Grade is B")
    elif score>=70 and score<=79:
        print("The Grade is C")
    elif score>=60 and score<=69:
        print("The Grade is D")
    elif score >= 50 and score <= 59:
        print("The Grade is E")
    else:
        print("The Grade is F and student is fail")