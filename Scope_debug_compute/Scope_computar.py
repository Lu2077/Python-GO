"""
Complete the total_xp function. It accepts two integers as input:

level
xp_to_add
There are 100 xp per level. total_xp should convert the current level to xp, then add this current xp to the xp_to_add argument and return the player's total xp. For example:

If a player is level 1 and gains 100 xp, they have 200 total xp.
If a player is level 2 and gains 250 xp, they have 450 total xp.
If a player is level 170 and gains 590 xp, they have 17590 total xp.
###Se utilizan las variables de la función, que luego es llamada desde otra
###En otro Script
###main.py
def total_xp(level, xp_to_add):
    pass
    
"""
#---------------------------Aquí importamos la función y el calculo xp------------------------------
"""
from main import total_xp

run_cases = [
    (1, 200, 300),
    (2, 50, 250),
]

submit_cases = run_cases + [
    (0, 0, 0),
    (0, 200, 200),
    (176, 350, 17950),
    (250, 100, 25100),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expected: {expected_output}")
    result = total_xp(input1, input2)
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
"""

###-----------------SOL----------------------------------------->
def total_xp(level, xp_to_add):
    level = level*100
    xp_to_add = level + xp_to_add
    return xp_to_add 
    
    
#-------------------Output--------------------------------------->
"""
---------------------------------
Inputs: 1, 200
Expected: 300
Actual:   300
Pass
---------------------------------
Inputs: 2, 50
Expected: 250
Actual:   250
Pass
---------------------------------
Inputs: 0, 0
Expected: 0
Actual:   0
Pass
---------------------------------
Inputs: 0, 200
Expected: 200
Actual:   200
Pass
---------------------------------
Inputs: 176, 350
Expected: 17950
Actual:   17950
Pass
---------------------------------
Inputs: 250, 100
Expected: 25100
Actual:   25100
Pass
============= PASS ==============
6 passed, 0 failed
"""

