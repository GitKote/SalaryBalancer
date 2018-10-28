""" when i enter salary --

salary -deductions = balance
"""
import os
os.system('CLS')
salary_credited=int(input("enter the salary\n"))
deductions ={'HDFC':13112 , 'ICICI':12120, 'RENT':5500}
cuttings=sum([j for i,j in deductions.items()])
#sum (cuttings)
print ("Savings will be",salary_credited-cuttings)
