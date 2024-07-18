up:
	docker compose up -d
down:
	docker compose down
py-exec:
	docker exec -it python bash
clear-reformat:
	rm -rf ./data/reformated/*