class Employee:
    def __init__(self, name:str, des:str, sal:int, ot_con:dict):
        self.emp_name = name
        self.des = des
        self.salary = sal
        self.ot_con = ot_con
        self.ot_status = False
        # self.t_ot = 0


class Organization:
    def __init__(self, emps:list):
        self.emps = emps
        self.emp_ot = []


    def set_status(self, th):
        for e in self.emps:
            total_ot = 0
            for v in e.ot_con.values():
                total_ot += v

            if total_ot >= th:
                e.ot_status = True
            # e.t_ot = total_ot
            self.emp_ot.append(total_ot)


    def get_total_ot(self, rate):
        total_ot_paid = 0
        idx = 0
        for e in self.emps:
            if e.ot_status == True:
                emp_ot = self.emp_ot[idx]
                total_ot_paid += emp_ot
            idx += 1

        return total_ot_paid * rate

# main

emps = []
# inputs
t = int(input()) 
while t:
    t-=1

    name = input()
    des = input()
    sal = int(input())

    n = int(input())
    ot_con = {}
    for _ in range(n):
        mn = input()
        ot = int(input())
        ot_con[mn] = ot
        
    a_emp = Employee(name, des, sal, ot_con)
    emps.append(a_emp)


org = Organization(emps)
ot_th = int(input())
rate = int(input())

#functions call
org.set_status(ot_th)
bonus = org.get_total_ot(rate)


# outputs
for e in emps:
    print(e.emp_name, e.ot_status)

print(bonus)