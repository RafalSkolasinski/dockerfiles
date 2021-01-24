REPOSITORY ?= rafalskolasinski
IMAGE_NAME ?= ml-env

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

docker-serve:
	docker run --rm -d -p 8888:8888 -v ${PWD}:/home/jovyan/work --name ml-env ${LATEST_NAME}

install:
	poetry install

serve:
	poetry run jupyter lab
