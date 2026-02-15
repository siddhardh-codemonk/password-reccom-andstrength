import subprocess
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import random
import string



RUST_BINARY = r"D:\Vscodeprojects\Cybersecurityworks(imp)\password_crypto\target\release\password_crypto.exe"


def rust_encrypt(text):
    result = subprocess.run(
        [RUST_BINARY, "enc", text],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def rust_decrypt(text):
    result = subprocess.run(
        [RUST_BINARY, "dec", text],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def password_features(pwd):
    return [
        len(pwd),
        sum(c.isupper() for c in pwd),
        sum(c.islower() for c in pwd),
        sum(c.isdigit() for c in pwd),
        sum(c in "!@#$%^&*" for c in pwd)
    ]

def generate_password():
    length = random.randint(6, 16)
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def strength_label(pwd):
    score = 0
    if len(pwd) > 10: score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c in "!@#$%^&*" for c in pwd): score += 1
    if any(c.isupper() for c in pwd): score += 1
    
    return 1 if score >= 3 else 0

def train_model():
    X = []
    y = []

    for _ in range(3000):
        pwd = generate_password()
        X.append(password_features(pwd))
        y.append(strength_label(pwd))

    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def evaluate_password(model, pwd):
    features = np.array(password_features(pwd)).reshape(1, -1)
    prediction = model.predict(features)[0]
    return "Strong" if prediction == 1 else "Weak"

def recommend_password(base="warrior"):
    return base + str(random.randint(100,999)) + "@A"


if __name__ == "__main__":
    
    model = train_model()

    user_password = "cyberwarrior"
    print("Original:", user_password)

    strength = evaluate_password(model, user_password)
    print("ML Strength:", strength)

    if strength == "Weak":
        user_password = recommend_password(user_password)
        print("Recommended Strong Password:", user_password)

    encrypted = rust_encrypt(user_password)
    print("Encrypted:", encrypted)

    decrypted = rust_decrypt(encrypted)
    print("Decrypted:", decrypted)
