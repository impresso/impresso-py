# Impresso API resources

## Search

Search content items in the Impresso corpus.

```python
# Search for content items
impresso.search.find(term='Titanic', limit=10)

# Get facets to analyze search results
impresso.search.facet(facet='newspaper', term='war')
```

::: impresso.resources.search.SearchResource

::: impresso.api_client.models.search_order_by.SearchOrderByLiteral
::: impresso.resources.search.SearchDataContainer

## Entities

Search entities in the Impresso corpus.

```python
# Search for entities
impresso.entities.find(term="Douglas Adams")

# Get a specific entity by ID
impresso.entities.get("entity-id")
```

::: impresso.resources.entities.EntitiesResource

::: impresso.resources.entities.EntityType
::: impresso.api_client.models.find_entities_order_by.FindEntitiesOrderByLiteral
::: impresso.resources.entities.FindEntitiesContainer

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
# Get a content item by ID
impresso.content_items.get("NZZ-1794-08-09-a-i0002")

# Get a content item with embeddings
impresso.content_items.get("NZZ-1794-08-09-a-i0002", include_embeddings=True)

# Get only the embeddings of a content item
embeddings = impresso.content_items.get_embeddings("NZZ-1794-08-09-a-i0002")
```

::: impresso.resources.content_items.ContentItemsResource

::: impresso.resources.content_items.GetContentItemContainer

## Images

Search images in the Impresso corpus. Supports text search, filtering by various metadata, and visual similarity search using embeddings.

```python
# Search for images by keyword
impresso.images.find(term="war")

# Search by visual similarity
from impresso import DateRange
embedding = impresso.tools.embed_image("path/to/image.jpg", target="image")
impresso.images.find(embedding=embedding, date_range=DateRange(start="1900-01-01", end="1910-12-31"))

# Get a specific image by ID
impresso.images.get("image-id")

# Get only the embeddings of an image
embeddings = impresso.images.get_embeddings("image-id")
```

::: impresso.resources.images.ImagesResource

::: impresso.api_client.models.find_images_order_by.FindImagesOrderByLiteral
::: impresso.resources.images.FindImagesContainer
::: impresso.resources.images.GetImageContainer

## Topics

Search topics in the Impresso database. Topics are thematic clusters discovered through topic modeling of the newspaper content.

```python
# Search for topics
impresso.topics.find(term="economy")

# Get a specific topic by ID
impresso.topics.get("topic-id")
```

::: impresso.resources.topics.TopicsResource

::: impresso.api_client.models.find_topics_order_by.FindTopicsOrderByLiteral
::: impresso.resources.topics.FindTopicsContainer
::: impresso.resources.topics.GetTopicContainer

## Data Providers

Search data providers in the Impresso database. Data providers are partner institutions that provide content to Impresso, such as libraries, archives, and media organizations.

```python
# Search for data providers
impresso.data_providers.find(term="library")

# Get a specific data provider by ID
impresso.data_providers.get("provider-id")
```

::: impresso.resources.data_providers.DataProvidersResource

::: impresso.resources.data_providers.FindDataProvidersContainer
::: impresso.resources.data_providers.GetDataProviderContainer

## Experiments

Execute experiments with the Impresso platform. Experiments allow you to interact with various computational tools and models.

```python
# List all available experiments
experiments = impresso.experiments.find()

# Execute a specific experiment
result = impresso.experiments.execute(
    experiment_id="some-experiment-id",
    body={"param": "value"}
)
```

::: impresso.resources.experiments.ExperimentsResource

::: impresso.resources.experiments.FindExperimentsContainer

## Collections

Work with collections

```python
# Search for collections
impresso.collections.find(term="war")

# Get a specific collection by ID
impresso.collections.get("collection-id")

# List items in a collection
impresso.collections.items("collection-id")

# Add items to a collection
impresso.collections.add_items("collection-id", ["item-id-1", "item-id-2"])

# Remove items from a collection
impresso.collections.remove_items("collection-id", ["item-id-1"])
```

::: impresso.resources.collections.CollectionsResource

::: impresso.api_client.models.find_collections_order_by.FindCollectionsOrderByLiteral
::: impresso.resources.collections.FindCollectionsContainer
::: impresso.resources.collections.GetCollectionContainer

## Named entity recognition

The python library contains a set of named entity recognition methods that use the same NER model used to add entities to the Impresso database.

```python
# Extract named entities from text (fast)
impresso.tools.ner("Napoleon visited Paris in 1815.")

# Extract and link entities to Wikidata (slower but more detailed)
impresso.tools.ner_nel("Napoleon visited Paris in 1815.")

# Link pre-tagged entities to external resources
impresso.tools.nel("[START]Napoleon[END] visited [START]Paris[END] in 1815.")

# Generate text embeddings for semantic search
embedding = impresso.tools.embed_text("military conflict", target="text")
impresso.search.find(embedding=embedding)

# Generate image embeddings from file or URL
embedding = impresso.tools.embed_image("path/to/image.jpg", target="image")
impresso.images.find(embedding=embedding)
```

::: impresso.resources.tools.ToolsResource
::: impresso.resources.tools.NerContainer

## Text reuse

Two resources can be used to search text reuse clusters and passages.

```python
# Find text reuse clusters
impresso.text_reuse_clusters.find(cluster_size=(10, 20))

# Get facets for clusters (e.g., newspaper distribution)
impresso.text_reuse_clusters.facet(facet='newspaper', order_by='count')

# Find text reuse passages
impresso.text_reuse_passages.find(term='revolution', country='FR')

# Get facets for passages
impresso.text_reuse_passages.facet(facet='newspaper')
```

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
