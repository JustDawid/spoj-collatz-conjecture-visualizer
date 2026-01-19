def problem_collatza(x):
    print(x)
    if x == 1:
        return 1
    elif x % 2 == 0:
        return problem_collatza(x//2)
    else:
        return problem_collatza(3*x + 1)
    
lista = [11, 2, 5, 8, 7]

for i in lista:
    print(problem_collatza(i))