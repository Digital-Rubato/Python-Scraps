def firstfunc(one, two):

#this is also known as encapsulation to hide the function from the global
	def secondfunc(one):
		print("This is one: ", one)

#without the calls, the functions will not output
	secondfunc(one)

	def thirdfunc(two):
		print("This is two: ", two)

	thirdfunc(two)

one = 1

two = 2

#printing "print(firstfunc(one, two)) returns "None"
firstfunc(one, two)

#doesnt display because encapsulation
#"NameError: name 'secondfunc' is not defined
#secondfunc(one)

#class in function test

def funcclass(input):
	class Classfunc:
		def __init__(self, input):
			self.input = input
		def funcinthisclass(self):
			print("This is the funcinthisclass output: ", self.input)
# can call classes inside of function. and have them print out
	p1 = Classfunc(input)
	p1.funcinthisclass()

funcclass(30)

#cannot call class outside of function because of encapsulation
#p1 = funcinthisclass(25)

# can, of course, put the base function in a variable
#why does this, display without printing P1, and why doesn't it display when printing
p1 = funcclass(35)

print("this is the p1 variable: ",p1)
#prints as: this is the p1 variable: None

#does not work as a method
#p1.funcclass()