# SearchList

Article search response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Article]**](Article.md) |  | 
**limit** | **int** | The number of articles returned in this response | 
**skip** | **int** | The number of articles skipped in this response | 
**total** | **int** | The total number of articles matching the query | 
**info** | **object** | Additional information about the search response. | 

## Example

```python
from impresso.api_client.models.search_list import SearchList

# TODO update the JSON string below
json = "{}"
# create an instance of SearchList from a JSON string
search_list_instance = SearchList.from_json(json)
# print the JSON string representation of the object
print(SearchList.to_json())

# convert the object into a dict
search_list_dict = search_list_instance.to_dict()
# create an instance of SearchList from a dict
search_list_form_dict = search_list.from_dict(search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


