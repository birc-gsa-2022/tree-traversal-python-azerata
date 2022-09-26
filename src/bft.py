"""A module for breadth-first traversal of trees."""

from collections import deque
from dataclasses import dataclass
from typing import Iterable
from tree import T


def bf_order(t: T | None) -> Iterable[int]:
    """Breadth-first traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(bf_order(tree))
    [2, 1, 4, 3, 5]
    """
    queue = deque([t])
    while queue:
        match queue[-1]:
            case T():
                tmp = queue.pop()
                queue.appendleft(tmp.val)
                queue.appendleft(tmp.left)
                queue.appendleft(tmp.right)
            case int():
                yield queue.pop()
            case None:
                queue.pop()

    return None  # FIXME


if __name__ == '__main__':
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    print([t for t in bf_order(tree)])
