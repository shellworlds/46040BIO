from setuptools import setup, find_packages

setup(
    name="quantum-vqe-anaerobic",
    version="0.1.0",
    author="Quantum POC Team",
    description="VQE simulation for anaerobic organism metabolism",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shellworlds/46040BIO",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Quantum Computing",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "matplotlib>=3.5.0",
        "scipy>=1.7.0",
        "qiskit>=0.39.0",
    ],
    extras_require={
        "dev": ["pytest", "black", "flake8", "sphinx"],
        "docs": ["sphinx", "sphinx-rtd-theme"],
    },
    entry_points={
        "console_scripts": [
            "vqe-sim=src.vqe_simulation:main",
        ],
    },
)
