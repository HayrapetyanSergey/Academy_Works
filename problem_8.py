def shop(h, m):
    sum = 0
    sum += h * 75
    sum += m * 112
    return sum

hush = int(input())
manr = int(input())

print (shop(hush,manr))
