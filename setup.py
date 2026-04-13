from setuptools import setup, find_packages

setup(
    name="prg_mamba",
    version="1.0.0",
    author="Akoramurthy B, Surendiran B, Xiaochun Cheng",
    description="PRG-Mamba: Periodic Relational Graph-Mamba for rPPG",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "torch>=2.0.0",
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "timm>=0.9.0",
        "einops>=0.6.1",
        "omegaconf>=2.3.0",
    ],
)
