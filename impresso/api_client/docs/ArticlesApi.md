# impresso.api_client.ArticlesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**articles_get**](ArticlesApi.md#articles_get) | **GET** /articles | 
[**articles_id_get**](ArticlesApi.md#articles_id_get) | **GET** /articles/{id} | 


# **articles_get**
> SearchList articles_get(resolve=resolve, order_by=order_by, filters=filters, limit=limit, skip=skip)



Find articles that match the given query

### Example

* Bearer Authentication (BearerAuth):

```python
import impresso.api_client
from impresso.api_client.models.articles_get_filters_parameter import ArticlesGetFiltersParameter
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
    api_instance = impresso.api_client.ArticlesApi(api_client)
    resolve = 'resolve_example' # str | TODO (optional)
    order_by = 'order_by_example' # str | Order by term (optional)
    filters = impresso.api_client.ArticlesGetFiltersParameter() # ArticlesGetFiltersParameter | Filters to apply (optional)
    limit = 56 # int | Total items to return (optional)
    skip = 56 # int | Items to skip (optional)

    try:
        # 
        api_response = api_instance.articles_get(resolve=resolve, order_by=order_by, filters=filters, limit=limit, skip=skip)
        print("The response of ArticlesApi->articles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticlesApi->articles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolve** | **str**| TODO | [optional] 
 **order_by** | **str**| Order by term | [optional] 
 **filters** | [**ArticlesGetFiltersParameter**](.md)| Filters to apply | [optional] 
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

# **articles_id_get**
> Article articles_id_get(id)



Retrieves a single resource with the given id from the service.

### Example

* Bearer Authentication (BearerAuth):

```python
import impresso.api_client
from impresso.api_client.models.article import Article
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
    api_instance = impresso.api_client.ArticlesApi(api_client)
    id = 56 # int | ID of articles to return

    try:
        # 
        api_response = api_instance.articles_id_get(id)
        print("The response of ArticlesApi->articles_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticlesApi->articles_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of articles to return | 

### Return type

[**Article**](Article.md)

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
**404** | not found |  -  |
**500** | general error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

