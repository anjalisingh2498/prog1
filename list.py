while True:
	q=int(input("1.List Operation \n 2. Set Operation \n 3.Exit"))
	if q==1:
		f1=1
		n=int(input("Enter the length of the list:- "))
		lst=[]
		for i in range(n):
			m=int(input("Enter the number:- "))
			lst.append(m)
		print(lst)

		while f1==1:
			print("Menu")
			print("1.Insert element \n 2.Remove element \n 3.Reverse element \n 4.Pop Element \n 5.Append element \n 6.Slicing \n 7.In \n 8. Not In \n 9.Copy \n 10. sorted \n 11.clear \n 12.Extend")
			ch=int(input("Enter the choice :- "))
			if ch==1:
				m=int(input("Enter the index position:;- "))
				n=int(input("Enter the element:- "))
				lst.insert(m,n)
				print(lst)
			elif ch==2:
				n=int(input("Enter the element:- "))
				lst.remove(n)
				print(lst)
			elif ch==3:
				lst.reverse()
				print(lst)
			elif ch==4:
				lst.pop()
				print(lst)
			elif ch==5:
				n=int(input("Enter the element:- "))
				lst.append(n)
				print(lst)
			elif ch==6:
				a=int(input("Enter the start postion:- "))
				b=int(input("Enter the end position:- "))
				print(lst[a:b])
			elif ch==7:
				a=int(input("Enter the element:- "))
				print('a' in lst)
			elif ch==8:
				b=int(input("Enter the element:- "))
				print('b' not in lst)
			elif ch==9:
				print("Copy List:- ", lst.copy())
			elif ch==10:
				lst.sort()
				print("Sorted list:- ", lst)
			elif ch==11:
				print("Clear list:- ", lst.clear())
			elif ch==12:
				l=[33,21,30]
				lst.extend(l)
				print("Extend List:- ", lst)
			else:
				break
	elif q==2:
		f2=1
		set1=set(input("Enter the element:- ").split())
		set2=set(input("Enter the element:- ").split())
		print(set1)
		print(set2)

		while f2==1:
			print("Menu")
			print("1.Union set \n 2.Intersection set \n 3.Difference Set \n 4.Subset \n 5.Proper Subset \n 6.Symmetric Difference \n 7.Superset \n 8.Proper Superset \n 9. Equivalent set \n 10.Not Equivalent \n 11.In \n 12.Not In")
			ch=int(input("Enter the choice:- "))
			if ch==1:
				print("Union Set:- ", set1 | set2)
			elif ch==2:
				print("Intersection Set:- ", set1 & set2)
			elif ch==3:
				print("Difference Set:- ", set1 - set2)
			elif ch==4:
				print("Subset:- ", set1 <= set2)
			elif ch==5:
				print("Proper Subset:- ", set1 < set2)
			elif ch==6:
				print("Symmetric Difference:- ", set1 ^ set2)
			elif ch==7:
				print("Superset:- ", set1 >= set2)
			elif ch==8:
				print("Proper Superset:- ", set1 > set2)
			elif ch==9:
				print("Equivalent Set:- ", set1==set2)
			elif ch==10:
				print("Not Equivalent Set:- ", set1!=set2)
			elif ch==11:
				print("In :- ", 4 in set1)
			elif ch==12:
				print("Not In:- ",55 not in set1)
			else:
				break
	else:
		exit()
