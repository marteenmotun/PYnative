number = input("Type in Number to check: ")

if number == number[::-1]:
    print(f"original number {number}")
    print(f"Yes. given number is palindrome number")
else:
    print(f"original number {number}")
    print(f"No. given number is not palindrome number")
