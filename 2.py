# Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

elemento = int(input("Insira o elemento que deseja da sequência\n")) 
print(fibonacci(elemento))   