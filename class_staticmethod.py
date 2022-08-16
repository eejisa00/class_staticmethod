class Student:
	fees = 10000
	def __init__(self, name, rollno, age ):
		self.name = name
		self.rollno = rollno
		self.age = age
	@classmethod
	def change_fees(cls,cost):
		cls.fees = cost
		return cls.fees
	@staticmethod
	def department(dep):
		l = ["ECE","EEE","CIVIL","Chemical"]
		if dep in l:
			return "True"
		return "False"
stu1 = Student("anu","1A87","19")
stu2 = Student("ajay","1B67","20")
stu3 = Student("vinay","1C56","18")
Student.change_fees(20000)
print(stu1.name)
print(Student.fees)
print(Student.department("ECE"))
		