num = int(input("Enter a positive Number : "))

if num>1:

    for i in range(2, int(num/2) + 1):

        if num % i == 0:
            print(num, " is not Prime Number")
            break

    else:
        print(num, " is Prime Number")

else:
    print(num, " is not Prime Number")
