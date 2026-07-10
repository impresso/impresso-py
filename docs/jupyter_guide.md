# Jupyter Notebook Quick Start Guide

Welcome to the Impresso Python library! This guide is designed to help you get up and running quickly with Impresso in Jupyter Notebooks. It explains the most important tools for searching, accessing, and analyzing newspaper data.

---

## 1. Connecting to Impresso

Before you can search the database, you need to connect to the Impresso API.

```python
from impresso import connect

# Create a session client
client = connect()
```

### How the Token Works
1. **First-time Login:** When you run `connect()` for the first time, a link will appear in your notebook. Click it to log in with your Impresso credentials.
2. **Copy the Token:** Copy the secret key (token) shown on that page.
3. **Paste in Jupyter:** Paste it into the input box that appears in Jupyter and press **Enter**.
4. **Auto-Save:** The library saves this token to a configuration file (`~/.impresso_py.yml`) on your computer. Next time you run your notebook, you won't need to log in again!

---

## 2. Searching and Faceting (The `client.search` Resource)

The `client.search` resource allows you to query the Impresso database to find relevant newspaper articles and group results by metadata attributes.

### A. Searching for Articles (`client.search.find`)

To find articles matching your keywords, use the `.find()` method:

```python
# Search for articles containing "moon landing"
results = client.search.find(term="moon landing")
```

#### Most Common Search Parameters

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| **`term`** | `str` | The keywords you want to search for in the text. | `term="revolution"` |
| **`date_range`** | `DateRange` | Filter articles by a specific timeframe. | `date_range=DateRange("1914-07-28", "1918-11-11")` |
| **`newspaper_id`** | `str` or `OR` | Limit results to specific newspapers. | `newspaper_id="GDL"` or `newspaper_id=OR("GDL", "EXP")` |
| **`language`** | `str` | Filter by language (2-letter ISO code: `en`, `fr`, `de`). | `language="fr"` |
| **`limit`** | `int` | How many results to return on the current page (max 100). | `limit=50` |
| **`with_text_contents`**| `bool` | If `True`, only returns articles with readable text. | `with_text_contents=True` |

