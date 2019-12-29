# -*- coding: utf-8 -*-
"""
Module containing abstractions for SCPI operations (i.e., commands and queries).
"""

import logging
import types
from itertools import zip_longest
from typing import Callable, Optional, Iterable, Any

from .parameter import Parameter
from ...base import MessageBasedConnection
from ...scpi.formatter.operation import comma_separated

logger = logging.getLogger(__name__)

FormatterT = Callable[[str, Any], str]
ParametersT = Iterable[Parameter]


class Operation:
    """Abstraction for a SCPI operation (i.e., commands and queries).

    Instances of this class are intended to be used just like descriptors would.

    Example:
        Base usage::

            class Instrument:
                idn = Operation('*IDN?')
    """

    def __init__(self, command: str, formatter: FormatterT = comma_separated,
                 parameters: Optional[Iterable[Parameter]] = None):
        """SCPI operation (command or query) builder.

        Example:
            Intended to be used in class attribute initialization::

                class Sample:
                    idn = Operation('*IDN?')

        Args:
            command: Full SCPI command string (without parameters). SCPI queries are expected to end with a ``?``.
            formatter: Customize building and formatting the SCPI operation string before sending it to the device.
                Defaults to format ``<scpi-command> <arg1>[, <arg2>[, ...<argN>]]``.
            parameters: Define iterable of allowed parameters, including optional validation and formatting.
        """

        self.command = command.strip().upper()
        self.formatter = formatter
        self.parameters = parameters

    def __get__(self, caller: MessageBasedConnection, cls=None) -> Callable[..., Any]:
        """Get function wrapping SCPI operation parameter validation and device communication, and bind it to ``caller``.

        Args:
            caller: Instrument instance.
            cls: Instrument instance type.

        Returns:
            Callable implementing the actual parameter validation and communication with the device.
        """

        def _operation(oself: MessageBasedConnection, *args: Any, **kwargs: Any) -> Any:
            """Actual parameter validation and operation execution.

            Args:
                oself: Device connection.
                *args: SCPI operation arguments.
                **kwargs: SCPI operation keyword arguments.

            Returns:
                Whatever is returned by the executed SCPI operation.

            Raises:
                ValueError: If a value is not allowed for a parameter (usually if not whitelisted).
                TypeError: If required parameters are missing or custom validator is of unsupported type.
            """

            if self.parameters is None:
                return self._execute(oself, *args, **kwargs)

            arguments = []
            for arg, param in zip_longest(args, self.parameters, fillvalue=None):
                if param is None:
                    break
                if arg is None and not param.optional:
                    raise TypeError(f'Expected field {param.name}, but no argument were given')

                if param.validator is None:
                    logger.debug(f'No validation requested for {param.name}={arg}')
                    continue

                if not param.validator(arg):
                    raise ValueError(f'{param.name}={arg} not within whitelisted values')

                logger.debug(f'Validated {param.name}={arg}')
                arguments.append(param.formatter(arg))

            return self._execute(oself, *arguments)

        return types.MethodType(_operation, caller)

    def _execute(self, connection: MessageBasedConnection, *args, **kwargs) -> Any:
        """Build SCPI operation string and send it over the provided ``connection``.

        Args:
            connection: Device connection.
            *args: SCPI operation arguments.
            **kwargs: SCPI operation keyword arguments.

        Returns:
            Whatever is returned by the executed SCPI operation.
        """

        send_message_fn = connection.query if self.command.endswith('?') else connection.command

        message = self.formatter(self.command, *args, **kwargs)  # type: ignore

        logger.debug(f'Sending message: {message}')
        response = send_message_fn(message)

        logger.debug(f'Got response: {response}')
        return response
