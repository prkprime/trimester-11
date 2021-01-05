#!/usr/bin/env python3

import sys
import json
import os
from hashlib import sha3_512
from tabulate import tabulate

# instead of using memory equals to the file size,
# we will read 100MB chunk at a time and calculate the hash
BUF_SIZE = 104857600 # 100MB

def get_sha_obj():
    return sha3_512()

def calc_file_hash(filename: str) -> str:
    '''
    param filename : filename of the file that you wan't to check the hash of
    returns : hash value of that file. exits the program if file not found
    '''
    try:
        with open(filename, 'rb') as f:
            sha3 = get_sha_obj()
            while True:
                data = f.read(BUF_SIZE) # reading next 64kb of file
                if not data:
                    break
                sha3.update(data)
        return sha3.hexdigest()
    except FileNotFoundError:
        sys.exit(f'{filename} : file not found. exiting...')

if len(sys.argv) == 2:
    if sys.argv[1] == '--check':
        try:
            with open('sha3sum', 'r') as f:
                data = json.load(f)
                results = []
                for filename, hash_value in data.items():
                    if os.path.exists(filename):
                        if hash_value == calc_file_hash(filename):
                            results.append([filename, 'OK'])
                        else:
                            results.append([filename, 'ERROR'])
                    else:
                        results.append([filename, 'FILE_NOT_FOUND'])
                print(
                    tabulate(
                        results,
                        headers=(
                            'FileName',
                            'Status'
                        )
                    )
                )
        except FileNotFoundError:
            sys.exit(f'sha3sum : file not found. exiting...')
    else:
        filename = sys.argv[1]
        hash_value = calc_file_hash(filename)
        print(f'{filename} : {hash_value}')
        try:
            with open('sha3sum', "r+") as f:
                data = json.load(f)
                data.update({filename : hash_value})
                f.seek(0)
                json.dump(data, f)
        except FileNotFoundError:
            with open('sha3sum', 'w') as f:
                json.dump({filename : hash_value}, f)
        
else:
    sys.exit(f'Syntax error\n\tUse \'hashpy <filename>\' to calculate the hash.\n\tUse \'hashpy --check\' to check')