# ArticlesGetFiltersParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**q** | **str** |  | [optional] 

## Example

```python
from impresso.api_client.models.articles_get_filters_parameter import ArticlesGetFiltersParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ArticlesGetFiltersParameter from a JSON string
articles_get_filters_parameter_instance = ArticlesGetFiltersParameter.from_json(json)
# print the JSON string representation of the object
print(ArticlesGetFiltersParameter.to_json())

# convert the object into a dict
articles_get_filters_parameter_dict = articles_get_filters_parameter_instance.to_dict()
# create an instance of ArticlesGetFiltersParameter from a dict
articles_get_filters_parameter_form_dict = articles_get_filters_parameter.from_dict(articles_get_filters_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


