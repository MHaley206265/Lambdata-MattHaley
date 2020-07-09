import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-dspt6-MattHaley",
    version="0.0.1",
    author="Matt Haley",
    author_email="matthew-haley@lambdastudents.com",
    description="A small package with helpful functions for working with DataFrames",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MHaley206265/Lambdata-MattHaley",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)