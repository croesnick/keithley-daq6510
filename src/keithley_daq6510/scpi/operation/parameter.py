from typing import Generic, Callable, Optional, TypeVar, Union, Iterable

T = TypeVar('T')
FormatterT = Callable[..., str]
Validator = Union[Iterable[T], Callable[[T], bool]]


class Parameter(Generic[T]):
    def __init__(self, name: str, formatter: Callable[[T], str] = str, validator: Optional[Validator] = None):
        self.name = name
        self.formatter = formatter
        self.validator = validator
