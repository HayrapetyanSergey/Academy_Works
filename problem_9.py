def bank(a):
    first_year = a + ((a * 4) / 100 )
    sec_year = first_year + ((first_year * 4) / 100)
    thr_year = sec_year + ((sec_year * 4) / 100)

    return  (f'1st year is {first_year}' ,f'2nd year is {sec_year}', f'3th year is {thr_year}')
money = float(input())
print  ( bank(money))