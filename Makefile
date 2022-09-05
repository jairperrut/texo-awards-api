build:  ## Docker: Initialize project
	docker-compose build

run-server:  ## Docker: Run server
	docker-compose up
	
run-tests:  ## Docker: Run tests
	docker-compose run --service-ports --no-deps --rm api bash -c "pytest awards_api"
