from setuptools import setup, find_packages

setup(
    name='granda',
    version='0.1.0',
    packages=find_packages(where='src'),  # This should find your packages
    package_dir={'': 'src'},  # This tells setuptools where to find packages
    install_requires=[
        'numpy',
        'pandas',
    ],
)
