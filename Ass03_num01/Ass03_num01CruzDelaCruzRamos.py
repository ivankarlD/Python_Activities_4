import GrossSalary as GrossSalary
import NetSalary as NetSalary
import OvertimePay as OvertimePay
import SalaryDeductions as SalaryDeductions

name = str(input("Name: "))
rate = int(input("Rate: "))
WHours = int(input("Number of Hours: "))
OHours = int(input("Overtime Hours: "))
gs = GrossSalary.GetGrossSalary(rate, WHours, OHours)

print(f"Gross Salary: {gs}")
print(f"\nTax: {SalaryDeductions.GetTax(gs)}")
loan = int(input("Loan: "))
insurance = int(input("Insurance: "))
sd = SalaryDeductions.GetTotalSalaryDeduction(gs, loan, insurance)
print(f"\nTotal Deductions: {sd}")
print(f"\nNet Salary: {NetSalary.GetNetSalary(gs, sd)}")
