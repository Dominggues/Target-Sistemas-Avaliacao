def fibonacci_sequence(limit):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def check_fibonacci(num):
    if num < 0:
        return False
    sequence = fibonacci_sequence(num)
    return num in sequence

def main():
    # Número a ser verificado (pode ser modificado ou definido pelo usuário)
    num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

    if check_fibonacci(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
