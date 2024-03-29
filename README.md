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

```shell
poetry install
```

This will create and activate a virtual environment with all the dependencies installed.

## Testing

```shell
poetry run pytest
```

## Linting

```shell
poetry run pytest
poetry run flake8 impresso tests
poetry run mypy impresso tests
```

## OpenAPI client generation

The OpenAPI client is generated using the OpenAPI Generator. The following command generates the client code in the `tmp/generated` directory and copies it over to the source directory:

```shell
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
```

We also need to generate Pydantic models from the OpenAPI spec. This is done separately as follows:

```shell
poetry run datamodel-codegen \
  --url http://localhost:3030/swagger.json \
  --input-file-type openapi \
  --output impresso/api_models.py \
  --disable-timestamp \
  --field-constraints \
  --enum-field-as-literal all \
  --use-annotated \
  --use-generic-container-types \
  --output-model-type pydantic_v2.BaseModel
```
