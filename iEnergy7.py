import itertools
import random

def generate_extended_truth_table():
    """Generates a detailed truth table for E = mc mod 2 with larger variations"""
    
    print(f"{'m':<5} {'c (binary)':<20} {'E = mc mod 2':<15}")
    print("-" * 45)

    # Basic binary values
    test_cases = [
        (0, 0), (0, 1), (1, 0), (1, 1),
        (1, 11), (1, 101), (1, 1101),
        (1, 10011), (1, 11111), (1, 1010101)
    ]

    # Adding random binary-like values (5-bit and 10-bit)
    for _ in range(5):
        random_5bit = int(''.join(random.choices('01', k=5)), 2)  # Convert binary string to int
        random_10bit = int(''.join(random.choices('01', k=10)), 2)
        test_cases.append((1, random_5bit))
        test_cases.append((1, random_10bit))

    for m, c in test_cases:
        energy = (m * c) % 2  # E = mc mod 2
        print(f"{m:<5} {bin(c)[2:]:<20} {energy:<15}")  # Convert c to binary format

generate_extended_truth_table()
import itertools
import random

def generate_extended_truth_table():
    """Generates a detailed truth table for E = mc mod 2 with larger variations"""
    
    print(f"{'m':<5} {'c (binary)':<20} {'E = mc mod 2':<15}")
    print("-" * 45)

    # Basic binary values
    test_cases = [
        (0, 0), (0, 1), (1, 0), (1, 1),
        (1, 11), (1, 101), (1, 1101),
        (1, 10011), (1, 11111), (1, 1010101)
    ]

    # Adding random binary-like values (5-bit and 10-bit)
    for _ in range(5):
        random_5bit = int(''.join(random.choices('01', k=5)), 2)  # Convert binary string to int
        random_10bit = int(''.join(random.choices('01', k=10)), 2)
        test_cases.append((1, random_5bit))
        test_cases.append((1, random_10bit))

    for m, c in test_cases:
        energy = (m * c) % 2  # E = mc mod 2
        print(f"{m:<5} {bin(c)[2:]:<20} {energy:<15}")  # Convert c to binary format

generate_extended_truth_table()
import itertools
import random

def generate_extended_truth_table():
    """Generates a detailed truth table for E = mc mod 2 with larger variations"""
    
    print(f"{'m':<5} {'c (binary)':<20} {'E = mc mod 2':<15}")
    print("-" * 45)

    # Basic binary values
    test_cases = [
        (0, 0), (0, 1), (1, 0), (1, 1),
        (1, 11), (1, 101), (1, 1101),
        (1, 10011), (1, 11111), (1, 1010101)
    ]

    # Adding random binary-like values (5-bit and 10-bit)
    for _ in range(5):
        random_5bit = int(''.join(random.choices('01', k=5)), 2)  # Convert binary string to int
        random_10bit = int(''.join(random.choices('01', k=10)), 2)
        test_cases.append((1, random_5bit))
        test_cases.append((1, random_10bit))

    for m, c in test_cases:
        energy = (m * c) % 2  # E = mc mod 2
        print(f"{m:<5} {bin(c)[2:]:<20} {energy:<15}")  # Convert c to binary format

generate_extended_truth_table()
import itertools
import random

def generate_extended_truth_table():
    """Generates a detailed truth table for E = mc mod 2 with larger variations"""
    
    print(f"{'m':<5} {'c (binary)':<20} {'E = mc mod 2':<15}")
    print("-" * 45)

    # Basic binary values
    test_cases = [
        (0, 0), (0, 1), (1, 0), (1, 1),
        (1, 11), (1, 101), (1, 1101),
        (1, 10011), (1, 11111), (1, 1010101)
    ]

    # Adding random binary-like values (5-bit and 10-bit)
    for _ in range(5):
        random_5bit = int(''.join(random.choices('01', k=5)), 2)  # Convert binary string to int
        random_10bit = int(''.join(random.choices('01', k=10)), 2)
        test_cases.append((1, random_5bit))
        test_cases.append((1, random_10bit))

    for m, c in test_cases:
        energy = (m * c) % 2  # E = mc mod 2
        print(f"{m:<5} {bin(c)[2:]:<20} {energy:<15}")  # Convert c to binary format

