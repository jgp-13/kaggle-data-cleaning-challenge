from setuptools import setup, find_packages

setup(
    name="kaggle_cleaning",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "pickle5"  # Optional, if needed for Python 3.8 compatibility
    ],
)
