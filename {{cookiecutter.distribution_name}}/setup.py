from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements_dev.txt'), encoding='utf-8') as f:
    requirements_dev = f.readlines()

setup(
    name='{{cookiecutter.distribution_name}}',
    version='0.1.0',
    description='{{cookiecutter.description}}',
    long_description=long_description,
    url='https://github.com/{{cookiecutter.github_username}}./{{cookiecutter.project_name}}',
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :distribution_name 3.5',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
    ],
    extras_require={
        'dev': [
            requirements_dev,
        ],
    },
    package_data={
        # 'sample': ['package_data.dat'],
    },
    entry_points={
        'console_scripts': [
            # 'sample=sample:main',
        ],
    },
)
