from hashlib import sha256


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transaction, previous_hash, prefix_zeros):
    for nonce in range(MAX_NONCE):

        text = str(block_number) + transcations + previous_hash + str(nonce)
        new_hash = SHA256(text)
    return new_hash


if __name__ == '__main__':
    transcations = '''
    Dhaval->Bhavin->20,
    Mando->Cara->45
    '''

    difficulty = 4
    new_hash = mine(5, transcations, '0000000xa036944e29568d0cff17edbe038f81208fect9a66be9a2b8321c6ec7', difficulty)
    print(SHA256("ABC"))