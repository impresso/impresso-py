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

# A Glance:

## Create a session

```
from impresso import connect
client = connect()
```

## Search 
```
results = client.search.find(term="moon landing")
results
```
'results' will be displayed as preview of pandas data frame. To see full data frame, run:
```
results.df
```
## Pagination
'results' are paginated. This data frame just displays the first 100 results. To navigate through pages, use:
```
# Define the total amount of items you want to retrieve 
total_results = 2000
limit = 1000

# This creates a list called 'all_results' to save your items 
all_results = []

# Now you loop through pages of 1000 outputs until you have collected all the items you defined in 'total_results'
# Results are saved in the list 'all_results'
for offset in range(0, total_results, limit):
    results = client.search.find(
        term="Titanic",
        order_by="-date",
        limit=limit,
        offset=offset
    )
    all_results.append(results.df)

# To conclude, you transform your list into a Pandas Dataframe and visualise it by running 'full_results_df'
full_results_df = pd.concat(all_results, ignore_index=True)
full_results_df
```
## Accessing transcripts 
Transcripts, text data from content items, can accessed by sending a request using the content item id. See example below:
```
results = client.content_items.get("NZG-1877-10-20-a-i0024")
# transcript data is shown in column 'text.content'
```
## See content item on Web App (shortcut)
To see a specific content item on the Web App, just add the content item id on the URL
https://impresso-project.ch/app/article/{id}


## About Impresso

### Impresso project

[Impresso - Media Monitoring of the Past](https://impresso-project.ch) is an interdisciplinary research project that aims to develop and consolidate tools for processing and exploring large collections of media archives across modalities, time, languages and national borders. The first project (2017-2021) was funded by the Swiss National Science Foundation under grant No. [CRSII5_173719](http://p3.snf.ch/project-173719) and the second project (2023-2027) by the SNSF under grant No. [CRSII5_213585](https://data.snf.ch/grants/grant/213585) and the Luxembourg National Research Fund under grant No. 17498891.

### Copyright

Copyright (C) 2024 The Impresso team.

### License

This program is provided as open source under the [GNU Affero General Public License](https://github.com/impresso/impresso-pyindexation/blob/master/LICENSE) v3 or later.
