import string

HASH_LENGTHS = {
        32: ["MD5", "NTLM", "MD4"],
        40: ["SHA-1"],
        64: ["SHA-256"]
    }

BCRYPT_CHARSET = "./ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

def is_bcrypt_format(hash_value):

    # 1. Check the total length
    if len(hash_value) != 60:
        return False

    # 2. Check the bcrypt prefix
    if not hash_value.startswith(("$2a$", "$2b$", "$2y$")):
        return False

    # 3. Extract the cost and encoded data
    cost = hash_value[4:6]
    bcrypt_data = hash_value[7:]

    # 4. Check that the cost contains ASCII digits
    if not (cost.isascii() and cost.isdigit()):
        return False

    # 5. Check that the cost is between 4 and 31
    if not 4 <= int(cost) <= 31:
        return False

    # 6. Check the separator after the cost
    if hash_value[6] != "$":
        return False

    # 7. Check allowed characters
    if not all(c in BCRYPT_CHARSET for c in bcrypt_data):
        return False

    # 8. All checks passed
    return True

def identify_hash(hash_value):

    if is_bcrypt_format(hash_value):
        return ["bcrypt"]

    hash_length = len(hash_value)

    if hash_length not in HASH_LENGTHS:
        return ["Unknown hash"]

    if not all(c in string.hexdigits for c in hash_value):
        return ["Unknown hash"]

    return HASH_LENGTHS[hash_length]


if __name__ == "__main__":
    hash_value = input("Write your hash: ")
    result = identify_hash(hash_value)
    print(result)