def large():
    l1=[]
    a=eval(input("Enter 'a' no= "))
    if a>1:
        for i in range(1,a+1):
            if int(a%i==0):
                l1.append(i)
                print("List of factors is = ",l1)
                l2=[]
                for j in l1[1:]:
                    for k in range(2,j):
                        if j % k ==0:
                            break
            else:
                l2.append(j)
                print()
                print(f"largest prime factor of a number {a} is = ",max(l2))
    else:
        print(f"factor of {a} is not found")
        
        
large()