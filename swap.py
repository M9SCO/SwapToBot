import enum


class LayoutMappings(enum.Enum):
    EN = "qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL;\"ZXCVBNM<>?`~!@#$%^&*()_+"
    RU = "йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,ёЁ!\"№;%:?*()_+"



def swap(text: str) -> str:
    result = get_in_another_layout(text, LayoutMappings.EN.value, LayoutMappings.RU.value)
    if result == text:
        result = get_in_another_layout(text, LayoutMappings.RU.value, LayoutMappings.EN.value)

    return result


def get_in_another_layout(text: str, map_from: str, map_to: str) -> str:
    zipped = dict(zip(map_from, map_to))
    return "".join(map(lambda c: zipped.get(c, c), text))
