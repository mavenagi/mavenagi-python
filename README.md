# Mavenagi Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fmavenagi%2Fmavenagi-python)
[![pypi](https://img.shields.io/pypi/v/mavenagi)](https://pypi.python.org/pypi/mavenagi)

The Mavenagi Python library provides convenient access to the Mavenagi API from Python.

## Installation

```sh
pip install mavenagi
```

## Reference

A full reference for this library is available [here](./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from mavenagi import MavenAGI
from mavenagi.analytics import (
    ConversationColumnDefinition,
    ConversationGroupBy,
    ConversationMetric_Average,
    ConversationMetric_Count,
    ConversationMetric_Percentile,
)
from mavenagi.conversation import ConversationFilter

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.analytics.get_conversation_table(
    conversation_filter=ConversationFilter(
        languages=["en", "es"],
    ),
    time_grouping="DAY",
    field_groupings=[
        ConversationGroupBy(
            field="Category",
        )
    ],
    column_definitions=[
        ConversationColumnDefinition(
            header="count",
            metric=ConversationMetric_Count(),
        ),
        ConversationColumnDefinition(
            header="avg_first_response_time",
            metric=ConversationMetric_Average(
                target_field="FirstResponseTime",
            ),
        ),
        ConversationColumnDefinition(
            header="percentile_handle_time",
            metric=ConversationMetric_Percentile(
                target_field="HandleTime",
                percentile=25.0,
            ),
        ),
    ],
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio

from mavenagi import AsyncMavenAGI
from mavenagi.analytics import (
    ConversationColumnDefinition,
    ConversationGroupBy,
    ConversationMetric_Average,
    ConversationMetric_Count,
    ConversationMetric_Percentile,
)
from mavenagi.conversation import ConversationFilter

client = AsyncMavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)


async def main() -> None:
    await client.analytics.get_conversation_table(
        conversation_filter=ConversationFilter(
            languages=["en", "es"],
        ),
        time_grouping="DAY",
        field_groupings=[
            ConversationGroupBy(
                field="Category",
            )
        ],
        column_definitions=[
            ConversationColumnDefinition(
                header="count",
                metric=ConversationMetric_Count(),
            ),
            ConversationColumnDefinition(
                header="avg_first_response_time",
                metric=ConversationMetric_Average(
                    target_field="FirstResponseTime",
                ),
            ),
            ConversationColumnDefinition(
                header="percentile_handle_time",
                metric=ConversationMetric_Percentile(
                    target_field="HandleTime",
                    percentile=25.0,
                ),
            ),
        ],
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from mavenagi.core.api_error import ApiError

try:
    client.analytics.get_conversation_table(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Streaming

The SDK supports streaming responses, as well, the response will be a generator that you can loop over.

```python
from mavenagi import MavenAGI
from mavenagi.commons import EntityIdBase
from mavenagi.conversation import Attachment

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
response = client.conversation.ask_stream(
    conversation_id="conversation-0",
    conversation_message_id=EntityIdBase(
        reference_id="message-0",
    ),
    user_id=EntityIdBase(
        reference_id="user-0",
    ),
    text="How do I reset my password?",
    attachments=[
        Attachment(
            type="image/png",
            content="iVBORw0KGgo...",
        )
    ],
    transient_data={"userToken": "abcdef123", "queryApiKey": "foobar456"},
)
for chunk in response:
    yield chunk
```

## Advanced

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retriable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retriable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.analytics.get_conversation_table(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from mavenagi import MavenAGI

client = MavenAGI(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.analytics.get_conversation_table(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.
```python
import httpx
from mavenagi import MavenAGI

client = MavenAGI(
    ...,
    httpx_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
