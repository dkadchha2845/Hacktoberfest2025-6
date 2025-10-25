string = input("Enter String: ")
cc = input("Enter Character To Count: ")
count = 0
for char in string:
    if char == cc:
        count += 1
print(f"The Character '{cc}' Appears {count} Times In The String")
print()
