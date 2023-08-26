#RE-phone number
import re
def func1(text):
   pattern1=r'[(?][0-9]{3}[)?]\-[0-9]{3}\-[0-9]{4}'
   pattern2=r'[0-9]{3}-[0-9]{3}-[0-9]{4}'
   match1=re.search(pattern1,text)
   match2=re.search(pattern2,text)
   if match1 or match2:
     print("Valid phone number")

   else:
     print("Invalid phone number")
text=str(input("Enter the phone number:"))
func1(text)

#RE- password
import re
def func1(text):
 pattern2=r'[A-Z]+'
 pattern3=r'[a-z]+'
 pattern4=r'[0-9]+'
 pattern5=r'[@ - / , .]+'
 match2=re.search(pattern2,text)
 match3=re.search(pattern3,text)
 match4=re.search(pattern4,text)
 match5=re.search(pattern5,text)
 if match2 and match3 and match4 and match5:
   print("Password Set Successfully")
 else:
   print("Set a Valid Password")
text=str(input("Enter password:"))
func1(text)

"""
OUTPUT:
Enter the phone number:987-654-3210
Valid phone number
Enter password:Abc@123
Password Set Successfully
"""