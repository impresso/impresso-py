from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.authentication_create_request_strategy import AuthenticationCreateRequestStrategy

T = TypeVar("T", bound="AuthenticationCreateRequest")


@_attrs_define
class AuthenticationCreateRequest:
    """Request body for the authentication endpoint

    Attributes:
        strategy (AuthenticationCreateRequestStrategy):
        email (str):
        password (str):
    """

    strategy: AuthenticationCreateRequestStrategy
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
        strategy = AuthenticationCreateRequestStrategy(d.pop("strategy"))

        email = d.pop("email")

        password = d.pop("password")

        authentication_create_request = cls(
            strategy=strategy,
            email=email,
            password=password,
        )

        return authentication_create_request
