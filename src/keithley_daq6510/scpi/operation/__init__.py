import logging
import types
from itertools import zip_longest
from typing import Callable, Optional, Iterable, Any

from .parameter import Parameter
from ...base import MessageBasedConnection
from ...scpi.formatter.operation import comma_separated

logger = logging.getLogger(__name__)

FormatterT = Callable[..., str]


class Operation:
    def __init__(self, command: str, formatter: Optional[FormatterT] = None,
                 parameters: Optional[Iterable[Parameter]] = None):
        self.command = command.strip().upper()
        self.formatter = formatter if formatter is not None else comma_separated
        self.parameters = parameters

    def __get__(self, caller, _type=None) -> Callable[..., Any]:
        def _operation(oself: MessageBasedConnection, *args: Any, **kwargs: Any) -> Any:
            if self.parameters is None:
                return self._run(oself, *args, **kwargs)
            else:
                arguments = []
                for value, field in zip_longest(args, self.parameters, fillvalue=None):
                    if field is None:
                        break
                    if value is None and not field.optional:
                        raise ValueError(f'Expected field {field.name}, but no argument were given')

                    if field.validator is None:
                        logger.debug(f'No validation requested for {field.name}={value}')
                        continue

                    if isinstance(field.validator, Iterable) or isinstance(field.validator, Callable):  # type: ignore
                        if not field.validator(value):
                            raise ValueError(f'{field.name}={value} not within whitelisted values')
                    else:
                        raise TypeError(f'Unsupported validation type: {type(field.validator)}')

                    logger.debug(f'Validated {field.name}={value}')
                    arguments.append(field.formatter(value))

                return self._run(oself, *arguments)

        return types.MethodType(_operation, caller)

    def _run(self, connection: MessageBasedConnection, *args, **kwargs) -> Any:
        send_message_fn = connection.query if self.command.endswith('?') else connection.command

        message = self.formatter(self.command, *args, **kwargs)  # type: ignore

        logger.debug(f'Sending message: {message}')
        response = send_message_fn(message)

        logger.debug(f'Got response: {response}')
        return response
