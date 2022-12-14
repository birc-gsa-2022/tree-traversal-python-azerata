"""A module for depth-first (in-order) traversal of trees."""

from dataclasses import dataclass
from typing import Iterable
from tree import T


@dataclass
class stack:
    stack: list[None | T | int]

    def add(self, element: T | None | int) -> None:
        self.stack.append(element)

    def top(self) -> T | int | None:
        return self.stack[-1]

    def pop(self) -> T | int | None:
        return self.stack.pop()

    def is_empty(self) -> bool:
        if self.stack:
            return False
        else:
            return True


def in_order(t: T | None) -> Iterable[int]:
    """In-order traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(in_order(tree))
    [1, 2, 3, 4, 5]
    """
    if t is not None:
        yield from in_order(t.left)
        yield t.val
        yield from in_order(t.right)
    else:
        pass

    return  # FIXME


def in_order_stack(t: T | None) -> Iterable[int]:
    exp_stack = stack([])
    exp_stack.add(t)

    print(exp_stack.top())
    while not exp_stack.is_empty():
        if type(exp_stack.top()) == T:
            tmp = exp_stack.pop()
            exp_stack.add(tmp.left)
            exp_stack.add(tmp.val)
            exp_stack.add(tmp.right)
        elif exp_stack.top() is None:
            exp_stack.pop()
        elif type(exp_stack.top()) == int:
            yield exp_stack.pop()
        print(exp_stack.stack)
    return


if __name__ == '__main__':
    tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    print([t for t in in_order_stack(tree)])
    print([t for t in in_order(tree)])
