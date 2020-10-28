employees = (
	{"name": 'James', "age": 40, "total_year": 10, "salary": 50000, "gender": 'male'},
	{"name": 'Suresh', "age": 30, "total_year": 5, "salary": 55000, "gender": 'male'},
	{"name": 'Kishore', "age": 50, "total_year": 2, "salary": 56000, "gender": 'male'},
	{"name": 'Jane', "age": 23, "total_year": 6, "salary": 52000, "gender": 'female'},
	{"name": 'Kevin', "age": 60, "total_year": 10, "salary": 40000, "gender": 'male'},
	{"name": 'Robin', "age": 50, "total_year": 12, "salary": 30000, "gender": 'male'},
	{"name": 'Robert', "age": 41, "total_year": 3, "salary":20000, "gender": 'male'},
	{"name": 'Rose', "age": 23, "total_year": 3, "salary": 60000, "gender": 'female'},
	{"name": 'Jack', "age": 44, "total_year": 5, "salary": 58000, "gender": 'male'},
	{"name": 'Morgan', "age": 55, "total_year": 7, "salary": 51000, "gender": 'female'},
	{"name": 'Ramesh', "age": 40, "total_year": 5, "salary": 10000, "gender": 'male'},
	{"name": 'Jerry', "age": 41, "total_year": 10, "salary": 30000, "gender": 'male'}
)


#class for employee.
class employee:
	def __init__(self,name,age,total_year,salary,gender):
		self.name=name
		self.age=age
		self.total_year=total_year
		self.salary=salary
		self.gender=gender

	def promotion (self):
			if self.total_year>5 and self.age>40:
				print(self.name)


#making objects of class employee.
print("\nemployees eligible for promotion: ")
emp=[]
for i in range(len(employees)):
	emp.append(employee(employees[i]['name'],employees[i]['age'],employees[i]['total_year'],employees[i]['salary'],employees[i]['gender']))
	emp[i].promotion()

#function for Find all employees who are senior (age > 45) using loops and functions
def find_senior(e):
	for i in range(len(e)):
		if e[i].age >45:
			print(e[i].name)

#calling the find_senior function.
print("\nemployees who are senior (age > 45)")
find_senior(emp)

#function for Find all employees who are females and age greater than 40
def find_female_g_40(e):
	for i in range(len(e)):
		if e[i].gender=="female" and e[i].age>40:
			print(e[i].name)

#calling the find_female_g_40() function.
print("\nemployees who are senior (age > 45)")
find_female_g_40(emp)

"""
emp = Employee(item)
Assignment
 - Find all employees who are senior (age > 45) using loops and functions
 - Find all employees who are females and age greater than 40
 - Build a method which should take each employees as input and only print the
 one who is eligible for promotion `criteria total_year greater than 5 and age is above
 40`
"""