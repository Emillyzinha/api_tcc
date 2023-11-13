from django.test import TestCase
import unidecode
from main import settings

encryption_chars = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "@", "f": "!", "g": "*", "h": "#", "j": "&"}

pasword = "bbacdehjg"

print(settings.BASE_DIR)

def encrypt_password(password):
    for l in password:
        password=password.replace(l, encryption_chars[l])
    return password


def decrypt_password(encrypted_password):
    for l in encrypted_password:
        for key, value in encryption_chars.items():
            if value == l:
                encrypted_password = encrypted_password.replace(l, key)
    return encrypted_password


print(encrypt_password(password=pasword))
print(decrypt_password(encrypt_password(pasword)))
