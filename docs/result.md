# Result object

When you execute a query, a `DataContainer` object is returned. This object encapsulates the query results along with metadata about the query. Additionally, it provides a suite of utility methods for accessing the results in various ways.

## Understanding DataContainer

All API methods that retrieve data (`find()`, `get()`, `facet()`) return specialized container objects that extend the base `DataContainer` class. These containers provide multiple ways to access and work with your results.

## Accessing Result Data

The `DataContainer` provides several properties for accessing the same data in different formats:

### As a Pandas DataFrame

The `df` property returns results as a pandas DataFrame, which is ideal for data analysis, filtering, and manipulation:

```python
results = impresso.search.find(term="revolution", limit=10)
df = results.df

# Use standard pandas operations
print(df.head())
print(df.columns)
filtered = df[df['language'] == 'fr']
```

For image results, the DataFrame includes special formatting that renders thumbnail images in Jupyter notebooks.

### As Raw Dictionary

The `raw` property returns the complete API response as a Python dictionary:

```python
results = impresso.search.find(term="revolution", limit=10)
raw_data = results.raw

# Access the raw response structure
items = raw_data['data']
pagination = raw_data['pagination']
```

This is useful when you need the complete, unprocessed API response or want to serialize the results.

### As Pydantic Model

The `pydantic` property returns the data as a validated Pydantic model:

```python
results = impresso.search.find(term="revolution", limit=10)
model = results.pydantic

# Access data with IDE autocompletion and type checking
for item in model.data:
    print(item.title)
```

Pydantic models provide type validation and can be useful for structured data processing.

## Pagination Information

DataContainer objects include metadata about pagination:

```python
results = impresso.search.find(term="revolution", limit=20, offset=40)

print(results.total)   # Total number of results across all pages
print(results.size)    # Number of items in current page
print(results.limit)   # Maximum items per page
print(results.offset)  # Starting index of current page
```

## Iterating Through Pages

Use the `pages()` method to iterate through all pages of results automatically:

```python
# Get first page with 50 items per page
results = impresso.search.find(term="revolution", limit=50)

# Iterate through all pages
for page in results.pages():
    print(f"Processing page at offset {page.offset}")
    print(f"Contains {page.size} items")

    # Process each page's data
    for item in page.df.itertuples():
        print(item.title)
```

This is efficient for processing large result sets without loading everything into memory at once.

## Notebook Visualization

In Jupyter notebooks or similar environments, DataContainer objects automatically render a rich HTML preview when displayed:

```python
results = impresso.search.find(term="revolution", limit=10)

# Simply display the container - no need to access .df
results  # Renders as formatted HTML with preview
```

The preview includes:

- **Result summary**: Type of result, number of items, and total count
- **Link to Impresso App**: Direct link to view results in the web interface
- **Data preview**: First few rows of the DataFrame
- **Visual charts**: For facet results, displays a bar chart of the distribution

## Specialized Containers

Different API methods return specialized container types with additional features:

### Search Results (`SearchDataContainer`)

Returned by `search.find()`, contains content items with full-text search results.

### Facet Results (`FacetDataContainer`)

Returned by `search.facet()` and text reuse facet methods. Includes automatic chart visualization showing the distribution of facet values.

```python
facets = impresso.search.facet(facet='newspaper', term='war')

# The preview automatically shows a bar chart
facets  # Displays chart in notebook

# Access the data
print(facets.df['count'])  # Counts for each facet value
```

### Image Results (`FindImagesContainer`, `GetImageContainer`)

Returned by `images.find()` and `images.get()`. The DataFrame includes special formatting to display image thumbnails in notebooks:

```python
images = impresso.images.find(term='portrait', limit=10)

# In Jupyter, the DataFrame shows thumbnail images
images.df  # Displays images inline
```

### NER Results (`NerContainer`)

Returned by `tools.ner()`, `tools.ner_nel()`, and `tools.nel()`. Contains named entities extracted from text:

```python
entities = impresso.tools.ner("Napoleon visited Paris in 1815.")

# Access entities as DataFrame
print(entities.df)  # Shows entity text, type, and position
```

### Collection/Entity/Topic Containers

Single-item containers returned by `get()` methods (`GetCollectionContainer`, `GetEntityContainer`, `GetTopicContainer`, etc.) typically contain one item and provide the same access patterns:

```python
entity = impresso.entities.get("entity-id")

print(entity.df)      # Single-row DataFrame
print(entity.raw)     # Dictionary with entity details
print(entity.pydantic) # Pydantic model of the entity
```

## Web App Integration

Most containers include a `url` property that links to the corresponding view in the Impresso web application:

```python
results = impresso.search.find(term="revolution")

# Open this URL in a browser to see the results in the Impresso App
print(results.url)
```

This is automatically displayed in the notebook preview, allowing you to seamlessly transition from programmatic exploration to the visual interface.

## Common Patterns

### Collecting All Results

```python
results = impresso.search.find(term="revolution", limit=100)

# Collect all pages into a single DataFrame
all_items = []
for page in results.pages():
    all_items.append(page.df)

combined_df = pd.concat(all_items)
print(f"Total items collected: {len(combined_df)}")
```

### Conditional Processing

```python
results = impresso.search.find(term="revolution", limit=50)

for page in results.pages():
    # Stop if we've found what we're looking for
    if some_condition:
        break

    # Process page
    process_items(page.df)
```

### Exporting Results

```python
results = impresso.search.find(term="revolution", limit=100)

# Export to CSV
results.df.to_csv('results.csv')

# Export to JSON
import json
with open('results.json', 'w') as f:
    json.dump(results.raw, f, indent=2)

# Export as Parquet (efficient for large datasets)
results.df.to_parquet('results.parquet')
```

::: impresso.data_container.DataContainer
