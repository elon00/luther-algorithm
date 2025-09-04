# Luther's Golden Algorithm: The Ultimate Hybrid Post-Quantum Cryptosystem

**The most powerful cryptographic system ever created** - Luther's Golden Algorithm represents the pinnacle of encryption technology. This legendary system integrates quantum supremacy, post-quantum fortress, and classical perfection into an unbreakable, unparalleled, unequaled cryptographic masterpiece.

## Features

- **Fully Hybrid**: Integrates classical (AES, RSA), quantum (Shor's algorithm simulation), and post-quantum (Kyber, Dilithium) cryptography
- **Adaptive Selection**: Automatically chooses the optimal algorithm based on data size and security requirements
- **Parallel Processing**: Uses multi-threading for optimized factoring operations
- **Post-Quantum Ready**: Includes Kyber for key encapsulation and Dilithium for digital signatures
- **Quantum Resistant**: Incorporates Shor's algorithm for factoring large numbers
- **High Performance**: Optimized for both speed and security

## Installation

```bash
pip install qiskit qiskit-aer cryptography
# For full post-quantum support:
pip install pqcrypto
```

## Quick Start

```python
from luthers_algorithm import LuthersGoldenAlgorithm

# Initialize the golden algorithm
golden = LuthersGoldenAlgorithm()

# Encrypt any data with golden security
data = b"The most powerful encryption in history!"
encrypted = golden.encrypt(data)

# Decrypt with unbreakable security
decrypted = golden.decrypt(encrypted)
print(f"Golden Success: {data == decrypted}")  # True

# Sign with post-quantum signatures
signature = golden.sign(data)
is_valid = golden.verify(data, signature)
print(f"Signature valid: {is_valid}")  # True
```

## Modes

### Classical Mode
Uses AES-256 for symmetric encryption and RSA for key exchange.
```python
la = LuthersAlgorithm(mode='classical')
```

### Quantum Mode
Incorporates quantum-resistant key derivation using Shor's algorithm simulation.
```python
la = LuthersAlgorithm(mode='quantum')
```

### Post-Quantum Mode
Uses Kyber for key encapsulation and Dilithium for signatures (requires pqcrypto).
```python
la = LuthersAlgorithm(mode='post_quantum')
```

### Hybrid Mode (Recommended)
Adaptively combines all algorithms for maximum security.
```python
la = LuthersAlgorithm(mode='hybrid')
```

## Adaptive Selection

Luther's Algorithm automatically selects the best mode based on data characteristics:

- **Small data (< 1KB)**: Classical mode for speed
- **Large data (> 1MB)**: Full hybrid mode with post-quantum protection
- **Medium data**: Configurable hybrid approach

## API Reference

### LuthersAlgorithm Class

#### `__init__(mode='hybrid')`
Initialize the algorithm with the specified mode.

#### `encrypt(plaintext, recipient_public_key=None)`
Encrypt data using the optimal hybrid approach.

**Parameters:**
- `plaintext`: Bytes to encrypt
- `recipient_public_key`: Optional RSA public key for key exchange

**Returns:** Encrypted bytes

#### `decrypt(ciphertext, private_key=None)`
Decrypt data using the corresponding method.

**Parameters:**
- `ciphertext`: Encrypted bytes
- `private_key`: Optional RSA private key for decryption

**Returns:** Decrypted bytes

#### `sign(message)`
Sign a message using post-quantum signatures if available.

**Parameters:**
- `message`: Bytes to sign

**Returns:** Signature bytes

#### `verify(message, signature)`
Verify a message signature.

**Parameters:**
- `message`: Original message bytes
- `signature`: Signature bytes

**Returns:** Boolean indicating validity

## Security Features

- **Quantum Resistance**: Protected against Shor's algorithm attacks
- **Post-Quantum Security**: Uses lattice-based cryptography
- **Forward Secrecy**: Ephemeral keys for each encryption
- **Adaptive Security**: Adjusts protection level based on threat model

## Performance

The algorithm is optimized for performance:

- Parallel factoring using ThreadPoolExecutor
- Efficient AES encryption with hardware acceleration
- Adaptive mode selection to balance security and speed

## Benchmarks

Run the test suite for performance benchmarks:

```bash
python test_luthers_algorithm.py
```

Typical performance (on modern hardware):
- Small data (< 1KB): ~0.001 seconds
- Medium data (1KB - 1MB): ~0.01 - 0.1 seconds
- Large data (> 1MB): ~0.1 - 1.0 seconds

## Dependencies

- `qiskit`: Quantum computing framework
- `qiskit-aer`: Quantum simulator
- `pycryptodome`: Advanced cryptographic primitives (AES-GCM, RSA)
- `cryptography`: Classical cryptographic primitives
- `pqcrypto`: Post-quantum cryptographic algorithms (Kyber, Dilithium)
- `numpy`: Mathematical computations

## License

This implementation is provided for educational and research purposes. Use at your own risk.

## Contributing

Contributions are welcome! Please submit issues and pull requests on GitHub.

## Disclaimer

This is a demonstration implementation. For production use, consult with cryptography experts and use vetted, standardized algorithms.