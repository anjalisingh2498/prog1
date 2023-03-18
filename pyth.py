#using single quotes
str1='Heello python'
print(str1)
#using double quotes
str2="Hello World"
print(str2)

#string Indexing 
str="HELLO"
print(str[3])
print(str[-5])

#string splitting
str="ANJALI"
print(str[0:])
print(str[1:3])

#display reverse
print(str[-5:-3])
print(str[::-1])

#Reassigning strings
str="SINGH"
#str[3]="H"  throws error we can't ressign string
print(str)

#Delete string
#Operator
print("Anjali" + "Singh")
print(3*"ram")

str="MAYA"
print('Y' in str)
print("YA"not in str)
print("The string str:- %s" %(str))

#string formatting
str="""They said," What's there?"""
print(str)

print('They said."What\'s going on?"')

print("They said,\"What's going on?\"")

#format Methood


# Using Curly braces
print("{} and {} both are the best friend".format("Devansh","Abhishek"))

#Positional Argument
print("{1} and {0} best players ".format("Virat","Rohit"))
#Keyword Argument
print("{a},{b},{c}".format(a = "James", b = "Peter", c = "Ricky"))

