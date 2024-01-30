# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    Optional,
    Sequence,
    Tuple,
)

from google.cloud.dataproc_v1.types import session_templates


class ListSessionTemplatesPager:
    """A pager for iterating through ``list_session_templates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataproc_v1.types.ListSessionTemplatesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``session_templates`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSessionTemplates`` requests and continue to iterate
    through the ``session_templates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataproc_v1.types.ListSessionTemplatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., session_templates.ListSessionTemplatesResponse],
        request: session_templates.ListSessionTemplatesRequest,
        response: session_templates.ListSessionTemplatesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataproc_v1.types.ListSessionTemplatesRequest):
                The initial request object.
            response (google.cloud.dataproc_v1.types.ListSessionTemplatesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = session_templates.ListSessionTemplatesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[session_templates.ListSessionTemplatesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[session_templates.SessionTemplate]:
        for page in self.pages:
            yield from page.session_templates

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSessionTemplatesAsyncPager:
    """A pager for iterating through ``list_session_templates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataproc_v1.types.ListSessionTemplatesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``session_templates`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSessionTemplates`` requests and continue to iterate
    through the ``session_templates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataproc_v1.types.ListSessionTemplatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[session_templates.ListSessionTemplatesResponse]
        ],
        request: session_templates.ListSessionTemplatesRequest,
        response: session_templates.ListSessionTemplatesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataproc_v1.types.ListSessionTemplatesRequest):
                The initial request object.
            response (google.cloud.dataproc_v1.types.ListSessionTemplatesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = session_templates.ListSessionTemplatesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[session_templates.ListSessionTemplatesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[session_templates.SessionTemplate]:
        async def async_generator():
            async for page in self.pages:
                for response in page.session_templates:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
