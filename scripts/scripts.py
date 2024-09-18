import subprocess


def _run(bash_script):
    return subprocess.call(bash_script, shell=True)


def generate_openapi_client():
    return _run("./scripts/generate_openapi_client.sh")


def generate_data_models():
    return _run("./scripts/generate_data_models.sh")


def generate_api_client():
    generate_openapi_client()
    generate_data_models()


def generate_protobuf():
    return _run("./scripts/generate_protobuf.sh")
