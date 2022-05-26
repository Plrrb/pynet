from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="pynet",
    version="0.0.1",
    license="Unlicense License",
    author="Plrrb (https://github.com/Plrrb)",
    author_email="<plrrb@proton.me>",
    description="Pynet is a Python library for making Servers and Clients.",
    long_description=long_description,
    keywords=["python", "client", "library", "server"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)