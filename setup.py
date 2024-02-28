from setuptools import setup, find_packages

setup(
    name='granda',
    version='0.1.0',
    packages=find_packages(),  # This should automatically find and include all packages in your project
    include_package_data=True,  # This tells setuptools to include any data files specified in MANIFEST.in
    install_requires=[
        'numpy',
        'pandas',
        # other dependencies...
    ],
    # Optional: specify package data files explicitly
    # package_data={
    #     'your_package': ['data_files/*'],
    # },
)
