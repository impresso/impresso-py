# Impresso API resources

## Search

Search content items in the Impresso corpus.

```python
impresso.search.find(term='Titanic', limit=10)
```

::: impresso.resources.search.SearchResource

::: impresso.api_client.models.search_order_by.SearchOrderByLiteral
::: impresso.resources.search.SearchDataContainer

## Entities

Search entities in the Impresso corpus.

```python
impresso.entities.find(term="Douglas Adams")
```

::: impresso.resources.entities.EntitiesResource

::: impresso.resources.entities.EntityType
::: impresso.api_client.models.find_entities_order_by.FindEntitiesOrderByLiteral

## Media sources

Search media sources available in the Impresso corpus.

```python
impresso.media_sources.find(
    term="wort",
    order_by="lastIssue",
)
```

::: impresso.resources.media_sources.MediaSourcesResource

::: impresso.api_client.models.find_media_sources_order_by.FindMediaSourcesOrderByLiteral
::: impresso.resources.media_sources.FindMediaSourcesContainer

## Content Items

Get a single content item by ID.

```python
impresso.content_items.get("NZZ-1794-08-09-a-i0002")
```

## Collections

Work with collections

::: impresso.resources.collections.CollectionsResource

::: impresso.api_client.models.find_collections_order_by.FindCollectionsOrderByLiteral
::: impresso.resources.collections.FindCollectionsContainer

## Named entity recognition

The python library contains a set of named entity recognition methods that use the same NER model used to add entities to the Impresso database.

::: impresso.resources.tools.ToolsResource
::: impresso.resources.tools.NerContainer

## Text reuse

Two resources can be used to search text reuse clusters and passages.

::: impresso.resources.text_reuse.clusters.TextReuseClustersResource
::: impresso.resources.text_reuse.passages.TextReusePassagesResource

## Pagination

When you search for content items, entities, or other resources, the library returns a limited subset of the results. This means that the results are divided into pages, and you can request a specific page of results by specifying the `limit` and `offset` parameters in your query. This is done to improve performance and avoid transferring large amounts of data at once.

The `limit` parameter specifies the maximum number of items to return in a single page, and the `offset` parameter specifies the starting index of the items to return. For example, if you set `limit=10` and `offset=20`, the API will return items 20 through 29. When these parameters are not specified, the library uses default values, which is usually 0 for the `offset` and between 10 and 50 for the `limit`, depending on the resource.

The response object, an instance of `DataContainer`, contains information about the pagination, such as the total number of items (`total`), the number of items in the current page (`size`), the `limit`, and the `offset`.

When a `find` or `facet` method is called, the response object contains data for the first page or the page set by the `offset` and `limit` parameters. To get the subsequent pages, you can use the `pages` method of the response object. This method returns an iterator which yields new `DataContainer` objects for each of the subsequent pages until it reaches the end of the result set.

For example, if you want to get all the content items that mention "Titanic" with 20 items per page, you can use the following code:

```python
result = impresso.search.find(
    term="titanic",
    limit=20,
)

for page in result.pages():
    print(
        f"Got page {page.offset} - {page.offset + page.size} of {page.total}. "
        + f"The first title is {page.raw['data'][0]['title']}"
    )
```

::: impresso.data_container.DataContainer
