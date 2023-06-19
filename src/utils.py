def has_common_patterns(password):
    common_patterns = ["12345", "123456", "123456789", "password", "qwerty", "abc123"]
    for pattern in common_patterns:
        if pattern in password:
            return True
    return False


