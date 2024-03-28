# Page

A page of an article

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The unique identifier of the page | 
**num** | **int** | The number of the page | 
**issue_uid** | **str** | Reference to the article | 
**newspaper_uid** | **str** | Unique ID of the newspaper | 
**iiif** | **str** | The IIF image file name of the page | [optional] 
**iiif_thumbnail** | **str** | The IIF image thumbnail file name of the page | 
**access_rights** | **str** | The access rights code | 
**labels** | **List[str]** | Page labels | 
**has_coords** | **bool** | Whether the page has coordinates | 
**has_errors** | **bool** | Whether the page has errors | 
**regions** | **List[object]** | Regions of the page | 
**obfuscated** | **bool** | Whether the page image has been obfuscated because the user is not authorised to access it | [optional] 
**iiif_fragment** | **str** | The IIIF fragment of the page, image file name | [optional] 

## Example

```python
from impresso.api_client.models.page import Page

# TODO update the JSON string below
json = "{}"
# create an instance of Page from a JSON string
page_instance = Page.from_json(json)
# print the JSON string representation of the object
print(Page.to_json())

# convert the object into a dict
page_dict = page_instance.to_dict()
# create an instance of Page from a dict
page_form_dict = page.from_dict(page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


