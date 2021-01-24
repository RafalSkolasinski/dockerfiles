REPOSITORY ?= rafalskolasinski
IMAGE_NAME ?= echo-server

DIRTY_STATUS := $(shell git diff --quiet || echo '-dirty')
IMAGE_TAG := $(shell git describe --tags --dirty)
IMAGE_SHA := $(shell git rev-parse --short HEAD)${DIRTY_STATUS}

BASE_NAME := ${REPOSITORY}/${IMAGE_NAME}
LATEST_NAME := ${BASE_NAME}:latest

BASE_VERSION := latest

image:
	docker build -f Dockerfile --build-arg BASE_VERSION=${BASE_VERSION} -t ${LATEST_NAME} .

	docker tag ${LATEST_NAME} ${REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG}
	docker tag ${LATEST_NAME} ${REPOSITORY}/${IMAGE_NAME}:${IMAGE_SHA}

push: image
	docker push ${REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG}
	docker push ${REPOSITORY}/${IMAGE_NAME}:${IMAGE_SHA}
	docker push ${LATEST_NAME}


install:
	poetry install

test:
	poetry run pytest -v .

check: flakes fmt

flakes:
	poetry run pyflakes .

fmt:
	poetry run black .



serve:
	poetry run echo-server

docker-serve:
	docker run -it --rm -p 5000:5000 ${LATEST_NAME}
