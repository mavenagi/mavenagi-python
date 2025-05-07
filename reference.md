# Reference
## Actions
<details><summary><code>client.actions.<a href="src/mavenagi/actions/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an action or create it if it doesn't exist
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI
from mavenagi.commons import EntityIdBase, Precondition_Group, Precondition_User

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.actions.create_or_update(
    action_id=EntityIdBase(
        reference_id="get-balance",
    ),
    name="Get the user's balance",
    description="This action calls an API to get the user's current balance.",
    user_interaction_required=False,
    user_form_parameters=[],
    precondition=Precondition_Group(
        operator="AND",
        preconditions=[
            Precondition_User(
                key="userKey",
            ),
            Precondition_User(
                key="userKey2",
            ),
        ],
    ),
    language="en",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action_id:** `EntityIdBase` — ID that uniquely identifies this action
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the action. This is displayed to the end user as part of forms when user interaction is required. It is also used to help Maven decide if the action is relevant to a conversation.
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — The description of the action. Must be less than 1024 characters. This helps Maven decide if the action is relevant to a conversation and is not displayed directly to the end user. Descriptions are used by the LLM.
    
</dd>
</dl>

<dl>
<dd>

**user_interaction_required:** `bool` — Whether the action requires user interaction to execute. If false, and all of the required action parameters are known, the LLM may call the action automatically. If true, an conversations ask call will return a BotActionFormResponse which must be submitted by an API caller. API callers must display a button with the buttonName label to confirm the user's intent.
    
</dd>
</dl>

<dl>
<dd>

**user_form_parameters:** `typing.Sequence[ActionParameter]` — The parameters that the action uses as input. An action will only be executed when all of the required parameters are provided. During execution, actions all have access to the full Conversation and User objects. Parameter values may be inferred from the user's conversation by the LLM.
    
</dd>
</dl>

<dl>
<dd>

**button_name:** `typing.Optional[str]` — When user interaction is required, the name of the button that is shown to the end user to confirm execution of the action. Defaults to "Submit" if not supplied.
    
</dd>
</dl>

<dl>
<dd>

**precondition:** `typing.Optional[Precondition]` — The preconditions that must be met for an action to be relevant to a conversation. Can be used to restrict actions to certain types of users.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — The ISO 639-1 code for the language used in all fields of this action. Will be derived using the description's text if not specified.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/mavenagi/actions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an action by its supplied ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.actions.get(
    action_reference_id="get-balance",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action_reference_id:** `str` — The reference ID of the action to get. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/mavenagi/actions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an action
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.actions.delete(
    action_reference_id="get-balance",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action_reference_id:** `str` — The reference ID of the action to unregister. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Analytics
<details><summary><code>client.analytics.<a href="src/mavenagi/analytics/client.py">get_conversation_table</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves structured conversation data formatted as a table, allowing users to group, filter, and define specific metrics to display as columns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

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
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**field_groupings:** `typing.Sequence[ConversationGroupBy]` 

Specifies the fields by which data should be grouped. Each unique combination forms a row.
If multiple fields are provided, the result is grouped by their unique value combinations.
If empty, all data is aggregated into a single row. |
Note: The field `CreatedAt` should not be used here, all time-based grouping should be done using the `timeGrouping` field.
    
</dd>
</dl>

<dl>
<dd>

**column_definitions:** `typing.Sequence[ConversationColumnDefinition]` — Specifies the metrics to be displayed as columns. Column headers act as keys, with computed metric values as their mapped values. There needs to be at least one column definition in the table request.
    
</dd>
</dl>

<dl>
<dd>

**time_grouping:** `typing.Optional[TimeInterval]` — Defines the time interval for grouping data. If specified, data is grouped accordingly  based on the time they were created. Example: If set to "DAY," data will be aggregated by day.
    
</dd>
</dl>

<dl>
<dd>

**conversation_filter:** `typing.Optional[ConversationFilter]` — Optional filter applied to refine the conversation data before processing.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.analytics.<a href="src/mavenagi/analytics/client.py">get_conversation_chart</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches conversation data visualized in a chart format. Supported chart types include pie chart, date histogram, and stacked bar charts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI
from mavenagi.analytics import (
    ConversationChartRequest_BarChart,
    ConversationGroupBy,
    ConversationMetric_Count,
)
from mavenagi.conversation import ConversationFilter

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.analytics.get_conversation_chart(
    request=ConversationChartRequest_BarChart(
        conversation_filter=ConversationFilter(
            languages=["en", "es"],
        ),
        bar_definition=ConversationGroupBy(
            field="Category",
        ),
        metric=ConversationMetric_Count(),
        vertical_grouping=ConversationGroupBy(
            field="ResolutionStatus",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ConversationChartRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.analytics.<a href="src/mavenagi/analytics/client.py">get_feedback_table</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves structured feedback data formatted as a table, allowing users to group, filter,  and define specific metrics to display as columns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI
from mavenagi.analytics import (
    FeedbackColumnDefinition,
    FeedbackGroupBy,
    FeedbackMetric_Count,
)
from mavenagi.conversation import FeedbackFilter

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.analytics.get_feedback_table(
    feedback_filter=FeedbackFilter(
        types=["THUMBS_UP", "INSERT"],
    ),
    field_groupings=[
        FeedbackGroupBy(
            field="CreatedBy",
        )
    ],
    column_definitions=[
        FeedbackColumnDefinition(
            header="feedback_count",
            metric=FeedbackMetric_Count(),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**field_groupings:** `typing.Sequence[FeedbackGroupBy]` 

Specifies the fields by which data should be grouped. Each unique combination forms a row. 
If multiple fields are provided, the result is grouped by their unique value combinations. 
If empty, all data is aggregated into a single row. 
Note: The field CreatedAt should not be used here, all the time-based grouping should be done using the timeGrouping field.
    
</dd>
</dl>

<dl>
<dd>

**column_definitions:** `typing.Sequence[FeedbackColumnDefinition]` 

Specifies the metrics to be displayed as columns.
Column headers act as keys, with computed metric values as their mapped values.
There needs to be at least one column definition in the table request.
    
</dd>
</dl>

<dl>
<dd>

**time_grouping:** `typing.Optional[TimeInterval]` 

Defines the time interval for grouping data. If specified, data is grouped accordingly based on the time they were created.
 Example: If set to "DAY," data will be aggregated by day.
    
</dd>
</dl>

<dl>
<dd>

**feedback_filter:** `typing.Optional[FeedbackFilter]` — Optional filter applied to refine the feedback data before processing.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AppSettings
<details><summary><code>client.app_settings.<a href="src/mavenagi/app_settings/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for app settings which have the `$index` key set to the provided value.

You can set the `$index` key using the Update app settings API.

<Warning>This API currently requires an organization ID and agent ID for any agent which is installed on the app. This requirement will be removed in a future update.</Warning>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.app_settings.search(
    index="index",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**index:** `str` — Will return all settings which have the `$index` key set to the provided value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_settings.<a href="src/mavenagi/app_settings/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get app settings set during installation
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.app_settings.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.app_settings.<a href="src/mavenagi/app_settings/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update app settings. Performs a merge of the provided settings with the existing app settings.

- If a new key is provided, it will be added to the app settings.
- If an existing key is provided, it will be updated.
- No keys will be removed.

Note that if an array value is provided it will fully replace an existing value as arrays cannot be merged.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.app_settings.update(
    request={"string": {"key": "value"}},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Conversation
<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">initialize</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initialize a new conversation. 
Only required if the ask request wishes to supply conversation level data or when syncing to external systems.

Conversations can not be modified using this API. If the conversation already exists then the existing conversation will be returned.

After initialization,
- metadata can be changed using the `updateConversationMetadata` API.
- messages can be added to the conversation with the `appendNewMessages` or `ask` APIs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI
from mavenagi.commons import EntityIdBase
from mavenagi.conversation import ConversationMessageRequest

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.conversation.initialize(
    conversation_id=EntityIdBase(
        reference_id="referenceId",
    ),
    messages=[
        ConversationMessageRequest(
            user_id=EntityIdBase(
                reference_id="referenceId",
            ),
            text="text",
            user_message_type="USER",
            conversation_message_id=EntityIdBase(
                reference_id="referenceId",
            ),
        ),
        ConversationMessageRequest(
            user_id=EntityIdBase(
                reference_id="referenceId",
            ),
            text="text",
            user_message_type="USER",
            conversation_message_id=EntityIdBase(
                reference_id="referenceId",
            ),
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `EntityIdBase` — An externally supplied ID to uniquely identify this conversation
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Sequence[ConversationMessageRequest]` — The messages in the conversation
    
</dd>
</dl>

<dl>
<dd>

**response_config:** `typing.Optional[ResponseConfig]` — Optional configurations for responses to this conversation
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[str]` — The subject of the conversation
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The url of the conversation
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — The date and time the conversation was created
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` — The date and time the conversation was last updated
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Set[str]]` — The tags of the conversation. Used for filtering in Agent Designer.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` — The metadata of the conversation supplied by the app which created the conversation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a conversation
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.conversation.get(
    conversation_id="conversationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The ID of the conversation to get
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — The App ID of the conversation to get. If not provided the ID of the calling app will be used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Wipes a conversation of all user data. 
The conversation ID will still exist and non-user specific data will still be retained. 
Attempts to modify or add messages to the conversation will throw an error. 

<Warning>This is a destructive operation and cannot be undone. <br/><br/>
The exact fields cleared include: the conversation subject, userRequest, agentResponse. 
As well as the text response, followup questions, and backend LLM prompt of all messages.</Warning>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.conversation.delete(
    conversation_id="conversation-0",
    reason="GDPR deletion request 1234.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The ID of the conversation to delete
    
</dd>
</dl>

<dl>
<dd>

**reason:** `str` — The reason for deleting the conversation. This message will replace all user messages in the conversation.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — The App ID of the conversation to delete. If not provided the ID of the calling app will be used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">append_new_messages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Append messages to an existing conversation. The conversation must be initialized first. If a message with the same ID already exists, it will be ignored. Messages do not allow modification.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI
from mavenagi.commons import EntityIdBase
from mavenagi.conversation import ConversationMessageRequest

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.conversation.append_new_messages(
    conversation_id="conversationId",
    request=[
        ConversationMessageRequest(
            user_id=EntityIdBase(
                reference_id="referenceId",
            ),
            text="text",
            user_message_type="USER",
            conversation_message_id=EntityIdBase(
                reference_id="referenceId",
            ),
        ),
        ConversationMessageRequest(
            user_id=EntityIdBase(
                reference_id="referenceId",
            ),
            text="text",
            user_message_type="USER",
            conversation_message_id=EntityIdBase(
                reference_id="referenceId",
            ),
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The ID of the conversation to append messages to
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Sequence[ConversationMessageRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">ask</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an answer from Maven for a given user question. If the user question or its answer already exists, 
they will be reused and will not be updated. Messages do not allow modification once generated. 

Concurrency Behavior:
- If another API call is made for the same user question while a response is mid-stream, partial answers may be returned.
- The second caller will receive a truncated or partial response depending on where the first stream is in its processing. The first caller's stream will remain unaffected and continue delivering the full response.

Known Limitation:
- The API does not currently expose metadata indicating whether a response or message is incomplete. This will be addressed in a future update.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

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
client.conversation.ask(
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
    timezone="America/New_York",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The ID of a new or existing conversation to use as context for the question
    
</dd>
</dl>

<dl>
<dd>

**conversation_message_id:** `EntityIdBase` — Externally supplied ID to uniquely identify this message within the conversation. If a message with this ID already exists it will be reused and will not be updated.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityIdBase` — Externally supplied ID to uniquely identify the user that created this message
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — The text of the message
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[typing.Sequence[Attachment]]` — The attachments to the message.
    
</dd>
</dl>

<dl>
<dd>

**transient_data:** `typing.Optional[typing.Dict[str, str]]` — Transient data which the Maven platform will not persist. This data will only be forwarded to actions taken by this ask request. For example, one may put in user tokens as transient data.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — IANA timezone identifier (e.g. "America/New_York", "Europe/London") to be used for time-based operations in the conversation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">ask_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an answer from Maven for a given user question with a streaming response. The response will be sent as a stream of events. 
The text portions of stream responses should be concatenated to form the full response text. 
Action and metadata events should overwrite past data and do not need concatenation.

If the user question or its answer already exists, they will be reused and will not be updated. 
Messages do not allow modification once generated.
        
Concurrency Behavior:
- If another API call is made for the same user question while a response is mid-stream, partial answers may be returned.
- The second caller will receive a truncated or partial response depending on where the first stream is in its processing. The first caller's stream will remain unaffected and continue delivering the full response.

Known Limitation:
- The API does not currently expose metadata indicating whether a response or message is incomplete. This will be addressed in a future update.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

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
    timezone="America/New_York",
)
for chunk in response:
    yield chunk

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The ID of a new or existing conversation to use as context for the question
    
</dd>
</dl>

<dl>
<dd>

**conversation_message_id:** `EntityIdBase` — Externally supplied ID to uniquely identify this message within the conversation. If a message with this ID already exists it will be reused and will not be updated.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityIdBase` — Externally supplied ID to uniquely identify the user that created this message
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — The text of the message
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[typing.Sequence[Attachment]]` — The attachments to the message.
    
</dd>
</dl>

<dl>
<dd>

**transient_data:** `typing.Optional[typing.Dict[str, str]]` — Transient data which the Maven platform will not persist. This data will only be forwarded to actions taken by this ask request. For example, one may put in user tokens as transient data.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — IANA timezone identifier (e.g. "America/New_York", "Europe/London") to be used for time-based operations in the conversation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">generate_maven_suggestions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This method is deprecated and will be removed in a future release. Use either `ask` or `askStream` instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI
from mavenagi.commons import EntityIdBase

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.conversation.generate_maven_suggestions(
    conversation_id="conversationId",
    conversation_message_ids=[
        EntityIdBase(
            reference_id="referenceId",
        ),
        EntityIdBase(
            reference_id="referenceId",
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The ID of a conversation the messages belong to
    
</dd>
</dl>

<dl>
<dd>

**conversation_message_ids:** `typing.Sequence[EntityIdBase]` — The message ids to generate a suggested response for. One suggestion will be generated for each message id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">categorize</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uses an LLM flow to categorize the conversation. Experimental.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.conversation.categorize(
    conversation_id="conversationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The ID of the conversation to categorize
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">create_feedback</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update feedback or create it if it doesn't exist
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI
from mavenagi.commons import EntityIdBase

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.conversation.create_feedback(
    feedback_id=EntityIdBase(
        reference_id="feedback-0",
    ),
    user_id=EntityIdBase(
        reference_id="user-0",
    ),
    conversation_id=EntityIdBase(
        reference_id="conversation-0",
    ),
    conversation_message_id=EntityIdBase(
        reference_id="message-1",
    ),
    type="THUMBS_UP",
    text="Great answer!",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**feedback_id:** `EntityIdBase` — The ID that uniquely identifies this feedback
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `EntityIdBase` — The ID that uniquely identifies the the conversation the feedback is about
    
</dd>
</dl>

<dl>
<dd>

**conversation_message_id:** `EntityIdBase` — The ID that uniquely identifies the message within the conversation the feedback is about
    
</dd>
</dl>

<dl>
<dd>

**type:** `FeedbackType` — The type of feedback
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[EntityIdBase]` — The ID of the user who is creating the feedback
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` — The feedback text
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">submit_action_form</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit a filled out action form
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.conversation.submit_action_form(
    conversation_id="conversationId",
    action_form_id="actionFormId",
    parameters={"parameters": {"key": "value"}},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The ID of a conversation the form being submitted belongs to
    
</dd>
</dl>

<dl>
<dd>

**action_form_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Dict[str, typing.Optional[typing.Any]]` — Map of parameter IDs to values provided by the user. All required action fields must be provided.
    
</dd>
</dl>

<dl>
<dd>

**transient_data:** `typing.Optional[typing.Dict[str, str]]` — Transient data which the Maven platform will not persist. This data will only be forwarded to actions taken. For example, one may put in user tokens as transient data.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">add_conversation_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaced by `updateConversationMetadata`. 

Adds metadata to an existing conversation. If a metadata field already exists, it will be overwritten.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.conversation.add_conversation_metadata(
    conversation_id="conversationId",
    request={"string": "string"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The ID of a conversation the metadata being added belongs to
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">update_conversation_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update metadata supplied by the calling application for an existing conversation. 
Does not modify metadata saved by other apps.

If a metadata field already exists for the calling app, it will be overwritten. 
If it does not exist, it will be added. Will not remove metadata fields.

Returns all metadata saved by any app on the conversation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.conversation.update_conversation_metadata(
    conversation_id="conversation-0",
    app_id="conversation-owning-app",
    values={"key": "newValue"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The ID of the conversation to modify metadata for
    
</dd>
</dl>

<dl>
<dd>

**values:** `typing.Dict[str, str]` — The metadata values to add to the conversation.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — The App ID of the conversation to modify metadata for. If not provided the ID of the calling app will be used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search conversations
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.conversation.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sort:** `typing.Optional[ConversationField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[ConversationFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number to return, defaults to 0
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to return, defaults to 20
    
</dd>
</dl>

<dl>
<dd>

**sort_desc:** `typing.Optional[bool]` — Whether to sort descending, defaults to true
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Inbox
<details><summary><code>client.inbox.<a href="src/mavenagi/inbox/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a paginated list of inbox items for an agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.inbox.search()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**statuses:** `typing.Optional[typing.Sequence[InboxItemStatus]]` — List of inbox item statuses to filter by.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Sequence[InboxItemType]]` — List of inbox item types to filter by.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[dt.datetime]` — Filter for items created after this timestamp.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[dt.datetime]` — Filter for items created before this timestamp.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number to return, defaults to 0
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The size of the page to return, defaults to 20
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inbox.<a href="src/mavenagi/inbox/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of a specific inbox item by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.inbox.get(
    inbox_item_id="inboxItemId",
    app_id="appId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inbox_item_id:** `str` — The ID of the inbox item to get. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `str` — The App ID of the inbox item to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inbox.<a href="src/mavenagi/inbox/client.py">get_fix</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a suggested fix. Includes document information if the fix is a Missing Knowledge suggestion.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.inbox.get_fix(
    inbox_item_fix_id="inboxItemFixId",
    app_id="appId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inbox_item_fix_id:** `str` — Unique identifier for the inbox fix.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `str` — The App ID of the inbox item fix to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inbox.<a href="src/mavenagi/inbox/client.py">apply_fix</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply a fix to an inbox item with a specific document.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.inbox.apply_fix(
    inbox_item_fix_id="inboxItemFixId",
    app_id="appId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inbox_item_fix_id:** `str` — Unique identifier for the inbox fix.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**add_document_request:** `typing.Optional[AddDocumentFixRequest]` — Content for Add Document fixes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inbox.<a href="src/mavenagi/inbox/client.py">ignore</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ignore a specific inbox item by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.inbox.ignore(
    inbox_item_id="inboxItemId",
    app_id="appId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inbox_item_id:** `str` — Unique identifier for the inbox item.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `str` — The App ID of the inbox item fix to ignore
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Knowledge
<details><summary><code>client.knowledge.<a href="src/mavenagi/knowledge/client.py">create_or_update_knowledge_base</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a knowledge base or create it if it doesn't exist.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI
from mavenagi.commons import EntityIdBase

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.knowledge.create_or_update_knowledge_base(
    knowledge_base_id=EntityIdBase(
        reference_id="help-center",
    ),
    name="Help center",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_id:** `EntityIdBase` — ID that uniquely identifies this knowledge base
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the knowledge base
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` — Metadata for the knowledge base.
    
</dd>
</dl>

<dl>
<dd>

**precondition:** `typing.Optional[Precondition]` — (Beta) The preconditions that must be met for knowledge base be relevant to a conversation. Can be used to limit knowledge to certain types of users.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/mavenagi/knowledge/client.py">get_knowledge_base</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an existing knowledge base by its supplied ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.knowledge.get_knowledge_base(
    knowledge_base_reference_id="help-center",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_reference_id:** `str` — The reference ID of the knowledge base to get. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/mavenagi/knowledge/client.py">create_knowledge_base_version</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new knowledge base version.

If an existing version is in progress, then that version will be finalized in an error state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI
from mavenagi.commons import EntityId

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.knowledge.create_knowledge_base_version(
    knowledge_base_reference_id="help-center",
    version_id=EntityId(
        type="KNOWLEDGE_BASE_VERSION",
        reference_id="versionId",
        app_id="maven",
        organization_id="acme",
        agent_id="support",
    ),
    type="FULL",
    status="IN_PROGRESS",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_reference_id:** `str` — The reference ID of the knowledge base to create a version for. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `EntityId` — The unique ID of the knowledge base version.
    
</dd>
</dl>

<dl>
<dd>

**type:** `KnowledgeBaseVersionType` — Indicates whether the completed version constitutes a full or partial refresh of the knowledge base. Deleting and updating documents is only supported for partial refreshes.
    
</dd>
</dl>

<dl>
<dd>

**status:** `KnowledgeBaseVersionStatus` — The status of the knowledge base version
    
</dd>
</dl>

<dl>
<dd>

**error_message:** `typing.Optional[str]` — A user-facing error message that provides more details about a version failure.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/mavenagi/knowledge/client.py">finalize_knowledge_base_version</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Finalize the latest knowledge base version. Required to indicate the version is complete. Will throw an exception if the latest version is not in progress.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI
from mavenagi.commons import EntityIdWithoutAgent

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.knowledge.finalize_knowledge_base_version(
    knowledge_base_reference_id="help-center",
    version_id=EntityIdWithoutAgent(
        type="KNOWLEDGE_BASE_VERSION",
        reference_id="versionId",
        app_id="maven",
    ),
    status="SUCCEEDED",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_reference_id:** `str` — The reference ID of the knowledge base to finalize a version for. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `typing.Optional[EntityIdWithoutAgent]` — ID that uniquely identifies which knowledge base version to finalize. If not provided will use the most recent version of the knowledge base.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[KnowledgeBaseVersionFinalizeStatus]` — Whether the knowledge base version processing was successful or not.
    
</dd>
</dl>

<dl>
<dd>

**error_message:** `typing.Optional[str]` — A user-facing error message that provides more details about a version failure.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/mavenagi/knowledge/client.py">create_knowledge_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create knowledge document. Requires an existing knowledge base with an in progress version. Will throw an exception if the latest version is not in progress.
        
<Tip>
This API maintains document version history. If for the same reference ID neither the `title` nor `text` fields 
have changed, a new document version will not be created. The existing version will be reused.
</Tip>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI
from mavenagi.commons import EntityIdBase, EntityIdWithoutAgent

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.knowledge.create_knowledge_document(
    knowledge_base_reference_id="help-center",
    knowledge_document_id=EntityIdBase(
        reference_id="getting-started",
    ),
    version_id=EntityIdWithoutAgent(
        type="KNOWLEDGE_BASE_VERSION",
        reference_id="versionId",
        app_id="maven",
    ),
    content_type="MARKDOWN",
    content="## Getting started\\nThis is a getting started guide for the help center.",
    title="Getting started",
    metadata={"category": "getting-started"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_reference_id:** `str` — The reference ID of the knowledge base to create a document for. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**knowledge_document_id:** `EntityIdBase` — ID that uniquely identifies this knowledge document within its knowledge base
    
</dd>
</dl>

<dl>
<dd>

**content_type:** `KnowledgeDocumentContentType` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` — The content of the document. Not shown directly to users. May be provided in HTML or markdown. HTML will be converted to markdown automatically. Images are not currently supported and will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — The title of the document. Will be shown as part of answers.
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `typing.Optional[EntityIdWithoutAgent]` — ID that uniquely identifies which knowledge base version to create the document in. If not provided will use the most recent version of the knowledge base.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` — Metadata for the knowledge document.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The URL of the document. Should be visible to end users. Will be shown as part of answers. Not used for crawling.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — The document language. Must be a valid ISO 639-1 language code.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — The time at which this document was created.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` — The time at which this document was last modified.
    
</dd>
</dl>

<dl>
<dd>

**author:** `typing.Optional[str]` — The name of the author who created this document.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/mavenagi/knowledge/client.py">update_knowledge_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Not yet implemented. Update knowledge document. Requires an existing knowledge base with an in progress version of type PARTIAL. Will throw an exception if the latest version is not in progress.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI
from mavenagi.commons import EntityIdBase, EntityIdWithoutAgent

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.knowledge.update_knowledge_document(
    knowledge_base_reference_id="help-center",
    knowledge_document_id=EntityIdBase(
        reference_id="getting-started",
    ),
    version_id=EntityIdWithoutAgent(
        type="KNOWLEDGE_BASE_VERSION",
        reference_id="versionId",
        app_id="maven",
    ),
    content_type="MARKDOWN",
    content="## Getting started\\nThis is a getting started guide for the help center.",
    title="Getting started",
    metadata={"category": "getting-started"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_reference_id:** `str` — The reference ID of the knowledge base that contains the document to update. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**knowledge_document_id:** `EntityIdBase` — ID that uniquely identifies this knowledge document within its knowledge base
    
</dd>
</dl>

<dl>
<dd>

**content_type:** `KnowledgeDocumentContentType` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` — The content of the document. Not shown directly to users. May be provided in HTML or markdown. HTML will be converted to markdown automatically. Images are not currently supported and will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — The title of the document. Will be shown as part of answers.
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `typing.Optional[EntityIdWithoutAgent]` — ID that uniquely identifies which knowledge base version to create the document in. If not provided will use the most recent version of the knowledge base.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` — Metadata for the knowledge document.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The URL of the document. Should be visible to end users. Will be shown as part of answers. Not used for crawling.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — The document language. Must be a valid ISO 639-1 language code.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — The time at which this document was created.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` — The time at which this document was last modified.
    
</dd>
</dl>

<dl>
<dd>

**author:** `typing.Optional[str]` — The name of the author who created this document.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/mavenagi/knowledge/client.py">delete_knowledge_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Not yet implemented. Delete knowledge document. Requires an existing knowledge base with an in progress version of type PARTIAL. Will throw an exception if the latest version is not in progress.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mavenagi import MavenAGI

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.knowledge.delete_knowledge_document(
    knowledge_base_reference_id="help-center",
    knowledge_document_reference_id="getting-started",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**knowledge_base_reference_id:** `str` — The reference ID of the knowledge base that contains the document to delete. All other entity ID fields are inferred from the request
    
</dd>
</dl>

<dl>
<dd>

**knowledge_document_reference_id:** `str` — The reference ID of the knowledge document to delete. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organizations
<details><summary><code>client.organizations.<a href="src/mavenagi/organizations/client.py">get_conversation_table</a>(...)</code></summary>
