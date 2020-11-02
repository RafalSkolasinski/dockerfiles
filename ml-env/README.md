# ML-ENV

Basic environment for various machine learning research and playground explorations.

Image's environment is controlled with `poetry` and its lock file.

This is sort of to experiment if `poetry` can be be successfully used to control research environments and if this works well with jupyter notebook inside Docker.


## How to use

The build images are uploaded to Docker Hub as [rafalskolasinski/ml-env](https://hub.docker.com/r/rafalskolasinski/ml-env/tags).

Using image is almost identical as using any of official image for Jupyter's [docker-stacks](https://github.com/jupyter/docker-stacks/).

To run latest image simply:
```bash
docker run --rm -d -p 8888:8888 -v ${PWD}:/home/jovyan/work \
    --name ml-env rafalskolasinski/ml-env:latest
```

Check token with:
```bash
docker logs ml-env
```

And open browser:
```bash
xdg-open http://localhost:8888
```


## Test Without Docker

To test without docker you will need Python 3.8 (duh... ;-)) and [poetry](https://python-poetry.org/). Simply type
```bash
poetry install
```
to create python environment and install packages.

> :warning: **If executed in existing virtual env it may erase some packages**: best to execute without any virtual env activated or after activating a new venv.

Once environment is set up start `jupyter lab` with
```bash
poetry run jupyter lab
```


## Technical Notes

- Environmental variable `JUPYTER_ENABLE_LAB` is set to `yes`
- Environment is installed into new `venv` which overwrites `Python 3` kernel inside image. This means that `Jupyter Lab` is running using original environment that comes with `jupyter/minimal-notebook` image but kernel used to execute notebook comes from `poetry`.
