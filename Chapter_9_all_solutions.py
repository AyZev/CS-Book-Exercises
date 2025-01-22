
def ch9_1():
    a = int(input("Enter the length (in cm) : "))
    print(f"{ a *2.54} inches") if a> 0 else print("Invalid")


def ch9_2():
    n = int(input("Enter the number of items : "))
    total = 0
    if n < 0:
        print("Idiotic number")
    elif n > 10:
        total += n * 120
    elif 10 <= n <= 99:
        total += n * 100
    elif n >= 100:
        total += n * 70
    print(total)


def ch9_3():
    h = int(input("Enter hour between 1-12 : "))
    x = int(input("How many hours ahead : "))
    print(f"Time at that time would be : {(h + x - 1) % 12 + 1} O' clock")


def ch9_4():
    n1, n2 = [float(input(f"Enter the number {i + 1} : ")) for i in range(2)]
    diff = abs(n1 - n2)
    if diff <= 0.001:
        print("Close")
    else:
        print("Not Close")


def ch9_5():
    n = int(input("Enter the year : "))
    leap = False
    if n % 400 == 0 or all((n % 4 == 0, n % 100 != 0)):
        leap = True
    print(f"{n} is a leap year") if leap else print(f"{n} is not a leap year")


def ch9_6():
    s1, s2, s3 = [int(input(f"Enter the length of side {i + 1} : ")) for i in range(3)]
    if s1 + s2 <= s3 or s2 + s3 <= s1 or s3 + s1 <= s2:
        print("Nope! Not a triangle.")
    else:
        print("A triangle can be formed.")


def ch9_7():
    n = int(input("Enter the digit : "))
    if n == 0:
        print("Zero")
    elif n == 1:
        print("One")
    elif n == 2:
        print("Two")
    elif n == 3:
        print("Three")
    elif n == 4:
        print("Four")
    elif n == 5:
        print("Five")
    elif n == 6:
        print("Six")
    elif n == 7:
        print("Seven")
    elif n == 8:
        print("Eight")
    elif n == 9:
        print("Nine")
    else:
        print("Need some software update to reach to that level.")


