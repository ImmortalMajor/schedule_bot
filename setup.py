import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='schedule_bot',
    version='1.0.0',
    author='ImmortalMajor',
    author_email='...',
    description='Simple schedule telegram bot',
    packages=[],
    long_description=read('README.md'),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Telegram Bot",
    ],
)
