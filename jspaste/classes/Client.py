from typing import Any, Optional
from ..types.Client import APIEndpointVersion
from .HTTP import HTTP
from .. import __version__


class Client:
    @property
    def default_http_options(self):
        """The default http options for the client."""

        return {
            "headers": {
                "User-Agent": f"JSPaste-Py/{__version__} (https://github.com/tnfAngel/jspaste-py)"
            },
            "retries": 3,
            "timeout": 1000,
        }

    @property
    def default_jsp_options(self):
        """The default JSPaste options for the client."""

        return {
            "api": "https://jspaste.eu/api",
            "version": APIEndpointVersion.v2.value,
            "http": self.default_http_options,
        }

    def __init__(self, options: Optional[dict] = None):
        self.options = options if options is not None else self.default_jsp_options
        self.endpoint = f"{self.options.get('api')}/v{self.options.get('version')}"
        self.http = HTTP(self.options.get("http"))

    async def access(self, key: str, options: Optional[dict] = None) -> dict:
        """Access to the specified document using the key."""

        headers = {}

        if options:
            password = options.get("password")
            headers.update({"password": password}) if password else None

        return await self.http.fetch(
            f"{self.endpoint}/documents/{key}",
            options={"method": "GET", "headers": headers},
        )

    async def publish(self, data: Any, options: Optional[dict] = None) -> dict:
        """Publish a document with the given data and options."""

        headers = {}

        if options:
            key = options.get("key")
            headers.update({"key": key}) if key else None

            key_length = options.get("key_length")
            headers.update({"keyLength": key_length}) if key_length else None

            secret = options.get("secret")
            headers.update({"secret": secret}) if secret else None

            password = options.get("password")
            headers.update({"password": password}) if password else None

            lifetime = options.get("lifetime")
            headers.update({"lifetime": lifetime}) if lifetime else None

        return await self.http.fetch(
            f"{self.endpoint}/documents",
            options={"method": "POST", "body": data, "headers": headers},
        )

    async def exists(self, key: str) -> bool:
        """Check if a document exists using the key. API Version >=v2."""

        if self.options["version"] < APIEndpointVersion.v2:
            raise ValueError('"Exists" can only be used with API version 2 or higher.')

        return await self.http.fetch(
            f"{self.endpoint}/documents/{key}/exists",
            options={
                "method": "GET",
            },
        )

    async def edit(self, key: str, options: dict) -> dict:
        """Edit a document using the key and the document secret. API Version >=v2."""

        if self.options["version"] < APIEndpointVersion.v2:
            raise ValueError('"Edit" can only be used with API version 2 or higher.')

        headers = {}

        if options:
            secret = options.get("secret")
            headers.update({"secret": secret}) if secret else None

        return await self.http.fetch(
            f"{self.endpoint}/documents/{key}",
            options={
                "method": "PATCH",
                "body": options.get("new_body"),
                "headers": headers,
            },
        )

    async def remove(self, key: str, options: dict) -> dict:
        """Delete a document using the key and the document secret."""

        headers = {}

        if options:
            secret = options.get("secret")
            headers.update({"secret": secret}) if secret else None

        return await self.http.fetch(
            f"{self.endpoint}/documents/{key}",
            options={"method": "DELETE", "headers": headers},
        )
