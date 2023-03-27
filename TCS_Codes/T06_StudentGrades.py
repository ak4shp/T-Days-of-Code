#!/bin/python3
'''test cases
example 1
Input (stdin)
123
Rahul
3
80
70
80

Your Output (stdout)
76
B


example 2
Input (stdin)
200
Asha
4
90
90
80
60

Your Output (stdout)
80
A

'''
#------------- Solution ------------#
class Student:
    def __init__(self, roll, name, marks_list):
        self.roll = roll
        self.name = name
        self.marks_list = marks_list
        
    def calculate_percentage(self):
        return sum(self.marks_list)//len(self.marks_list)
    
    def find_grade(self):
        percentage = self.calculate_percentage()
        grade = ""
        if percentage >= 80:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "F"
        return grade
        

#Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    roll=int(input())
    name=input()
    count=int(input())
    marks=[]
    for i in range(count):
        marks.append(int(input()))
    s=Student(roll,name,marks)
    print(s.calculate_percentage())
    print(s.find_grade())