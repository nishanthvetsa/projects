name="nishanth"
vowels=['a','e','i','o','u']
dupli=[]
us=[]
li=list(name)
print(li)

for alpha in li:
    if alpha in vowels:
        li.remove(alpha)
print(li)

for check in li:
    if check not in dupli:
        dupli.append(check)
print(dupli)

for comp in dupli:
    if comp !=li:
        us.append(comp)
        print("duplicates found")
print(comp)