.PHONY: test upload clean bootstrap

test:
	sh -c '. _virtualenv/bin/activate; py.test tests'
	_virtualenv/bin/pyflakes precisely tests

test-all:
	tox

upload: test-all
	python setup.py sdist bdist_wheel upload
	make clean

register:
	python setup.py register

clean:
	rm -f MANIFEST
	rm -rf dist

bootstrap: _virtualenv
	_virtualenv/bin/pip install -e .
ifneq ($(wildcard test-requirements.txt),)
	_virtualenv/bin/pip install -r test-requirements.txt
endif
	make clean

_virtualenv:
	python3 -m venv _virtualenv
	_virtualenv/bin/pip install --upgrade pip
	_virtualenv/bin/pip install --upgrade setuptools
