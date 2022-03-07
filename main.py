#Day 1 task

total=0
stu = int(input("how many students: "))
for i in range(stu):
    name=input("Enter student name: ")
    sub=int(input("how many subjects"))
    for i in range(sub):
        marks=int(input("enter marks: "))
        total=total+marks
    print(total)