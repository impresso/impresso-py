# impresso.api_client.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_post**](AuthenticationApi.md#authentication_post) | **POST** /authentication | 


# **authentication_post**
> AuthResponseSchema authentication_post(auth_request_schema)



Authenticate user

### Example

* Bearer Authentication (BearerAuth):

```python
import impresso.api_client
from impresso.api_client.models.auth_request_schema import AuthRequestSchema
from impresso.api_client.models.auth_response_schema import AuthResponseSchema
from impresso.api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = impresso.api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = impresso.api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with impresso.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = impresso.api_client.AuthenticationApi(api_client)
    auth_request_schema = impresso.api_client.AuthRequestSchema() # AuthRequestSchema | 

    try:
        # 
        api_response = api_instance.authentication_post(auth_request_schema)
        print("The response of AuthenticationApi->authentication_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authentication_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_request_schema** | [**AuthRequestSchema**](AuthRequestSchema.md)|  | 

### Return type

[**AuthResponseSchema**](AuthResponseSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**401** | not authenticated |  -  |
**500** | general error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

