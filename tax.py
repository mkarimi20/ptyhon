usd_to_afs = 80
currnet_income = 1500
income_in_afs = usd_to_afs*currnet_income
def tax_calculator(income_in_afs):
    if income_in_afs >= 100000:
        tax_in_afs = (((income_in_afs) - 100000) * (20/100)) + 8900
        print("your tax in Afghani will be " + str(tax_in_afs))
        tax_in_usd = tax_in_afs/usd_to_afs
        print("your tax in USD will be " + str(tax_in_usd))
    elif income_in_afs >= 12500:
        tax_in_afs = (((income_in_afs) - 100000) * (10/100))
        print("your tax in Afghani will be" + str(tax_in_afs))
        tax_in_usd = tax_in_afs/usd_to_afs
        print("your tax in USD will be" + str(tax_in_usd))
    else:
        pass
print(tax_calculator(income_in_afs))