# Preparing queries

Some filter parameters accept a combination of modifiers that can be used to create complex queries. For example, if we want to search for a term `Titanic` and `ship`, we can use the `AND` modifier to combine the two conditions:

```python
from impresso import AND, OR

impresso.search.find(term=AND("Titanic", "ship"))
```

We can refine this condition and search for all content items that mention `Titanic` and `ship` together **OR** mention `Titanic` and `iceberg` together **AND** do not mention `Di Caprio`. 


```python
from impresso import AND, OR

impresso.search.find(
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