import setuptools
import treevizer

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='treevizer',
    version=treevizer.__version__,
    author="Andreas Arnesson",
    author_email="aar@bth.se",
    description="A graph visualization tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/andreasarne/treeviz",
    packages=setuptools.find_packages(exclude=[
        "tests.*",
        "tests"
    ]),
    install_requires=[
        'Pillow==8.2.0;sys_platform!="cygwin"', # https://www.python.org/dev/peps/pep-0508/
    ],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )
