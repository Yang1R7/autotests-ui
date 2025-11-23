from elements.base_element import BaseElement


class Image(BaseElement):
    class Icon(BaseElement):
        @property
        def type_of(self) -> str:
            return "image"
