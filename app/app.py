from collections import defaultdict
from typing import List

def dedupe_header(columns: List[str]) -> List[str]:
    """
    通过附加数字后缀使重复的表头列名变得唯一。

    规则：
    - 名称的第一次出现保持原样。
    - 同一名称的第 2 次、第 3 次...出现将附加 ".1"、".2" 等。
      （这类似于 pandas 等工具处理重复列标签的方式。）
    - 完全保留给定的顺序。
    - 输入是一个字符串列表（列名）；输出是一个相同长度的列表。

    示例：
    ["id", "name", "id", "name", "name"] -> ["id", "name", "id.1", "name.1", "name.2"]
    """
    seen_counts = defaultdict(int)
    result: List[str] = []
    for col in columns:
        count = seen_counts[col]
        if count == 0:
            result.append(col)
        else:
            result.append(f"{col}.{count}")
        seen_counts[col] += 1
    return result