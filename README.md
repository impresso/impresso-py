# Impresso-py, Pympresso for friends

## deployment on PyPi

Deployment is automated using GitHub Actions. The following steps are required to deploy a new version of the package:
https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/

To build the package manually:

```shell
poetry build
```

## Development

We are using Poetry for dependency management. To install the package in development mode, run the following command in the root directory of the project:

```
poetry install
```

This will create and activate a virtual environment with all the dependencies installed.

## Testing

```
poetry run pytest
```

## OpenAPI client generation

The OpenAPI client is generated using the OpenAPI Generator. The following command generates the client code in the `tmp/generated` directory:

```shell
# Download the OpenAPI spec because we cannot reach localhost from the docker container
wget http://localhost:3030/swagger.json -P tmp/

# Generate the client code
docker run --rm \
  -v ${PWD}:/local openapitools/openapi-generator-cli generate \
  -i /local/tmp/swagger.json \
  -g python \
  -o /local/tmp/generated \
  --skip-validate-spec \
  --additional-properties=generateSourceCodeOnly=true,packageName=impresso.api_client
```

The code is generated in the `tmp/generated` directory. We keep the generated code in a different place so a bit of manual work is needed to get it there:

```shell
# copy to source directory
cp -r tmp/generated/impresso/api_client impresso/
# move tests to tests/ directory
mkdir -p tests/api_client
mv impresso/api_client/test/* tests/api_client/
# remove the test directory
rm -r impresso/api_client/test

# remove the generated directory and swagger.json
rm -r tmp/generated tmp/swagger.json
```
