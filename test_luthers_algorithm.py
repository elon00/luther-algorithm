"""
Comprehensive tests and benchmarks for Luther's Algorithm
"""

import time
import unittest
from luthers_algorithm import LuthersGoldenAlgorithm
from cryptography.hazmat.primitives.asymmetric import rsa

class TestLuthersGoldenAlgorithm(unittest.TestCase):
    def setUp(self):
        self.plaintext_small = b"Hello, World!"
        self.plaintext_large = b"A" * 10**6  # 1MB data
        self.golden = LuthersGoldenAlgorithm()

        # Generate RSA keys for testing
        from Crypto.PublicKey import RSA
        self.rsa_key = RSA.generate(2048)

    def test_golden_encrypt_decrypt_small(self):
        """Test golden encryption for small data"""
        encrypted = self.golden.encrypt(self.plaintext_small)
        decrypted = self.golden.decrypt(encrypted)
        self.assertEqual(self.plaintext_small, decrypted)

    def test_golden_encrypt_decrypt_large(self):
        """Test golden encryption for large data"""
        encrypted = self.golden.encrypt(self.plaintext_large)
        decrypted = self.golden.decrypt(encrypted)
        self.assertEqual(self.plaintext_large, decrypted)

    def test_golden_sign_verify(self):
        """Test golden signing and verification"""
        signature = self.golden.sign(self.plaintext_small)
        verified = self.golden.verify(self.plaintext_small, signature)
        self.assertTrue(verified)

    def test_golden_sign_verify_invalid(self):
        """Test golden signing with invalid data"""
        signature = self.golden.sign(self.plaintext_small)
        verified = self.golden.verify(b"Invalid", signature)
        self.assertFalse(verified)

    def test_golden_quantum_factor(self):
        """Test golden quantum factoring"""
        factors = self.golden._quantum_factor_parallel(1025)  # > 2**10
        self.assertIn(5, factors)
        self.assertIn(205, factors)  # 1025 = 5 * 205

    def benchmark_golden_encryption(self):
        """Benchmark golden encryption performance"""
        data_sizes = [100, 1000, 10000, 100000]

        print("\nBenchmarking Luther's Golden Algorithm:")
        for size in data_sizes:
            data = b"A" * size
            start_time = time.time()
            for _ in range(10):  # Average over 10 runs
                encrypted = self.golden.encrypt(data)
                self.golden.decrypt(encrypted)
            end_time = time.time()
            avg_time = (end_time - start_time) / 10
            print(f"  Size {size} bytes: {avg_time:.4f} seconds")

if __name__ == '__main__':
    # Run unit tests
    unittest.main(verbosity=2)

    # Run benchmarks
    test_instance = TestLuthersGoldenAlgorithm()
    test_instance.setUp()
    test_instance.benchmark_golden_encryption()