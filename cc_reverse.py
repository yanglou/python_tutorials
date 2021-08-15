def reverse(str):
    reverse_str = ''
    for i in range(0, len(str), 1):
        reverse_str += str[len(str)-i-1]
    return reverse_str


name = input("What is your name? ")
print("Your name reversed is:", reverse(name))
