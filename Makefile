.PHONY: start stop bash restart

# Project variables
PROJECT_NAME ?= blog

# Filenames
DEV_COMPOSE_FILE := docker/dev/docker-compose.yml

start:
	$(INFO) "Start local..."
	@ docker-compose -p $(PROJECT_NAME) -f $(DEV_COMPOSE_FILE) up web

stop:
	$(INFO) "Stop local..."
	@ docker-compose -p $(PROJECT_NAME) -f $(DEV_COMPOSE_FILE) stop web

restart:
	${INFO} "Restart..."
	@ docker-compose -p $(PROJECT_NAME) -f $(DEV_COMPOSE_FILE) restart web

bash:
	${INFO} "connecting to container..."
	@ docker exec -it blog_web_1 /bin/bash


# Cosmetics
YELLOW := "\e[1;33m"
NC := "\e[0m"

# Shell Functions
INFO := @bash -c '\
  printf $(YELLOW); \
  echo "=> $$1"; \
  printf $(NC)' SOME_VALUE