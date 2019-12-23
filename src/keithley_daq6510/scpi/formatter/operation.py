from typing import Any


def comma_separated(cmd: str, *args: Any, **kwargs: Any) -> str:
    if kwargs:
        raise ValueError(f'Got keyword arguments, but do not know how to format them into a SCPI command. '
                         f'Cowardly refusing to build the command. '
                         f'args: {args}. kwargs: {kwargs}')

    if not args:
        return cmd.upper()

    return f'{cmd.upper()} {", ".join([str(arg) for arg in args])}'
