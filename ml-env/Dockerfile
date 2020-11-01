ARG BASE_VERSION

FROM rafalskolasinski/poetry-notebook:$BASE_VERSION
LABEL maintainer="Rafal Skolasinski <r.j.skolasinski@gmail.com>"

# Change workdir to avoid `cd`
WORKDIR /home/$NB_USER/work/

# Install environment
COPY poetry.lock pyproject.toml /home/$NB_USER/work/
RUN  poetry install && rm ~/.cache/pip -rf

# Overwrite Python 3 kernel
RUN poetry run ipython kernel install --name python3 --display-name "Python 3" --user

# Change back workdir so it runs as it should
WORKDIR /home/$NB_USER
