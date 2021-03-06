#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup script."""

import importlib.util
from pathlib import Path
from setuptools import setup, find_packages
from codecs import open


# Get the long description from the relevant file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# Get the base version from the library.  (We'll find it in the `version.py`
# file in the src directory, but we'll bypass actually loading up the library.)
vspec = importlib.util.spec_from_file_location(
    "version",
    str(Path(__file__).resolve().parent / "npc_engine_import_wizard" / "version.py"),
)
vmod = importlib.util.module_from_spec(vspec)
vspec.loader.exec_module(vmod)
version = getattr(vmod, "__version__")

# Define requirements here, dont forget to add them to the extras_require

requirements = ["npc-engine[cpu]>=0.0.1,<1.0.0"]

requirements_dev = [
    "pip-check-reqs>=2.0.1,<3",
    "black>=19.10b0",
    "flake8>=3.7.9,<4",
    "flake8-docstrings>=1.5.0,<2",
    "pytest>=6.0.1",
    "pytest-cov>=2.5.1,<3",
    "pytest-pythonpath>=0.7.2,<1",
    "setuptools>=38.4.0",
    "tox>=3.0.0,<4",
    "twine==3.2.0",
]

requirements_flowtron_tts = [
    "torch>=1.0.0,<2.0.0",
    "tensorboardX",
]

requirements_transformers = ["torch>=1.0.0,<2.0.0", "transformers>=4.0.0,<5.0.0"]

requirements_espnet = ["torch>=1.0.0,<2.0.0", "espnet"]

all = requirements_flowtron_tts + requirements_transformers + requirements_espnet


setup(
    name="npc-engine-import-wizard",
    description="Import wizard for npc-engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    version=version,
    install_requires=requirements,
    extras_require={
        "dev": requirements_dev,
        "flowtron-tts": requirements_flowtron_tts,
        "transformers": requirements_transformers,
        "espnet": requirements_espnet,
        "all": all,
    },
    entry_points="""
    [console_scripts]
    npc-engine-import-wizard=npc_engine_import_wizard.cli:cli
    """,
    python_requires=">=3.7.0",
    license="MIT",
    author="eublefar",
    author_email="evil.unicorn1@gmail.com",
    # Use the URL to the github repo.
    url="https://github.com/npc-engine/npc-engine-import-wizard",
    keywords=["npc", "AI", "inference", "deep-learning"],
    # See https://PyPI.python.org/PyPI?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    include_package_data=True,
)
