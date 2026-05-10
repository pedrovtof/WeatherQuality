# Makefile for python code
# 
# > make help
#

PYTHONPATH=.
VENV_PATH=env
VENV_PATH_ACTIVATE=env/bin/activate
PYTHON_APP_MAIN=src/app/main.py
PYTHON_APP_PORT=8000
ENVIRONMENT_VARIABLE_FILE=src/.env
DOCKER_NAME=python_app
DOCKER_TAG=571fa8e02764296ea35969f2252fea2c # https://generate-random.org/hashes md5 128 -> lower

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

help:
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)


init: ## sets up environment and installs requirements
init:
	pip install -r requirements.txt

env: ## Source venv and environment files for testing
env:
	python3 -m venv $(VENV_PATH)
	@echo "execute=> source $(VENV_PATH_ACTIVATE) && source $(ENVIRONMENT_VARIABLE_FILE)"

leave: ## deactivate venv
leave:
	deactivate

test: ## Run pytest
test:
	pytest . -p no:logging -p no:warnings

build: ## Build docker image
build:
	docker build --target $(DOCKER_NAME):$(DOCKER_TAG)

run: ## build and run docker image
run:
	docker compose up -d -f ./docker/docker-compose.yml

startup: ## run local dev server
	PYTHONPATH=$(PYTHONPATH) fastapi dev $(PYTHON_APP_MAIN) --port $(PYTHON_APP_PORT)

