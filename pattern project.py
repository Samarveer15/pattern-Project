print("Right Angled triangle of stars (*) :")
b = int(input("Enter the number of rows : "))

for i in range(b):
    for j in range(b+1):
        print("* ", end="")
    print()