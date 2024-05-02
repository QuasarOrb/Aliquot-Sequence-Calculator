import time

def aliquot_sequence(n):
    sequence = [n]
    highest_term = n  # Initialize highest term with the first number
    while True:
        divisors_sum = sum([i for i in range(1, sequence[-1]) if sequence[-1] % i == 0])
        if divisors_sum in sequence or divisors_sum == 0:
            break
        sequence.append(divisors_sum)
        print(f"Term {len(sequence)}: {divisors_sum}")  # Print each term calculation
        if divisors_sum > highest_term:
            highest_term = divisors_sum  # Update highest term if a new highest term is found
            
        # Write the highest term to the file
        with open("highest_term.txt", "w") as file:
            file.write(f"{n}:{highest_term}\n")

    return sequence, highest_term

# Get user input for the first number
number = int(input("Enter the first number: "))
# Calculate the aliquot sequence and get the highest term
sequence, highest_term = aliquot_sequence(number)
