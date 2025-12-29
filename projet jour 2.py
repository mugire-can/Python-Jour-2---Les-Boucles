#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Jour 2 - Les Boucles
Training exercises on Python loops (for and while)
"""

# ============================================================================
# JOB 01: Display numbers from 0 to 20
# ============================================================================
print("=== JOB 01: Numbers from 0 to 20 ===")
for nombre in range(21):
    print(nombre)
print()


# ============================================================================
# JOB 02: Display every other number from 0 to 20
# ============================================================================
print("=== JOB 02: Every other number from 0 to 20 ===")
for nombre in range(0, 21, 2):
    print(nombre)
print()


# ============================================================================
# JOB 03: Display squares of numbers from 1 to 20
# ============================================================================
print("=== JOB 03: Squares of numbers from 1 to 20 ===")
for nombre in range(1, 21):
    print(f"{nombre}^2 = {nombre**2}")
print()


# ============================================================================
# JOB 04: Display multiplication tables from 1 to N
# ============================================================================
print("=== JOB 04: Multiplication tables ===")
N = int(input("Veuillez entrer un entier supérieur à zéro : "))

if N > 0:
    for i in range(1, N + 1):
        print(f"Table de multiplication de {i} :")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()
else:
    print("Veuillez entrer un entier supérieur à zéro.")
print()


# ============================================================================
# JOB 05: Convert for loop to while loop (numbers 0 to 12)
# ============================================================================
print("=== JOB 05: Numbers 0 to 12 (using while loop) ===")
count = 0
while count < 13:
    print(count)
    count += 1
print()


# ============================================================================
# JOB 06: While loop for multiplication results by 7
# ============================================================================
print("=== JOB 06: Multiplication by 7 (using while loop) ===")
N = int(input("Entrez un numero: "))
count = 1
while count <= 10:
    print(f"{N} x {count} = {N * count}")
    count += 1
print()


# ============================================================================
# JOB 07: Loop 12 times, display triple of iteration minus 2
# ============================================================================
print("=== JOB 07: Triple of iteration minus 2 ===")
for tour in range(1, 13):
    result = (tour * 3) - 2
    print(result)
print()


# ============================================================================
# JOB 08: Loop 12 times, display iteration number + 2
# ============================================================================
print("=== JOB 08: Iteration number plus 2 ===")
for tour in range(1, 13):
    result = tour + 2
    print(result)
print()


# ============================================================================
# JOB 09: Display even and odd numbers from 1 to 30
# ============================================================================
print("=== JOB 09: Even and odd numbers from 1 to 30 ===")
for nombre in range(1, 31):
    if nombre % 2 == 0:
        print(f"{nombre} - Pair")
    else:
        print(f"{nombre} - Impair")


