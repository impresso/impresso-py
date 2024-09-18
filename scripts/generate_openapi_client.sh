rm -rf tmp/generated
mkdir -p tmp/generated
pushd .
cd tmp/generated
poetry run openapi-python-client \
  generate \
  --url http://localhost:3030/swagger.json \
  --config ../../.apigen.yml
popd
rm -rf impresso/api_client
mv tmp/generated/impresso/api_client impresso/