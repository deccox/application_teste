def fibonacci(value):
    t2 = 1
    t1 = 0
    fib = [0,1]
    length = 0
    while value >= fib[length]:
        if (value in fib):
            print(f"valor: {value} - encontrado")
            exit()
        else:
            length = len(fib)
            Term = t1 + t2
            t1 = t2
            t2 = Term
            fib.append(Term)
    print(f"valor {value} nao encontrado")
    
fibonacci(34)