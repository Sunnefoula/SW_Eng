from typing import Union, Optional, Tuple


def test_function(a: int)-> int:
    return a


def test_print(a: tuple) -> None:
    print(a)


def division(a: int, b :Optional[int]) -> Union[float, None]:
    if b is None:
        return a
    if b!=0:
        return a/b
    return


def test_unpack(input_val: dict[str, int], dict_key: str) -> Tuple[str, int]:
    return input_val(dict_key)


return_value = test_function(3)
print(return_value)

test_print("1")

