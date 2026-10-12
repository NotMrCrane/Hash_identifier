import string

HASH_LENGTHS = {
        32: ["MD5", "NTLM", "MD4"],
        40: ["SHA-1"],
        64: ["SHA-256"]
    }



def identify_hash(hash_value):

    hash_length = len(hash_value)

    if hash_value.startswith(("$2a$", "$2b$", "$2y$")) and hash_length == 60:

        cost = hash_value[4:6]

        if (
            cost.isascii()
            and cost.isdigit()
            and 4 <= int(cost) <= 31
            and hash_value[6] == "$"
        ):
            return ["bcrypt"]

    if hash_length not in HASH_LENGTHS:
        return ["Unknown hash"]

    if not all(c in string.hexdigits for c in hash_value):
        return ["Unknown hash"]

    return HASH_LENGTHS[hash_length]


if __name__ == "__main__":
    hash_value = input("Write your hash: ")
    result = identify_hash(hash_value)
    print(result)