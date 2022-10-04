import re
import os
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools import setup

from clu.spacy.info import info


class PackageDevelop(develop):
    def run(self):
        develop.run(self)


class PackageInstall(install):
    def run(self):
        # install everything else
        install.run(self)


# use requirements.txt as deps list
with open("requirements.txt", "r") as f:
    required = [dep.strip() for dep in f.read().splitlines() if dep.strip() is not None]

# get readme
with open("README.md", "r") as f:
    readme = f.read()

test_deps = required + ["green==3.3.0", "coverage==6.2", "mypy==0.931"]

dev_deps = test_deps + [
    "black==21.12b0",
    "wheel==0.37.1",
    # "black @ git+git://github.com/psf/black.git",
    "mkdocs==1.2.3",
    # "portray @ git+git://github.com/myedibleenso/portray.git@issue/83",
    # "portray @ git+git://github.com/myedibleenso/portray.git@avoid-regressions",
    # "mkapi==1.0.14",
    "pdoc3==0.10.0",
    "mkdocs-git-snippet==0.1.1",
    "mkdocs-git-revision-date-localized-plugin==0.11.1",
    "mkdocs-git-authors-plugin==0.6.3",
    "mkdocs-rtd-dropdown==1.0.2",
    "pre-commit==2.16.0",
]

setup(
    name="clu-spacy",
    packages=["clu.spacy"],
    scripts=[os.path.join("bin", file) for file in os.listdir("bin")],
    version=info.version,
    keywords=["nlp", "converter"],
    description=info.description,
    long_description=readme,
    url=info.repo,
    download_url=info.download_url,
    author=" and ".join(info.authors),
    author_email=info.contact,
    license=info.license,
    install_requires=required,
    cmdclass={
        "install": PackageInstall,
        "develop": PackageDevelop,
    },
    classifiers=(
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
    ),
    python_requires=">=3.8",
    tests_require=test_deps,
    extras_require={"test": test_deps, "all": dev_deps + required},
    include_package_data=True,
    zip_safe=False,
)
