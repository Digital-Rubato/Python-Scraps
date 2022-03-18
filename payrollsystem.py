#in hr.py
#https://realpython.com/inheritance-composition-python/

class PayrollSystem:
	def calculate_payroll(self, employees):
		print('Calculating Payroll')
		print(20*'-')
		for employee in employees:
			print(f'Payroll for: {employee.id} - {employee.name}')
			print(f' - Check amount: {employee.calculate_payroll()}')
			print('')

#in hr.py
#Base class for all employee types(must have an id and name to ccalculate)
class Employee:
	def __init__(self, id, name):
		self.id = id
		self.name = name

#derived class that inherits Employee
#super() is used to initalize members of the base class. 
#super() gives you access to methods in a superclass from the subclass that inherits from it.
#alone it returns a temp obj of the superclass that then allows you to call that superclass's methods and extends the functionality of previously built classes
#super() saves you from needing to reweite those methods in your subclass, and allows you to swap out superclasses with minimal changes in code
#see superclass.py for more

class SalaryEmployee(Employee):
	def __init__(self, id, name, weekly_salary):
		super().__init__(id,name)
		self.weekly_salary = weekly_salary

	def calculate_payroll(self):
		return self.weekly_salary

#initialized with id and name (from base class Employee) with hours_worked and hour_rate to calc. 
class HourlyEmployee(Employee):
	def __init__(self, id, name, hours_worked, hour_rate):
		super().__init__(id,name)
		self.hours_worked = hours_worked
		self.hour_rate = hour_rate

	def calculate_payroll(self):
		return self.hours_worked * self.hour_rate

#derived from SalaryEmployee b/c both classes have a weekly_salary
class CommissionEmployee(SalaryEmployee):
	def __init__(self, id, name, weekly_salary, commission):
		super().__init__(id, name, weekly_salary)
		self.commission = commission

	def calculate_payroll(self):
		fixed = super().calculate_payroll()
		return fixed + self.commission

from abc import ABC, abstractmethod

class Employee(ABC):
	def __init__(self, id, name):
		self.id = id
		self.name = name

#decorator for .calculate_payroll() method
	#make sure employee cant be created. 
	#Telling other devs working on the 'hr' module that if employee is derived, then they must override .calculate_payroll() abstract method
	#without the '@' symbol the program will execute 'as normal' or will not display an error message
	@abstractmethod
	def calculate_payroll(self):
		pass

#duck typing: if it behaves like a duck, then it's a duck.

#to illustrate: An object that implements the desired "interface" can be used in place of another obj. Hence duck typing

#example:

class DisgruntledEmployee:
	def __init__(self,id,name):
		self.id = id
		self.name = name

	def calculate_payroll(self):
		return 1000000

#the DE class does not derive from the Employee base class but carries the same interface(elements) required by the calculate_payroll() method

#Remember: PayrollSystem.calculate_payroll() requires - 
#an ID property
#a name property
#and the .calculate_payroll() method (does not take any params and returns the payroll amount to process)