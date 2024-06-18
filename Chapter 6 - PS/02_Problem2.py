sub1 = int(input("Enter Sub1 Marks : "))
sub2 = int(input("Enter Sub2 Marks : "))
sub3 = int(input("Enter Sub3 Marks : "))

if sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    if (sub1+sub2+sub3)/3 >= 40:
        print("Student passed the exam")
    else:
        print("Student Failed the exam")
else:
    print("Student Failed the exam as He didn't qualify the minimum subject marks criteria")