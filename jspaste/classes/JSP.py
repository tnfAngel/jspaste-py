from typing import Any, Optional

from .Client import Client

# TODO: instantiate Document & ClientDocument Classes for responses


class JSP:
    def __init__(self, client_options: Optional[dict] = None):
        self.client = Client(client_options)

    async def access(self, key: str):
        return await self.client.access(key)

    async def publish(self, data: Any, options: Optional[dict] = None):
        return await self.client.publish(data, options)

    async def exists(self, key: str):
        return await self.client.exists(key)

    async def edit(self, data: Any, options: dict):
        return await self.client.edit(data, options)

    async def remove(self, key: str, options: dict):
        return await self.client.remove(key, options)
