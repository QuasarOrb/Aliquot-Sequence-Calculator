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
            # Read existing highest term from file, if any
        existing_highest_term = None
        
        with open("highest_term.txt", "r") as file:
            existing_highest_term = int(file.read().strip().split(":")[1])
       

# Write the new highest term to the file if it is larger than the existing one
        if existing_highest_term is None or highest_term > existing_highest_term:
         with open("highest_term.txt", "w") as file:
               file.write(f"{number}:{highest_term}\n")
    return sequence, highest_term

# Get user input for the first number
number = int(input("Enter the first number: "))
# Calculate the aliquot sequence and get the highest term
sequence, highest_term = aliquot_sequence(number)

input('Enter to quit') 