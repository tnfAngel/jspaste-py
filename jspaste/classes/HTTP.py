from aiohttp import ClientSession, ClientResponse


class HTTP:
    def __init__(self, options: dict):
        self.options = options

    async def fetch(self, endpoint: str, options: dict):
        """Do a HTTP Request and return the response body."""

        async with ClientSession() as session:
            self.session = session

        headers = {}

        self_headers = self.options.get("headers")
        if self_headers:
            headers.update(self_headers)

        explicit_headers = options.get("headers")
        if explicit_headers:
            headers.update(explicit_headers)

        method = options.get("method")
        body = options.get("body", None)

        # TODO: Perf: Reuse the same session for every request
        async with ClientSession() as session:
            if method == "GET":
                response = await session.get(endpoint, headers=headers)
            elif method == "POST":
                response = await session.post(endpoint, headers=headers, json=body)
            elif method == "PATCH":
                response = await session.patch(endpoint, headers=headers, json=body)
            elif method == "DELETE":
                response = await session.delete(endpoint, headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            return await self.parse_response(response)

    async def parse_response(self, response: ClientResponse):
        """Parse the HTTP response."""

        content_type = response.headers.get("Content-Type")

        if not content_type:
            return None

        if content_type.startswith("application/json"):
            return await response.json()

        raise ValueError("Unknown response type.")
