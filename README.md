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

The OpenAPI client is generated using the OpenAPI Generator. Pydantic models from the OpenAPI spec are generated too. The following command generates both the client code and the pydantic models:

```shell
poetry run generate-client
```

Whenever the OpenAPI spec changes, the client code and the pydantic models must be regenerated.

### Protobuf

Filters used in some endpoints are serialized as a protobuf message. The protobuf message is defined in the `impresso-jscommons` project. The python code is generated using the `protoc` compiler (must be installed). The following command generates the python code for it:

```shell
poetry run generate-protobuf
```