generate_extended_truth_table()
import itertools
import random

def generate_extended_truth_table():
    """Generates a detailed truth table for E = mc mod 2 with larger variations"""
    
    print(f"{'m':<5} {'c (binary)':<20} {'E = mc mod 2':<15}")
    print("-" * 45)

    # Basic binary values
    test_cases = [
        (0, 0), (0, 1), (1, 0), (1, 1),
        (1, 11), (1, 101), (1, 1101),
        (1, 10011), (1, 11111), (1, 1010101)
    ]

    # Adding random binary-like values (5-bit and 10-bit)
    for _ in range(5):
        random_5bit = int(''.join(random.choices('01', k=5)), 2)  # Convert binary string to int
        random_10bit = int(''.join(random.choices('01', k=10)), 2)
        test_cases.append((1, random_5bit))
        test_cases.append((1, random_10bit))

    for m, c in test_cases:
        energy = (m * c) % 2  # E = mc mod 2
        print(f"{m:<5} {bin(c)[2:]:<20} {energy:<15}")  # Convert c to binary format

generate_extended_truth_table()
import itertools
import random

def generate_extended_truth_table():
    """Generates a detailed truth table for E = mc mod 2 with larger variations"""
    
    print(f"{'m':<5} {'c (binary)':<20} {'E = mc mod 2':<15}")
    print("-" * 45)

    # Basic binary values
    test_cases = [
        (0, 0), (0, 1), (1, 0), (1, 1),
        (1, 11), (1, 101), (1, 1101),
        (1, 10011), (1, 11111), (1, 1010101)
    ]

    # Adding random binary-like values (5-bit and 10-bit)
    for _ in range(5):
        random_5bit = int(''.join(random.choices('01', k=5)), 2)  # Convert binary string to int
        random_10bit = int(''.join(random.choices('01', k=10)), 2)
        test_cases.append((1, random_5bit))
        test_cases.append((1, random_10bit))

    for m, c in test_cases:
        energy = (m * c) % 2  # E = mc mod 2
        print(f"{m:<5} {bin(c)[2:]:<20} {energy:<15}")  # Convert c to binary format

generate_extended_truth_table()
import itertools
import random

def generate_extended_truth_table():
    """Generates a detailed truth table for E = mc mod 2 with larger variations"""
    
    print(f"{'m':<5} {'c (binary)':<20} {'E = mc mod 2':<15}")
    print("-" * 45)

    # Basic binary values
    test_cases = [
        (0, 0), (0, 1), (1, 0), (1, 1),
        (1, 11), (1, 101), (1, 1101),
        (1, 10011), (1, 11111), (1, 1010101)
    ]

    # Adding random binary-like values (5-bit and 10-bit)
    for _ in range(5):
        random_5bit = int(''.join(random.choices('01', k=5)), 2)  # Convert binary string to int
        random_10bit = int(''.join(random.choices('01', k=10)), 2)
        test_cases.append((1, random_5bit))
        test_cases.append((1, random_10bit))

    for m, c in test_cases:
        energy = (m * c) % 2  # E = mc mod 2
        print(f"{m:<5} {bin(c)[2:]:<20} {energy:<15}")  # Convert c to binary format

generate_extended_truth_table()
import itertools
import random

