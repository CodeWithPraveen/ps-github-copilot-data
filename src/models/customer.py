from dataclasses import dataclass


@dataclass
class Customer:
    id: str
    email: str
    locale: str
    country_code: str
