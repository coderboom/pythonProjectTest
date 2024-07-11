"""类的封装"""
from typing import Optional


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ProductReporter:
    NAME_LIST_LENGTH: int = 40
    PRICE_LENGTH: int = 40
    COL_NAME: str = 'NAME'
    COL_PRICE: str = "PRICE"
    HEADER_SPLITER_CHARACTER = '_'
    LINE_SPLITER_CHARACTER = '-'

    def __init__(self,
                 priducts: list[Product],
                 name_list_length: Optional[int] = NAME_LIST_LENGTH,
                 price_length: Optional[int] = PRICE_LENGTH,
                 col_name: Optional[str] = COL_NAME,
                 col_price: Optional[str] = COL_PRICE,
                 header_spliter_character: Optional[str] = HEADER_SPLITER_CHARACTER,
                 line_spliter_character: Optional[str] = LINE_SPLITER_CHARACTER
                 ) -> None:
        self.products = priducts
        self.name_list_length = name_list_length
        self.price_length = price_length
        self.col_name = col_name
        self.col_price = col_price
        self.header_spliter_character = header_spliter_character
        self.line_spliter_character = line_spliter_character

    def _get_spliter(self, spliter_charters: str) -> str:
        size = self.name_list_length + self.price_length
        return spliter_charters * size

    def _get_sumerize(self, total_price) -> str:
        return f"Total:{total_price:>{self.price_length}}"

    def _get_total_price(self) -> float:
        return sum([product.price for product in self.products])

    def _output_sumerize(self) -> None:
        # 1 获取总价
        total_price = self._get_total_price()
        # 2 产生输出内容字符串
        sumerize_content = self._get_sumerize(total_price)
        # 3 输出
        total_length = self.name_list_length + self.price_length
        print(f"{sumerize_content:>{total_length}}")

    def _get_line_spliter(self) -> str:
        return self._get_spliter(self.LINE_SPLITER_CHARACTER)

    def _get_line_item(self, name: str, price: str) -> str:
        return f"{name:<{self.name_list_length}}{price:>{self.price_length}}"

    def _output_line_item(self, name: str, price: str) -> str:
        # 1 获取每行的输出字符串
        line_item = self._get_line_item(name, price)
        print(line_item)
        # 2 获取分割符
        spliter = self._get_line_spliter()
        print(spliter)

    def _handle_product_price(self, product: Product) -> str:
        return str(product.price)

    def _handle_product_name(self, product: Product) -> str:
        name_length = len(product.name)
        half_text_width = int((self.name_list_length / 2) - 1)
        left_characters = product.name[:half_text_width]
        right_characters = product.name[-half_text_width:]
        name = f"{left_characters}...{right_characters}" if name_length > self.name_list_length else product.name
        return name

    def _output_list_item(self) -> None:
        """负责迭代项，取出内容"""
        for product in self.products:
            # 1 处理名称，空值字符在40（或规定长度），按照规则处理
            name = self._handle_product_name(product)
            # 2 处理价格
            price = self._handle_product_price(product)
            # 3 输出
            self._output_line_item(name, price)

    def _get_header_spliter(self):
        return self._get_spliter(self.HEADER_SPLITER_CHARACTER)

    def _get_header(self) -> str:
        return f'{self.col_name:^{self.name_list_length}}{self.col_price:>{self.price_length}}'

    def _output_header(self) -> None:
        # 获取头部内容
        header = self._get_header()
        # 输出
        print(header)
        # 获取分割线
        spliter = self._get_header_spliter()
        # 输出
        print(spliter)

    def report(self):  # 暴露出来的接口
        # 1 输出头部
        self._output_header()

        # 2 输出列表内容
        self._output_list_item()

        # 3 输出统计部分
        self._output_sumerize()


data = (
    {
        'name': 'Apple is a super good fruit',
        'price': 231.23},
    {
        'name': 'Ogange is aosdaosidjaosndaosiyi basndaosdjaidasaubdfjadhbfoadgfuyadgfaudfadbhwuegurqygefusdbf',
        'price': 12.8
    },
    {
        'name': 'dcudcuduc is aosdao231972371sdaoiduaousdqadbhwbbbbbbbbbbbb',
        'price': 123819
    }
)

products = [Product(**item) for item in data]
reporter = ProductReporter(products)
reporter.report()
