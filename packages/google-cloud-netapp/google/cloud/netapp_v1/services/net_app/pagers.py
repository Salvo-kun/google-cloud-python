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

from google.cloud.netapp_v1.types import (
    active_directory,
    kms,
    replication,
    snapshot,
    storage_pool,
    volume,
)


class ListStoragePoolsPager:
    """A pager for iterating through ``list_storage_pools`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListStoragePoolsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``storage_pools`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListStoragePools`` requests and continue to iterate
    through the ``storage_pools`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListStoragePoolsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., storage_pool.ListStoragePoolsResponse],
        request: storage_pool.ListStoragePoolsRequest,
        response: storage_pool.ListStoragePoolsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListStoragePoolsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListStoragePoolsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = storage_pool.ListStoragePoolsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[storage_pool.ListStoragePoolsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[storage_pool.StoragePool]:
        for page in self.pages:
            yield from page.storage_pools

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListStoragePoolsAsyncPager:
    """A pager for iterating through ``list_storage_pools`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListStoragePoolsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``storage_pools`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListStoragePools`` requests and continue to iterate
    through the ``storage_pools`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListStoragePoolsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[storage_pool.ListStoragePoolsResponse]],
        request: storage_pool.ListStoragePoolsRequest,
        response: storage_pool.ListStoragePoolsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListStoragePoolsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListStoragePoolsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = storage_pool.ListStoragePoolsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[storage_pool.ListStoragePoolsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[storage_pool.StoragePool]:
        async def async_generator():
            async for page in self.pages:
                for response in page.storage_pools:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVolumesPager:
    """A pager for iterating through ``list_volumes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListVolumesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``volumes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVolumes`` requests and continue to iterate
    through the ``volumes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListVolumesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., volume.ListVolumesResponse],
        request: volume.ListVolumesRequest,
        response: volume.ListVolumesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListVolumesRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListVolumesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = volume.ListVolumesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[volume.ListVolumesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[volume.Volume]:
        for page in self.pages:
            yield from page.volumes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVolumesAsyncPager:
    """A pager for iterating through ``list_volumes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListVolumesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``volumes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVolumes`` requests and continue to iterate
    through the ``volumes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListVolumesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[volume.ListVolumesResponse]],
        request: volume.ListVolumesRequest,
        response: volume.ListVolumesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListVolumesRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListVolumesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = volume.ListVolumesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[volume.ListVolumesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[volume.Volume]:
        async def async_generator():
            async for page in self.pages:
                for response in page.volumes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSnapshotsPager:
    """A pager for iterating through ``list_snapshots`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListSnapshotsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``snapshots`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSnapshots`` requests and continue to iterate
    through the ``snapshots`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListSnapshotsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., snapshot.ListSnapshotsResponse],
        request: snapshot.ListSnapshotsRequest,
        response: snapshot.ListSnapshotsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListSnapshotsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListSnapshotsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = snapshot.ListSnapshotsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[snapshot.ListSnapshotsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[snapshot.Snapshot]:
        for page in self.pages:
            yield from page.snapshots

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSnapshotsAsyncPager:
    """A pager for iterating through ``list_snapshots`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListSnapshotsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``snapshots`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSnapshots`` requests and continue to iterate
    through the ``snapshots`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListSnapshotsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[snapshot.ListSnapshotsResponse]],
        request: snapshot.ListSnapshotsRequest,
        response: snapshot.ListSnapshotsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListSnapshotsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListSnapshotsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = snapshot.ListSnapshotsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[snapshot.ListSnapshotsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[snapshot.Snapshot]:
        async def async_generator():
            async for page in self.pages:
                for response in page.snapshots:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListActiveDirectoriesPager:
    """A pager for iterating through ``list_active_directories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListActiveDirectoriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``active_directories`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListActiveDirectories`` requests and continue to iterate
    through the ``active_directories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListActiveDirectoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., active_directory.ListActiveDirectoriesResponse],
        request: active_directory.ListActiveDirectoriesRequest,
        response: active_directory.ListActiveDirectoriesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListActiveDirectoriesRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListActiveDirectoriesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = active_directory.ListActiveDirectoriesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[active_directory.ListActiveDirectoriesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[active_directory.ActiveDirectory]:
        for page in self.pages:
            yield from page.active_directories

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListActiveDirectoriesAsyncPager:
    """A pager for iterating through ``list_active_directories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListActiveDirectoriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``active_directories`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListActiveDirectories`` requests and continue to iterate
    through the ``active_directories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListActiveDirectoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[active_directory.ListActiveDirectoriesResponse]
        ],
        request: active_directory.ListActiveDirectoriesRequest,
        response: active_directory.ListActiveDirectoriesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListActiveDirectoriesRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListActiveDirectoriesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = active_directory.ListActiveDirectoriesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[active_directory.ListActiveDirectoriesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[active_directory.ActiveDirectory]:
        async def async_generator():
            async for page in self.pages:
                for response in page.active_directories:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListKmsConfigsPager:
    """A pager for iterating through ``list_kms_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListKmsConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``kms_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListKmsConfigs`` requests and continue to iterate
    through the ``kms_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListKmsConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., kms.ListKmsConfigsResponse],
        request: kms.ListKmsConfigsRequest,
        response: kms.ListKmsConfigsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListKmsConfigsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListKmsConfigsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = kms.ListKmsConfigsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[kms.ListKmsConfigsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[kms.KmsConfig]:
        for page in self.pages:
            yield from page.kms_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListKmsConfigsAsyncPager:
    """A pager for iterating through ``list_kms_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListKmsConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``kms_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListKmsConfigs`` requests and continue to iterate
    through the ``kms_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListKmsConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[kms.ListKmsConfigsResponse]],
        request: kms.ListKmsConfigsRequest,
        response: kms.ListKmsConfigsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListKmsConfigsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListKmsConfigsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = kms.ListKmsConfigsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[kms.ListKmsConfigsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[kms.KmsConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.kms_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReplicationsPager:
    """A pager for iterating through ``list_replications`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListReplicationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``replications`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReplications`` requests and continue to iterate
    through the ``replications`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListReplicationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., replication.ListReplicationsResponse],
        request: replication.ListReplicationsRequest,
        response: replication.ListReplicationsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListReplicationsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListReplicationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = replication.ListReplicationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[replication.ListReplicationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[replication.Replication]:
        for page in self.pages:
            yield from page.replications

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReplicationsAsyncPager:
    """A pager for iterating through ``list_replications`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListReplicationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``replications`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReplications`` requests and continue to iterate
    through the ``replications`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListReplicationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[replication.ListReplicationsResponse]],
        request: replication.ListReplicationsRequest,
        response: replication.ListReplicationsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListReplicationsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListReplicationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = replication.ListReplicationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[replication.ListReplicationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[replication.Replication]:
        async def async_generator():
            async for page in self.pages:
                for response in page.replications:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
