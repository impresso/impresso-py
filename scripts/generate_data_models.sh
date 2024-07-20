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