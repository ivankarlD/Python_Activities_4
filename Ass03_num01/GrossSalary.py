import OvertimePay as OvertimePay


def GetGrossSalary(rate, WHours, OHours) :
    ot = OvertimePay.GetOvertimePay(rate, OHours)
    return round((rate*WHours)+ot, 2)