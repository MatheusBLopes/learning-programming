if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[a, b, c] for a in [x, y, z] for b in [x, y, z] for c in [x, y, z]])