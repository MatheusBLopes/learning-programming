if __name__ == '__main__':
    n = int(input())
    stamps = set()
    for _ in range(n):
        country_stamp = input()
        stamps.add(country_stamp)

    print(len(stamps))