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
from google.ai.generativelanguage_v1beta import gapic_version as package_version

__version__ = package_version.__version__


from .services.discuss_service import DiscussServiceAsyncClient, DiscussServiceClient
from .services.generative_service import (
    GenerativeServiceAsyncClient,
    GenerativeServiceClient,
)
from .services.model_service import ModelServiceAsyncClient, ModelServiceClient
from .services.permission_service import (
    PermissionServiceAsyncClient,
    PermissionServiceClient,
)
from .services.retriever_service import (
    RetrieverServiceAsyncClient,
    RetrieverServiceClient,
)
from .services.text_service import TextServiceAsyncClient, TextServiceClient
from .types.citation import CitationMetadata, CitationSource
from .types.content import (
    Blob,
    Content,
    FunctionCall,
    FunctionDeclaration,
    FunctionResponse,
    GroundingPassage,
    GroundingPassages,
    Part,
    Schema,
    Tool,
    Type,
)
from .types.discuss_service import (
    CountMessageTokensRequest,
    CountMessageTokensResponse,
    Example,
    GenerateMessageRequest,
    GenerateMessageResponse,
    Message,
    MessagePrompt,
)
from .types.generative_service import (
    AttributionSourceId,
    BatchEmbedContentsRequest,
    BatchEmbedContentsResponse,
    Candidate,
    ContentEmbedding,
    CountTokensRequest,
    CountTokensResponse,
    EmbedContentRequest,
    EmbedContentResponse,
    GenerateAnswerRequest,
    GenerateAnswerResponse,
    GenerateContentRequest,
    GenerateContentResponse,
    GenerationConfig,
    GroundingAttribution,
    SemanticRetrieverConfig,
    TaskType,
)
from .types.model import Model
from .types.model_service import (
    CreateTunedModelMetadata,
    CreateTunedModelRequest,
    DeleteTunedModelRequest,
    GetModelRequest,
    GetTunedModelRequest,
    ListModelsRequest,
    ListModelsResponse,
    ListTunedModelsRequest,
    ListTunedModelsResponse,
    UpdateTunedModelRequest,
)
from .types.permission import Permission
from .types.permission_service import (
    CreatePermissionRequest,
    DeletePermissionRequest,
    GetPermissionRequest,
    ListPermissionsRequest,
    ListPermissionsResponse,
    TransferOwnershipRequest,
    TransferOwnershipResponse,
    UpdatePermissionRequest,
)
from .types.retriever import (
    Chunk,
    ChunkData,
    Condition,
    Corpus,
    CustomMetadata,
    Document,
    MetadataFilter,
    StringList,
)
from .types.retriever_service import (
    BatchCreateChunksRequest,
    BatchCreateChunksResponse,
    BatchDeleteChunksRequest,
    BatchUpdateChunksRequest,
    BatchUpdateChunksResponse,
    CreateChunkRequest,
    CreateCorpusRequest,
    CreateDocumentRequest,
    DeleteChunkRequest,
    DeleteCorpusRequest,
    DeleteDocumentRequest,
    GetChunkRequest,
    GetCorpusRequest,
    GetDocumentRequest,
    ListChunksRequest,
    ListChunksResponse,
    ListCorporaRequest,
    ListCorporaResponse,
    ListDocumentsRequest,
    ListDocumentsResponse,
    QueryCorpusRequest,
    QueryCorpusResponse,
    QueryDocumentRequest,
    QueryDocumentResponse,
    RelevantChunk,
    UpdateChunkRequest,
    UpdateCorpusRequest,
    UpdateDocumentRequest,
)
from .types.safety import (
    ContentFilter,
    HarmCategory,
    SafetyFeedback,
    SafetyRating,
    SafetySetting,
)
from .types.text_service import (
    BatchEmbedTextRequest,
    BatchEmbedTextResponse,
    CountTextTokensRequest,
    CountTextTokensResponse,
    Embedding,
    EmbedTextRequest,
    EmbedTextResponse,
    GenerateTextRequest,
    GenerateTextResponse,
    TextCompletion,
    TextPrompt,
)
from .types.tuned_model import (
    Dataset,
    Hyperparameters,
    TunedModel,
    TunedModelSource,
    TuningExample,
    TuningExamples,
    TuningSnapshot,
    TuningTask,
)

