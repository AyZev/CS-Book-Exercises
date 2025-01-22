def ch10_1():
    string = input("Enter the string : ")
    char = input("Enter the character whose occurrences you want to check : ")
    occur = string.count(char)
    print(f"{char} occurs {occur} times in {string}.")


def ch10_2():
    new_string = ""
    string = input("Enter the string : ")
    for i in string:
        if i in "aeiou":
            new_string += "*"
        else:
            new_string += i
    print(new_string)


def ch10_3():
    string = "ayush"
    new_string = ""
    # print(new_string[::-1])
    while string:
        new_string += string[-1]
        string = string[:-1]
    print(new_string)


def ch10_4():
    # Format : 017-555-1212
    ph_no = (input("Enter the phone number : "))
    is_correct = False
    if ph_no[3] == "-" and ph_no[7] == "-":
        if ph_no[:3].isnumeric() and ph_no[4:7].isnumeric() and ph_no[8:13].isnumeric():
            is_correct = True
    print(f"The format of phone number is {is_correct}.")


def ch10_5():
    string: str = input("Enter your string : ")
    digits = ""
    sum_digits = 0
    for i in string:
        if i.isdigit():
            digits += i
    for i in digits:
        sum_digits += int(i)
    if not digits:
        print(f"{string} has no strings.")
    else:
        print(f"{string} has the digits {digits} which sum to {sum_digits}.")


def ch10_6():
    while True:
        sentence: str = input("Enter a sentence(leave blank to exit) : ")
        if not sentence:
            break
        length = len(sentence)
        al_num_char = 0
        words = 0
        current_word = ""
        for i in sentence:
            if not i.isspace():
                current_word += i
            else:
                words += 1 if current_word else 0
                current_word = ""
            if i.isalnum():
                al_num_char += 1
        words += 1 if current_word else 0
        # words = len(sentence.split())
        print(f"Number of characters in the above sentence : {length}")
        print(f"Number of words in the above sentence : {words}")
        print(f"Percentage of alphanumeric characters in the above sentence : {round(100 * al_num_char / length, 2)}%")


def ch10_7():
    while True:
        sentence = input("Enter a sentence (q to quit) : ")
        if sentence == "q":
            break
        # print(sentence.swapcase())
        sentence_swapped = ""
        for i in sentence:
            if i.islower():
                sentence_swapped += i.upper()
            elif i.isupper():
                sentence_swapped += i.lower()
            else:
                sentence_swapped += i
        print(sentence_swapped)


def ch10_8():
    integers = int(input("Enter the number : "))
    string = input("Enter the string : ")
    str_int = ""
    for i in string:
        if i.isdigit():
            str_int += i
    print(f"For inputs {integers}, {string} ==> {integers} + {str_int or 0} = {int(str_int or 0) + integers}")


def ch10_9():
    string1 = input("Enter your string : ")
    string2 = input("Enter your string : ")
    larger = max((string1,string2),key=len)
    space = 2
    total_space = 2*(len(larger)-2)
    for i in range(len(larger)//2):
        print(f"{larger[i]} {total_space*" "} {larger[len(larger)-i-1]}")
        total_space -= 4
        print(space*" ",end="")
        space += 2


def ch10_10():
    num = int(input("Enter your number : "))
    if num <= 0:
        print("Enter a natural number to convert.")
    else:
        roman_num = ""
        values = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
                  ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
        for (symbol, value) in values:
            while num >= value:
                num -= value
                roman_num += symbol
        print(roman_num)


def ch10_11():
    sentence = input("Enter a string having only single space between words : ").strip()
    words = 1
    for i in sentence:
        if i.isspace():
            words += 1
    print(f"Number of words : {words}")


def ch10_12():
    formula = input("Enter the formula : ")
    open_paren = 0
    close__paren = 0
    for i in formula:
        if i == "(":
            open_paren += 1
        elif i == ")":
            close__paren += 1
    if open_paren == close__paren:
        print("Yes the number of open and close parenthesis are same.")
    else:
        print("No the number of open and close parenthesis are not same.")


def ch10_13():
    sentence = input("Enter a sentence : ")
    counter = 0
    for i in sentence:
        if i in "aeiou":
            counter += 1
    print(f"There are {counter} vowels in the sentence \"{sentence}\".")


def ch10_14():
    sentence = input("Enter a sentence : ").strip().rstrip(".")
    max_word = ""
    # for i in sentence.split():
    #     if len(max_word)<len(i):
    #         max_word = i
    current_word = ""
    for i in f"{sentence} ":
        if not i.isspace():
            current_word += i
        else:
            if len(current_word) > len(max_word):
                max_word = current_word
            current_word = ""
    print(f"Biggest word length-wise : {max_word}")


def ch10_15():
    sentence = input("Enter the sentence : ").strip().rstrip(".")
    reversed_sentence = ""
    # for i in sentence.split():
    #     reversed_sentence += f"{i[::-1]} "
    current_word = ""
    for i in f"{sentence} ":
        if not i.isspace():
            current_word += i
        else:
            reversed_sentence += f"{current_word[::-1]} "
            current_word = ""
    print(f"\nReversed Sentence : {reversed_sentence}.")
    
ch10_15()
