FROM python:3.8
LABEL maintainer="Rafal Skolasinski <r.j.skolasinski@gmail.com>"

ENV POETRY_HOME /opt/poetry

ENV HOME /home/user
ENV WORKDIR ${HOME}/work

WORKDIR $WORKDIR

# Install linux tools
RUN apt-get update && apt-get -y install nano wget curl git

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3

ENV PATH "$POETRY_HOME/bin:$PATH"
RUN poetry config virtualenvs.create false

# Install environment (just deps so code change does not affect docker caching)
COPY poetry.lock pyproject.toml ${WORKDIR}/
RUN poetry install && rm ~/.cache/pip -rf

# Install environment (local code)
COPY echo_server.py ${WORKDIR}/echo_server.py
# COPY tests/ ${WORKDIR}/tests/
RUN poetry install

# Setup Jupyter Notebook
EXPOSE 5000
CMD echo-server --host 0.0.0.0 --port 5000
