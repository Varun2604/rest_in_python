import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rest_in_python",
    version="0.0.1",
    author="Varun V Iyer",
    author_email="iyervarun2604@gmail.com",
    description="An extensively extendable and intelligent REST api framework for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Varun2604/rest_in_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
