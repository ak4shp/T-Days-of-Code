# Employees Bonus
class Employee:
    def __init__(self, name:str, designation:str, salary:int, overtime:dict) -> None:
        self.employee_name = name
        self.designation = designation
        self.salary = salary
        self.overTimeContribution = overtime
        self.overTimeStatus = False


class Organisation:
    def __init__(self) -> None:
        self.employee_list = []
        self.employee_overtime = []


    def set_emp_to_org(self, emp:object):
        self.employee_list.append(emp)


    def set_eligible_employee(self, ot_threshold:int):
        for a_emp in self.employee_list:
            total_overtime = 0
            for overtime in a_emp.overTimeContribution.values():
                total_overtime += overtime

            self.employee_overtime.append(total_overtime)
            if total_overtime >= ot_threshold:
                a_emp.overTimeStatus = True


    def get_total_bonus(self, rate:int)-> int:
        total_bonus = 0
        for idx, a_emp in enumerate(self.employee_list):
            if a_emp.overTimeStatus == True:
                bonus = self.employee_overtime[idx] * rate
                total_bonus += bonus

        return total_bonus


organisation = Organisation()
t = int(input())
for _ in range(t):
    name = input()
    designation = input()
    salary = int(input())
    month_count = int(input())

    overtime = {}
    for i in range(month_count):
        month = input()
        ot = int(input())
        overtime[month] = ot

    new_emp = Employee(name, designation, salary, overtime)
    organisation.set_emp_to_org(new_emp)
  
    
threshold_overtime = int(input())
rate_per_hour = int(input())

organisation.set_eligible_employee(threshold_overtime)
bonus_amount = organisation.get_total_bonus(rate_per_hour)

for i in range(t):
    emp = organisation.employee_list[i].employee_name
    status = organisation.employee_list[i].overTimeStatus
    print(emp, status)
    
print(bonus_amount)
