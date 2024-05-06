import time
from typing import Optional
from .Client import Client


class Document:
    def __init__(
        self,
        client: Client,
        key: str,
        data: str,
        url: Optional[str] = None,
        password: Optional[str] = None,
        lifetime: Optional[int] = None,
        expiration_timestamp: Optional[int] = None,
        secret: Optional[str] = None,
    ):
        self.client = client
        self.key = key
        self.data = data
        self.url = url
        self.password = password
        self.lifetime = lifetime
        self.expiration_timestamp = expiration_timestamp
        self.secret = secret

    def set_key(self, key: str):
        return self.refresh(key=key)

    def set_data(self, data: str):
        return self.refresh(data=data)

    def set_password(self, password: str):
        return self.refresh(password=password)

    def set_secret(self, secret: str):
        return self.refresh(secret=secret)

    def set_lifetime(self, lifetime: int):
        return self.refresh(lifetime=lifetime)

    async def access(self):
        document = await self.client.access(self.key)

        return self.refresh(
            key=document.get("key"),
            data=document.get("data"),
            url=document.get("url"),
            expiration_timestamp=document.get("expirationTimestamp"),
        )

    async def publish(self, data: Optional[dict] = None):
        if data:
            self.data = data

        lifetime = None

        if self.lifetime or self.expiration_timestamp:
            lifetime = (
                str((self.expiration_timestamp or 0) - int(time.time()))
                if self.expiration_timestamp
                else None
            )

        document = await self.client.publish(
            self.data,
            key=self.key,
            lifetime=lifetime,
            password=self.password,
            secret=self.secret,
        )

        return self.refresh(
            key=document.get("key"),
            secret=document.get("secret"),
            url=document.get("url"),
            expiration_timestamp=document.get("expirationTimestamp"),
        )

    async def exists(self):
        return await self.client.exists(self.key)

    def refresh(
        self,
        key: Optional[str] = None,
        data: Optional[str] = None,
        url: Optional[str] = None,
        password: Optional[str] = None,
        lifetime: Optional[int] = None,
        expiration_timestamp: Optional[int] = None,
        secret: Optional[str] = None,
    ):
        if key:
            self.key = key
        if data:
            self.data = data
        if url:
            self.url = url
        if password:
            self.password = password
        if lifetime or lifetime == 0:
            self.lifetime = lifetime
        if expiration_timestamp or expiration_timestamp == 0:
            self.expiration_timestamp = expiration_timestamp
        if secret:
            self.secret = secret

        return self
