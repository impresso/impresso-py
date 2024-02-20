# Impresso-py, Pympresso for friends

## deployment on PyPi

Deploymebnt is largely automated using GitHub Actions. The following steps are required to deploy a new version of the package:
https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/

## Development

Using pipenv for dependency management. To install the package in development mode, run the following command in the root directory of the project:

```
pipenv run pip install -e .
```

## Testing

```
python -m unittest discover -s tests
```
