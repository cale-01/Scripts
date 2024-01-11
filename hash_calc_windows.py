"""
This scripts reads a file which then feeds the data into 
two different hashing algorithms (MD5 and SHA256)

"""
# To Use
# Example for CMD 
# python {path of script} {path of one or more files wish to retrieve hashes}

# python C:\Users\bob\hash_calc_windows.py C:\Users\bob\Desktop\file.txt


import hashlib
import sys

def calculate_hashes(filename, algorithms):
    hashes = {algorithm: hashlib.new(algorithm) for algorithm in algorithms}

    with open(filename, 'rb') as file:
        while chunk := file.read(2**20):
            for algorithm in algorithms:
                hashes[algorithm].update(chunk)

    return {algorithm: hash_object.hexdigest() for algorithm, hash_object in hashes.items()}

def print_hashes(filename, hashes):
    print(f'---------- HASHES FOR {filename} ----------')
    for algorithm, hash_value in hashes.items():
        print(f'{algorithm}: {hash_value}')

if __name__ == '__main__':
    supported_algorithms = ['md5', 'sha256']

    for filename in sys.argv[1:]:
        file_hashes = calculate_hashes(filename, supported_algorithms)
        print_hashes(filename, file_hashes)
