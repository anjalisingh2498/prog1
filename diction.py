d=dict()
class Employee:
	def input(self):
		self.name=input("Enter the name :- ")
		self.age=int(input("Enter the age:- "))
		self.address=input("Enter the address:- ")
		self.basic_sal=int(input("Enter the basic salary:- "))
		self.tds=0.25*self.basic_sal
		self.hra=0.10*self.basic_sal
		self.da=0.20*self.basic_sal
		self.deduct=0.10*self.basic_sal
		self.gross=self.basic_sal+self.hra+self.tds+self.da
		self.net=self.gross-self.deduct
		self.update()
	def update(self):
		d.update({self.name:{
		"NAME" : self.name,
		"Age" : self.age,
		"Address" : self.address,
		"Basic Salary" : self.basic_sal,
		"TDS " : self.tds,
		"HRA" : self.hra,
		"DA " : self.da,
		"DEDUCT" : self.deduct,
		"GROSS" : self.gross,
		"NET " : self.net}})
	def search(self,name):
		flag=0
		for key in d:
			if key == name:
				print("Emp found")
				for i in  d[key]:
					print(i,d[key][i])
					flag=1
		if flag==0:
			print("Emp Not Found")
	def display(self):
		for key in d:
			print(key,d[key])
emp=Employee()
while True:
	print("1. Add \n 2.Display \n 3.Search \n 4.Exit")
	ch=int(input("Enter the choice: -"))
	if ch==1:
		emp.input()
	elif ch==2:
		emp.display()
	elif ch==3:
		name=input("Enter the name:- ")
		emp.search(name)
