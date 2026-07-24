"""
Assignment
Complete the take_magic_damage function. It should return the new health after calculating how much magic-type damage the player takes. Here is a description of the parameters:

health: The player's starting health
resist: The player's magic resistance. This reduces the damage they take by a static amount
amp: The attacker's magic amplification. This increases the damage they deal by a multiplier
spell_power: The base damage of the spell
First, calculate the total maximum damage to be inflicted by multiplying the spell_power by the amp. Then, subtract the resist from the total damage to get the actual damage dealt. Apply that damage to the player's health and return the new health.
----Pasar-la-funcion-----
def take_magic_damage(health, resist, amp, spell_power):
    pass
    
a; 

from main import take_magic_damage

run_cases = [
    (100, 5, 2, 20, 65),
    (200, 10, 1, 25, 185),
]

submit_cases = run_cases + [
    (0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1),
    (100, 2, 3, 1, 99),
    (2500, 3, 2, 2, 2499),
]


def test(input1, input2, input3, input4, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
    result = take_magic_damage(input1, input2, input3, input4)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


	... etc ...
	
def main()

	.
	.
	.
	.
main()
"""

####------------------SOl---------------------------------


def take_magic_damage(health, resist, amp, spell_power):
    health = health
    resist = resist
    spell_power = spell_power*amp-resist
    spell_power = health - spell_power
    return spell_power


""""
ALSO

Process for Solving Hard Coding Problems
Read the lesson first! Figure out the examples before writing your own code.
Read the assignment. Understand the goal of the assignment before you start writing code.
Start writing code.
Add print() statements. Don't wait until you've written a lot of code to start testing. Add print() statements and use the Run button to see if your code is doing what you expect at each step. It's easier to find issues in small bits of code than in large blocks of code.
Keep running, printing, and fixing until you're confident your code is working.
Submit your code. If the assignment you're working on has unit tests, no need to remove your debugging print() statements. If the assignment you're working on is testing console output, be sure to remove your print() statements before submitting.
Compare your code to the instructor's. You will not be penalized for looking at the solution after you have successfully completed the assignment.
"""
