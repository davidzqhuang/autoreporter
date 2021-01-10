import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autoreporter", # Replace with your own username
    version="0.0.1",
    author="David Huang",
    author_email="dhuang26@gmail.com",
    description="To easily format, design, and automatically generate reports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davidzqhuang/autoreporter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
