#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0 
        for x in my_list:
            print (x)
            count += 1
        print (count)
    except Exception as e :
        print(e, 'Error!') 


