from typing import Callable, Any
from outputer import Outputer

creation_functions: dict[str, Callable[..., Outputer]] = {}


def register(kind: str, creation_function: Callable[..., Outputer]):
    creation_functions[kind] = creation_function


def unregister(kind: str):
    creation_functions.pop(kind, None)


def create(args: dict[str, Any]) -> Outputer:
    the_args = args.copy()
    kind = the_args.pop('kind')
    try:
        creation_function = creation_functions[kind]
        return creation_function(**the_args)
    except KeyError:
        raise ValueError(f"未知的outputer{kind}") from None
