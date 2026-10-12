import string

hash_value = input("Write your hash: ")


def identify_hash(hash_value):
    hash_lengths = {
        32: ["MD5", "NTLM", "MD4"],
        40: ["SHA-1"],
        64: ["SHA-256"]
    }

    if hash_value.startswith(("$2a$", "$2b$", "$2y$")):
        return ["bcrypt"]

    hash_length = len(hash_value)

    if hash_length not in hash_lengths:
        return ["Unknown hash"]

    if not all(c in string.hexdigits for c in hash_value):
        return ["Unknown hash"]

    return hash_lengths[hash_length]


result = identify_hash(hash_value)
print(result)