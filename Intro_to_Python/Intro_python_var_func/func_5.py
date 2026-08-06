"""def to_celsius(f):
    
    pass


## Don't touch below this line


def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")


test(100)
test(88)
test(104)
test(112)
"""



###SOL;
def to_celsius(f):
    
    return 5/9 * (f - 32)


## Don't touch below this line


def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")


test(100)
test(88)
test(104)
test(112)

#SIGUIENTE EJERCICIO; MISMO PROBLEMA ->
"""def hours_to_seconds(hours):
    
    return hours*3600


# Don't touch below this line


def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(25)
test(100)
test(33)"""
