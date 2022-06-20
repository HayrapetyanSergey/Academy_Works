def shish(a,b):
    sum = a * 0.10
    sum += b * 0.25
    
    return f"$ {sum:.2f}"
print(shish(5,4))

