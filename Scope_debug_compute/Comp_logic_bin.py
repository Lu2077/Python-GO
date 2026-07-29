"""A 1 in binary is the same as True, while 0 is False. So a bitwise operation is just a bunch of logical operations that are completed in tandem. When two binary numbers are "or"ed together, the result has a 1 in any place where either of the input numbers has a 1 in that place.

| is the bitwise "or" operator in Python. 5 | 7 = 7 and 5 | 2 = 7 as well!

0101 is 5
0010 is 2
0101
|
0010
=
0111

Guild Permissions
A "guild" is a team of 2-4 players. Here are the guild-specific permissions:

can_invite – Leftmost bit (0b1000)
can_kick – Second to leftmost bit (0b0100)
can_enter_dungeon – Second to rightmost bit (0b0010)
can_surrender – Rightmost bit (0b0001)
When players are in a guild together, they gain all the permissions of all the other members of the guild!

For example, if:

Jack has the can_invite permission: 0b1000
Jill has the can_kick permission: 0b0100
Then, when they are in a guild together, they should both have the can_invite and can_kick permissions: 0b1100.

Assignment
Complete the calculate_guild_perms function. It takes as input four binary numbers representing the separate permissions of each member of the guild: glorfindel, galadriel, elendil and elrond. It should return a single binary number that represents the combined permissions of all the members of the guild.

Use a series of bitwise "or" operations to calculate the union of all the member's permissions.

----------->

def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    return 
"""

##------------------------------------1ST_Try-----------------------------------------
"""
def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    glorfindel = 0b1000
    galadriel = glorfindel #= 0b0100
    elendil = 0b0010
    elrond = 0b0001
    return glorfindel | galadriel | elendil | elrond

run_cases = [
    (0b0001, 0b0010, 0b0001, 0b1011, 0b1011),"""
##-------------------------------------SOL----------------------------------------------   
def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    #glorfindel = 0b1000
    #galadriel = glorfindel #= 0b0100
    #elendil = 0b0010
    #elrond = 0b0001
    return glorfindel | galadriel | elendil | elrond

"""run_cases = [
    (0b0001, 0b0010, 0b0001, 0b1011, 0b1011),"""
    
##------------------------------------------------------------------->

"""
from main import calculate_guild_perms

run_cases = [
    (0b0001, 0b0010, 0b0001, 0b1011, 0b1011),
]

submit_cases = run_cases + [
    (0b0000, 0b0000, 0b0000, 0b1011, 0b1011),
    (0b1001, 0b0010, 0b1101, 0b1011, 0b1111),
]


def test(input1, input2, input3, input4, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
    result = calculate_guild_perms(input1, input2, input3, input4)
    print(f"Expected: {expected_output}")
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

main()"""
