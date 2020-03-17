import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt', 'r') as f:
    install_requires = f.readlines()

setup(
    name='radea',
    version='0.0.0',
    packages=find_packages(exclude=('radea','tests','test')),
    python_requires='>=3.7',
    install_requires=install_requires,
    include_package_data=True,
    license='Copyright (c) Nordic ID Oy. All rights reserved.',  # example license
    description='radea ml',
    long_description=README,
    url='https://www.nordicid.com',
    author='Arvin Cudanin, Jussi Tikkanen, Enrique Aldana, Dwitiya Tiwari, Juha Fonsen, Petteri Huotari',
    author_email='RadeaDevTeam@nordicid.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)