#!/usr/bin/python3
"""Password hashing"""

import bcrypt


def hash_password(plain_password: str) -> str:
    """Hashes a plaintext password using bcrypt and returns the hashed password."""
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed_password = bcrypt.hashpw(plain_password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plaintext password against a hashed password."""
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )
