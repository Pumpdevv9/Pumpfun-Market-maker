from __future__ import annotations
from abc import ABC, abstractmethod
from ..models import Quote

class Venue(ABC):
    @abstractmethod
    def get_mid(self) -> float: ...

    @abstractmethod
    def place_quote(self, quote: Quote) -> None: ...

    @abstractmethod
    def poll_fills(self) -> list[tuple[str, float, float]]:
        """
        returns list of (side, price, size)
        side: "buy" => our bid filled; "sell" => our ask filled
        """
        ...
