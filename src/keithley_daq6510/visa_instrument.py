from typing import Optional, Any

from pyvisa import ResourceManager

from .base import MessageBasedConnection


class VisaInstrument(MessageBasedConnection):
    def __init__(self, name: str, address: str, read_term: str, write_term: str,
                 resource_manager: Optional[ResourceManager] = None):
        self.name = name
        self.address = address
        self.read_termination = read_term
        self.write_termination = write_term

        self.resource_manager = resource_manager if resource_manager is not None else ResourceManager()

        # noinspection PyTypeChecker
        self.conn = \
            self.resource_manager.open_resource(self.address,
                                                read_termination=self.read_termination,
                                                write_termination=self.write_termination)

    def query(self, message: str) -> Any:
        return self.conn.query(message)

    def command(self, message: str) -> Any:
        return self.conn.write(message)
