from dataclasses import dataclass


@dataclass
class ShipDevice:
    name: str
    ski: str
    ip_addresses: list[str]
    port: int
    model: str
    type: str
    id: str
    path: str