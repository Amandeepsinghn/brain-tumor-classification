from setuptools import setup,find_packages


__version__="0.0.0"


setup(
    name="brain_tumor",
    author="Amandeep",
    version=__version__,
    author_email="amandeepsingh.kaillay@gmail.com",
    package_dir={"":"src"},
    packages=find_packages(where="src")

)