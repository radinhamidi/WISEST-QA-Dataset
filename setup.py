from setuptools import setup, find_packages

setup(
    name='custom_dataset_fetcher',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests'],
    author='Kevin Sun',
    author_email='kevinuoft.sun@mail.utoronto.ca',
    description='A package for fetching custom datasets from the internet',
    url='https://github.com/radinhamidi/WISEST-QA-Dataset',
    license='MIT',
)