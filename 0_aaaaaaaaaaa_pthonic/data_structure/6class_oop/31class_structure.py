print('--------------')
"""
class 
    # 类常量
    DEFAULT_TITAL：str ='DEFAULT_TITAL' 
    DEFAULT STRING MAX LENGTH: int =10
    
    # __init__ () 构造方法，初始化————实例的属性和初始值
    def __init__(self):
    
    # 特殊方法、魔术方法————给类增添一些特色功能
    def __call__(self):
    def __repr__(self):
    
    # 类方法  ————不需要实例化就可以调用
    @classmethod
    def some class method(cls[,]):
    
    
    # 静态方法  ————和类方法雷同，只是没有cls
    @staticmethod
    def some static method():
    
    ————————————————————————————————————————————————用类方法调用静态方法完成类方法的实现
    
    
    # 私有方法  ————约定是私有方法，不要去调用
    def some private method(self[,]):
    
    # 实例方法  ————主要用来实现业务逻辑的方法
    def build(self[, ....])
    
"""
print('------------实现SideBar的类，结构见图片31class_structure_test.png----------------')


class Sidebar:
    DIV: str = 'div'
    H1: str = 'h1'
    MORE: str = 'more'
    MORE_TIEMS_LENGTH: int = 3
    SHOULD_COMPRESS_HTML: bool = True

    def __init__(self,
                 title: str,
                 menu_item: [str],
                 more: str = MORE,
                 more_items_length: int = MORE_TIEMS_LENGTH,
                 should_compress_html: bool = SHOULD_COMPRESS_HTML
                 ) -> None:
        self.title = title
        self.more = more
        self.menu_item = menu_item
        self.more_items_length = more_items_length
        self.should_compress_html = should_compress_html

    def __len__(self):
        return len(self.menu_item)

    def __repr__(self):
        return f"Sidebar:{len(self)} menu items"

    @classmethod
    def _header(cls, title):
        return cls._build_header(cls.H1, title)

    @classmethod
    def _body(cls, menu_items: [str], should_compress_html: bool):
        join_char = cls._get_split_char(should_compress_html)
        return join_char.join(
            list(cls._build_body(cls.DIV, menu_items))
        )

    @classmethod
    def _more(cls, more):
        return cls._build_more(cls.DIV, more)

    @staticmethod
    def _build_header(tag_name: str, title: str) -> str:
        return f"<{tag_name}>{title}</{tag_name}>"

    @staticmethod
    def _build_body(tag_name: str, menu_items: [str]) -> str:
        for menu_item in menu_items:
            yield f"<{tag_name}>{menu_item}</{tag_name}>"

    @staticmethod
    def _build_more(tag_name: str, text: str) -> str:
        return f"<{tag_name}>{text}</{tag_name}>"

    @staticmethod
    def _get_split_char(should_compress_html: bool):
        return '' if should_compress_html else '\n'

    def _is_few_items(self):
        return len(self) < self.more_items_length

    def build(self):
        header = self._header(self.title)
        body = self._body(self.menu_item, self.should_compress_html)
        footer = self._more(self.more) if self._is_few_items() else ''
        split_char = self._get_split_char(self.should_compress_html)
        html = split_char.join([header, body, footer])
        return html


side_bar = Sidebar('DEMO SIDE BAR',
                   ['a', 'b', 'c'],
                   should_compress_html=False,
                   more_items_length=6)
print(side_bar.build())

print(side_bar._header('babbabababa'))
print(Sidebar._header('bababbababab111'))
