"""
dchecker setup
Please read the documentation in README.md.
Quick install:
	$ python setup.py bdist_egg
	$ sudo easy_install dist/dchecker*.egg
"""
from setuptools import setup, find_packages

execfile('dchecker/version.py')

setup(
    name='dchecker',
    author='Nicholas Rejack',
    author_email="v.pandey@ufl.edu",
    maintainer="UF CTS-IT",
    maintainer_email="ctsit@ctsi.ufl.edu",
    version=__version__,
    packages=find_packages(exclude=['test']),
    url='http://github.com/ctsit/dchecker2',
    keywords=['VIVO', 'data integrity', 'SPARQL'],
    license='Apache 2.0',
    description='Data integrity checker for VIVO researcher\'s database',
    long_description=open('README.md').read(),
    package_data={
                '': ['*.rq'],
                '': ['*.py']
    },
    entry_points={
        'console_scripts': [
            'dchecker = dchecker2.dchecker2:main',
        ],
    },
    install_requires=[
        "tempita",
        "Click"
    ],
)
