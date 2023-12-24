import os

from setuptools import setup, find_packages

VERSION = "3.1.2-dev"

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-keycloak",
    version=VERSION,
    long_description=README,
    package_dir={"": "src"},
    packages=find_packages("src"),
    extras_require={
        "dev": [
            "bumpversion>=0.6.0",
            "twine",
        ],
        "doc": [
            "Sphinx>=7.2.6",
            "sphinx-autobuild>=2021.3.14",
        ],
    },
    setup_requires=[
        "pytest-runner",
        "python-keycloak-client",
    ],
    install_requires=[
        "python-keycloak-client>=0.2.3",
        "Django>=4",
    ],
    tests_require=[
        "pytest-django",
        "pytest-cov",
        "mock>=5.1.0",
        "factory-boy",
        "freezegun",
    ],
    url="https://github.com/MohammadrezaAmani/django-keycloak",
    license="MIT",
    author="Mohammadreza Amani",
    author_email="more.amani@yahoo.com",
    description="New  Django Keycloak.",
    classifiers=[],
)
