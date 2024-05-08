def lists():
    n=int(input("Enter how many values you need to enter "))
    c=0
    thislist=[]
    while c<n:
        values=input("Enter the values ")
        thislist.append(values)
        c=c+1
    print(thislist)            
    
def len_lists():
    n=int(input("Enter how many values you need to enter "))
    c=0
    thislist=[]
    while c<n:
        values=input("Enter the values ")
        thislist.append(values)
        c=c+1
    print(len(thislist))
    
def check_lists():
    n=int(input("Enter how many values you need to enter "))
    c=0
    thislist=[]
    while c<n:
        values=input("Enter the values ")
        thislist.append(values)
        c=c+1
    num=input("Enter the value you want to search for ")
    if num in thislist:
        print("Found")
    else:
        print("Not Found")    

def insert_at_specific_index():
    n=int(input("Enter how many values you need to enter "))
    c=0
    thislist=[]
    while c<n:
        values=input("Enter the values ")
        thislist.append(values)
        c=c+1
    print("The Original List Is : ",thislist)   
     
    num=input("Enter the value you want to insert ")
    index=int(input("Enter the index at which you want to insert "))
    thislist.insert(index,num)
    print("Final List Is ",thislist)
    
def extend_lists():
    n=int(input("Enter how many values you need to enter in first list "))
    c=0
    thislist1=[]
    while c<n:
        values=input("Enter the values ")
        thislist1.append(values)
        c=c+1
    n=int(input("Enter how many values you need to enter in second list "))
    c=0
    thislist2=[]
    while c<n:
        values=input("Enter the values ")
        thislist2.append(values)
        c=c+1    
    
    print("The first List is ",thislist1)
    print("The second list is ",thislist2)
    
    thislist1.extend(thislist2)
    
    print("Extended List is ",thislist1)


def pop_lists():
    n=int(input("Enter how many values you need to enter in  list "))
    c=0
    thislist=[]
    while c<n:
        values=input("Enter the values ")
        thislist.append(values)
        c=c+1
    print("The Original List Is ",thislist)
    
    n=int(input("Enter the index you want to pop "))
    thislist.pop(n)
    print("Popped List Is ",thislist)
       

def clear_lists():
    n=int(input("Enter how many values you need to enter in  list "))
    c=0
    thislist=[]
    while c<n:
        values=input("Enter the values ")
        thislist.append(values)
        c=c+1
    print("The Original List Is ",thislist)
    
    thislist.clear()
    
    print("Cleared List ",thislist)    
    
def sorting():
    n=int(input("Enter how many values you need to enter in  list "))
    c=0
    thislist=[]
    while c<n:
        values=input("Enter the values ")
        thislist.append(values)
        c=c+1
    print("The Original List Is ",thislist)
    print("Choose 1 to sort in ascending order")
    print("Choose 2 to sort in reverse order")
    
    
    n=int(input("Enter your choice "))
    
    if n==1:
        thislist.sort()
        print(thislist)
    elif n==2:
        thislist.sort(reverse=True)
        print(thislist)
    
    else:
        print("Choose Between 1,2 ")            
        
def slice_lists():
    n=int(input("Enter how many values you need to enter in  list "))
    c=0
    thislist=[]
    while c<n:
        values=input("Enter the values ")
        thislist.append(values)
        c=c+1
    print("The Original List Is ",thislist)  
    
    n=int(input("Enter the value upto which you want to slice "))
    
    x=slice(n)
    
    print("The sliced list is ",thislist[x])

def count_lists():
    n=int(input("Enter how many values you need to enter in  list "))
    c=0
    thislist=[]
    while c<n:
        values=input("Enter the values ")
        thislist.append(values)
        c=c+1
    print("The Original List Is ",thislist)  
    
    n=input("Enter the value you want to count ")
    x=thislist.count(n)
    print("The number of times it appears in the list is",x)
    

print(" Choose 1 to Enter and Print values in a list")
print(" Choose 2 to Enter and find length of a list")
print(" Choose 3 to Enter and find if a value is present in a list")
print(" Choose 4 to Enter and Print values specific index in a list")
print(" Choose 5 to Enter and extend values in a list from another list")
print(" Choose 6 to Enter and Pop values from a list")
print(" Choose 7 to Enter and Clear values from a list")
print(" Choose 8 to Implement Sorting in a list")
print(" Choose 9 to Slice values in a list")
print(" Choose 10 to Count how many times an entered value is present in a list")

n=int(input("Enter your choice "))

if n==1:
   lists() 
elif n==2:
    len_lists()
elif n==3:
    check_lists()
elif n==4:
    insert_at_specific_index()
elif n==5:
    extend_lists()
elif n==6:
    pop_lists()
elif n==7:
    clear_lists()
elif n==8:
    sorting()
elif n==9:
    slice_lists()
elif n==10:
    count_lists()
else:
    print("Wrong Choice ")
    
                                           