import random



# Define the characters used in for password generation

characters = '0123456789abcdef'



def generate_password(length=40):

    return ''.join(random.choice(characters) for _ in range(length))



# Number of variations you want to generate

num_variations = 1000  # You can change this to any number you need



# File to output the generated passwords

output_file = 'generated_passwords.txt'



# Generate and write the variations to the file

with open(output_file, 'w') as f:

    for _ in range(num_variations):

        f.write(generate_password() + '\n')



print(f"{num_variations} password variations have been written to {output_file}")

