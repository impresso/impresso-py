# Article

A journal/magazine article

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The unique identifier of the article | 
**type** | **str** | The type of the article. NOTE: may be empty. | 
**title** | **str** | The title of the article | 
**size** | **int** | The size of the article in characters | 
**nb_pages** | **int** | The number of pages in this article | 
**pages** | [**List[Page]**](Page.md) |  | 
**is_cc** | **bool** | TODO | 
**excerpt** | **str** | The excerpt of the article | 
**locations** | [**List[Entity]**](Entity.md) |  | [optional] 
**persons** | [**List[Entity]**](Entity.md) |  | [optional] 

## Example

```python
from impresso.api_client.models.article import Article

# TODO update the JSON string below
json = "{}"
# create an instance of Article from a JSON string
article_instance = Article.from_json(json)
# print the JSON string representation of the object
print(Article.to_json())

# convert the object into a dict
article_dict = article_instance.to_dict()
# create an instance of Article from a dict
article_form_dict = article.from_dict(article_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


