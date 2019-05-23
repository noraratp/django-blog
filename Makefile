.PHONY: start stop bash down
start:
	docker-compose -f docker/dev/docker-compose.yml up

stop:
	docker-compose -f docker/dev/docker-compose.yml stop

down:
	docker-compose -f docker/dev/docker-compose.yml down

bash:
	docker exec -it dev_web_1 bash
