import pytest

from jspaste import JSP

jsp = JSP()

publish_result = None


@pytest.mark.asyncio
async def test_jsp_publish():
    """Check if the publish if working."""

    global publish_result

    data = "Hello, world!"

    print(f"Submitting {data} to JSP")

    result = await jsp.publish(data)

    print(f"Got {result}")

    expected_result = {
        "key": str,
        "secret": str,
        "url": str,
    }

    assert isinstance(result, dict)
    assert isinstance(expected_result, dict)

    for key, value_type in expected_result.items():
        assert key in result
        assert isinstance(result[key], value_type), "Invalid result type."

    publish_result = result

    assert publish_result is not None, "Invalid publish result."


@pytest.mark.asyncio
async def test_jsp_access():
    """Check if the access if working."""

    global publish_result

    assert publish_result is not None, "Publish Test failed."

    print(f"Getting key {publish_result['key']}")

    result = await jsp.access(publish_result["key"])

    expected_result = {
        "key": str,
        "data": str,
        "url": str,
    }

    for key, value_type in expected_result.items():
        assert key in result
        assert isinstance(result[key], value_type), "Invalid result type."

    print(f"Got {result}")


if __name__ == "__main__":
    pytest.main()
