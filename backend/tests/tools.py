import random


def get_rand_id():
    return random.getrandbits(64).to_bytes(8).hex()
