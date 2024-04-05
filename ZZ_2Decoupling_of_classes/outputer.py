from abc import abstractmethod, ABC
from typing import Optional

"""
定义与作用

Optional[T] 是一个类型别名，表示 Union[T, NoneType]。这里的 T 是一个类型变量，代表任意有效的类型（如 int, str, List[MyClass], 等）。
    因此，Optional[T] 表示的是一个值既可以是类型 T，也可以是 None。在类型检查上下文中，
    使用 Optional 注解可以帮助开发者明确表达某个变量或参数可能存在“空”值（即 None）的情况。
"""


class Outputer(ABC):
    def outputer(self, content: str) -> None:
        print(content)


class PrintOutputer(Outputer):
    def outputer(self, content: str) -> None:
        print(content)


class FileOutputer(Outputer):
    DEFAULT_PATH: str = "product_report.txt"

    def __init__(self, path: Optional[str] = DEFAULT_PATH):
        self.path = path

    def outputer(self, content: str) -> None:
        with open(self.path, 'a') as f:
            f.write(f"{content}\n")


class CombineOutputer(Outputer):
    def __init__(self):
        self._print_outputer = PrintOutputer()
        self._file_outputer = FileOutputer()

    def outputer(self, content: str) -> None:
        self._print_outputer.outputer(content)
        self._file_outputer.outputer(content)
