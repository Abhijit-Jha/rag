"""
Configuration settings for the Vertex AI RAG engine.
"""

# Google Cloud Project Settings
PROJECT_ID = "proj-id"  # Replace with your project ID
LOCATION = "europe-west3"  # Default location for Vertex AI resources

# GCS Storage Settings
GCS_DEFAULT_STORAGE_CLASS = "STANDARD"
GCS_DEFAULT_LOCATION = "US"
GCS_LIST_BUCKETS_MAX_RESULTS = 50
GCS_LIST_BLOBS_MAX_RESULTS = 100
GCS_DEFAULT_CONTENT_TYPE = "application/pdf"  # Default content type for file uploads

# RAG Corpus Settings
RAG_DEFAULT_EMBEDDING_MODEL = "text-embedding-004"
RAG_DEFAULT_TOP_K = 10  # Default number of results for single corpus query
RAG_DEFAULT_SEARCH_TOP_K = 5  # Default number of results per corpus for search_all
RAG_DEFAULT_VECTOR_DISTANCE_THRESHOLD = 0.5
RAG_DEFAULT_PAGE_SIZE = 50  # Default page size for listing files

# Agent Settings
AGENT_NAME = "rag_agent"  # Changed from "rag-agent" to comply with Python identifier rules
AGENT_MODEL = "gemini-2.0-flash-exp"
AGENT_OUTPUT_KEY = "rag_response"

# Logging Settings
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"