> [!NOTE]
> The table above lists only the most common search filters. For a complete list of parameters—including search by title (`title`), front page status (`front_page`), entity ID (`entity_id`), entity mention (`mention`), topic ID (`topic_id`), collection ID (`collection_id`), country code (`country`), partner ID (`partner_id`), issue ID (`issue_id`), text reuse cluster ID (`text_reuse_cluster_id`), semantic embeddings (`embedding`), copyright status (`copyright`), and whether to include embeddings (`include_embeddings`)—please see the detailed [Search Resource Reference in Resources](resources.md#search).

#### Combining Search Terms
You can build complex search queries using `AND` and `OR` helper objects:

```python
from impresso import AND, OR, DateRange

results = client.search.find(
    term=AND("Titanic", "iceberg"),
    newspaper_id=OR("GDL", "EXP"),
    date_range=DateRange("1912-04-01", "1912-05-01"),
    language="fr"
)
```

---

### B. Aggregating Results (`client.search.facet`)

Faceting lets you count and group search results by a specific attribute—for example, finding how many matching articles appeared in each newspaper, or how many were written in French vs. German.

```python
# Count articles mentioning "war" grouped by newspaper
newspaper_facets = client.search.facet(facet="newspaper", term="war")
```

#### Key Facet Parameters

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| **`facet`** | `str` | The attribute to group by (`newspaper`, `language`, `year`, `decade`). | `facet="newspaper"` |
| **`term`** | `str` | Filter articles matching these terms before grouping. | `term="aviation"` |
| **`order_by`** | `str` | Sort order for the groups (`value` or `count`). | `order_by="count"` |
| **`limit`** | `int` | Maximum number of groups to return. | `limit=10` |

> [!NOTE]
> `client.search.facet` accepts the exact same search filters as `client.search.find` (like `date_range`, `language`, `newspaper_id`, etc.). For details on all filtering parameters, see [Search Resource Reference in Resources](resources.md#search). For all facet ordering options, check [SearchOrderBy in Resources](resources.md#search).

When run in a Jupyter Notebook, a facet result automatically renders as a **bar chart** showing the distribution.

---

## 3. Working with Other Resources

Besides general search, the Impresso library provides dedicated resources for accessing structured entities, media metadata, images, topic models, and collections.

### A. Entities (`client.entities`)
Find named entities (people, locations, organizations) in the Impresso database or link them to Wikidata:

```python
# Find entities matching "Douglas Adams"
entities = client.entities.find(term="Douglas Adams")

# Filter by location and resolve Wikidata details
locations = client.entities.find(term="Paris", entity_type="location", resolve=True)
```

#### Key Entity Parameters
* `term` (`str`): The name of the entity.
* `entity_type` (`str`): Type filter (e.g. `'person'` or `'location'`).
* `resolve` (`bool`): If `True`, retrieves detailed attributes from Wikidata.

> [!NOTE]
> For other parameters (such as `wikidata_id`, sorting parameters, and specific entity schemas), see the [Entities API Reference in Resources](resources.md#entities).

---

### B. Media Sources (`client.media_sources`)
Retrieve information about newspapers, magazines, and other periodicals available in the corpus:

```python
# Find media sources matching "wort" sorted by last issue date
publications = client.media_sources.find(term="wort", order_by="lastIssue")
```

#### Key Media Source Parameters
* `term` (`str`): Keyword matching the publication name.
* `order_by` (`str`): Sort criteria (e.g., `'name'`, `'firstIssue'`, `'lastIssue'`).

> [!NOTE]
> For additional media source parameters (like filtering by media type or complete ordering values), see the [Media Sources API Reference in Resources](resources.md#media-sources).

---

### C. Images (`client.images`)
Search for historical illustrations and images in newspapers, or perform visual similarity searches:

```python
# Search for images matching keyword "rocket"
images = client.images.find(term="rocket", content_type="object")
```

#### Key Image Parameters
* `term` (`str`): Metadata keyword matching the image.
* `content_type` (`str`): Classification of the image contents (e.g., `'object'`, `'portrait'`).
* `embedding` (`list`): Embedding array for similarity-based lookups.

> [!NOTE]
> For image search filters (including image-level metadata, limits, offsets, and embedding details), see the [Images API Reference in Resources](resources.md#images).

---

### D. Topics (`client.topics`)
Browse topics and thematic clusters generated through topic modeling algorithms on the newspaper texts:

```python
# Search for topics related to "economy"
topics = client.topics.find(term="economy")
```

> [!NOTE]
> For the complete list of topic attributes, ordering fields, and detail configurations, see the [Topics API Reference in Resources](resources.md#topics).

---

### E. Collections (`client.collections`)
Explore user-created and public collections of articles, or add/remove items to/from them:

```python
# Search for collections mentioning "war"
collections = client.collections.find(term="war")
```

> [!NOTE]
> For full collection management methods (including how to add and remove items with `client.collections.add_items` and `client.collections.remove_items`), see the [Collections API Reference in Resources](resources.md#collections).

---

### F. Text Reuse (`client.text_reuse`)
Explore instances where blocks of text have been repeated or syndicated across different newspapers:

```python
# Search for clusters of text reuse with 10 to 20 passages
clusters = client.text_reuse.clusters.find(cluster_size=(10, 20))

# Search for individual repeated passages mentioning "revolution" in France
passages = client.text_reuse.passages.find(term="revolution", country="FR")
```

> [!NOTE]
> For details on text reuse faceting and other parameters (such as `date_range`, `newspaper_id`, or `limit`), see the [Text Reuse API Reference in Resources](resources.md#text-reuse).

---

### G. Data Providers (`client.data_providers`)
Information about the libraries and archives that partner with Impresso to provide content:

```python
# Search for partner libraries
providers = client.data_providers.find(term="library")
```

> [!NOTE]
> For a full breakdown of provider schemas, see the [Data Providers API Reference in Resources](resources.md#data-providers).

---

## 4. Understanding the Result Object (`DataContainer`)

When you fetch data from any resource, the library returns a **`DataContainer`** (specifically a subclass like `SearchDataContainer` or `FindEntitiesContainer`). This object is a wrapper around your data and provides powerful tools to interact with it.

### Rich Preview in Jupyter
If you type the variable name of your result in a cell and run it, Jupyter will render a beautiful visual summary:

```python
# Just type the variable to see a rich HTML preview!
results
```

The preview shows:
- **Total results** found in the entire database.
- **Current page status** (e.g. showing items 0 to 50).
- **A link to the Web App** ("*See this result in the Impresso App*"), which opens the exact same search in your browser.
- **A Data Preview table** showing the first few rows of the dataset.

---

### Accessing the Data

The result object offers multiple ways to access the data, but the most important one for analysis is **`.df`**:

#### 1. As a Pandas DataFrame (`.df`)
The `.df` property converts the current page of results into a standard **Pandas DataFrame**. This is perfect for filtering, grouping, and exporting:

```python
# Get the DataFrame
df = results.df

# Inspect the columns
print(df.columns)

# See the first few rows
df.head()
```

#### 2. Pagination Metadata
You can inspect the pagination status using these properties:
* `results.total`: The total number of matching items in the entire database.
* `results.size`: The number of items in the current page.
* `results.limit`: The maximum page size set for the request.
* `results.offset`: The starting position of the current page.

#### 3. Raw Response (`.raw`)
Returns the raw API response as a Python dictionary. Helpful if you need to inspect the direct JSON structure.
```python
raw_dict = results.raw
```

---

## 5. Practical Code Snippets

Here are some ready-to-use recipes for common tasks in Jupyter.

### A. Downloading All Pages of Results (Pagination)

By default, the library only fetches the first page of results (usually 50 or 100 items). To download all pages and combine them into a single Pandas DataFrame, use the `.pages()` method:

```python
import pandas as pd

# 1. Fetch the first page
results = client.search.find(term="moon landing", limit=100)

print(f"Downloading {results.total} results...")

# 2. Iterate through all pages and collect their DataFrames
all_pages_dfs = []
for page in results.pages():
    all_pages_dfs.append(page.df)

# 3. Combine everything into one single DataFrame
full_df = pd.concat(all_pages_dfs)

print(f"Successfully loaded {len(full_df)} articles into the DataFrame!")
```

!!! warning "Check the Total Before Downloading!"
    Every Impresso user has a **monthly quota of 200,000 content items**. If a search matches 150,000 items and you download all pages, you will consume most of your monthly quota!
    
    Always check `results.total` before running a pagination loop:
    ```python
    results = client.search.find(term="common word")
    if results.total > 5000:
        print(f"Warning: Too many results ({results.total}). Please refine your search filters.")
    ```

---

### B. Getting the Full Text of an Article

To keep the search fast, `client.search.find()` does **not** download the full text of the articles. 

If you want to read or analyze the full text of a specific article, use `client.content_items.get()` with the article's unique ID:

```python
# 1. Get the article using its ID
article = client.content_items.get("NZG-1877-10-20-a-i0024")

# 2. Access the full text content
full_text = article.raw['text']['content']
print(full_text[:500]) # Print first 500 characters
```

---

### C. Extracting Named Entities (NER)

Named Entity Recognition (NER) finds people, locations, and organizations in a text. You can run NER on any text or article content:

```python
text = "Albert Einstein was born in Ulm, Germany, and later lived in Switzerland."

# Extract and link entities to Wikidata
ner_results = client.tools.ner_nel(text)

# View results as a table
ner_results.df
```

This returns a table showing:
* **The entity name** (e.g., "Albert Einstein")
* **Its type** (e.g., Person, Location)
* **The Wikidata URL/ID** (e.g., `Q937`), which you can use to fetch more info online.

---

### D. Exporting Your Data

Once you have your results in a Pandas DataFrame, you can easily save them to your computer:

```python
# Save to a CSV file (can be opened in Excel)
full_df.to_csv("my_impresso_results.csv")

# Save as Excel file
full_df.to_excel("my_impresso_results.xlsx")
```

---

## Need More Details?
* Learn how to write complex boolean searches in [Preparing Queries](preparing_queries.md).
* Read a complete reference of the result structure in [Result Object](result.md).
* Explore other resources like images, topics, and collections in [Resources](resources.md).
