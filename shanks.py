#shanks one piece algorithm here.....the red head..
import math as m

def inverse(x,y):

    t=1
    while(True):
        if(((x*t)-1)%y==0):
            return t
            break
        t+=1
        
    
if __name__=="__main__":

    n=809
    alpha=3
    beta=525

    m=m.ceil(m.sqrt(n-1))

    list1=[]
    for j in range(m):
        list_t=[]
        temp=(alpha**(m*j))%n
        list_t.append(temp)
        list_t.append(j)
        list1.append(list_t)

    list2=[]
    for i in range(m):
         list_t2=[]
         temp=alpha**i
         temp=inverse(temp,n)
         temp=(temp*beta)%n
         list_t2.append(temp)
         list_t2.append(i)
         list2.append(list_t2)

    list1.sort()
    list2.sort()
    for i in list1:
        i.reverse()
    for i in list2:
        i.reverse()
        
    print(list1)
    print()
    print()
    print(list2)
    #now 2 lists are generated then we have to compare...
    for j in list1:
        for i in list2:
            if(j[1]==i[1]):
                found_j=j[0]
                found_i=i[0]
            
    print()
    print("j value is ",found_j) 
    print("i value is ",found_i)

    print("The answer of the log value is ",((m*found_j)+found_i)%n)
    
         

        

    
    
