# Dictionaries
from pprint import pprint


def ch13_1():
    n = int(input('Enter number of employees : '))
    dict1 = {input("Enter the name of employee : "): input("Enter the salary of employee : ") for _ in range(n)}
    print(dict1)


def ch13_2():
    string = input('Enter a string : ')
    dict1 = {k: string.count(k) for k in sorted(string)}
    print(dict1)


def ch13_3():
    number = input('Enter the number to convert into words : ')
    dict1 = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven',
             '8': 'Eight', '9': 'Nine'}
    string = [dict1[i] for i in number]
    print(f"{number} in words : {" ".join(string)}")


def ch13_4():
    n = int(input("Enter number of teams : "))
    dict1 = {(k := input(f"Enter name of team {i + 1} : ")): [int(input(f"Enter number of wins for team {k} : ")),
                                                              int(input(f"Enter number of loses for team {k} : "))] for
             i in range(n)}
    print(dict1)
    win_per = {k: 100 * v[0] / sum(v) for k, v in dict1.items()}
    print(f"Win percentage of each team : {win_per}")
    list1 = [i[0] for i in dict1.values()]
    print(f"Number of wins by each team : {list1}")
    list2 = [i for i, j in dict1.items() if (j[0] - j[1]) > 0]
    print(f"Teams with more wins than loses : {list2}")


def ch13_5():
    dict1 = {}
    while True:
        product_names = input("Enter the name of product (or 'exit' to quit) : ").lower()
        if product_names == 'exit':
            break
        prices = float(input("Enter the price of product : "))
        dict1[product_names] = prices
    if dict1:
        while True:
            name_pro = input("Enter the name of product to check the price for (or 'exit' to break) : ").lower()
            if name_pro == 'exit':
                break
            print(dict1.get(name_pro, f"{name_pro.capitalize()} does not exist."))


def ch13_6():
    month_days = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31,
                  "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
    print(sorted(month_days), "\n")
    pprint({k: v for k, v in month_days.items() if v == 31})
    print()
    print(dict(sorted(month_days.items(), key=lambda x: x[1])))
    while True:
        month = input("Enter the name of month (or 'exit' to quit) : ").capitalize()
        if month == "exit":
            break
        if month in month_days:
            print(f"{month} contains {month_days[month]} days.")
        else:
            print("Enter the full name of month")


def ch13_7():
    # Yes we can store the details of 10 students in a dictionary
    stu_data = {"StuName":"rno name marks grade age".split()}


def ch13_8():
    dict1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
    # dict2 = {v:k for k,v in dict1.items()}
    dict2 = {}
    for i,j in dict1.items():
        dict2[j] = i
    pprint(dict1)
    pprint(dict2)


def ch13_9():
    d1 = {
        'name': 'Ayush',
        'age': 16,
        'subject': 'Physics',
        'city': 'Gorakhpur'
    }

    d2 = {
        'name': 'Ayush',
        'age': 16,
        'school': 'XYZ School',
        'hobby': 'Coding'
    }

    # Intersection of d1 and d2
    overlapping_keys = set(d1.keys()) & set(d2.keys())
    pprint(overlapping_keys)

def ch13_10():
    d1 = {'a': 10, 'b': 20, 'c': 10, 'd': 10, 'e': 10, 'f': 10}
    ctr = 0
    rep_values = set()
    for v in d1.values():
        if v not in rep_values:
            rep_values.add(v)
        else:
            ctr += 1
    ctr += 1 if ctr != 0 else 0
    if ctr:
        print(f"{ctr} keys have same values.")
    else:
        print("No keys have same values.")

def ch13_11():
    d1 = {1:11,2:12}
    d2 = {1:11,2:12,3:13,4:14}
    print(all(i in d2.items() for i in d1.items()))

def ch13_12():
    d1 = {'A':[1,2,3], 'B':[4,5,6]}
    d2 = {k:sum(v) for k,v in d1.items()}
    pprint(d2)

ch13_12()
