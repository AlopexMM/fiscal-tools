from setuptools import setup, find_packages

setup(
    name="Fiscal-tools",
    version="0.1.0",
    packages=find_packages(include=["afip", "afip.*"]),
    install_requires = [],
    setup_requires=["pytest-runner", "flake8"],
    tests_require=["pytest"]
)
