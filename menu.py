str1=input("Enter the first input:-")
str2=input("Enter the second input:- ")
while True:
 print("Menu")
 print("1.Concatenation")
 print("2.Length")
 print("3.Repetition")
 print("4.Formatting")
 print("5.maximum of string")
 print("6.minimun of string")
 print("7.upper")
 print("8.lower")
 print("9.Reverse of string")
 print("10.Split a string into the list:-")
 print("11.Sorted:- )
 ch=int(input('Enter the menu number:- ')
 if ch==1:
  print(str1+str2)
 elif ch==2:
  print(len(str1))
 elif ch==3:
  print(str1*10)
 elif ch==4:
  print(The string:- %s" %(str1))
 elif ch==5:
  print(max(str1))
 elif ch==6:
  print(min(str1))
 elif ch==7:
  print(str1.upper())
 elif ch==8:
  print(str1.lower())
 elif ch==9:
  print(str1[::-1])
 elif ch==10:
  print(str1.split())
 elif ch==11:
  print(sorted(str1))
 else:
  exit()
