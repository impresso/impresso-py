# impresso.api_client.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_get**](SearchApi.md#search_get) | **GET** /search | 


# **search_get**
> SearchList search_get(group_by, q=q, order_by=order_by, facets=facets, filters=filters, limit=limit, skip=skip)



Find articles that match the given query

### Example

* Bearer Authentication (BearerAuth):

```python
import impresso.api_client
from impresso.api_client.models.search_get_filters_parameter_inner import SearchGetFiltersParameterInner
from impresso.api_client.models.search_list import SearchList
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
    api_instance = impresso.api_client.SearchApi(api_client)
    group_by = 'group_by_example' # str | Group by term
    q = 'q_example' # str | Search query term (optional)
    order_by = 'order_by_example' # str | Order by term (optional)
    facets = 'facets_example' # str | Facet to return (optional)
    filters = [impresso.api_client.SearchGetFiltersParameterInner()] # List[SearchGetFiltersParameterInner] | Filters to apply (optional)
    limit = 56 # int | Total items to return (optional)
    skip = 56 # int | Items to skip (optional)

    try:
        # 
        api_response = api_instance.search_get(group_by, q=q, order_by=order_by, facets=facets, filters=filters, limit=limit, skip=skip)
        print("The response of SearchApi->search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_by** | **str**| Group by term | 
 **q** | **str**| Search query term | [optional] 
 **order_by** | **str**| Order by term | [optional] 
 **facets** | **str**| Facet to return | [optional] 
 **filters** | [**List[SearchGetFiltersParameterInner]**](SearchGetFiltersParameterInner.md)| Filters to apply | [optional] 
 **limit** | **int**| Total items to return | [optional] 
 **skip** | **int**| Items to skip | [optional] 

### Return type

[**SearchList**](SearchList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**401** | not authenticated |  -  |
**500** | general error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

