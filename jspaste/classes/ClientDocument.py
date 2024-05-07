from .Client import Client
from .Document import Document
from typing import Optional


class ClientDocument(Document):
    def __init__(
        self,
        client: Client,
        key: str,
        secret: str,
        data: str,
        url: Optional[str] = None,
        password: Optional[str] = None,
        lifetime: Optional[int] = None,
        expiration_timestamp: Optional[int] = None,
        edited: Optional[bool] = None,
        removed: Optional[bool] = None,
    ):
        super().__init__(
            client, key, data, url, password, lifetime, expiration_timestamp, secret
        )

        self.secret = secret
        self.edited = edited
        self.removed = removed

    async def edit(self, data: Optional[str] = None):
        """Edit the client document."""

        result = await self.client.edit(
            self.key, {"secret": self.secret, "new_body": data or self.data}
        )

        return self.refresh(edited=result.get("edited"), data=data or self.data)

    async def remove(self):
        """Delete the client document."""

        result = await self.client.remove(self.key, {"secret": self.secret})

        return self.refresh(removed=result.get("removed"))

    def refresh(
        self,
        key: Optional[str] = None,
        data: Optional[str] = None,
        url: Optional[str] = None,
        password: Optional[str] = None,
        lifetime: Optional[int] = None,
        expiration_timestamp: Optional[int] = None,
        secret: Optional[str] = None,
        edited: Optional[bool] = None,
        removed: Optional[bool] = None,
    ):
        """Refresh the local document."""

        if key:
            self.key = key
        if data:
            self.data = data
        if url:
            self.url = url
        if password:
            self.password = password
        if lifetime:
            self.lifetime = lifetime
        if expiration_timestamp:
            self.expiration_timestamp = expiration_timestamp
        if secret:
            self.secret = secret
        if edited:
            self.edited = edited
        if removed:
            self.removed = removed

        return self
