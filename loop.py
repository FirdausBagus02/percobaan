
num = 1

while num <= 10:
    if num > 1:
        is_prime = True
        i = 2
        while i <= num ** 0.5:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print(num, "merupakan bilangan prima")
        else:
            print(num, "bukan merupakan bilangan prima")
    else:
        print(num, "bukan merupakan bilangan prima")
    
    num += 1
