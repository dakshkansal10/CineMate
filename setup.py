from setuptools import setup

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'Daksh Kansal'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='dakshkansal03@gmail.com',
    description='MovieMind',
    long_description='movie recommendation system',
    package = [SRC_REPO],
    python_used = '3.12.7',
    install_requires = LIST_OF_REQUIREMENTS,
)
    
    