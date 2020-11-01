ARG JUPYTER_VERSION

FROM jupyter/minimal-notebook:$JUPYTER_VERSION
LABEL maintainer="Rafal Skolasinski <r.j.skolasinski@gmail.com>"


# Install linux tools
USER root
RUN apt-get update && apt-get -y install nano wget curl git
USER $NB_UID:$NB_UID

# Install Poetry
ENV POETRY_HOME /home/$NB_USER/.poetry
RUN curl -sSL \
    https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py \
    | python3

ENV PATH "$POETRY_HOME/bin:$PATH"


# Add some handy configuration
ENV JUPYTER_ENABLE_LAB yes
COPY extras/shortcuts.jupyterlab-settings \
    /home/$NB_USER/.jupyter/lab/user-settings/@jupyterlab/shortcuts-extension/
