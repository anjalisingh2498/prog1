d={}
class student:
	def __init__(self):
		self.usn=input("Enter USN:- ")
		self.name=str(input("Enter name:- "))
		self.age=int(input("Enter age:- "))
	def display(self):
		print("USN:- ", self.usn)
		print("Name:- ", self.name)
		print("Age:- ", self.age)

class stud1(student):
	def __init__(self):
		student.__init__(self)
		self.sem=input("Enter semster:-")
		self.sub=[]
		self.total=0
		for i in range (1,6):
			m=int(input("Enter the marks in subject:- "))
			self.sub.append(m)
			self.total+=m
		self.per=(self.total/500)*100
		stud2.display(self)
	def display(self):
		student.display(self)
		print("semster:- ", self.sem)
		for i in range(5):
			print("marks in subject are: ",self.sub[i])
		print("Percent = ", self.per)
class stud2(stud1):
	def __init__(self):
		stud1.__init__(self)
		d.update({self.name:{
		"Name":self.name,
		"USN":self.usn,
		"Age":self.age,
		"Semester":self.sem,
		"Subject":self.sub,
		"total" : self.total,
		"Percent":self.per
		}})
def prt():
	for key in d:
		print(key,d[key])

while True:
	print("1.Add \n 2.Display \n 3.Exit")
	ch=int(input("Enter the choice"))
	if ch==1:
		d2=stud2()
	elif ch==2:
		prt()
	else:
		break
