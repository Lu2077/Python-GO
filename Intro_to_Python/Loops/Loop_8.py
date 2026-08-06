def count_down(start, end):
    for i in range(start, end, -1):
        print(i)


# Don't edit below this line


def test(start, end):
    print(f"Using inputs start: {start} and end: {end}")
    print(f"Printing numbers from {start} to {end + 1}:")
    count_down(start, end)
    print("=====================================")


def main():
    test(10, 0)
    test(20, 10)
    test(15, 11)


main()
"""
---------OUTPUT
Using inputs start: 10 and end: 0
Printing numbers from 10 to 1:
10
9
8
7
6
5
4
3
2
1
=====================================
Using inputs start: 20 and end: 10
Printing numbers from 20 to 11:
20
19
18
17
16
15
14
13
12
11
=====================================
Using inputs start: 15 and end: 11
Printing numbers from 15 to 12:
15
14
13
12
====================================="""
