.PHONY: start stop bash
start:
	docker-compose -f docker/dev/docker-compose.yml up

stop:
	docker-compose -f docker/dev/docker-compose.yml stop

bash:
	docker exec -it dev_web_1 bash
