# Enter your code here. Read input from STDIN. Print output to STDOUT

a = set(input().split())
values = []
for n in range(int(input())):
    b = set(input().split())
    
    values.append(a.issuperset(b))

if len(values) > 1: 
    print(False)
else:
    print(values[0])