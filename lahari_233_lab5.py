#Zero division error
try:
  a=int(input("Enter 1st number=")) 
  b=int(input("Enter 2nd number="))
  c=a/b
  print(c)
except ZeroDivisionError as e:
  print(e)

#indexError
try:
  arr1=["Lahari","R",1,2]
  print(arr1[4])
  print(arr1[3])
  a=int(input("Enter 1st number="))
  b=int(input("Enter 2nd number="))
  if(b==0):
    raise ZeroDivisionError("ZeroDivisionError")
  else:
    print(a/b)
except IndexError as e:
  print(e)
finally:
  print("The code ran successfully")

"""
OUTPUT:
Enter 1st number=3
Enter 2nd number=4
0.75
list index out of range
The code ran successfully
"""