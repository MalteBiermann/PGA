from setuptools import setup, find_packages

setup(
    name = "Geodätische Toolbox",
    version = "0.1",
    description = "Geodätische Toolbox",
    keywords = ["geodätisch","geodetic","toolbox"],
    url = "https://github.com/MalteBiermann/PGA",
    author = ["Svenja Rode", "Chris Arends", "Hendrik Gebben", "Malte Biermann"],
    author_email = "malte.biermann@student.jade-hs.de",
    license = "GNU GPLv3",
    packages = find_packages(),
    #package_dir={'': "src"},
    )
