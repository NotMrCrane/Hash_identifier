hash_value = input("Write your hash: ")


def identify_hash(hash_value):
    hash_lengths = {
        32: ["MD5", "NTLM", "MD4"],
        40: ["SHA-1"],
        64: ["SHA-256"]
    }

    hash_length = len(hash_value)

    if hash_length in hash_lengths:
        return hash_lengths[hash_length]

    return ["Unknown hash"]


result = identify_hash(hash_value)
print(result)