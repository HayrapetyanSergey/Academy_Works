def rest(a):
    tipe = (a * 18) / 100 
    AAH = ((a + tipe) * 20) / 100
    sum = a + tipe + AAH
    return f"tipe is {tipe}", f"AAH is  {AAH}", f"Sum is {sum}"

money = float(input())
print (rest(money))