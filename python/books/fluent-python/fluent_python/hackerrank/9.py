na = int(input())

a = set(input().split())

other_sets = int(input())

for i in range(other_sets):
    operation, number = input().split()
    set_to_operate = set(input().split())
    
    if operation == 'update':
        eval('a.update(set_to_operate)')
    if operation == 'intersection_update':
        eval('a.intersection_update(set_to_operate)')
    if operation == 'difference_update':
        eval('a.difference_update(set_to_operate)')
    if operation == 'symmetric_difference_update':
        eval('a.symmetric_difference_update(set_to_operate)')

b = [int(n) for n in a]
print(sum(b))


# alternativa

if __name__ == '__main__':
    (_, A) = (int(input()),set(map(int, input().split())))
    B = int(input())
    for _ in range(B):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        getattr(A, command)(newSet)

    print (sum(A))