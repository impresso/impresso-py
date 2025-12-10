# Impresso API resources

## Search

Search content items in the Impresso corpus.

```python
# Search for content items
impresso.search.find(term='Titanic', limit=10)

# Complex queries with AND/OR operators
from impresso import AND, OR
impresso.search.find(term=AND("hitler", "stalin") & OR("molotow", "ribbentrop"))

# Search with date range
from impresso import DateRange
impresso.search.find(term="independence", date_range=DateRange("1921-05-21", "2001-01-02"))

# Search by entity mentions
impresso.search.find(entity_id=AND("aida-0001-54-Switzerland", "aida-0001-50-Albert_Einstein"))

# Limit to specific newspapers
impresso.search.find(term="independence", newspaper_id=OR("EXP", "GDL"))

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

# Filter by entity type
impresso.entities.find(term="Paris", entity_type="location")

# Get entities with Wikidata details
impresso.entities.find(term="Paris", resolve=True)

# Search by Wikidata IDs
from impresso import AND
impresso.entities.find(wikidata_id=AND("Q2", "Q4", "Q42"))

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

::: impresso.resources.content_items.ContentItemDataContainer

## Images

Search images in the Impresso corpus. Supports text search, filtering by various metadata, and visual similarity search using embeddings.

```python
# Search for images by keyword and content type
impresso.images.find(term="rocket", content_type="object")

# Get an image with its embeddings
image = impresso.images.get("luxwort-1930-09-26-a-i0036", include_embeddings=True)

# Search for similar images using an in-corpus image
embeddings = impresso.images.get_embeddings("luxwort-1930-09-26-a-i0036")
impresso.images.find(embedding=embeddings[0], limit=10)

# Search for similar images using external image
embedding = impresso.tools.embed_image("https://example.com/image.png", target="image")
impresso.images.find(embedding=embedding, limit=10)

# Multimodal search: find images using text
text_embedding = impresso.tools.embed_text(text="portrait", target="multimodal")
impresso.images.find(embedding=text_embedding, limit=10)
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
collection = impresso.collections.get("collection-id")
collection_id = collection.raw["uid"]

# List items in a collection
items = impresso.collections.items(collection_id)

# Add items to a collection (asynchronous - may take a few minutes)
content_item = impresso.content_items.get("NZZ-1794-08-09-a-i0002")
impresso.collections.add_items(collection_id, [content_item.pydantic.uid])

# Remove items from a collection (asynchronous - may take a few minutes)
impresso.collections.remove_items(collection_id, [content_item.pydantic.uid])
```

::: impresso.resources.collections.CollectionsResource

::: impresso.api_client.models.find_collections_order_by.FindCollectionsOrderByLiteral
::: impresso.resources.collections.FindCollectionsContainer
::: impresso.resources.collections.GetCollectionContainer

## Tools: Named entity recognition and Embeddings

The python library provides tools for text processing and semantic search:

- **Named Entity Recognition (NER)**: Extract and classify named entities (people, places, organizations) from text.
- **Named Entity Linking (NEL)**: Resolve recognized entities to Wikidata entries.
- **Text Embeddings**: Generate semantic embeddings from text for similarity search across the corpus.
- **Image Embeddings**: Generate embeddings from images for visual similarity search and multimodal retrieval.

```python
text = "Jean-Baptiste Nicolas Robert Schuman (29 June 1886 – 4 September 1963) was a Luxembourg-born French statesman."

# Extract named entities from text (fast)
result = impresso.tools.ner(text)
result.df  # View entities as DataFrame

# Extract and link entities to Wikidata (slower but more detailed)
result = impresso.tools.ner_nel(text)
result.df  # Includes Wikidata links

# Link pre-tagged entities to external resources (requires [START] and [END] markers)
tagged_text = "[START] Jean-Baptiste Nicolas Robert Schuman [END] was a statesman."
impresso.tools.nel(tagged_text)

# Generate text embeddings for semantic search
text_embedding = impresso.tools.embed_text("European integration", target="text")
results = impresso.search.find(embedding=text_embedding, limit=5)

# Use in-corpus embedding for similar article search
first_item_id = results.df.index[0]
in_corpus_embedding = impresso.content_items.get_embeddings(first_item_id)[0]
impresso.search.find(embedding=in_corpus_embedding, limit=10)

# Generate image embeddings from URL
image_embedding = impresso.tools.embed_image("https://example.com/image.png", target="image")
impresso.images.find(embedding=image_embedding)
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
