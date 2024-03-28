# AuthResponseSchemaAuthentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** |  | [optional] 
**payload** | **object** |  | [optional] 

## Example

```python
from impresso.api_client.models.auth_response_schema_authentication import AuthResponseSchemaAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of AuthResponseSchemaAuthentication from a JSON string
auth_response_schema_authentication_instance = AuthResponseSchemaAuthentication.from_json(json)
# print the JSON string representation of the object
print(AuthResponseSchemaAuthentication.to_json())

# convert the object into a dict
auth_response_schema_authentication_dict = auth_response_schema_authentication_instance.to_dict()
# create an instance of AuthResponseSchemaAuthentication from a dict
auth_response_schema_authentication_form_dict = auth_response_schema_authentication.from_dict(auth_response_schema_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


