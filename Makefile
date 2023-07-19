MDBOOK ?= mdbook
PYTHON ?= python3


.PHONY: dependencies generate clean preview

check-dependencies:
  $(if $(shell command -v $(MDBOOK) 2> /dev/null),,$(error "mdbook is not available, please follow the installation instructions in the README.md"))

generate: check-dependencies
	@ $(PYTHON) book.py generate

clean:
	@ $(PYTHON) book.py clean

preview:
	@ $(PYTHON) book.py preview