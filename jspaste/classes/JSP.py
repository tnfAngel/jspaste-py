from typing import Any, Optional

from .Client import Client

# TODO: instantiate Document & ClientDocument Classes for client responses


class JSP:
    def __init__(self, client_options: Optional[dict] = None):
        self.client = Client(client_options)

    async def access(self, key: str):
        """Access to the specified document using the key."""

        return await self.client.access(key)

    async def publish(self, data: Any, options: Optional[dict] = None):
        """Publish a document with the given data and options."""

        return await self.client.publish(data, options)

    async def exists(self, key: str):
        """Check if a document exists using the key. API Version >=v2."""

        return await self.client.exists(key)

    async def edit(self, data: Any, options: dict):
        """Edit a document using the key and the document secret. API Version >=v2."""

        return await self.client.edit(data, options)

    async def remove(self, key: str, options: dict):
        """Delete a document using the key and the document secret."""

        return await self.client.remove(key, options)
