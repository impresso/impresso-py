from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.authentication_request_strategy import AuthenticationRequestStrategy

T = TypeVar("T", bound="AuthenticationRequest")


@_attrs_define
class AuthenticationRequest:
    """Authentication request

    Attributes:
        strategy (AuthenticationRequestStrategy):
        email (str):
        password (str):
    """

    strategy: AuthenticationRequestStrategy
    email: str
    password: str

    def to_dict(self) -> Dict[str, Any]:
        strategy = self.strategy.value

        email = self.email

        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "strategy": strategy,
                "email": email,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        strategy = AuthenticationRequestStrategy(d.pop("strategy"))

        email = d.pop("email")

        password = d.pop("password")

        authentication_request = cls(
            strategy=strategy,
            email=email,
            password=password,
        )

        return authentication_request
