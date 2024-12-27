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
