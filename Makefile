MDBOOK ?= mdbook
PYTHON ?= python3

.PHONY: generate clean preview

generate:
	@ $(PYTHON) book.py generate

clean:
	@ $(PYTHON) book.py clean

preview:
	@ $(PYTHON) book.py preview
