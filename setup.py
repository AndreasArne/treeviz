import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='treeviz',
    version='0.0.4',
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
        'wsl-path-converter'
    ],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )