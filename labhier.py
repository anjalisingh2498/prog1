class Student:
        def __init__(self):
                self.usn=input("Enter the USN:-  ")
                self.name=input("Enter the Name:- ")
                self.age=input("Enter the Age:- ")

        def display(self):
                print("USN:- ",self.usn)
                print("Name:- ",self.name)
                print("Age:- ",self.age)

class Ugstudent(Student):
        def __init__(self):
                super().__init__()
                self.sem=input("Enter the Semester:- ")
                self.fees=int(input("Enter the Fees:- "))
                self.stipend=int(input("Enter the Stipend:- "))


        def display(self):
                super().display()
                print("Semester:- ",self.sem)
                print("Fees:- ",self.fees)
                print("stipend:- ",self.stipend)



class Pgstudent(Student):
        def __init__(self):
                super().__init__() 
                self.sem=input("Enter the Semester:- ")
                self.fees=int(input("Enter the fees:- "))
                self.stipend=int(input("Enter the Stipend:- "))


        def display(self):
                super().display()
                print("Semester:- ",self.sem)
                print("Fees:- ",self.fees)
                print("Stipend:- ",self.stipend)


while(True):
        print("1.Ugstudent \n 2.Pgstudnet \n3.exit")
        ch=int(input("enter your choice "))
        if ch==1:
                obj1=Ugstudent()
                obj1.display()
        elif ch==2:
                obj2=Pgstudent()
                obj2.display()
        elif ch==3:
                exit()
        else:
                exit()
