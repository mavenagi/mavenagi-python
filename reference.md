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
from mavenagi.actions import Precondition_Group, Precondition_User
from mavenagi.commons import EntityIdBase

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

**description:** `str` — The description of the action. This helps Maven decide if the action is relevant to a conversation and is not displayed directly to the end user.
    
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

**button_name:** `typing.Optional[str]` — When user interaction is required, the name of the button that is shown to the end user to confirm execution of the action
    
</dd>
</dl>

<dl>
<dd>

**precondition:** `typing.Optional[Precondition]` — The preconditions that must be met for an action to be relevant to a conversation. Can be used to restrict actions to certain types of users.
    
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

## AppSettings
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

## Conversation
<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">initialize</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initialize a new conversation. Only required if the ask request wishes to supply conversation level data or when syncing to external systems.
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
import datetime

from mavenagi import MavenAGI
from mavenagi.commons import EntityIdBase
from mavenagi.conversation import ConversationMessageRequest, ResponseConfig

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.conversation.initialize(
    conversation_id=EntityIdBase(
        reference_id="string",
    ),
    messages=[
        ConversationMessageRequest(
            conversation_message_id=EntityIdBase(
                reference_id="string",
            ),
            user_id=EntityIdBase(
                reference_id="string",
            ),
            text="string",
            user_message_type="USER",
            created_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            updated_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
    ],
    response_config=ResponseConfig(
        capabilities=["MARKDOWN"],
        is_copilot=True,
        response_length="SHORT",
    ),
    subject="string",
    url="string",
    created_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    updated_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    tags={"string"},
    metadata={"string": "string"},
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

**metadata:** `typing.Optional[typing.Dict[str, str]]` — The metadata of the conversation.
    
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
    conversation_id="string",
    app_id="string",
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

<details><summary><code>client.conversation.<a href="src/mavenagi/conversation/client.py">append_new_messages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Append messages to an existing conversation. The conversation must be initialized first. If a message with the same id already exists, it will be ignored.
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
import datetime

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
    conversation_id="string",
    request=[
        ConversationMessageRequest(
            conversation_message_id=EntityIdBase(
                reference_id="string",
            ),
            user_id=EntityIdBase(
                reference_id="string",
            ),
            text="string",
            user_message_type="USER",
            created_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            updated_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
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

Ask a question
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
    conversation_id="string",
    conversation_message_id=EntityIdBase(
        reference_id="message-1",
    ),
    user_id=EntityIdBase(
        reference_id="user-1",
    ),
    text="How do I reset my password?",
    attachments=[
        Attachment(
            type="image/png",
            content="iVBORw0KGgo...",
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

**conversation_id:** `str` — The ID of a new or existing conversation to use as context for the question
    
</dd>
</dl>

<dl>
<dd>

**conversation_message_id:** `EntityIdBase` — Externally supplied ID to uniquely identify this message within the conversation
    
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

Ask a question with a streaming response. The response will be sent as a stream of events. The text portions of stream responses should be concatenated to form the full response text. Action and metadata events should overwrite past data and do not need concatenation.
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
        reference_id="message-1",
    ),
    user_id=EntityIdBase(
        reference_id="user-1",
    ),
    text="How do I reset my password?",
    attachments=[
        Attachment(
            type="image/png",
            content="iVBORw0KGgo...",
        )
    ],
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

**conversation_message_id:** `EntityIdBase` — Externally supplied ID to uniquely identify this message within the conversation
    
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

Generate a response suggestion for each requested message id in a conversation
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
    conversation_id="string",
    conversation_message_ids=[
        EntityIdBase(
            reference_id="string",
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
    conversation_id="string",
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

Create feedback
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
        reference_id="string",
    ),
    conversation_id=EntityIdBase(
        reference_id="string",
    ),
    conversation_message_id=EntityIdBase(
        reference_id="string",
    ),
    type="THUMBS_UP",
    text="string",
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
    conversation_id="string",
    action_form_id="string",
    parameters={"string": {"key": "value"}},
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

Add metadata to an existing conversation. If a metadata field already exists, it will be overwritten.
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
    conversation_id="string",
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
    type="API",
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

**type:** `KnowledgeBaseType` — The type of the knowledge base. Can not be changed once created.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The URL to pull content from for RSS and URL knowledge bases.
    
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

Create a new knowledge base version. Only supported on API knowledge bases. Will throw an exception if there is an existing version in progress.
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

client = MavenAGI(
    organization_id="YOUR_ORGANIZATION_ID",
    agent_id="YOUR_AGENT_ID",
    app_id="YOUR_APP_ID",
    app_secret="YOUR_APP_SECRET",
)
client.knowledge.finalize_knowledge_base_version(
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

**knowledge_base_reference_id:** `str` — The reference ID of the knowledge base to finalize a version for. All other entity ID fields are inferred from the request.
    
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
client.knowledge.create_knowledge_document(
    knowledge_base_reference_id="help-center",
    knowledge_document_id=EntityIdBase(
        reference_id="getting-started",
    ),
    content_type="MARKDOWN",
    content="## Getting started\\nThis is a getting started guide for the help center.",
    title="Getting started",
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
from mavenagi.commons import EntityIdBase

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
    content_type="MARKDOWN",
    content="## Getting started\\nThis is a getting started guide for the help center.",
    title="Getting started",
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

**type:** `EventTriggerType` — The type of event trigger this app wishes to handle
    
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

## Users
<details><summary><code>client.users.<a href="src/mavenagi/users/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a user or create it if it doesn't exist.
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

Get a user by its supplied ID
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

**user_id:** `str` — The reference ID of the user to get. All other entity ID fields are inferred from the request.
    
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

