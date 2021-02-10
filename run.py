fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
counter = 0

while counter < len(fruits):
    if fruits[counter] == "banana":
        counter += 1
        continue

    print(fruits[counter])
    counter += 1

print("Iteration completed")
