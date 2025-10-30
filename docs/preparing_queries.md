# Preparing queries

Some filter parameters accept a combination of modifiers to create complex queries. For example, to search for content that mentions both `Titanic` and `ship`, you can use the `AND` modifier to combine these conditions:

```python
from impresso import AND

client.search.find(term=AND("Titanic", "ship"))
```

We can refine this condition and search for all content items that mention `Titanic` and `ship` together **OR** mention `Titanic` and `iceberg` together **AND** do not mention `Di Caprio`.


```python
from impresso import AND, OR

client.search.find(
  term=(
    AND("Titanic", "ship") | 
    AND("Titanic", "iceberg")
  ) & ~OR("Di Caprio")
)
```

## Modifiers

::: impresso.structures.OR
::: impresso.structures.AND
::: impresso.structures.DateRange
::: impresso.structures.NumericRange