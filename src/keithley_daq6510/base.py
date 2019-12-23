from typing import Any

from pyvisa.resources import MessageBasedResource


class MessageBasedConnection:
    conn: MessageBasedResource

    def query(self, message: str) -> Any:
        ...

    def command(self, message: str) -> Any:
        ...
