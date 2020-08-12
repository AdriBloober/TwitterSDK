from setuptools import setup

VERSION = "0.1.1"

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


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
    packages=["twitter"],
    classifiers=classifiers,
    python_requires=">=3.6",
    install_requirements=requirements,
)
