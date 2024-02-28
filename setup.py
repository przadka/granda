from setuptools import setup, find_packages

setup(
    name='granda',
    version='0.1.0',
    package_dir={'': 'src'},  # Specify the root directory for your packages
    packages=find_packages(where='src'),  # Find packages in the 'src' directory
    install_requires=[
        'numpy',
        'pandas',
    ],
)
