"""   Read bill amount as input. Calculate 12% of GST amount. Find
total amount to be paid. Read number of EMIs. Find emi amount to
be paid per month.    """



def emi_bill_cal():
    
 bill_Amount = float(input("enter the bill amount"))
 emis = int(input("enter the number of emis you want"))
 gst = bill_Amount / 100 *12
 totatl_bill_amount = bill_Amount + gst

 print(f"total gst amount is :{gst}")
 print(f"total billamount amount to be pay is :{totatl_bill_amount}")

 if emis > 0:
      emi_per_month = totatl_bill_amount / emis
 else :
     print(f"number of emi has to be greater the zero")
 print(f"total emi amount to be pay per month is :{emi_per_month} for {emis} months")


emi_bill_cal()



