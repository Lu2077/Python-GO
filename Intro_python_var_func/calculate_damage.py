def calculate_damage(opening_attack, core_damage, finishing_move):
    total = opening_attack + core_damage + finishing_move
    return total

stab_damage = calculate_damage(10, 20, 30)
slash_damage = calculate_damage(5, 10, 15)
fireball_damage = calculate_damage(50, 60, 70)
print(stab_damage)
print(slash_damage)
print(fireball_damage)



"""
Boots:
How many times is the calculate_damage function called and where are the results stored?

user:
3

Boots:
You're partway there. You've correctly identified that the function is called three times.

Now, take another look at those three lines where calculate_damage is being called. When each call finishes and returns its total, what happens to that returned value? Where does it land?

user:
it lands on on stab_damage, slash_damage and fireball_damage

Boots:
Excellent work. You nailed it: the calculate_damage function is called three times, and each returned total is stored in the stab_damage, slash_damage, and fireball_damage variables respectively."""
