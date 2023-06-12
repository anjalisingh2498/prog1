import time
def caltime(func):
	def inner(*args):
		st=time.time()
		print("Start time:- ", st)
		func()
		et=time.time()
		print("End time:- ", et)
		d=st-et
		print("Total time:- ",d)
	return inner

def Fibs():
	a,b=0,1
	while(1):
		yield a
		a,b=b,a+b

n=int(input("Enter the number:- "))
@caltime
def my():
	fib=Fibs()
	for f in range(n):
		print(next(fib))
if "__main__":
	my()
