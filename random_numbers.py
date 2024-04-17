import random

def generate_unique_numbers(num_of_numbers):
    generated_numbers = set()
    while len(generated_numbers) < num_of_numbers:
        new_number = '{:016d}'.format(random.randint(0, 10**16 - 1))
        generated_numbers.add(new_number)
    return generated_numbers

def write_to_txt_file(numbers, filename):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"'{number}\n")

if __name__ == "__main__":
    num_of_numbers = 2000  # Change this to the desired number of unique 16-digit numbers
    output_filename = "unique_numbers.txt"
    unique_numbers = generate_unique_numbers(num_of_numbers)
    write_to_txt_file(unique_numbers, output_filename)