def ch9_8():
    n = int(input("Enter the number : "))
    sqr_root = round((n ** (1 / 2)), 2)
    is_prime = True
    for i in range(2, (int(sqr_root // 2)) + 1):
        if sqr_root % i == 0:
            is_prime = False
    if is_prime:
        print(f"Square root of {n} is {str(sqr_root).rstrip("0").rstrip(".")} and it is prime.")
    else:
        print(f"Square root of {n} is {str(sqr_root).rstrip("0").rstrip(".")} and it is not prime.")


def ch9_9():
    n = int(input("Enter number of odd nums : "))
    for i in range(n, 0, -1):
        print(2 * i - 1, end=" ")


def ch9_10_i():
    for i in range(1, 41, 3):
        print(i)


def ch9_10_ii():
    sign = 1
    for i in range(1, 41, 3):
        print(i * sign, end=" ")
        sign = -sign


def ch9_11():
    t_sum = 0
    ctr = 0
    while True:
        x = int(input(f"Enter value {ctr + 1} (Enter 0 to exit) : "))
        if x == 0:
            break
        t_sum += x
        ctr += 1
    print(f'Average of numbers : {t_sum / ctr}')


def ch9_12():
    s1, s2, s3 = [int(input(f"Enter the length of side {i + 1} : ")) for i in range(3)]
    if s1 == s2 == s3:
        print("The triangle is equilateral.")
    elif s1 != s2 != s3:
        print("The triangle is scalene.")
    else:
        print("The triangle is isosceles.")


def ch9_13():
    n = int(input("Enter any integer : "))
    if n % 10 == 4:
        print(f"{n} ends with 4.")
    elif n % 10 == 8:
        print(f"{n} ends with 8.")
    else:
        print(f"{n} ends with neither 4 nor 8.")


def ch9_14():
    n = int(input("Enter any number greater than 20 : "))
    if n <= 20:
        print("The number is not greater than 20.")
    else:
        for i in range(11, n + 1):
            if i % 21 == 0:
                print("TipsyTopsy")
            elif i % 3 == 0:
                print("Tipsy")
            elif i % 7 == 0:
                print("Topsy")


def ch9_15():
    maximum = 0
    i = 0
    while True:
        n = (input(f"Enter number {i + 1} (Enter 'end' to break): "))
        i += 1
        if n.lower() == "end":
            break
        elif int(n) > maximum:
            maximum = int(n)
    print(f"Maximum number : {maximum}")


def ch9_16():
    maximum = float("-inf")
    sec_max = float("-inf")
    i = 0
    while True:
        n = (input(f"Enter number {i + 1} (Enter 'end' to break): "))
        i += 1
        if n.lower() == "end":
            break
        elif int(n) > maximum:
            sec_max = maximum
            maximum = int(n)
        elif sec_max < int(n) != maximum:
            sec_max = int(n)
    print(f"Second Largest number : {sec_max}")


def ch9_17():
    n = int(input("Enter a number : "))
    rev_num = 0
    temp = n
    while temp > 0:
        rev_num = rev_num * 10 + temp % 10
        temp //= 10
    if n == rev_num:
        print("The number is palindrome.")
    else:
        print("The number is not palindrome.")


def ch9_18():
    x = int(input("Enter an integer : "))
    length = 0
    rev_num = 0
    temp = x
    while temp > 0:
        length += 1
        temp //= 10
    temp = x
    while temp > 0:
        rev_num = rev_num * 10 + temp % 10
        temp //= 10
    msd = rev_num % 10
    print(f"The resultant integer : {length * 10 + msd}")


def ch9_19():
    n = int(input("Enter a range n : "))
    m = int(input("Enter a value to check the divisibility : "))
    even = " "
    odd = " "
    for i in range(m, n + 1, m):
        if i % 2 == 0:
            even += f" {i}"
        else:
            odd += f' {i}'
    print(f"Even integers between 1 and {n} divisible by {m} : {even}")
    print(f"Odd integers between 1 and {n} divisible by {m}: {odd}")


def ch9_20_a():
    numerator = 2
    denominator = 9
    tsum = 0
    sign = 1
    for i in range(7):
        tsum += sign * numerator / denominator
        sign *= -1
        numerator += 3
        denominator += 4
    print(tsum)


def ch9_20_b():
    n = int(input("Enter the range : "))
    tsum = 0
    for i in range(1, n + 1):
        x = 2 * i - 1
        tsum += x * x
    print(tsum)


def ch9_21():
    tsum = 0
    n = int(input("Enter range of series : "))
    for i in range(n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        tsum += 1 / factorial
    print(tsum)


def ch9_22():
    ll = int(input("Enter lower limit : "))
    ul = int(input("Enter upper limit : "))
    emp_n = 0
    n = int(input("Enter number of employee : "))
    for i in range(n):
        emp = int(input(f"Enter age of employee {i + 1}: "))
        if emp in range(ll, ul + 1):
            emp_n += 1
    print(f"Number of employees ageing in range from {ll} to {ul} : {emp_n}")


def ch9_23():
    x = int(input("Enter the value of x : "))
    n = int(input("Enter range of series : "))
    tsum = 0
    sign = 1
    for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        tsum += sign * x ** i / factorial
        sign *= -1
    print(tsum)


def ch9_24_a():
    print("Diamond pattern")
    n = int(input('Enter length of pattern : '))
    for i in range(1, n + 1):
        for _ in range(i, n + 1):
            print(" ", end='')
        for _ in range(i):
            print("*", end=" ")
        print()

    for i in range(n + 1, 0, -1):
        for _ in range(i, n + 1):
            print(" ", end='')
        for _ in range(i):
            print("*", end=" ")
        print()


def ch9_24_b():
    print('Symmetrical right angle triangle pattern')
    n = int(input("Enter number of lines : ")) // 2
    for i in range(1, n + 1):
        for _ in range(i):
            print("*", end=" ")
        print()
    for i in range(n + 1, 0, -1):
        for _ in range(i):
            print("*", end=" ")
        print()


def ch9_24_c():
    # Hollow diamond pattern
    n = int(input(
        "Enter number of rows in the hollow diamond : ")) // 2  # The number of rows for the top half (adjust for size)
    for i in range(n):
        for j in range(i, n):
            print(" ", end="")
        for k in range(i + 1):
            if k == 0 or k == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    for i in range(n, -1, -1):
        for j in range(i, n):
            print(" ", end="")
        for k in range(i + 1):
            if k == 0 or k == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def ch9_24_d():
    n = int(input("Enter number of lines : ")) // 2 + 1
    for i in range(1, n):
        for j in range(i):
            if j == 0 or j == i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    for i in range(n, 0, -1):
        for j in range(i):
            if j == 0 or j == i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def ch9_25_a():
    n = 6
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(j + 65), end=" ")
        print()


def ch9_25_b():
    n = 5
    for i in range(n):
        for j in range(i + 1):
            print(chr(i + 65), end=" ")
        print()


def ch9_25_c():
    n = 5
    for i in range(n):
        for j in range(i + 1):
            print(i * 2, end=" ")
        print()


def ch9_25_d():
    n = 4
    for i in range(1, n + 1):
        for j in range(i):
            print(i * 2, end=" ")
        print()


def ch9_26():
    for i in range(6):
        for j in range(20):
            print("*", end=" ")
        print()


def ch9_27():
    a = int(input("Enter integer A : "))
    b = int(input("Enter integer B : "))
    c = int(input("Enter integer C : "))

    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    print(f"\nSmallest Number : {a}")
    print(f"Next Higher Number : {b}")
    print(f"Highest Number : {c}")


def ch9_28():
    temp = float(input("Enter the temperature : "))
    if (x := input("Enter 0 to convert into fahrenheit and 1 to convert into celsius : ")) == "0":
        print(f"Temperature in Celsius : {temp} {chr(176)}C ")
        print(f"Temperature in Fahrenheit : {temp * (9 / 5) + 32} {chr(176)}F")
    elif x == "1":
        print(f"Temperature in Fahrenheit : {temp} {chr(176)}F")
        print(f"Temperature in Celsius : {(temp - 32) * (5 / 9)} {chr(176)}C")
    else:
        print("Enter either 0 or 1 ! Nothing else would work.")


def ch9_29():
    temp = int(input("Enter temperature in Celsius : "))
    if temp < -273.15:
        print("Invalid! The temperature is below absolute zero.")
    elif temp == -273.15:
        print("The temperature is absolute zero.")
    elif -273.15 > temp > 0:
        print("The temperature is below freezing point.")
    elif temp == 0:
        print("The temperature is at the freezing point.")
    elif 0 > temp > 100:
        print("The temperature is at the normal range.")
    elif temp == 100:
        print("The temperature is at the boiling point.")
    elif temp > 100:
        print("The temperature is above boiling point.")
    else:
        print("Damn bro you are crazy I covered all possible situations.")


def ch9_30():
    n = int(input("Enter a maximum value to display : "))
    for i in range(1, n + 1):
        prime = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                prime = False
        if prime and not i == 1:
            print(f"{i} = {i} (prime)")
        elif i == 1:
            print(f"{i} = {i}")
        elif not prime:
            f = []  # I am using list because there is no other way to add multiplication symbol into the strings and I do not want to create my custom split() and join()
            a = i
            for k in range(2, n):
                while a % k == 0:
                    f.extend([f"{k}"])
                    a //= k

            print(f"{i} = {" x ".join(f)}")
