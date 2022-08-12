a = 5

b = '1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 '.split()

clone = [x for x in b if b.count(x) ==1]
    
print(clone)

# A imagem 10.jpg possui a explicação completa do problema


# Python 3

k,arr = int(input()),list(map(int, input().split()))

myset = set(arr)

print(((sum(myset)*k)-(sum(arr)))//(k-1))

# We simply calculate the difference in what the sum would be if there were K elements of all groups. We will have k-1*captains room number left, we simply didve by k-1 to get the answer.