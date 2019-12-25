import setuptools

with open("README.md", "r") as _file:
  long_description = _file.read()

setuptools.setup(
    name="jailcaliber",
    version="0.1",
    author="naragod",
    author_email="git.naragod@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/naragod/jailcaliber",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)