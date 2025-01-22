# TODO : Complete the 15 functions today


def ch12_1():
    n = 9
    tup1 = 0, 1
    for i in range(n - 1):
        tup1 += tup1[-2] + tup1[-1],
    print(tup1)


def ch12_2_a():
    tup = 7, 0, 6, 9, 4, 5
    index = int(input("Enter the index to check : "))
    print(tup[index])


def ch12_2_b():
    term = int(input("Enter the fibonacci term to check : "))
    tup1 = 0, 1
    found = False
    while True:
        tup1 += tup1[-2] + tup1[-1],
        if tup1[-1] == term:
            found = True
            break
        elif tup1[-1] > term:
            break
    if found:
        print(f"The position of the term {term} in the fibonacci series is {len(tup1)}.")
    else:
        print(f"The term {term} does not exist in the fibonacci series.")


def ch12_3():
    tup_min = float("inf")
    tup_max = float("-inf")
    n = int(input("Enter number of elements in the tuple : "))
    tup = tuple(int(input(f"Enter the value of element {i + 1} : ")) for i in range(n))
    for i in tup:
        if i > tup_max:
            tup_max = i
        if i < tup_min:
            tup_min = i
    print(f"Given tuple : {tup}")
    print(f"The maximum number in the tuple is {tup_max}.")
    print(f"The minimum number in the tuple is {tup_min}.")


def ch12_4():
    stu_data = ()
    n = int(input("Enter the number of students : "))
    for i in range(n):
        roll_no = input(f"Enter the roll no. of student {i + 1} : ")
        name = input(f"Enter the name of student {i + 1} : ")
        marks = input(f"Enter the total marks of student {i + 1} : ")
        stu_data += (roll_no, name, marks),
    print(stu_data)


class StuData:
    def __init__(self):
        # ch12_5
        self.n = int(input("Enter number of students : "))
        self.marks = tuple(
            tuple((int(input(f"Enter your marks in subject {i} for student {j + 1} : ")) for i in range(1, 4))) for j in
            range(self.n))
        print(self.marks)

    def ch12_6(self):
        data = ("Total Marks", "Average Marks"),
        for i in self.marks:
            data += (sum(i), (sum(i) / len(i))),
        print(data)


def ch12_7():
    tup1 = eval(input("Enter tuple 1 : "))
    tup2 = eval(input("Enter tuple 2 : "))
    tup3 = tup1 + tup2
    print(f"{tup3 = }")


def ch12_8():
    tup = eval(input("Enter tuple : "))
    if tup:
        print(f"Shortest character : {min(tup, key=len)}")
    else:
        print("It should contain at least one character.")


def ch12_9():
    tup1 = tuple(i * i for i in range(1, 51))
    print(f"{tup1 = }")
    tup2 = tuple(chr(i + 96) * i for i in range(1, 27))
    print(f"{tup2 = }")


def ch12_10():
    # tup = ((2, 5), (4, 2), (9, 8), (12, 10))
    n = int(input("Enter number of pairs : "))
    tup = tuple(eval(input(f"Enter tuple {i + 1} : ")) for i in range(n))
    even_pairs = tuple()
    even = 0
    for i in tup:
        if all(j % 2 == 0 for j in i):
            even_pairs += i,
            even += 1
    print(f"{even_pairs = }")
    print(f"Number of even pairs : {even}")


def ch12_11():
    seq_a = eval(input("Enter tuple A : "))
    seq_b = eval(input("Enter tuple B : "))
    for i in seq_a:
        if i not in seq_b:
            print(False)
            break
    else:
        print(True)


def ch12_12():
    tup1 = eval(input("Enter the tuple : "))
    print(f"Mean of tuple : {sum(tup1) / len(tup1)}")


def ch12_13():
    from statistics import mode
    tup1 = eval(input("Enter the tuple : "))
    get_mode = lambda tup: max(tup, key=tup.count)
    if get_mode(tup1) == mode(tup1):
        print(True)
        print(f"Mode : {mode(tup1)}")
    else:
        print(False)


def ch12_14():
    from statistics import mean
    tup1 = eval(input("Enter the tuple : "))
    get_mean = lambda tup: sum(tup) / len(tup)
    if get_mean(tup1) == mean(tup1):
        print(True)
        print(f"mean : {mean(tup1)}")
    else:
        print(False)
        print(f"mean : {mean(tup1)}")


def ch12_15():
    tup = tuple(eval(input(f"Enter the tuple {i+1} : ")) for i in range(7))
    mean = tuple(sum(i)/len(i) for i in tup)
    print(f"Mean of each tuple : {mean}")
    mean_of_means = sum(mean)/len(mean)
    print(f"Mean of means : {mean_of_means}")