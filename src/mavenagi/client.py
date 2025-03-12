# This file was auto-generated by Fern from our API Definition.

import typing
from .environment import MavenAGIEnvironment
import os
import httpx
from .core.client_wrapper import SyncClientWrapper
from .actions.client import ActionsClient
from .analytics.client import AnalyticsClient
from .app_settings.client import AppSettingsClient
from .conversation.client import ConversationClient
from .inbox.client import InboxClient
from .knowledge.client import KnowledgeClient
from .translations.client import TranslationsClient
from .triggers.client import TriggersClient
from .users.client import UsersClient
from .core.client_wrapper import AsyncClientWrapper
from .actions.client import AsyncActionsClient
from .analytics.client import AsyncAnalyticsClient
from .app_settings.client import AsyncAppSettingsClient
from .conversation.client import AsyncConversationClient
from .inbox.client import AsyncInboxClient
from .knowledge.client import AsyncKnowledgeClient
from .translations.client import AsyncTranslationsClient
from .triggers.client import AsyncTriggersClient
from .users.client import AsyncUsersClient


class MavenAGI:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : MavenAGIEnvironment
        The environment to use for requests from the client. from .environment import MavenAGIEnvironment



        Defaults to MavenAGIEnvironment.PRODUCTION



    organization_id : str
    agent_id : str
    app_id : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    app_secret : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from mavenagi import MavenAGI

    client = MavenAGI(
        organization_id="YOUR_ORGANIZATION_ID",
        agent_id="YOUR_AGENT_ID",
        app_id="YOUR_APP_ID",
        app_secret="YOUR_APP_SECRET",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MavenAGIEnvironment = MavenAGIEnvironment.PRODUCTION,
        organization_id: str,
        agent_id: str,
        app_id: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = os.getenv("MAVENAGI_APP_ID"),
        app_secret: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = os.getenv("MAVENAGI_APP_SECRET"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            organization_id=organization_id,
            agent_id=agent_id,
            app_id=app_id,
            app_secret=app_secret,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.actions = ActionsClient(client_wrapper=self._client_wrapper)
        self.analytics = AnalyticsClient(client_wrapper=self._client_wrapper)
        self.app_settings = AppSettingsClient(client_wrapper=self._client_wrapper)
        self.conversation = ConversationClient(client_wrapper=self._client_wrapper)
        self.inbox = InboxClient(client_wrapper=self._client_wrapper)
        self.knowledge = KnowledgeClient(client_wrapper=self._client_wrapper)
        self.translations = TranslationsClient(client_wrapper=self._client_wrapper)
        self.triggers = TriggersClient(client_wrapper=self._client_wrapper)
        self.users = UsersClient(client_wrapper=self._client_wrapper)


class AsyncMavenAGI:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : MavenAGIEnvironment
        The environment to use for requests from the client. from .environment import MavenAGIEnvironment



        Defaults to MavenAGIEnvironment.PRODUCTION



    organization_id : str
    agent_id : str
    app_id : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    app_secret : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from mavenagi import AsyncMavenAGI

    client = AsyncMavenAGI(
        organization_id="YOUR_ORGANIZATION_ID",
        agent_id="YOUR_AGENT_ID",
        app_id="YOUR_APP_ID",
        app_secret="YOUR_APP_SECRET",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MavenAGIEnvironment = MavenAGIEnvironment.PRODUCTION,
        organization_id: str,
        agent_id: str,
        app_id: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = os.getenv("MAVENAGI_APP_ID"),
        app_secret: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = os.getenv("MAVENAGI_APP_SECRET"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            organization_id=organization_id,
            agent_id=agent_id,
            app_id=app_id,
            app_secret=app_secret,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.actions = AsyncActionsClient(client_wrapper=self._client_wrapper)
        self.analytics = AsyncAnalyticsClient(client_wrapper=self._client_wrapper)
        self.app_settings = AsyncAppSettingsClient(client_wrapper=self._client_wrapper)
        self.conversation = AsyncConversationClient(client_wrapper=self._client_wrapper)
        self.inbox = AsyncInboxClient(client_wrapper=self._client_wrapper)
        self.knowledge = AsyncKnowledgeClient(client_wrapper=self._client_wrapper)
        self.translations = AsyncTranslationsClient(client_wrapper=self._client_wrapper)
        self.triggers = AsyncTriggersClient(client_wrapper=self._client_wrapper)
        self.users = AsyncUsersClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: MavenAGIEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
