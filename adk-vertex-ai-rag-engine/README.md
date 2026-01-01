# Vertex AI RAG Engine - Local Setup Guide

A powerful RAG (Retrieval-Augmented Generation) agent built with Google's Agent Development Kit (ADK) for managing and searching Vertex AI RAG corpora and Google Cloud Storage buckets.

## 🚀 Features

- **RAG Corpus Management**: Create, update, list, and delete RAG corpora
- **Document Management**: Import documents from GCS, list and manage files within corpora
- **Intelligent Search**: Query specific corpora or search across all available corpora
- **GCS Integration**: Create and manage GCS buckets, upload and list files
- **Citation Support**: Automatic citation tracking for search results

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10+** (Python 3.12 recommended)
- **Google Cloud SDK** ([Install here](https://cloud.google.com/sdk/docs/install))
- **Google Cloud Project** with billing enabled
- **Git** (for cloning the repository)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd adk-vertex-ai-rag-engine
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

The required packages are:
- `google-adk>=0.0.1`
- `google-cloud-aiplatform[adk,agent-engines]>=1.88.0`
- `google-cloud-storage`

### 3. Configure Google Cloud Authentication

#### Option A: Application Default Credentials (Recommended for Local Development)

```bash
gcloud auth application-default login
```

This will open a browser window for you to authenticate with your Google account.

#### Option B: Service Account Key (For Shared Credentials)

If you have a service account JSON key file, follow these steps:

##### Step 1: Save the JSON File Securely

Save the JSON key file in a secure location on your machine:

**Recommended locations:**
- **Windows**: `C:\Users\<username>\.gcp\service-account-key.json`
- **Linux/Mac**: `~/.gcp/service-account-key.json`

> ⚠️ **Security Warning**: Never commit this file to Git or share it publicly. The JSON file contains credentials that give access to your GCP project. Add it to `.gitignore`!

##### Step 2: Set the Environment Variable

**Windows PowerShell (Temporary - current session only):**
```powershell
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\abhij\.gcp\service-account-key.json"
```

**Windows PowerShell (Permanent - all sessions):**
```powershell
[System.Environment]::SetEnvironmentVariable('GOOGLE_APPLICATION_CREDENTIALS', 'C:\Users\abhij\.gcp\service-account-key.json', 'User')
```

**Windows CMD:**
```cmd
set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\abhij\.gcp\service-account-key.json
```

**Linux/Mac (Temporary):**
```bash
export GOOGLE_APPLICATION_CREDENTIALS="$HOME/.gcp/service-account-key.json"
```

**Linux/Mac (Permanent - add to `~/.bashrc` or `~/.zshrc`):**
```bash
echo 'export GOOGLE_APPLICATION_CREDENTIALS="$HOME/.gcp/service-account-key.json"' >> ~/.bashrc
source ~/.bashrc
```

##### Step 3: Verify the Setup

After setting the environment variable, verify it's set correctly:

**PowerShell:**
```powershell
echo $env:GOOGLE_APPLICATION_CREDENTIALS
```

**CMD:**
```cmd
echo %GOOGLE_APPLICATION_CREDENTIALS%
```

**Linux/Mac:**
```bash
echo $GOOGLE_APPLICATION_CREDENTIALS
```

##### Step 4: Test Authentication

Test if the authentication works:
```bash
gcloud auth application-default print-access-token
```

This should print an access token if authentication is successful.

> 📝 **Important Notes:**
> - The service account must have the required IAM roles (see Required IAM Permissions section)
> - Use absolute paths (full path) for the JSON file
> - On Windows, use forward slashes `/` or escaped backslashes `\\` in paths
> - Restart your terminal/IDE after setting environment variables
> - Add `*.json` to `.gitignore` to prevent accidental commits

### 4. Enable Required Google Cloud APIs

Run the following commands to enable the necessary APIs:

```bash
# Set your project ID
gcloud config set project YOUR_PROJECT_ID

# Enable required APIs
gcloud services enable aiplatform.googleapis.com
gcloud services enable storage.googleapis.com
gcloud services enable generativelanguage.googleapis.com
```

### 5. Configure Project Settings

Edit `rag/config.py` and update the following settings:

```python
# Google Cloud Project Settings
PROJECT_ID = "your-project-id"  # Replace with your actual project ID
LOCATION = "europe-west3"        # Or your preferred region (e.g., "europe-west3")
```

**Available Regions for Vertex AI:**
- `europe-west3` (Frankfurt)
- `asia-southeast1` (Singapore)

## 🎯 Running the RAG Agent

### Start the ADK Web Server

```bash
adk web
```

The server will start on `http://127.0.0.1:8000`

You should see output like:
```
+-----------------------------------------------------------------------------+
| ADK Web Server started                                                      |
|                                                                             |
| For local testing, access at http://127.0.0.1:8000.                         |
+-----------------------------------------------------------------------------+
```

### Access the Web Interface

Open your browser and navigate to:
```
http://127.0.0.1:8000
```

## 💡 Usage Examples

### 1. Create a GCS Bucket

```
Create a bucket named "my-rag-documents"
```

### 2. Upload Documents to GCS

```
Upload this PDF to bucket "my-rag-documents"
```
(Attach a PDF file to your message)

### 3. Create a RAG Corpus

```
Create a RAG corpus named "Technical Documentation" for storing technical docs
```

### 4. Import Documents into Corpus

```
Import the document from gs://my-rag-documents/document.pdf into corpus <corpus-id>
```

### 5. Search Across All Corpora

```
What are the best practices for API design?
```

### 6. Query a Specific Corpus

```
Search for "authentication methods" in corpus <corpus-id>
```

### 7. List Available Corpora

```
List all RAG corpora
```

## 🛠️ Configuration Options

### Agent Settings

Located in `rag/config.py`:

```python
# Agent Settings
AGENT_NAME = "rag_agent"
AGENT_MODEL = "gemini-2.0-flash-exp"  # Or "gemini-1.5-pro", "gemini-1.5-flash"
AGENT_OUTPUT_KEY = "rag_response"
```

### RAG Settings

```python
# RAG Corpus Settings
RAG_DEFAULT_EMBEDDING_MODEL = "text-embedding-004"
RAG_DEFAULT_TOP_K = 10                      # Results per corpus query
RAG_DEFAULT_SEARCH_TOP_K = 5                # Results per corpus in search_all
RAG_DEFAULT_VECTOR_DISTANCE_THRESHOLD = 0.5 # Similarity threshold
RAG_DEFAULT_PAGE_SIZE = 50                  # Pagination size
```

### GCS Settings

```python
# GCS Storage Settings
GCS_DEFAULT_STORAGE_CLASS = "STANDARD"
GCS_DEFAULT_LOCATION = "US"
GCS_LIST_BUCKETS_MAX_RESULTS = 50
GCS_LIST_BLOBS_MAX_RESULTS = 100
GCS_DEFAULT_CONTENT_TYPE = "application/pdf"
```

## 🔍 Available Tools

### RAG Corpus Management
- `create_corpus_tool` - Create a new RAG corpus
- `update_corpus_tool` - Update corpus metadata
- `list_corpora_tool` - List all corpora
- `get_corpus_tool` - Get corpus details
- `delete_corpus_tool` - Delete a corpus

### RAG File Management
- `import_document_tool` - Import documents from GCS
- `list_files_tool` - List files in a corpus
- `get_file_tool` - Get file details
- `delete_file_tool` - Delete a file from corpus

### RAG Query Tools
- `query_rag_corpus_tool` - Query a specific corpus
- `search_all_corpora_tool` - Search across all corpora

### GCS Bucket Management
- `create_bucket_tool` - Create a GCS bucket
- `list_buckets_tool` - List all buckets
- `get_bucket_details_tool` - Get bucket details and files
- `list_blobs_tool` - List files in a bucket
- `upload_file_gcs_tool` - Upload files to GCS

## 🐛 Troubleshooting

### Import Errors

If you encounter import errors like:
```
ImportError: cannot import name 'RAG_DEFAULT_PAGE_SIZE' from 'rag.config'
```

**Solution:** Ensure all required constants are defined in `rag/config.py`. The config file should include all settings listed in the Configuration Options section above.

### Authentication Errors

If you see authentication errors:
```
google.auth.exceptions.DefaultCredentialsError
```

**Solution:** 
1. Run `gcloud auth application-default login`
2. Or set `GOOGLE_APPLICATION_CREDENTIALS` environment variable
3. Ensure your account has the necessary permissions

### API Not Enabled Errors

If you see errors about APIs not being enabled:
```
API [aiplatform.googleapis.com] not enabled
```

**Solution:** Enable the required APIs:
```bash
gcloud services enable aiplatform.googleapis.com
gcloud services enable storage.googleapis.com
```

### Agent Name Validation Error

If you see:
```
Found invalid agent name: `rag-agent`
```

**Solution:** Agent names must be valid Python identifiers (no hyphens). Use underscores instead:
```python
AGENT_NAME = "rag_agent"  # ✅ Correct
AGENT_NAME = "rag-agent"  # ❌ Invalid
```

### Connection Rejected (403 Forbidden)

The WebSocket connection rejections are normal during startup. They occur while the server is initializing. Once you create a session through the web interface, the connections will succeed.

## 📝 Project Structure

```
adk-vertex-ai-rag-engine/
├── rag/
│   ├── __init__.py           # Package initialization
│   ├── agent.py              # Main agent definition
│   ├── config.py             # Configuration settings
│   └── tools/
│       ├── __init__.py       # Tools package
│       ├── corpus_tools.py   # RAG corpus management tools
│       └── storage_tools.py  # GCS storage tools
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── LICENSE                   # License information
└── .gitignore               # Git ignore rules
```

## 🔐 Required IAM Permissions

Your Google Cloud account or service account needs the following roles:

- **Vertex AI User** (`roles/aiplatform.user`)
- **Storage Admin** (`roles/storage.admin`) or **Storage Object Admin** (`roles/storage.objectAdmin`)
- **Service Usage Consumer** (`roles/serviceusage.serviceUsageConsumer`)

To grant these permissions:
```bash
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="user:YOUR_EMAIL@example.com" \
  --role="roles/aiplatform.user"

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="user:YOUR_EMAIL@example.com" \
  --role="roles/storage.admin"
```

## 📚 Additional Resources

- [Google ADK Documentation](https://cloud.google.com/agent-development-kit/docs)
- [Vertex AI RAG Documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/rag-overview)
- [Google Cloud Storage Documentation](https://cloud.google.com/storage/docs)
- [Vertex AI Embeddings](https://cloud.google.com/vertex-ai/docs/generative-ai/embeddings/get-text-embeddings)

## 🤝 Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review the Google Cloud logs: `gcloud logging read`
3. Ensure all prerequisites are met
4. Verify your GCP project has billing enabled

## 📄 License

See the [LICENSE](LICENSE) file for details.

---

**Happy RAG Building! 🚀**
