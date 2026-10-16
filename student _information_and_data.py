class student:
    def student_name():
        student_name=input("enter student name")
        student_id=input("enter student id")
        print(f"the name of student:{student_name}")
        print(f"the student id is :{student_id}")

    
    def student_subject():
        student_subject=input("enter student subject")
        student_fees=int(input("enter student fees"))

        if student_fees>=60000:
            print("yes student is join in the school")
        else:
            print("sorry please submit all fees to acess to check your marks")

    def marks():
        b=int(input("enter bio marks"))
        m=int(input("enter math marks"))
        p=int(input("enter physics marks"))
        c=int(input("enter chemistry marks"))

        avg=0

        avg=(b+m+p+c)/4

        print(f"this is student {avg} marks")

    student_name()
    student_subject()
    marks()
       