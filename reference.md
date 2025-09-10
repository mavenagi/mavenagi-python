# Reference
## Actions
<details><summary><code>client.actions.<a href="src/mavenagi/actions/client.py">search</a>(...)</code></summary>
<dl>
<dd>

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
client.actions.search()

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

**sort:** `typing.Optional[ActionField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[ActionFilter]` 
    
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

**app_id:** `typing.Optional[str]` — The App ID of the action to get. If not provided the ID of the calling app will be used.
    
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

<details><summary><code>client.actions.<a href="src/mavenagi/actions/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update mutable action fields

The `appId` field can be provided to update an action owned by a different app. 
All other fields will overwrite the existing value on the action only if provided.
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
client.actions.patch(
    action_reference_id="actionReferenceId",
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

**action_reference_id:** `str` — The reference ID of the action to patch.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — The App ID of the action to patch. If not provided the ID of the calling app will be used.
    
</dd>
</dl>

<dl>
<dd>

**instructions:** `typing.Optional[str]` — The instructions given to the LLM when determining whether to execute the action.
    
</dd>
</dl>

<dl>
<dd>

**llm_inclusion_status:** `typing.Optional[LlmInclusionStatus]` — Determines whether the action is sent to the LLM as part of a conversation.
    
</dd>
</dl>

<dl>
<dd>

**segment_id:** `typing.Optional[EntityId]` 

The ID of the segment that must be matched for the action to be relevant to a conversation. 
A null value will remove the segment from the action, it will be available on all conversations.

Segments are replacing inline preconditions - an action may not have both an inline precondition and a segment.
Inline precondition support will be removed in a future release.
    
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

## AgentCapabilities
<details><summary><code>client.agent_capabilities.<a href="src/mavenagi/agent_capabilities/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all capabilities for an agent.
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
client.agent_capabilities.list()

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

**capability_type:** `typing.Optional[AgentCapabilityType]` 
    
</dd>
</dl>

<dl>
<dd>

**pinned:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_ids:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**user_interaction_required:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_id:** `typing.Optional[AgentCapabilityField]` — The field to sort by, defaults to created timestamp
    
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

<details><summary><code>client.agent_capabilities.<a href="src/mavenagi/agent_capabilities/client.py">get</a>(...)</code></summary>
<dl>
<dd>

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
client.agent_capabilities.get(
    integration_id="integrationId",
    capability_id="capabilityId",
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

**integration_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**capability_id:** `str` 
    
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

<details><summary><code>client.agent_capabilities.<a href="src/mavenagi/agent_capabilities/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

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
client.agent_capabilities.patch(
    integration_id="integrationId",
    capability_id="capabilityId",
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

**integration_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**capability_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether this capability is enabled or disabled
    
</dd>
</dl>

<dl>
<dd>

**description_override:** `typing.Optional[str]` — Override description for action capabilities. Only applies to actions, ignored for triggers.
    
</dd>
</dl>

<dl>
<dd>

**pinned:** `typing.Optional[bool]` — Whether this action capability is pinned. Only applies to actions, ignored for triggers.
    
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

## Agents
<details><summary><code>client.agents.<a href="src/mavenagi/agents/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for agents across all organizations.

<Tip>
This endpoint requires additional permissions. Contact support to request access.
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

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.agents.search()

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

**sort:** `typing.Optional[AgentField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[AgentFilter]` 
    
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

<details><summary><code>client.agents.<a href="src/mavenagi/agents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all agents for an organization
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
client.agents.list(
    organization_reference_id="organizationReferenceId",
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

**organization_reference_id:** `str` — The ID of the organization.
    
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

<details><summary><code>client.agents.<a href="src/mavenagi/agents/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new agent

<Tip>
This endpoint requires additional permissions. Contact support to request access.
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

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.agents.create(
    organization_reference_id="organizationReferenceId",
    agent_reference_id="agentReferenceId",
    name="name",
    environment="DEMO",
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

**organization_reference_id:** `str` — The ID of the organization.
    
</dd>
</dl>

<dl>
<dd>

**agent_reference_id:** `str` — The ID of the agent.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the agent.
    
</dd>
</dl>

<dl>
<dd>

**environment:** `AgentEnvironment` — The environment of the agent.
    
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

<details><summary><code>client.agents.<a href="src/mavenagi/agents/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an agent
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
client.agents.get(
    organization_reference_id="organizationReferenceId",
    agent_reference_id="agentReferenceId",
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

**organization_reference_id:** `str` — The ID of the organization.
    
</dd>
</dl>

<dl>
<dd>

**agent_reference_id:** `str` — The ID of the agent.
    
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

<details><summary><code>client.agents.<a href="src/mavenagi/agents/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update mutable agent fields 
All fields will overwrite the existing value on the agent only if provided.

<Tip>
This endpoint requires additional permissions. Contact support to request access.
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

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.agents.patch(
    organization_reference_id="organizationReferenceId",
    agent_reference_id="agentReferenceId",
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

**organization_reference_id:** `str` — The ID of the organization.
    
</dd>
</dl>

<dl>
<dd>

**agent_reference_id:** `str` — The ID of the agent.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the agent.
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[AgentEnvironment]` — The environment of the agent.
    
</dd>
</dl>

<dl>
<dd>

**default_timezone:** `typing.Optional[str]` — The agent's default timezone. This is used when a timezone is not set on a conversation.
    
</dd>
</dl>

<dl>
<dd>

**enabled_pii_categories:** `typing.Optional[typing.Set[PiiCategory]]` — The PII categories that are enabled for the agent.
    
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

<details><summary><code>client.agents.<a href="src/mavenagi/agents/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an agent.

<Tip>
This endpoint requires additional permissions. Contact support to request access.
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

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.agents.delete(
    organization_reference_id="organizationReferenceId",
    agent_reference_id="agentReferenceId",
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

**organization_reference_id:** `str` — The ID of the organization.
    
</dd>
</dl>

<dl>
<dd>

**agent_reference_id:** `str` — The ID of the agent.
    
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

**timezone:** `typing.Optional[str]` 

IANA timezone identifier (e.g., "America/Los_Angeles").
When provided, time-based groupings (e.g., DAY) and date filters are evaluated in this timezone;
otherwise UTC is used.
    
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

**timezone:** `typing.Optional[str]` 

IANA timezone identifier (e.g., "America/Los_Angeles").
When provided, time-based groupings (e.g., DAY) and date filters are evaluated in this timezone;
otherwise UTC is used.
    
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

## Assets
<details><summary><code>client.assets.<a href="src/mavenagi/assets/client.py">initiate_upload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiate an upload. 
Returns a pre-signed URL for direct file upload and an asset ID for subsequent operations.
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
client.assets.initiate_upload(
    type="type",
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

**type:** `str` 

The mime-type of the attachment. Supported types are:
- image/jpeg
- image/jpg
- image/png
- image/gif
- image/webp
- application/pdf
- text/plain
- text/csv
- application/vnd.openxmlformats-officedocument.wordprocessingml.document
- application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
- application/vnd.openxmlformats-officedocument.presentationml.presentation
- application/msword
- application/vnd.ms-excel
- application/vnd.ms-powerpoint
- audio/aac
- audio/mpeg
- audio/mp4
- audio/wav
- audio/ogg
- video/mp4
- video/webm
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — An optional name for the attachment.
    
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

<details><summary><code>client.assets.<a href="src/mavenagi/assets/client.py">commit_upload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Commit an upload after successful file transfer.
Updates the asset status and makes it available for use.
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
client.assets.commit_upload(
    asset_reference_id="assetReferenceId",
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

**asset_reference_id:** `str` — The reference ID of the asset to commit (provided by the initiate call). All other entity ID fields are inferred from the API request.
    
</dd>
</dl>

<dl>
<dd>

**checksum:** `typing.Optional[str]` — Checksum of the uploaded file (optional verification)
    
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
            conversation_message_id=EntityIdBase(
                reference_id="referenceId",
            ),
            user_id=EntityIdBase(
                reference_id="referenceId",
            ),
            text="text",
            user_message_type="USER",
        ),
        ConversationMessageRequest(
            conversation_message_id=EntityIdBase(
                reference_id="referenceId",
            ),
            user_id=EntityIdBase(
                reference_id="referenceId",
            ),
            text="text",
            user_message_type="USER",
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

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update mutable conversation fields. 

The `appId` field can be provided to update a conversation owned by a different app. 
All other fields will overwrite the existing value on the conversation only if provided.
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
client.conversation.patch(
    conversation_id="conversation-0",
    llm_enabled=True,
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

**conversation_id:** `str` — The ID of the conversation to patch
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — The App ID of the conversation to patch. If not provided the ID of the calling app will be used.
    
</dd>
</dl>

<dl>
<dd>

**open:** `typing.Optional[bool]` — Whether the conversation is able to receive asynchronous messages. Only valid for conversations with the `ASYNC` capability.
    
</dd>
</dl>

<dl>
<dd>

**llm_enabled:** `typing.Optional[bool]` — Whether the LLM is enabled for this conversation.
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[typing.Sequence[AttachmentRequest]]` — A list of attachments to add to the conversation. Attachments can only be appended. Removal is not allowed.
    
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

**translation_language:** `typing.Optional[str]` — The language to translate the conversation analysis into
    
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
            conversation_message_id=EntityIdBase(
                reference_id="referenceId",
            ),
            user_id=EntityIdBase(
                reference_id="referenceId",
            ),
            text="text",
            user_message_type="USER",
        ),
        ConversationMessageRequest(
            conversation_message_id=EntityIdBase(
                reference_id="referenceId",
            ),
            user_id=EntityIdBase(
                reference_id="referenceId",
            ),
            text="text",
            user_message_type="USER",
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
from mavenagi.commons import AttachmentRequest, EntityIdBase

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
        AttachmentRequest(
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

**attachments:** `typing.Optional[typing.Sequence[AttachmentRequest]]` 

The attachments to the message. Image attachments will be sent to the LLM as additional data.
Non-image attachments can be stored and downloaded from the API but will not be sent to the LLM.
    
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
from mavenagi.commons import AttachmentRequest, EntityIdBase

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
        AttachmentRequest(
            type="image/png",
            content="iVBORw0KGgo...",
        )
    ],
    transient_data={"userToken": "abcdef123", "queryApiKey": "foobar456"},
    timezone="America/New_York",
)
for chunk in response.data:
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

**attachments:** `typing.Optional[typing.Sequence[AttachmentRequest]]` 

The attachments to the message. Image attachments will be sent to the LLM as additional data.
Non-image attachments can be stored and downloaded from the API but will not be sent to the LLM.
    
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

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">ask_object_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a structured object response based on a provided schema and user prompt with a streaming response. 
The response will be sent as a stream of events containing text, start, and end events.
The text portions of stream responses should be concatenated to form the full response text.

If the user question and object response already exist, they will be reused and not updated.

Concurrency Behavior:
- If another API call is made for the same user question while a response is mid-stream, partial answers may be returned.
- The second caller will receive a truncated or partial response depending on where the first stream is in its processing. The first caller's stream will remain unaffected and continue delivering the full response.

Known Limitations:
- Schema enforcement is best-effort and may not guarantee exact conformity.
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

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
response = client.conversation.ask_object_stream(
    conversation_id="conversationId",
    schema="schema",
    conversation_message_id=EntityIdBase(
        reference_id="referenceId",
    ),
    user_id=EntityIdBase(
        reference_id="referenceId",
    ),
    text="text",
)
for chunk in response.data:
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

**conversation_id:** `str` — The ID of a new or existing conversation to use as context for the object generation request
    
</dd>
</dl>

<dl>
<dd>

**schema:** `str` — JSON schema string defining the expected object shape.
    
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

**attachments:** `typing.Optional[typing.Sequence[AttachmentRequest]]` 

The attachments to the message. Image attachments will be sent to the LLM as additional data.
Non-image attachments can be stored and downloaded from the API but will not be sent to the LLM.
    
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

**parameters:** `typing.Dict[str, ActionFormRequestParamValue]` — Map of parameter IDs to values provided by the user. All required action fields must be provided.
    
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

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">deliver_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deliver a message to a user or conversation.

<Warning>
Currently, messages can only be successfully delivered to conversations with the `ASYNC` capability that are `open`. 
User message delivery is not yet supported.
</Warning>
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
from mavenagi.conversation import (
    ConversationMessageRequest,
    DeliverMessageRequest_User,
)

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.conversation.deliver_message(
    request=DeliverMessageRequest_User(
        user_id=EntityIdWithoutAgent(
            type="AGENT",
            app_id="appId",
            reference_id="referenceId",
        ),
        message=ConversationMessageRequest(
            conversation_message_id=EntityIdBase(
                reference_id="referenceId",
            ),
            user_id=EntityIdBase(
                reference_id="referenceId",
            ),
            text="text",
            user_message_type="USER",
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

**request:** `DeliverMessageRequest` 
    
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

## Events
<details><summary><code>client.events.<a href="src/mavenagi/events/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new event
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
from mavenagi.events import EventRequest_UserEvent, UserInfoBase

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.events.create(
    request=EventRequest_UserEvent(
        id=EntityIdBase(
            reference_id="referenceId",
        ),
        event_name="BUTTON_CLICKED",
        user_info=UserInfoBase(
            id=EntityIdBase(
                reference_id="referenceId",
            ),
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

**request:** `EventRequest` 
    
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

<details><summary><code>client.events.<a href="src/mavenagi/events/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search events
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
client.events.search()

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

**sort:** `typing.Optional[EventField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[EventFilter]` 
    
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

**filter:** `typing.Optional[InboxFilter]` 
    
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

<details><summary><code>client.inbox.<a href="src/mavenagi/inbox/client.py">apply_fixes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply a list of fixes belonging to an inbox item.
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
client.inbox.apply_fixes(
    inbox_item_id="inboxItemId",
    app_id="appId",
    fix_reference_ids=["fixReferenceIds", "fixReferenceIds"],
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

**app_id:** `str` — The appId of the inbox item and fixes.
    
</dd>
</dl>

<dl>
<dd>

**fix_reference_ids:** `typing.Sequence[str]` — A list of one or more reference IDs of fixes to apply. All must belong to the same inbox item.
    
</dd>
</dl>

<dl>
<dd>

**add_document_request:** `typing.Optional[AddDocumentFixRequest]` — Only applies to add document fixes, includes the document content to save.
    
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
<details><summary><code>client.knowledge.<a href="src/mavenagi/knowledge/client.py">search_knowledge_bases</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search knowledge bases
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
client.knowledge.search_knowledge_bases()

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

**sort:** `typing.Optional[KnowledgeBaseField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[KnowledgeBaseFilter]` 
    
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

**precondition:** `typing.Optional[Precondition]` — The preconditions that must be met for knowledge base be relevant to a conversation. Can be used to restrict knowledge bases to certain types of users.
    
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

**app_id:** `typing.Optional[str]` — The App ID of the knowledge base to get. If not provided the ID of the calling app will be used.
    
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

<details><summary><code>client.knowledge.<a href="src/mavenagi/knowledge/client.py">patch_knowledge_base</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update mutable knowledge base fields

The `appId` field can be provided to update a knowledge base owned by a different app. 
All other fields will overwrite the existing value on the knowledge base only if provided.
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
client.knowledge.patch_knowledge_base(
    knowledge_base_reference_id="knowledgeBaseReferenceId",
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

**knowledge_base_reference_id:** `str` — The reference ID of the knowledge base to patch.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — The App ID of the knowledge base to patch. If not provided the ID of the calling app will be used.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the knowledge base.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Set[str]]` — The tags of the knowledge base.
    
</dd>
</dl>

<dl>
<dd>

**llm_inclusion_status:** `typing.Optional[LlmInclusionStatus]` — Determines whether documents in the knowledge base are sent to the LLM as part of a conversation. Note that at this time knowledge bases can not be set to `ALWAYS`.
    
</dd>
</dl>

<dl>
<dd>

**precondition:** `typing.Optional[Precondition]` — The preconditions that must be met for a knowledge base to be relevant to a conversation. Can be used to restrict knowledge bases to certain types of users. A null value will remove the precondition from the knowledge base, it will be available on all conversations.
    
</dd>
</dl>

<dl>
<dd>

**segment_id:** `typing.Optional[EntityId]` 

The ID of the segment that must be matched for the knowledge base to be relevant to a conversation. 
A null value will remove the segment from the knowledge base, it will be available on all conversations.

Segments are replacing inline preconditions - a knowledge base may not have both an inline precondition and a segment.
Inline precondition support will be removed in a future release.
    
</dd>
</dl>

<dl>
<dd>

**refresh_frequency:** `typing.Optional[KnowledgeBaseRefreshFrequency]` — How often the knowledge base should be refreshed.
    
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

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.knowledge.create_knowledge_base_version(
    knowledge_base_reference_id="help-center",
    type="FULL",
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

**type:** `KnowledgeBaseVersionType` — Indicates whether the completed version constitutes a full or partial refresh of the knowledge base. Deleting and updating documents is only supported for partial refreshes.
    
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

<details><summary><code>client.knowledge.<a href="src/mavenagi/knowledge/client.py">list_knowledge_base_versions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all active versions for a knowledge base. Returns the most recent versions first.
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
client.knowledge.list_knowledge_base_versions(
    knowledge_base_reference_id="knowledgeBaseReferenceId",
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

**knowledge_base_reference_id:** `str` — The reference ID of the knowledge base to list versions for. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — The App ID of the knowledge base. If not provided the ID of the calling app will be used.
    
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

<details><summary><code>client.knowledge.<a href="src/mavenagi/knowledge/client.py">search_knowledge_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search knowledge documents
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
client.knowledge.search_knowledge_documents()

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

**sort:** `typing.Optional[KnowledgeDocumentField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[KnowledgeDocumentFilter]` 
    
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

<details><summary><code>client.knowledge.<a href="src/mavenagi/knowledge/client.py">create_knowledge_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update a knowledge document. Requires an existing knowledge base with an in progress version. 
Will throw an exception if the latest version is not in progress.
        
<Tip>
This API maintains document version history. If for the same reference ID none of the `title`, `text`, `sourceUrl`, `metadata` fields 
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

<details><summary><code>client.knowledge.<a href="src/mavenagi/knowledge/client.py">delete_knowledge_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete knowledge document from a specific version. 
Requires an existing knowledge base with an in progress version of type PARTIAL. Will throw an exception if the version is not in progress.
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
client.knowledge.delete_knowledge_document(
    knowledge_base_reference_id="help-center",
    knowledge_document_reference_id="getting-started",
    version_id=EntityIdWithoutAgent(
        type="KNOWLEDGE_BASE_VERSION",
        app_id="maven",
        reference_id="versionId",
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

**version_id:** `EntityIdWithoutAgent` — ID that uniquely identifies which knowledge base version to delete the document from.
    
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

<details><summary><code>client.knowledge.<a href="src/mavenagi/knowledge/client.py">get_knowledge_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a knowledge document by its supplied version and document IDs. Response includes document content in markdown format.
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
client.knowledge.get_knowledge_document(
    knowledge_base_version_reference_id="knowledgeBaseVersionReferenceId",
    knowledge_document_reference_id="knowledgeDocumentReferenceId",
    knowledge_base_version_app_id="knowledgeBaseVersionAppId",
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

**knowledge_base_version_reference_id:** `str` — The reference ID of the knowledge base version that contains the document. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**knowledge_document_reference_id:** `str` — The reference ID of the knowledge document to get. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**knowledge_base_version_app_id:** `str` — The App ID of the knowledge base version.
    
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
<details><summary><code>client.organizations.<a href="src/mavenagi/organizations/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new organization.

<Tip>
This endpoint requires additional permissions. Contact support to request access.
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

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.organizations.create(
    organization_reference_id="organizationReferenceId",
    name="name",
    default_language="defaultLanguage",
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

**organization_reference_id:** `str` — The reference ID of the organization.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the organization.
    
</dd>
</dl>

<dl>
<dd>

**default_language:** `str` — The default language for the organization in ISO 639-1 code format.
    
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

<details><summary><code>client.organizations.<a href="src/mavenagi/organizations/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an organization by ID
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
client.organizations.get(
    organization_reference_id="organizationReferenceId",
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

**organization_reference_id:** `str` — The reference ID of the organization.
    
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

<details><summary><code>client.organizations.<a href="src/mavenagi/organizations/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update mutable organization fields.
All fields will overwrite the existing value on the organization only if provided.

<Tip>
This endpoint requires additional permissions. Contact support to request access.
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

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.organizations.patch(
    organization_reference_id="organizationReferenceId",
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

**organization_reference_id:** `str` — The reference ID of the organization.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the organization.
    
</dd>
</dl>

<dl>
<dd>

**default_language:** `typing.Optional[str]` — The default language for the organization in ISO 639-1 code format.
    
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

<details><summary><code>client.organizations.<a href="src/mavenagi/organizations/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an organization.

<Tip>
This endpoint requires additional permissions. Contact support to request access.
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

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.organizations.delete(
    organization_reference_id="organizationReferenceId",
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

**organization_reference_id:** `str` — The reference ID of the organization.
    
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

<details><summary><code>client.organizations.<a href="src/mavenagi/organizations/client.py">get_conversation_table</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves structured conversation data across all organizations, formatted as a table, 
allowing users to group, filter, and define specific metrics to display as columns.

<Tip>
This endpoint requires additional permissions. Contact support to request access.
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
client.organizations.get_conversation_table(
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

**timezone:** `typing.Optional[str]` 

IANA timezone identifier (e.g., "America/Los_Angeles").
When provided, time-based groupings (e.g., DAY) and date filters are evaluated in this timezone;
otherwise UTC is used.
    
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

<details><summary><code>client.organizations.<a href="src/mavenagi/organizations/client.py">get_conversation_chart</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches conversation data across all organizations, visualized in a chart format. 
Supported chart types include pie chart, date histogram, and stacked bar charts.

<Tip>
This endpoint requires additional permissions. Contact support to request access.
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
client.organizations.get_conversation_chart(
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

## Segments
<details><summary><code>client.segments.<a href="src/mavenagi/segments/client.py">search</a>(...)</code></summary>
<dl>
<dd>

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
client.segments.search()

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

**sort:** `typing.Optional[SegmentField]` — The field to sort by, defaults to created timestamp
    
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

<details><summary><code>client.segments.<a href="src/mavenagi/segments/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a segment or create it if it doesn't exist.
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
client.segments.create_or_update(
    segment_id=EntityIdBase(
        reference_id="admin-users",
    ),
    name="Admin users",
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

**segment_id:** `EntityIdBase` — ID that uniquely identifies this segment
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the segment.
    
</dd>
</dl>

<dl>
<dd>

**precondition:** `Precondition` — The precondition that must be met for a conversation message to be included in the segment.
    
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

<details><summary><code>client.segments.<a href="src/mavenagi/segments/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a segment by its supplied ID
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
client.segments.get(
    segment_reference_id="admin-users",
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

**segment_reference_id:** `str` — The reference ID of the segment to get. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — The App ID of the segment to get. If not provided, the ID of the calling app will be used.
    
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

<details><summary><code>client.segments.<a href="src/mavenagi/segments/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update mutable segment fields

The `appId` field can be provided to update a segment owned by a different app. 
All other fields will overwrite the existing value on the segment only if provided.
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
client.segments.patch(
    segment_reference_id="segmentReferenceId",
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

**segment_reference_id:** `str` — The reference ID of the segment to update. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — The App ID of the segment to update. If not provided, the ID of the calling app will be used.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the segment.
    
</dd>
</dl>

<dl>
<dd>

**precondition:** `typing.Optional[Precondition]` — The precondition that must be met for a conversation message to be included in the segment.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[SegmentStatus]` — The status of the segment. Segments can only be deactivated if they are not set on any actions or active knowledge bases.
    
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

## Translations
<details><summary><code>client.translations.<a href="src/mavenagi/translations/client.py">translate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Translate text from one language to another
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
client.translations.translate(
    text="Hello world",
    target_language="es",
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

**text:** `str` — The text to translate
    
</dd>
</dl>

<dl>
<dd>

**target_language:** `str` — The target language to translate to, in ISO 639-1 code format.
    
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

## Triggers
<details><summary><code>client.triggers.<a href="src/mavenagi/triggers/client.py">search</a>(...)</code></summary>
<dl>
<dd>

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
client.triggers.search()

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

**sort:** `typing.Optional[TriggerField]` — The field to sort by, defaults to created timestamp
    
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

<details><summary><code>client.triggers.<a href="src/mavenagi/triggers/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an event trigger or create it if it doesn't exist.
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
client.triggers.create_or_update(
    trigger_id=EntityIdBase(
        reference_id="store-in-snowflake",
    ),
    description="Stores conversation data in Snowflake",
    type="CONVERSATION_CREATED",
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

**trigger_id:** `EntityIdBase` — ID that uniquely identifies this event trigger
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — The description of what the event trigger does, shown in the Maven Dashboard
    
</dd>
</dl>

<dl>
<dd>

**type:** `EventTriggerType` 

The type of event trigger this app wishes to handle.

Conversation triggers fire when a conversation is created, after each additional message, and upon deletion events.
There is a small delay before trigger execution to allow time for conversation analysis to complete.

Feedback can not be modified, so the feedback trigger fires immediately after feedback is created.
    
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

<details><summary><code>client.triggers.<a href="src/mavenagi/triggers/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an event trigger by its supplied ID
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
client.triggers.get(
    trigger_reference_id="store-in-snowflake",
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

**trigger_reference_id:** `str` — The reference ID of the event trigger to get. All other entity ID fields are inferred from the request.
    
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

<details><summary><code>client.triggers.<a href="src/mavenagi/triggers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an event trigger
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
client.triggers.delete(
    trigger_reference_id="store-in-snowflake",
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

**trigger_reference_id:** `str` — The reference ID of the event trigger to delete. All other entity ID fields are inferred from the request.
    
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

<details><summary><code>client.triggers.<a href="src/mavenagi/triggers/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an event trigger. Only the enabled field is editable.
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
client.triggers.partial_update(
    trigger_reference_id="triggerReferenceId",
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

**trigger_reference_id:** `str` — The reference ID of the event trigger to update. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — The App ID of the trigger to update. If not provided, the ID of the calling app will be used.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the trigger will be called by Maven.
    
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

## Users
<details><summary><code>client.users.<a href="src/mavenagi/users/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search across all agent users on an agent.

Agent users are a merged view of the users created by individual apps.
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
client.users.search()

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

**sort:** `typing.Optional[AgentUserField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[AgentUserFilter]` 
    
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

<details><summary><code>client.users.<a href="src/mavenagi/users/client.py">get_agent_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an agent user by its supplied ID.

Agent users are a merged view of the users created by individual apps.
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
client.users.get_agent_user(
    user_id="userId",
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

**user_id:** `str` — The ID of the agent user to get.
    
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

<details><summary><code>client.users.<a href="src/mavenagi/users/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an app user or create it if it doesn't exist.
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
from mavenagi.commons import AppUserIdentifier, EntityIdBase, UserData

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.users.create_or_update(
    user_id=EntityIdBase(
        reference_id="user-0",
    ),
    identifiers=[
        AppUserIdentifier(
            value="joe@myapp.com",
            type="EMAIL",
        )
    ],
    data={
        "name": UserData(
            value="Joe",
            visibility="VISIBLE",
        )
    },
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

**user_id:** `EntityIdBase` — ID that uniquely identifies this app user
    
</dd>
</dl>

<dl>
<dd>

**identifiers:** `typing.Sequence[AppUserIdentifier]` — Used to determine whether two users from different apps are the same
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Dict[str, UserData]` 
    
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

<details><summary><code>client.users.<a href="src/mavenagi/users/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an app user by its supplied ID
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
client.users.get(
    user_id="user-0",
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

**user_id:** `str` — The reference ID of the app user to get. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — The App ID of the app user to get. If not provided the ID of the calling app will be used.
    
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

<details><summary><code>client.users.<a href="src/mavenagi/users/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all identifiers and user data saved by the specified app. 
Does not modify data or identifiers saved by other apps.

If this user is linked to a user from another app, it will not be unlinked. Unlinking of users is not yet supported.

<Warning>This is a destructive operation and cannot be undone.</Warning>
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
client.users.delete(
    user_id="user-0",
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

**user_id:** `str` — The reference ID of the app user to delete. All other entity ID fields are inferred from the request.
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `typing.Optional[str]` — The App ID of the app user to delete. If not provided the ID of the calling app will be used.
    
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

