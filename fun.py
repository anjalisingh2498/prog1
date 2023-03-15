def my_function():
    print("Hello")
    
my_function()

def my_function(fname, lname):
    print(fname + "  " + lname)
my_function("Python", "Program")

def my_function(*dept):
    print("The department is " + dept[2])
my_function("MCA", "MBA" ,"Mtech")

def my_function(dept3, dept2, dept1):
    print("The department is " +dept1)
my_function(dept1="MCA", dept2="MBA" ,dept3="Mtech")

def my_function(country="Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function()
my_function("India")
my_function("Brazil")

def my_function(dept):
    for x in dept:
        print(x)
dept=["MCA","MBA","Mtech"]
my_function(dept)


def my_function(x):
    return 5*x 
print(my_function(3))
print(my_function(5))


def my_function(**person):
    print ("His last name is " + person["lname"])
my_function(fname="XYZ", lname="ABC")
