from distutils.core import setup
from  aiojobs.constants import __version__, REQUIRED_PYTHON_VER
from setuptools import setup, find_packages


PROJECT_NAME = 'aiojobs'
PROJECT_PACKAGE_NAME = 'aiojobs'
PROJECT_LICENSE = 'Apache Licence Version 2.0'
PROJECT_AUTHOR = 'Marky Egebäck'
PROJECT_EMAIL = 'marky@egeback.se'
PROJECT_DESCRIPTION = 'Async jobs'
PACKAGES = find_packages(exclude=['tests', 'tests.*'])
PROJECT_URL = 'https://github.com/egeback/aiojobs'
DOWNLOAD_URL = 'https://github.com/egeback/aiojobs/archive/v1.0.0.zip'

MIN_PY_VERSION = '.'.join(map(str, REQUIRED_PYTHON_VER))

REQUIRES = ['async_timeout']

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    long_description=long_description,
    long_description_content_type="text/markdown",
    name=PROJECT_PACKAGE_NAME,
    version=__version__,
    license=PROJECT_LICENSE,
    url=PROJECT_URL,
    download_url=DOWNLOAD_URL,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    description=PROJECT_DESCRIPTION,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=REQUIRES,
    python_requires='>={}'.format(MIN_PY_VERSION),
    test_suite='tests',
    keywords=['jobs', 'api'],
    entry_points={},
    # classifiers=PROJECT_CLASSIFIERS,
)