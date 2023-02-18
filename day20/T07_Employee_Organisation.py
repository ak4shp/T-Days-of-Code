#!/bin/python3
'''tesyt cases

example 1
Input (stdin)
1
AAA
123
25
M
120
30

Your Output (stdout)
1
-1
0


example 2
Input (stdin)
1
BBB
100
20
F
100
10

Your Output (stdout)
1
20
1
'''

#------------ Solution --------------#

class Employee:
    def __init__(self, name, emp_id, age, gender):
        self.name = name
        self.id = emp_id
        self.age = age
        self.gender = gender
        
        
class Organisation:
    def __init__(self, name, emp_list):
        self.name = name
        self.emp_list = emp_list
        
    def addEmployee(self, name, id, age, gender):
        new_emp = Employee(name, id, age, gender)
        self.emp_list.append(new_emp)
        
    def getEmployeeCount(self):
        return len(self.emp_list)
    
    def findEmployeeAge(self, id):
        for emp in self.emp_list:
            if id == emp.id:
                return emp.age
        return -1
    
    def countEmployees(self, age):
        ct = 0
        for emp in self.emp_list:
            if emp.age > age:
                ct += 1
        return ct
                
        
        
if __name__ == '__main__':
    employees=[]
    o = Organisation('XYZ',employees)
    n=int(input())
    for i in range(n):
        name=input()
        id=int(input())
        age=int(input())
        gender=input()
        o.addEmployee(name,id,age,gender)

    id=int(input())
    age=int(input())
    print(o.getEmployeeCount())
    print(o.findEmployeeAge(id))
    print(o.countEmployees(age))