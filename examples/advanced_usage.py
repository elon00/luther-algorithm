#!/usr/bin/env python3
"""
Advanced usage example for Luther's Golden Algorithm
Demonstrates performance benchmarking and large-scale operations
"""

import time
import os
from luther_algorithm import LuthersGoldenAlgorithm

def benchmark_performance():
    """Benchmark encryption/decryption performance"""
    print("Performance Benchmark - Luther's Golden Algorithm")
    print("=" * 60)

    golden = LuthersGoldenAlgorithm()
    sizes = [1000, 10000, 100000, 1000000]  # 1KB to 1MB

    for size in sizes:
        data = b"A" * size

        # Benchmark encryption
        start_time = time.time()
        for _ in range(10):
            encrypted = golden.encrypt(data)
        enc_time = (time.time() - start_time) / 10

        # Benchmark decryption
        start_time = time.time()
        for _ in range(10):
            decrypted = golden.decrypt(encrypted)
        dec_time = (time.time() - start_time) / 10

        print("2d"
              "6.4f"
              "6.4f"
              ".1f")

def demonstrate_security_features():
    """Demonstrate various security features"""
    print("\nSecurity Features Demonstration")
    print("=" * 40)

    golden = LuthersGoldenAlgorithm()

    # 1. Adaptive encryption based on data size
    print("1. Adaptive Encryption:")
    small_data = b"Small message"
    large_data = b"A" * 500000  # 500KB

    enc_small = golden.encrypt(small_data)
    enc_large = golden.encrypt(large_data)

    print(f"   Small data ({len(small_data)} bytes) -> {len(enc_small)} bytes")
    print(f"   Large data ({len(large_data)} bytes) -> {len(enc_large)} bytes")

    # 2. Digital signatures
    print("\n2. Post-Quantum Digital Signatures:")
    message = b"Critical security message"
    signature = golden.sign(message)
    verified = golden.verify(message, signature)

    print(f"   Message signed: {len(signature)} bytes")
    print(f"   Signature verified: {verified}")

    # 3. Tamper detection
    print("\n3. Tamper Detection:")
    original = b"Original message"
    encrypted = golden.encrypt(original)

    # Simulate tampering
    tampered = bytearray(encrypted)
    if len(tampered) > 10:
        tampered[10] ^= 0xFF  # Flip a bit

    try:
        decrypted_tampered = golden.decrypt(bytes(tampered))
        print("   Tamper detection: FAILED (should have failed)")
    except Exception as e:
        print("   Tamper detection: SUCCESS (correctly detected tampering)")

def file_encryption_demo():
    """Demonstrate file encryption/decryption"""
    print("\nFile Encryption Demonstration")
    print("=" * 35)

    golden = LuthersGoldenAlgorithm()

    # Create a sample file
    sample_content = b"This is a sample file content for encryption demonstration.\n" * 100
    filename = "sample.txt"

    with open(filename, "wb") as f:
        f.write(sample_content)

    print(f"Created sample file: {filename} ({len(sample_content)} bytes)")

    # Read and encrypt file
    with open(filename, "rb") as f:
        file_data = f.read()

    encrypted_data = golden.encrypt(file_data)
    print(f"Encrypted file size: {len(encrypted_data)} bytes")

    # Decrypt and verify
    decrypted_data = golden.decrypt(encrypted_data)
    success = file_data == decrypted_data
    print(f"File decryption successful: {success}")

    # Save decrypted file
    with open("decrypted_sample.txt", "wb") as f:
        f.write(decrypted_data)

    print("Decrypted file saved as: decrypted_sample.txt")

    # Cleanup
    os.remove(filename)
    os.remove("decrypted_sample.txt")

def main():
    """Main demonstration function"""
    print("LUTHER'S GOLDEN ALGORITHM - ADVANCED DEMO")
    print("=" * 55)

    try:
        benchmark_performance()
        demonstrate_security_features()
        file_encryption_demo()

        print("\n" + "=" * 55)
        print("ADVANCED DEMO COMPLETED SUCCESSFULLY!")
        print("Luther's Golden Algorithm: The Ultimate Cryptographic Solution")

    except Exception as e:
        print(f"\nError during demonstration: {e}")
        print("Make sure all dependencies are installed:")
        print("pip install -r requirements.txt")

if __name__ == "__main__":
    main()