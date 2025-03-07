# This file was auto-generated by Fern from our API Definition.

import typing
import httpx
from .http_client import HttpClient
from .http_client import AsyncHttpClient


class BaseClientWrapper:
    def __init__(
        self,
        *,
        organization_id: str,
        agent_id: str,
        app_id: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        app_secret: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
    ):
        self._organization_id = organization_id
        self._agent_id = agent_id
        self._app_id = app_id
        self._app_secret = app_secret
        self._base_url = base_url
        self._timeout = timeout

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "X-Fern-Language": "Python",
            "X-Fern-SDK-Name": "mavenagi",
            "X-Fern-SDK-Version": "1.0.7",
        }
        app_id = self._get_app_id()
        app_secret = self._get_app_secret()
        if app_id is not None and app_secret is not None:
            headers["Authorization"] = httpx.BasicAuth(app_id, app_secret)._auth_header
        headers["X-Organization-Id"] = self._organization_id
        headers["X-Agent-Id"] = self._agent_id
        return headers

    def _get_app_id(self) -> typing.Optional[str]:
        if isinstance(self._app_id, str) or self._app_id is None:
            return self._app_id
        else:
            return self._app_id()

    def _get_app_secret(self) -> typing.Optional[str]:
        if isinstance(self._app_secret, str) or self._app_secret is None:
            return self._app_secret
        else:
            return self._app_secret()

    def get_base_url(self) -> str:
        return self._base_url

    def get_timeout(self) -> typing.Optional[float]:
        return self._timeout


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        organization_id: str,
        agent_id: str,
        app_id: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        app_secret: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
        httpx_client: httpx.Client,
    ):
        super().__init__(
            organization_id=organization_id,
            agent_id=agent_id,
            app_id=app_id,
            app_secret=app_secret,
            base_url=base_url,
            timeout=timeout,
        )
        self.httpx_client = HttpClient(
            httpx_client=httpx_client,
            base_headers=self.get_headers,
            base_timeout=self.get_timeout,
            base_url=self.get_base_url,
        )


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        organization_id: str,
        agent_id: str,
        app_id: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        app_secret: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
        httpx_client: httpx.AsyncClient,
    ):
        super().__init__(
            organization_id=organization_id,
            agent_id=agent_id,
            app_id=app_id,
            app_secret=app_secret,
            base_url=base_url,
            timeout=timeout,
        )
        self.httpx_client = AsyncHttpClient(
            httpx_client=httpx_client,
            base_headers=self.get_headers,
            base_timeout=self.get_timeout,
            base_url=self.get_base_url,
        )
