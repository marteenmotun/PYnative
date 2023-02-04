num = list(map(int, input("Enter number seperated by space: ").split(" ")))

total = 0
counter = 0
for i in num:
    total += i
print("Total: ", total)

for i in num:
    if i != 0:
        counter += 1
print("counter: ", counter)

average = total / counter
print("Average number is: ", average)
