def GetTotalSalaryDeduction(grossSalary, loan, insurance) :
    return round(GetTax(grossSalary) + loan + insurance,2)

def GetTax(grossSalary) :
    return round((12/100)*grossSalary, 2)