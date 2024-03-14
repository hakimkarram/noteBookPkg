from setuptools import setup, find_packages

setup(
    name='notebook',
    version='1.0.0',
    author='hakim',
    author_email='hakima.kadhim@uokufa.edu.iq',
    description='Notebook package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hakimkarram/noteBookPkg',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # List of dependencies required by your package

    ],
)