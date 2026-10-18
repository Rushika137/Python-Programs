import json 
import os
def expense_tracker():
   while True:
      print("=======EXPENSE TRACKER=======")
      print("1.Add expense")
      print("2.View all expenses")
      print("3.search Expense")
      print("4.Update expense")
      print("5.Delete Expense")
      print("6.Total Expense")
      print("7.Categroy-Wise-Expenses")
      print("8.Monthly Expenses")
      print("9.Exit")
      while True:
         task=int(input("Enter the task number"))
         if task<0 or task<10:
            break
         else:
            print("enter between 1 to 9")
      
            