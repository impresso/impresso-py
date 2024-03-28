# AuthResponseSchema

Authentication response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**authentication** | [**AuthResponseSchemaAuthentication**](AuthResponseSchemaAuthentication.md) |  | 
**user** | [**User**](User.md) |  | 

## Example

```python
from impresso.api_client.models.auth_response_schema import AuthResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AuthResponseSchema from a JSON string
auth_response_schema_instance = AuthResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AuthResponseSchema.to_json())

# convert the object into a dict
auth_response_schema_dict = auth_response_schema_instance.to_dict()
# create an instance of AuthResponseSchema from a dict
auth_response_schema_form_dict = auth_response_schema.from_dict(auth_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


