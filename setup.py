import os

from setuptools import setup, find_packages

VERSION = "0.1.5"

long_description = """
# TwitterAPI (Python)

## Installation

This python package requires python >= 3.6 with pip.

### Install with pip

```shell
python3 -m pip install --upgrade --user twitter_sdk
```

### Install manual

```shell
git clone https://github.com/AdriBloober/TwitterSDK && cd TwitterSDK
python3 setup.py install
```

# How to use?

**Go to https://github.com/AdriBloober/TwitterSDK and look there!**
"""

if os.path.exists("README.md"):
    with open("README.md", "r") as readme_file:
        r = readme_file.read()
        if r.startswith("# TwitterAPI"):
            long_description = r

requirements = ["requests", "requests-oauthlib"]


class DevelopmentStatus:
    PLANNING = "Development Status :: 1 - Planning"
    PRE_ALPHA = "Development Status :: 2 - Pre-Alpha"
    ALPHA = "Development Status :: 3 - Alpha"
    BETA = "Development Status :: 4 - Beta"
    PRODUCTION_STABLE = "Development Status :: 5 - Production/Stable"
    MATURE = "Development Status :: 6 - Mature"
    INACTIVE = "Development Status :: 7 - Inactive"


supported_python_versions = ["3", "3.6", "3.7", "3.8", "3.9"]

classifiers = [
    "Operating System :: OS Independent",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    DevelopmentStatus.PRE_ALPHA,
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Programming Language :: Python"
]
classifiers.extend(
    ["Programming Language :: Python :: " + spv for spv in supported_python_versions]
)

setup(
    name="twitter_sdk",
    version=VERSION,
    author="AdriBloober",
    author_email="adribloober@adribloober.wtf",
    description="Communicate with the official twitter api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AdriBloober/TwitterSDK",
    packages=find_packages(include=["twitter", "twitter.*"]),
    classifiers=classifiers,
    python_requires=">=3.6",
    install_requires=requirements,
)
