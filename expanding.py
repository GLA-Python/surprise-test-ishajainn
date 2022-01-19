def expanding(lst):
    lst1=[]
    for i in range(len(lst)-1):
        a=lst[i+1]-lst[i]
        lst1.append(a)
    c=0    
    for i in range(len(lst1)-1):
        if lst1[i+1]>lst1[i]:
            c=c+1
    if c==len(lst1)-1:
        return True
    else:
        return False
lst=eval(input("enter list"))
out=expanding(lst)
print(out)
