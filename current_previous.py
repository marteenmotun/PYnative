previous_number = 0
for i in range(1, 11):
    add = previous_number + i
    print(f"Current Number {i} Previous Number {previous_number} Sum: {add}")
    previous_number = i
