import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pulp_capsule_cleanup",
    version="0.0.1",
    author="Waldirio Pinheiro",
    author_email="waldirio@redhat.com",
    description="Script to check the capsule Lifecycle / Repos and remove when necessary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/waldirio/pulp_capsule_cleanup",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
