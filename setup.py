import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="flydb",
    version="2.0",
    description="fly stocks database",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/fchampalimaud/flydb",
    author=["Ricardo Ribeiro", "Hugo Cachitas"],
    author_email=[
        "ricardo.ribeiro@research.fchampalimaud.org",
        "hugo.cachitas@research.fchampalimaud.org",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Framework :: Django :: 2.2",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords="django fly drosophila",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    include_package_data=True,
    install_requires=["django>2.1.0", "django-model-utils~=3.1.0"],
    extras_require={"dev": ["black==19.3b0"]},
    python_requires=">3.6",
)
