REPOSITORY ?= rafalskolasinski
IMAGE_NAME ?= poetry-notebook

DIRTY_STATUS := $(shell git diff --quiet || echo '-dirty')
IMAGE_TAG := $(shell git describe --tags --dirty)
IMAGE_SHA := $(shell git rev-parse --short HEAD)${DIRTY_STATUS}

BASE_NAME := ${REPOSITORY}/${IMAGE_NAME}
LATEST_NAME := ${BASE_NAME}:latest

JUPYTER_VERSION := latest

image:
	docker build -f Dockerfile -t ${LATEST_NAME} --build-arg JUPYTER_VERSION=${JUPYTER_VERSION} .


	docker tag ${LATEST_NAME} ${REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG}
	docker tag ${LATEST_NAME} ${REPOSITORY}/${IMAGE_NAME}:${IMAGE_SHA}

push: image
	docker push ${REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG}
	docker push ${REPOSITORY}/${IMAGE_NAME}:${IMAGE_SHA}
	docker push ${LATEST_NAME}