def generate_extended_truth_table():
    """Generates a detailed truth table for E = mc mod 2 with larger variations"""
    
    print(f"{'m':<5} {'c (binary)':<20} {'E = mc mod 2':<15}")
    print("-" * 45)

    # Basic binary values
    test_cases = [
        (0, 0), (0, 1), (1, 0), (1, 1),
        (1, 11), (1, 101), (1, 1101),
        (1, 10011), (1, 11111), (1, 1010101)
    ]

    # Adding random binary-like values (5-bit and 10-bit)
    for _ in range(5):
        random_5bit = int(''.join(random.choices('01', k=5)), 2)  # Convert binary string to int
        random_10bit = int(''.join(random.choices('01', k=10)), 2)
        test_cases.append((1, random_5bit))
        test_cases.append((1, random_10bit))

    for m, c in test_cases:
        energy = (m * c) % 2  # E = mc mod 2
        print(f"{m:<5} {bin(c)[2:]:<20} {energy:<15}")  # Convert c to binary format

generate_extended_truth_table()
import itertools
import random

def generate_extended_truth_table():
    """Generates a detailed truth table for E = mc mod 2 with larger variations"""
    
    print(f"{'m':<5} {'c (binary)':<20} {'E = mc mod 2':<15}")
    print("-" * 45)

    # Basic binary values
    test_cases = [
        (0, 0), (0, 1), (1, 0), (1, 1),
        (1, 11), (1, 101), (1, 1101),
        (1, 10011), (1, 11111), (1, 1010101)
    ]

    # Adding random binary-like values (5-bit and 10-bit)
    for _ in range(5):
        random_5bit = int(''.join(random.choices('01', k=5)), 2)  # Convert binary string to int
        random_10bit = int(''.join(random.choices('01', k=10)), 2)
        test_cases.append((1, random_5bit))
        test_cases.append((1, random_10bit))

    for m, c in test_cases:
        energy = (m * c) % 2  # E = mc mod 2
        print(f"{m:<5} {bin(c)[2:]:<20} {energy:<15}")  # Convert c to binary format

generate_extended_truth_table()
import itertools
import random

def generate_extended_truth_table():
    """Generates a detailed truth table for E = mc mod 2 with larger variations"""
    
    print(f"{'m':<5} {'c (binary)':<20} {'E = mc mod 2':<15}")
    print("-" * 45)

    # Basic binary values
    test_cases = [
        (0, 0), (0, 1), (1, 0), (1, 1),
        (1, 11), (1, 101), (1, 1101),
        (1, 10011), (1, 11111), (1, 1010101)
    ]

    # Adding random binary-like values (5-bit and 10-bit)
    for _ in range(5):
        random_5bit = int(''.join(random.choices('01', k=5)), 2)  # Convert binary string to int
        random_10bit = int(''.join(random.choices('01', k=10)), 2)
        test_cases.append((1, random_5bit))
        test_cases.append((1, random_10bit))

    for m, c in test_cases:
        energy = (m * c) % 2  # E = mc mod 2
        print(f"{m:<5} {bin(c)[2:]:<20} {energy:<15}")  # Convert c to binary format

generate_extended_truth_table()
import itertools
import random

def generate_extended_truth_table():
    """Generates a detailed truth table for E = mc mod 2 with larger variations"""
    
    print(f"{'m':<5} {'c (binary)':<20} {'E = mc mod 2':<15}")
    print("-" * 45)

    # Basic binary values
    test_cases = [
        (0, 0), (0, 1), (1, 0), (1, 1),
        (1, 11), (1, 101), (1, 1101),
        (1, 10011), (1, 11111), (1, 1010101)
    ]

    # Adding random binary-like values (5-bit and 10-bit)
    for _ in range(5):
        random_5bit = int(''.join(random.choices('01', k=5)), 2)  # Convert binary string to int
        random_10bit = int(''.join(random.choices('01', k=10)), 2)
        test_cases.append((1, random_5bit))
        test_cases.append((1, random_10bit))

    for m, c in test_cases:
        energy = (m * c) % 2  # E = mc mod 2
        print(f"{m:<5} {bin(c)[2:]:<20} {energy:<15}")  # Convert c to binary format

generate_extended_truth_table()
