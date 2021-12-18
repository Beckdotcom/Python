#  File: Report.py
#  Description:  a program that prints a data report in a specific format.
#  Student's Name: Rebecca Dong
#  Student's UT EID: RND528
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created: 3/2 9:11PM
#  Date Last Modified: 3/3 2:35PM

def main():

    # input data
    companyName = "Lone Star Corporation"
    date = "March 5, 2020"
    cash = 7505.54
    acctsRec = 502.21
    supplies = 313.89
    land = 6456.23
    buildings = 81598.00
    machAndEquip = 8329.99
    patents = 2000.00
    acctsPay = 93569.23
    stock = 88100.00

    #totals
    totalAssets =  cash + acctsRec + supplies + land + buildings + machAndEquip + patents
    totalLiaAndStockEquit = acctsPay + stock 
    
    
    #format
    print("")
    print(format(companyName.upper(),"^80s"))
    print(format("Balance Sheet","^80s"))
    print(format(date,"^80s"))
    print("")
    print(format("Liabilities and",">58s")+ format(" ","22s"))
    print(format("Assets","46s")+ format("Stockholders' Equity","46s"))
    print("-" * 80)
    print("   Cash" + format(cash,">33.2f") + format("   Liabilities:","47s"))
    print("   Accounts Receivable" + format(acctsRec,">18.2f") + "      Accounts Payable" + format(acctsPay,">18.2f"))
    print("   Supplies" + format(supplies,">29.2f") + format(" ","40s"))
    print("   Land"+ format(land,">33.2f")+ format(" ","40s"))
    print("   Buildings" + format(buildings,">28.2f") + format("      Stockholders' Equity:","40s"))
    print("   Machines and Equipment" + format(machAndEquip,">15.2f") + "         Capital Stock" + format(stock,">18.2f"))
    print("   Patents"+ format(patents,">30.2f")+ format(" ","40s"))
    print("")
    print("Total Assets" + format(totalAssets,">28.2f") + format("   Total Liabilities and","40s"))
    print(format("Stockholders' Equity",">66s") + format(totalLiaAndStockEquit,">14.2f"))
  
main()
