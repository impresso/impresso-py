# Impresso Python

<p align="center">
  <img src="https://github.com/impresso/impresso.github.io/blob/master/assets/images/3x1--Yellow-Impresso-Black-on-White--transparent.png?raw=true" width="350" alt="Impresso Project Logo"/>
</p>

Impresso is a library designed to facilitate interaction with the [Impresso](https://impresso-project.ch/app) dataset. It offers a comprehensive set of classes for API interaction and a variety of tools to streamline data manipulation and analysis.

## Installation and prerequisites

The Impresso python library can be installed using `pip`:

```shell
pip install impresso
```

The library requires Python version `3.10` or higher. It also depends on several packages commonly found in Jupyter environments, such as `matplotlib` and `pandas`.

## At a glance

### Create a session

```python
from impresso import connect
client = connect()
```

### Search 

```python
results = client.search.find(term="moon landing")
results
```

`results` will display a summary of the result including a preview of a pandas data frame with the result data. Use `df` property to access the full data frame:

```python
results.df
```
### Pagination

!!! warning "Monthly Quota"
    Every Impresso user has a monthly quota of the content items they can access.
    The quota is currently set at 200,000 content items. Paginating through a
    large result set may see you hitting the quota limit fairly soon.
    Make sure to check the size of the full result set before fetching all pages.

By default every result object is the first page of the full result set. Use the following code to go through the rest of the pages:

```python
import pandas as pd
# Get first page with 100 items per page
results = impresso.search.find(term="landing", limit=100)
print(f"Full result contains {results.total} items.")

full_df = results.df

# Iterate through all pages
for page in results.pages():
    full_df = pd.concat([full_df, page.df])

full_df
```

### Accessing transcripts

Content item transcripts can be large and are not returned by default.
To access a transcript, request it by content item ID:

```python
result = client.content_items.get("NZG-1877-10-20-a-i0024")
result.df['text.content'][0]
```

### See content item on Web App (shortcut)
To see a specific content item in the Web App, look for the link "See this result in the Impresso App" in the rendered result summary:

```python
result = client.content_items.get("NZG-1877-10-20-a-i0024")
result
```

## About Impresso

### Impresso project

[Impresso - Media Monitoring of the Past](https://impresso-project.ch) is an interdisciplinary research project that aims to develop and consolidate tools for processing and exploring large collections of media archives across modalities, time, languages and national borders. The first project (2017-2021) was funded by the Swiss National Science Foundation under grant No. [CRSII5_173719](http://p3.snf.ch/project-173719) and the second project (2023-2027) by the SNSF under grant No. [CRSII5_213585](https://data.snf.ch/grants/grant/213585) and the Luxembourg National Research Fund under grant No. 17498891.

### Copyright

Copyright (C) 2024 The Impresso team.

### License

This program is provided as open source under the [GNU Affero General Public License](https://github.com/impresso/impresso-pyindexation/blob/master/LICENSE) v3 or later.
