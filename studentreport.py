def student_report(*marks,**student):
    count=0
    sum=0
    print("Student Information:")
    for label in student:
        print(label,"=",student[label])
    for i in marks:
        sum+=i
        count+=1
    avg=sum/count
    print(f"Total marks is {sum:.2f}")
    print(f"Average marks is {avg:.2f}")
student_report(97,95,92,name="Reda",rollno="4085")

    
