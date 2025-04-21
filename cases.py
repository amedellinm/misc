from collections.abc import Iterable, Mapping, Sequence

from pyspark.sql import functions as F
from pyspark.sql.column import Column


def cases(cases: list[tuple[Column, Column]], otherwise: Column = None) -> Column:
    """Build a chained when-otherwise expression from condition-value pairs."""
    ans = F
    for condition, value in cases:
        ans = ans.when(condition, value)
    return ans.otherwise(otherwise)


# @TYPEHINTHANDLER
def remap(
    column: str | Column,
    mapping: Mapping | Iterable[Sequence],
    otherwise: Column = Ellipsis,
) -> Column:
    """Change the data in `column` from the keys to the values of `mapping`."""
    if isinstance(mapping, Mapping):
        mapping = mapping.items()

    return cases(
        [(column == key, val) for key, val in mapping],
        column if otherwise is Ellipsis else otherwise,
    )
