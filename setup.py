from setuptools import setup, find_packages

setup(
    name='granda',
    version='0.1.0',
    packages=find_packages(),  # This now searches for packages at the root
    install_requires=[
        'numpy',
        'pandas',
    ],
)
