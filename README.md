# Rust + Python Password Security Tool (v1)

## Overview
This project demonstrates a cross-language cybersecurity pipeline combining:

- Rust (Encryption Engine)
- Python (Automation + Integration)
- Machine Learning (Password Strength Classification)

## Features
- Rust-based affine cipher encryption/decryption
- Python integration using subprocess
- ML-based password strength evaluation
- Automatic password recommendation

## Architecture
User Input → ML Evaluation → Recommendation → Rust Encryption → Output

## Technologies Used
- Rust
- Python
- scikit-learn
- NumPy

## How to Run

1. Build Rust binary:
cd password_crypto
cargo build --release
2. Run Python tool:
python rustconnector.py

## Version
v1 – Rust encryption + Python integration pipeline
