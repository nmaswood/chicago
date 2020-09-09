from setuptools import find_packages, setup

DEV_PACKAGES = ["mypy", "flake8", "pylint", "black"]

version = "0.0.1"

setup(
    name="chicago",
    version=version,
    install_requires=DEV_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    extras_require={"dev": DEV_PACKAGES},
)