__all__ = (
    "DiscussServiceAsyncClient",
    "GenerativeServiceAsyncClient",
    "ModelServiceAsyncClient",
    "PermissionServiceAsyncClient",
    "RetrieverServiceAsyncClient",
    "TextServiceAsyncClient",
    "AttributionSourceId",
    "BatchCreateChunksRequest",
    "BatchCreateChunksResponse",
    "BatchDeleteChunksRequest",
    "BatchEmbedContentsRequest",
    "BatchEmbedContentsResponse",
    "BatchEmbedTextRequest",
    "BatchEmbedTextResponse",
    "BatchUpdateChunksRequest",
    "BatchUpdateChunksResponse",
    "Blob",
    "Candidate",
    "Chunk",
    "ChunkData",
    "CitationMetadata",
    "CitationSource",
    "Condition",
    "Content",
    "ContentEmbedding",
    "ContentFilter",
    "Corpus",
    "CountMessageTokensRequest",
    "CountMessageTokensResponse",
    "CountTextTokensRequest",
    "CountTextTokensResponse",
    "CountTokensRequest",
    "CountTokensResponse",
    "CreateChunkRequest",
    "CreateCorpusRequest",
    "CreateDocumentRequest",
    "CreatePermissionRequest",
    "CreateTunedModelMetadata",
    "CreateTunedModelRequest",
    "CustomMetadata",
    "Dataset",
    "DeleteChunkRequest",
    "DeleteCorpusRequest",
    "DeleteDocumentRequest",
    "DeletePermissionRequest",
    "DeleteTunedModelRequest",
    "DiscussServiceClient",
    "Document",
    "EmbedContentRequest",
    "EmbedContentResponse",
    "EmbedTextRequest",
    "EmbedTextResponse",
    "Embedding",
    "Example",
    "FunctionCall",
    "FunctionDeclaration",
    "FunctionResponse",
    "GenerateAnswerRequest",
    "GenerateAnswerResponse",
    "GenerateContentRequest",
    "GenerateContentResponse",
    "GenerateMessageRequest",
    "GenerateMessageResponse",
    "GenerateTextRequest",
    "GenerateTextResponse",
    "GenerationConfig",
    "GenerativeServiceClient",
    "GetChunkRequest",
    "GetCorpusRequest",
    "GetDocumentRequest",
    "GetModelRequest",
    "GetPermissionRequest",
    "GetTunedModelRequest",
    "GroundingAttribution",
    "GroundingPassage",
    "GroundingPassages",
    "HarmCategory",
    "Hyperparameters",
    "ListChunksRequest",
    "ListChunksResponse",
    "ListCorporaRequest",
    "ListCorporaResponse",
    "ListDocumentsRequest",
    "ListDocumentsResponse",
    "ListModelsRequest",
    "ListModelsResponse",
    "ListPermissionsRequest",
    "ListPermissionsResponse",
    "ListTunedModelsRequest",
    "ListTunedModelsResponse",
    "Message",
    "MessagePrompt",
    "MetadataFilter",
    "Model",
    "ModelServiceClient",
    "Part",
    "Permission",
    "PermissionServiceClient",
    "QueryCorpusRequest",
    "QueryCorpusResponse",
    "QueryDocumentRequest",
    "QueryDocumentResponse",
    "RelevantChunk",
    "RetrieverServiceClient",
    "SafetyFeedback",
    "SafetyRating",
    "SafetySetting",
    "Schema",
    "SemanticRetrieverConfig",
    "StringList",
    "TaskType",
    "TextCompletion",
    "TextPrompt",
    "TextServiceClient",
    "Tool",
    "TransferOwnershipRequest",
    "TransferOwnershipResponse",
    "TunedModel",
    "TunedModelSource",
    "TuningExample",
    "TuningExamples",
    "TuningSnapshot",
    "TuningTask",
    "Type",
    "UpdateChunkRequest",
    "UpdateCorpusRequest",
    "UpdateDocumentRequest",
    "UpdatePermissionRequest",
    "UpdateTunedModelRequest",
)