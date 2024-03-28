# AuthRequestSchema

Authentication request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** |  | 
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from impresso.api_client.models.auth_request_schema import AuthRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRequestSchema from a JSON string
auth_request_schema_instance = AuthRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AuthRequestSchema.to_json())

# convert the object into a dict
auth_request_schema_dict = auth_request_schema_instance.to_dict()
# create an instance of AuthRequestSchema from a dict
auth_request_schema_form_dict = auth_request_schema.from_dict(auth_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


