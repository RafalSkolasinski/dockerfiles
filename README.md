# Collection of my Dockerfiles


## poetry-notebook

Jupyter's [minimal-notebook](https://github.com/jupyter/docker-stacks/tree/master/minimal-notebook) with added [poetry](https://python-poetry.org/).

This image is meant to be base for for my playground / research environments in which I want to control installed packages using `poetry` and its package locking mechanism.


## ml-env

Generic image I use as my data science / machine learning / deep learning playground.

I use [pyproject.toml](ml-env/pyproject.toml) file to specify my desired environment. The [poetry.lock](ml-env/poetry.lock) file guarantees that I will always get reproducible builds.
