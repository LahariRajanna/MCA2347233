#stringsplit function

def str1(stringsplit):
    parts = stringsplit.split('_')
    if len(parts) != 3:
        return None  
    dict1 = {
        'Name': parts[0],
        'Domain': parts[1],
        'Register': parts[2]
    }
    
    return dict1

str2 = "Lahari R_Railways Management System_2347233"
Output = str1(str2)
if Output is not None:
    print(Output)
else:
    print("Not Defined")


""" OUTPUT:
{'Name': 'Lahari R', 'Domain': 'Railways Management System', 'Register': '2347233'} """