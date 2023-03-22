import os

from setuptools import setup, find_packages


base_packages = ["numpy==1.24.2", "extra_streamlit_tools"]


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="streamlit_random_generator",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=base_packages,
    description="Random generator with streamlit front-end",
    author="Tomer Gabay",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
)
