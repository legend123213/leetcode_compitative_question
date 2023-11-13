def is_sorted(n):
    inti = 0 
    nexti = 1
    breaker = len(n) -1
    while nexti == breaker:
        if n[nexti]>n[inti]:
            return false
        inti +=1
        next +=1
    return True


