import math

choice = int(input("Enter 1 for a single Binomial Coeff.\nEnter 2 for multiple\nWhich option do you desire?: "))

if choice >2 or choice <1:
    print("Invalid input.")

if (choice == 1):
    n = int(input("n: "))
    #print("n is:",n)
    k = int(input("k: "))
    #print("k is: ",k)

    diff = n - k
    factN = math.factorial(n)
    factK = math.factorial(k)
    factNK = math.factorial(diff)
    BC = factN / (factK*factNK)
    print(n," Choose ",k, " is going to be", BC)

if choice == 2:
    p = float(input("(p should be less than 1) p: ")) #float
    n = int(input("n: "))


    start = int(input("Summation starts from: "))
    end = int(input("and ends at: "))
    res = 0

    factN = math.factorial(n)
    for i in range(start, end+1): #from start to the end inclusively 
        diff = n - i
        factK = math.factorial(i)
        factNK = math.factorial(diff)

        BC = factN / (factK*factNK)
        res = res + (BC * (p**i)* (1-p)**(n-i)  ) #C(N,k) * p^k * q^(n-k)
        

    print(res)
    print(1-res, "<- 1- res")
