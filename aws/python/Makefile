build: clean-build
	mkdir build
	pip freeze > ./build/requirements.txt
	cp *.py build
	docker run --rm -v ${PWD}/build:/var/task \
		-u 0 lambci/lambda\:build-python3.7 \
		python3.7 -m pip install -t /var/task/ -r /var/task/requirements.txt
	cd build && zip -r ../lambda.zip *

clean-build:
	rm -rf build
