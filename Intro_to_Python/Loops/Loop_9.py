#----------FIX-------->
def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += 1 
    return total
    
"""
ANSWER;
def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i 
    return total
"""

#--------FIX----------->
def sum_of_odd_numbers(end):
    total = 0
    for i in range(0,end):
        total += i
    return total
  
"""
ANSWER;
def sum_of_odd_numbers(end):
    total = 0
    for i in range(total+1,end,2):
        total += i
    return total
"""
