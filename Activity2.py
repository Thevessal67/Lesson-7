#membership operator
print("enter marks obtained in 5 subjects: ")
sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
total=sub1+sub2+sub3+sub4+sub5
avg=total//5
VaildRange=range(0,101)
if avg not in VaildRange:
    print("in vaild input")
elif avg in range (91,101):
    print("your grade A1")
elif avg in range(81,91):
    print("your grade is A2")
elif avg in range (71,81):
    print(" your grade is B1")
elif avg in range (61,71):
    print("your grade is B2")
elif avg in range (51,61):
    print("your grade is C1")
elif avg in range (41,51):
    print("your grade is C2")
elif avg in range (31,41):
    print("your grade is D")
elif avg in range (21,31):
    print("your grade is E1")
elif avg is range (0,21):
    print("your grade is E2")