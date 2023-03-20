d=dict()

class emp:
    def add(self):
        self.name=input("Enter your name:\n")
        self.address=input("Enter your address\n")
        self.pan=int(input("Enter pan card number"))
        self.basic_salary=int(input("Enter your basic salary"))
        self.tds=0.10*self.basic_salary
        self.deduction=0.20*self.basic_salary
        self.hra=0.10*self.basic_salary
        self.da=0.25*self.basic_salary
        self.gross_salary=self.basic_salary+self.tds+self.deduction+self.hra+self.da
        self.update()

    def update(self):
        d.update({self.name:{"Name":self.name,"Address":self.address,"Pan":self.pan,"Basic Salary":self.basic_salary,"Tds":self.tds,"Deduction":self.deduction,"Hra":self.hra,"DA":self.da,"Gross Salary":self.gross_salary}})

    def display(self):
        print(d)

    def search(self,name):
        for keys in d:
            if keys==name:
                print(d[name])
            else:
                print("Employee not found")
obj=emp()
while True:
    print("1.To add Employee\n2.Display\n3.Search\n4.Exit")
    ch=int(input("Enter your choice"))
    if(ch==1):
        obj.add()
    elif (ch==2):
        obj.display()
    elif(ch==3):
        name=input("Enter the name of employee to search")
        obj.search(name)
    elif(ch==4):
        break
    else:
        print("Enter correct value")