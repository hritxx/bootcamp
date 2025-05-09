.PHONY: run build-docker run-docker clean build-package publish-package

run:
	python3 main.py

build-docker:
	docker build -t file-processor .

run-docker:
	docker run -p 8000:8000 -v $(PWD)/watch_dir:/app/watch_dir file-processor

clean:
	find . -type f -name "*.pyc" -delete
	rm -rf __pycache__

build-package:
	python3 setup.py sdist bdist_wheel

publish-package:
	twine upload dist/*
