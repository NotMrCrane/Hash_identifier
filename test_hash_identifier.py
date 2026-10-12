from hash_identifier import identify_hash

def test_md5():
    result = identify_hash("5f4dcc3b5aa765d61d8327deb882cf99")

    assert result == ["MD5", "NTLM", "MD4"]

def test_invalid():
    result = identify_hash("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")

    assert result == ["Unknown hash"]

def test_bcrypt():
    bcrypt_input = "$2b$12$" + "a" * 53

    result = identify_hash(bcrypt_input)

    assert result == ["bcrypt"]

def test_invalid_bcrypt():
    bcrypt_input = "$2b$hello"

    result = identify_hash(bcrypt_input)

    assert result == ["Unknown hash"]

if __name__ == "__main__":
    test_md5()
    test_invalid()
    test_bcrypt()
    test_invalid_bcrypt()

    print("All 4 tests passed!")