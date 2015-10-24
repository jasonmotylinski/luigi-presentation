import os

from setuptools import setup

os.system('pip install -e git://github.com/jasonmotylinski/nfl.git#egg=scraper')

setup(
    name="luigipipeline",
    version="0.0.1",
    author="Jason Motylinski",
    author_email="jason@motylinski.com",
    license="BSD",
    keywords="example documentation tutorial",
    packages=['luigipipeline'],
    install_requires=[
        "BeautifulSoup",
        "elasticsearch"
    ]
)
