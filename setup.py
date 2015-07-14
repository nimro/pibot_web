from setuptools import setup, find_packages
import sys

setup(
    name = 'pibot_web',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = [
        "Flask",
        "requests",
        "nose",
    ] + (["setproctitle"] if "linux" in sys.platform else []),
    author = 'Steven Eardley',
    author_email = 'steve@eardley.xyz',
    description = 'A web interface for controlling pibot',
    license = 'MIT License',
    ],
)
