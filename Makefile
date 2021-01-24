#!/usr/bin/env make -f
#
# Makefile for recipe static site generator
#

# ---------------------------------------------------------------------------
#
# General setup
#

# Set default target
.DEFAULT_GOAL := test

# Decide if use python3 or python
ifeq (, $(@shell which python3))
	py = python3
else
	py = python
endif
# Decide if use pip3 or pip
ifeq (, $(@shell which pip3))
	pip = pip3
else
	pip = pip
endif
# Decide if use firefox or firefox.exe
ifeq (, $(@shell which firefox.exe))
	browser = firefox.exe
else
	browser = firefox
endif


# Detect OS
OS = $(shell uname -s)

# Defaults
ECHO = echo

# Make adjustments based on OS
ifneq (, $(findstring CYGWIN, $(OS)))
	ECHO = /bin/echo -e
endif

# Colors and helptext
NO_COLOR	= \033[0m
ACTION		= \033[32;01m
OK_COLOR	= \033[32;01m
ERROR_COLOR	= \033[31;01m
WARN_COLOR	= \033[33;01m

# Which makefile am I in?
WHERE-AM-I = $(CURDIR)/$(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))
THIS_MAKEFILE := $(call WHERE-AM-I)

# Echo some nice helptext based on the target comment
HELPTEXT = $(ECHO) "$(ACTION)--->" `egrep "^\# target: $(1) " $(THIS_MAKEFILE) | sed "s/\# target: $(1)[ ]*-[ ]* / /g"` "$(NO_COLOR)"



# ----------------------------------------------------------------------------
#
# Highlevel targets
#
# target: help                         - Displays help with targets available.
.PHONY:  help
help:
	@$(call HELPTEXT,$@)
	@echo "Usage:"
	@echo " make [target] ..."
	@echo "target:"
	@egrep "^# target:" Makefile | sed 's/# target: / /g'



# target: info                         - Displays versions.
.PHONY: info
info:
	@${py} --version
	@${py} -m pip --version



# target: tox                         - Run tox on project.
.PHONY: tox
tox:
	@${py} -m tox



# target: build                         - Build pip package.
.PHONY: build
build: clean-build
	@${py} setup.py bdist_wheel



# target: install-local-build           - Install dist package locally.
.PHONY: install-local-build
install-local-build:
	@${pip} uninstall treeviz
	@${pip} install dist/*.whl



# target: validate                     - Validate code with pylint
.PHONY: validate
validate:
	@pylint --rcfile=.pylintrc treeviz



# target: test-unit                    - Run tests in tests/unit with coverage.py
.PHONY: test-unit
test-unit: clean
	@$(ECHO) "$(ACTION)---> Running all tests in tests/" "$(NO_COLOR)"
	@${py} \
		-m coverage run --rcfile=.coveragerc \
		-m unittest discover tests
	$(MAKE) clean-py



# target: test                         - Run tests and display code coverage
.PHONY: test
test: validate test-unit
	${py} -m coverage report  --rcfile=.coveragerc
	$(MAKE) clean-cov




## target: clean-py                     - Remove generated python files
.PHONY: clean-py
clean-py:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +



## target: clean-cov                    - Remove generated coverage files
.PHONY: clean-cov
clean-cov:
	rm -f .coverage
	rm -rf tests/coverage_html



# target: clean-build                    - Remove all build files
.PHONY: clean-build
clean-build: clean-py
	rm -rf treeviz.egg-info
	rm -rf dist
	rm -rf build



# target: clean                        - Remove all generated files
.PHONY: clean
clean: clean-py clean-build clean-cov
	find . -name '*~' -exec rm -f {} +
	find . -name '*.log*' -exec rm -fr {} +



# target: install                      - Install all Python packages specified in requirement.txt (requirements/prod.txt)
.PHONY: install
install:
	${pip} install -r requirements.txt



# target: install-test                 - Install Python packages specified in requirement/test.txt
.PHONY: install-test
install-test:
	${pip} install -r requirements/test.txt



# target: install-pip                 - Install Python packages specified in requirement/pip.txt
.PHONY: install-pip
install-pip:
	${pip} install -r requirements/pip.txt



# target: setup-venv                   - Install venv and update to pip to latest. Run before make install.
.PHONY: setup-venv
setup-venv:
	python3 -m venv .venv
	. .venv/bin/activate &&	pip3 install --upgrade pip
