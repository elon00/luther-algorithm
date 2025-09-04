"""
Setup script for Luther's Golden Algorithm
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="luther-algorithm",
    version="1.0.0",
    author="Luther's Algorithm Team",
    author_email="contact@luthersalgorithm.com",
    description="The most powerful hybrid post-quantum cryptosystem ever created",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/luthers-golden-algorithm",
    packages=find_packages(exclude=['tests', 'examples']),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "qiskit>=1.0.0",
        "qiskit-aer>=0.12.0",
        "pycryptodome>=3.18.0",
        "cryptography>=41.0.0",
        "numpy>=1.21.0",
    ],
    extras_require={
        "postquantum": ["pqcrypto>=0.1.0"],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "luther-algorithm=luther_algorithm:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)