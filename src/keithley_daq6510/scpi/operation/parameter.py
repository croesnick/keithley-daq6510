from typing import Generic, Callable, Optional, TypeVar, Union, Iterable

T = TypeVar('T')
FormatterT = Callable[..., str]
Validator = Union[Iterable[T], Callable[[T], bool]]


class Parameter(Generic[T]):
    def __init__(self, name: str, formatter: Callable[[T], str] = str, validator: Optional[Validator] = None):
        """
        SCPI operation parameter abstraction.

        Examples:
            Most simple parameter with just a name::

                Parameter('bit_number')

            Parameter with range validation::

                Parameter('bit_number', validator=range(0, 15))

            Custom validator function rather than iterable of allowed values::

                Parameter('bit_number', validator=lambda n: 0 <= n <= 14)

            Parameter with custom formatter::

                Parameter('bit_number', formatter=lambda n: f'#b{n:b}')

        Args:
            name: Parameter name, preferably as in the official device documentation.
            formatter: Custom parameter-to-string converter to be called within SCPI operation string construction.
            validator: Custom parameter whitelist or validation function.
                Accepts an iterable of allowed values (whitelist) or a function.
                If given a function, it is expected to return True if and only if the passed value is allowed.

        Raises:
            TypeError: If validator is none of None, an iterable, or a callable.
        """
        self.name = name
        self.formatter = formatter

        if validator is not None:
            if not (isinstance(validator, Iterable) or isinstance(validator, Callable)):  # type: ignore
                raise TypeError(f'Unsupported validator type: {type(validator)}')

        self.validator = validator
