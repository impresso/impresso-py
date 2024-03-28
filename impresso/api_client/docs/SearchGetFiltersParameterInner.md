# SearchGetFiltersParameterInner

A single filter criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** |  | [optional] [default to 'include']
**op** | **str** |  | [optional] [default to 'OR']
**type** | **str** | Possible values are in &#39;search.validators:eachFilterValidator.type.choices&#39; | 
**precision** | **str** |  | [optional] [default to 'exact']
**q** | [**SearchGetFiltersParameterInnerQ**](SearchGetFiltersParameterInnerQ.md) |  | [optional] 
**daterange** | **str** |  | [optional] 
**uids** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from impresso.api_client.models.search_get_filters_parameter_inner import SearchGetFiltersParameterInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchGetFiltersParameterInner from a JSON string
search_get_filters_parameter_inner_instance = SearchGetFiltersParameterInner.from_json(json)
# print the JSON string representation of the object
print(SearchGetFiltersParameterInner.to_json())

# convert the object into a dict
search_get_filters_parameter_inner_dict = search_get_filters_parameter_inner_instance.to_dict()
# create an instance of SearchGetFiltersParameterInner from a dict
search_get_filters_parameter_inner_form_dict = search_get_filters_parameter_inner.from_dict(search_get_filters_parameter_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


