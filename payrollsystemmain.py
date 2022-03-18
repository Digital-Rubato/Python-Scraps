import payrollsystem as ps

salary_employee = ps.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = ps.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = ps.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
payroll_system = ps.PayrollSystem()
payroll_system.calculate_payroll([
	salary_employee,
	hourly_employee,
	commission_employee
])

#Notice that the Employee base class doesn't define a .calculate_payroll() method. Meaning that if you were to create a plain Employee obj and pass it to the Payroll System, then you would get an error

'''
employee = ps.Employee(1, 'Invalid')

payroll_system = ps.PayrollSystem()
payroll_system.calculate_payroll([employee])
'''

#this does not work b/c it can't .calculate_payroll() for an Employee. To meet the requirements of the PSystem, you'll want to convert the employee class, which is currently a concrete class, to an abstract class. That way, no employee is never just an employee, but one that implements .calculate_payroll()

#the employee base class is called an abstract base class. The ABC exists to be inherited, but never instantiated. Python provides the abc module to define abstract base classes.


#employee = ps.Employee(1, 'abstract')


#disgruntled employee example

salary_employee = ps.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = ps.HourlyEmployee(2, 'Jane Doe', 40,15)
commission_employee = ps.CommissionEmployee(3, 'Kevin Bacon', 1000,250)
disgruntled_employee = ps.DisgruntledEmployee(20000, 'Anon')
payroll_system = ps.PayrollSystem()
payroll_system.calculate_payroll([
	salary_employee,
	hourly_employee,
	commission_employee,
	disgruntled_employee
	])