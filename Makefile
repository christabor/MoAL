clean:
	@echo "Deleting docs/"
	trap 'rm -f docs' EXIT
docs:
	sphinx-apidoc -F -o docs MOAL
	@echo "Built all docs."
build: clean docs
	cd docs && make html
serve: build
	cd docs/_build/html && python -m SimpleHTTPServer 8001
