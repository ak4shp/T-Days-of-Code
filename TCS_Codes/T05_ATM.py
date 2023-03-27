''' #---- Sort dict by values acsending ----#

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
converted_dict = dict(sorted_footballers_by_goals)
'''

class Account:
  def __init__(self, cardNumber, pin, balance, wdAmount, acType):
    self.cardNumber = cardNumber
    self.pin = pin
    self.balance = balance
    self.wdAmount = wdAmount
    self.acType = acType
    
  def set_balance(self, wth_amnt):
    if wth_amnt <= self.balance:
      self.balance -= wth_amnt
      self.wdAmount = wth_amnt
      
    
class ATM:
  def __init__(self, acList):
    self.branch = ""
    self.acList = acList
    
    
  def check_atm(self, cardNum, pin, wth_amnt):
    for a_ac in self.acList:
      card = a_ac.cardNumber
      ac_pin = a_ac.pin
      if card == cardNum and ac_pin == pin:
        a_ac.set_balance(wth_amnt)
        return a_ac
    return None
      
    
  def filter(self, ac_type):
    ans_dict = {}
    for ac in self.acList:
      type_ac = ac.acType
      if type_ac.lower() == ac_type.lower():
        ans_dict[ac.cardNumber] = ac.balance
          
    sr = sorted(ans_dict.items(), key=lambda x:x[1])
    final_ans = dict(sr)
    if len(final_ans):
      return final_ans
    return None
  
#main

t = int(input())
acc_objs = []
for _ in range(t):
  crd = int(input())
  pn = int(input())
  bl = float(input())
  wd_amt = float(input())
  actyp = input()
  
  new_ac = Account(crd, pn, bl, wd_amt, actyp)
  acc_objs.append(new_ac)
  
atm = ATM(acc_objs)

t_card = int(input())
t_pin = int(input())
t_wth = float(input())

holder = atm.check_atm(t_card, t_pin, t_wth)

if holder:
  print(holder.cardNumber, holder.balance, holder.wdAmount)
else:
  print("No account Exists")

acc_tp = input()
val = atm.filter(acc_tp)
if val:
  for k, v in val.items():
    print(k, v)
else:
  print("No match Found")


'''Input:
2
12345
12
30.0
10.0
salary
45678
98
400.0
200.0
salary
45678
98
100.0
salary

Output:
45678 300.0 100.0
12345 30.0
45678 300.0

'''