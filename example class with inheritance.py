#!/bin/python3

class Employee:
	def __init__(self, name, position, department, clearance):
		self.name = name
		self.position = position
		self.department = department
		self.clearance = clearance
	
	def show(self):
		print(f"Name: {self.name}, Position: {self.position}, Department: {self.department}, Clearance: {self.clearance}")
		if self.clearance == "tier1":
			print("Top secret clearance")
			
		elif self.clearance == "tier2":
			print("Government clearance")
		
		elif self.clearance == "tier3":
			print("Limited clearance")
		
		else:
			print("No clearance")			
			
class Employee1(Employee):
	def show(self):
		print(f"Name: {self.name}, Position: {self.position}, Department: {self.department}, Clearance: {self.clearance}")
		if self.clearance == "tier1":
			print("Top secret clearance")
			
		elif self.clearance == "tier2":
			print("Government clearance")
		
		elif self.clearance == "tier3":
			print("Limited clearance")
		
		else:
			print("No clearance")#
				
class Employee2(Employee):
	def show(self):
		print(f"Name: {self.name}, Position: {self.position}, Department: {self.department}, Clearance: {self.clearance}")
		if self.clearance == "tier1":
			print("Top secret clearance")
			
		elif self.clearance == "tier2":
			print("Government clearance")
		
		elif self.clearance == "tier3":
			print("Limited clearance")
		
		else:
			print("No clearance")#
			
class Employee3(Employee):
	def show(self):
		print(f"Name: {self.name}, Position: {self.position}, Department: {self.department}, Clearance: {self.clearance}")
		if self.clearance == "tier1":
			print("Top secret clearance")
			
		elif self.clearance == "tier2":
			print("Government clearance")
		
		elif self.clearance == "tier3":
			print("Limited clearance")
		
		else:
			print("No clearance")#
	
e1 = Employee("Bob", "developers", "management", "tier1")
e1.show()
print("\n" * 2)

e2 = Employee2("Alice", "developers", "developer", "tier2")
e2.show()
print("\n" * 2)

e3 = Employee3("Eve", "developers", "error", "tier3")
e3.show()
print("\n" * 2)