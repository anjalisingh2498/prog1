class Student:
	def __init__(self):
		self.name=input("Enter the name:- ")
		self.age=int(input("Enter the age:- "))
		self.address=input("Enter the address:- ")
	def display(self):
		print("Name:- ", self.name)
		print("Age:- ", self.age)
		print("Address:- ", self.address)
class UgStudent(Student):
	def __init__(self):
		super().__init__()
		self.sem=int(input("Enter the sem:- "))
		self.fees=int(input("Enter the fees:- "))
	def display(self):
		super().display()
		print("Sem:- ",self.sem)
		print("Fees:- ",self.fees) 
class PgStudent(Student):
	def __init__(self):
		super().__init__()
		self.sem=int(input("Enter the sem:- "))
		self.fees=int(input("Enter the fees:- "))
	def display(self):
		super().display()
		print("Sem:- ",self.sem)
		print("Fees:- ",self.fees)
while True:
	print("1.Ug 2.Pg 3.Exit")
	ch=int(input("Enter the choice:- "))
	if ch==1:
		ug=UgStudent()
		ug.display()
	elif ch==2:
		pg=PgStudent()
		pg.display()
	else:
		break

