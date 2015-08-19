all:
	brew install protobuf
	pip install protobuf
	generate
generate:
	@echo "Generating protocol buffer python classes..."
	protoc protobuff.proto --python_out=./
