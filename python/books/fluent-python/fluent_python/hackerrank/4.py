n = int(input())
s = set(map(int, input().split()))

nc = int(input())

for _ in range(nc):
    command, *number = input().split()
    
    try:
        if number:
            number = int(number[0])
            
            if command == 'remove':
                eval('s.remove(number)')
            elif command == 'discard':
                eval('s.discard(number)')
        else:
            eval('s.pop()')
    except:
        continue

print(sum(s))