j,n=1,1
w=input("enter the character width for the pattern(odd number):")
print("\n")
l=input("enter the character length for the pattern(less than 3*odd number):")
print("\n")
l=int(l)
w=int(w)
while(j<=(w-(w//2))+1):
    while(n<=((w-1)//2)):
        for i in range((l-(3*(2*n-1)))//2):
            print("-",end='',sep='')
            if(i==((l-(3*(2*n-1)))//2)-1):
                string=(2*n-1)*".|."
                print(string,end='')
                for i in range((l-(3*(2*n-1)))//2):
                    print("-",end='')
                print("\n")
                n=n+1
    if(j==(w-(w//2))):
        for i in range((l-7)//2):
            print("-",end='')
        print("WELCOME",end='')
        for i in range((l-7)//2):
            print("-",end='')
        print("\n")
    if(j>(w-(w//2))):
        for i in range(((w-1)//2),0,-1):
            for h in range((l-(3*(2*i-1)))//2):
                print("-",end='')
                if(h==((l-(3*(2*i-1)))//2)-1):
                    string=(2*i-1)*".|."
                    print(string,end='')
                    for m in range((l-(3*(2*i-1)))//2):
                        print("-",end='')
                    print("\n")
    j=j+1
