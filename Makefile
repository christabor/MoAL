clean:
	@echo "Deleting docs/"
	rm -rf docs || true
docs: clean
	@echo "Building Sphinx API Docs..."
	# http://sphinx-doc.org/man/sphinx-apidoc.html
	sphinx-apidoc --private -M -A 'Chris Tabor' -H 'MoAL' -o docs MOAL
	@echo "Built all docs."
build: docs
	cd docs && make html -j 4
serve: build
	cd docs/_build/html && python -m SimpleHTTPServer 8001
cleancoverage:
	@echo "Cleaning up coverage report leftovers..."
	rm -r coverage_report
	rm .coverage
	rm MOAL/.coverage*
	rm *.png
static_coverage:
	@echo "Running pylint for static analysis... (output to static_output.txt)"
	python MOAL/test_files.py --static > static_output.txt
savetree:
	tree . > tree-example.txt
notebook:
	@echo "Running the interactive notebook!"
	ipython notebook
epydocs:
	# http://epydoc.sourceforge.net/manual-reference.html
	@echo "Generating epydocs and uml classes"
	epydoc --html --output=moal_epydocs ./MOAL/ --graph=umlclasstree
