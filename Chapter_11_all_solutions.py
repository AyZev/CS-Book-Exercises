# Will use list comprehension in this part

def ch11_1():
    l = [int(input(f"Enter the value {i + 1} : ")) for i in range(5)]
    n = int(input("Enter the number for incrementation : "))
    il = [i + n for i in l]
    print(il)


def ch11_2():
    l = [int(input(f"Enter the value {i + 1} : ")) for i in range(5)]
    l.reverse()
    print(l)


def ch11_3():
    l1 = [int(input(f"Enter the value {i + 1} of list 1 : ")) for i in range(5)]
    l2 = [int(input(f"Enter the value {i + 1} of list 2 : ")) for i in range(5)]
    l3 = l1 + l2
    print(l3)


def ch11_4():
    l1 = [int(input(f"Enter the value {i + 1}(in the range 1 and 12) : ")) for i in range(5)]
    l2 = [10 if i > 10 else i for i in l1]
    print(l2)


def ch11_5():
    l = [input(f"Enter the string {i + 1} : ") for i in range(5)]
    l0 = [i[1:] for i in l]
    print(l0)


def ch11_6():
    l = [int(input(f"Enter the string {i + 1} : ")) for i in range(5)]
    num = int(input("Enter the number to check : "))
    if num in l:
        print(f"Index of num in list : {l.index(num)}")
    else:
        print(f"{num} does not index in the list.")


def ch11_7():
    a = [i for i in range(0, 50)]
    b = [i ** 2 for i in range(1, 51)]
    c = [chr(65 + i) * i for i in range(26)]
    print(f"{a}\n{b}\n{c}")


def ch11_8():
    l1 = [int(input(f"Enter the value {i + 1} for list 1 : ")) for i in range(3)]
    l2 = [int(input(f"Enter the value {i + 1} for list 2 : ")) for i in range(3)]
    l3 = [j + k for j, k in zip(l1, l2)]


def ch11_9():
    l = [1, 2, 3, 4, 5]
    l0 = [l[-1]] + l[:-1]
    print(l0)


def ch11_10():
    n = int(input("Enter the term to calculate : "))
    fibonacci = [0, 1]
    for i in range(n - 1):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(f"The {n}th term of the fibonacci series is : {fibonacci[-1]}")


def ch11_11():
    l = eval(input("Enter a list : "))
    if len(l) > 1:
        print(f"The length of the longest string : {max(l, key=len)}")
    else:
        print("There should be at least two or more elements in the list.")


def ch11_12():
    l = eval(input("Enter a integer type list : "))
    num = int(input("Enter the num to increment each element : "))
    l0 = [i + num for i in l]
    print(l0)


def ch11_13():
    l = [int(input(f"Enter the value {i + 1} : ")) for i in range(5)]
    ll = int(input("Enter the lower limit : "))
    ul = int(input("Enter the upper limit : "))
    print(f"The maximum number in the list from index {ll} to index {ul} is {max(l[ll:ul])}")
    print(f"The minimum number in the list from index {ll} to index {ul} is {min(l[ll:ul])}")


def ch11_14():
    l = [5, 3, 7, 2, 8, 3, 9, 10, 7]
    result = []
    duplicates = []
    for i in l:
        if l.count(i) == 1:
            result.append(i)
        else:
            duplicates.append(i)
    print(result + duplicates)


def ch11_15():
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l2 = [1, 2, 3, 4, 5, 6, 7, 88, 9, 10]
    for i in range(min((len(l1), len(l2)))):
        if l1[i] != l2[i]:
            break
    print(f"Index at where both the lists differ : {i}")

ch11_15()