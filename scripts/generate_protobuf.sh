cd tmp
rm query.proto
wget https://raw.githubusercontent.com/impresso/impresso-jscommons/master/proto/query.proto
rm -rf ../impresso/protobuf
mkdir -p ../impresso/protobuf
touch ../impresso/protobuf/__init__.py
protoc --python_out=../impresso/protobuf --pyi_out=../impresso/protobuf query.proto
cd ..