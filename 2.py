def count_letter_a(s):
    count_lower = s.lower().count('a')
    return count_lower

def main():
    s = input("Informe uma string para verificar a quantidade de letras 'a': ")
    count = count_letter_a(s)
    
    if count > 0:
        print(f"A letra 'a' (maiúscula ou minúscula) aparece {count} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")

if __name__ == "__main__":
    main()
