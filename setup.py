from setuptools import setup, find_packages

setup(
    name='granda',
    version='0.1.0',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'numpy',
        'pandas',
    ],
    url='https://github.com/przadka/granda',
    author='Your Name',
    author_email='your.email@example.com',
    description='A versatile evaluation tool for benchmarking LLM architectures',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
