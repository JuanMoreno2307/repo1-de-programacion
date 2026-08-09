# mi_primer_script.py
print("¡Hola, GitHub!")

ID 000603744

juan esteban moreno

ingenieria aeronautica

programacion

upb

añado primera linea

agrego la segunda 

ponemos la tercera como la proxima libertadores del verde

💚🤍💚🤍

    🔅🔅🔅



proximos campeones

ahora si el codigo que nos tocaba hacer

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Buscar primos entre 1 y 1000
primos = [n for n in range(1, 1001) if es_primo(n)]

print("Números primos del 1 al 1000:")
print(primos)


