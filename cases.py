from pyspark.sql import functions as F
from pyspark.sql.column import Column


def cases(case_list: list[tuple[Column, Column]], otherwise: Column = F.lit(None)):
    """Build a chained when-otherwise expression from condition-value pairs."""
    ans = F
    for condition, value in case_list:
        ans = ans.when(condition, value)
    return ans.otherwise(otherwise)


def remap(column, mapping):
    """Change the data in `column` from the keys to the values of `mapping`."""
    return cases([(F.col(column) == key, val) for key, val in mapping.items()])
