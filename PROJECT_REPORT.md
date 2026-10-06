\# RAG Pipeline with LangChain, ChromaDB and Gemini



\## 1. Project Overview



This project implements a Retrieval-Augmented Generation (RAG) pipeline using LangChain, ChromaDB, HuggingFace embeddings, and the Gemini large language model.



The system allows a user to ask questions about a specific document collection. Instead of generating an answer only from the language model's general knowledge, the system first retrieves relevant information from the stored documents and then provides that information to the LLM as context.



The project also displays the source document used to generate the answer, making the responses easier to understand and verify.



\---



\## 2. Problem Statement



Large Language Models can sometimes generate information that is not present in the provided knowledge base.



The goal of this project is to build a question-answering system that:



\- Searches a document collection for relevant information.

\- Converts documents into vector representations.

\- Stores the vectors in a vector database.

\- Retrieves relevant document sections for a question.

\- Uses an LLM to generate an answer from the retrieved context.

\- Displays the source document used for the answer.



\---



\## 3. Objectives



The main objectives of the project are:



1\. Build a complete RAG pipeline.

2\. Load and process a document corpus.

3\. Split documents into smaller chunks.

4\. Generate embeddings for the document chunks.

5\. Store embeddings in ChromaDB.

6\. Retrieve relevant chunks for user questions.

7\. Generate grounded answers using Gemini.

8\. Display source information with each answer.

9\. Build an interactive Q\&A chatbot.

10\. Create a reproducible and documented project structure.



\---



\## 4. Technologies Used



| Technology | Purpose |

|---|---|

| Python | Main programming language |

| LangChain | RAG pipeline and LLM integration |

| ChromaDB | Vector database |

| HuggingFace | Text embeddings |

| Sentence Transformers | Embedding model |

| Gemini | Large Language Model |

| python-dotenv | Environment variable management |

| PyPDF | PDF document support |

| Git | Version control |

| GitHub | Source code hosting |



\### Embedding Model



The project uses:



`sentence-transformers/all-MiniLM-L6-v2`



This model converts text chunks into numerical vectors so that semantically similar content can be retrieved.



\### LLM



The current implementation uses the Gemini model:



`gemini-3.8-flash`



The LLM is configured with temperature `0` to provide more consistent responses.



\---



\## 5. Project Architecture



The overall workflow is:



```text

&#x20;                DOCUMENT CORPUS

&#x20;                      |

&#x20;                      v

&#x20;               Document Loader

&#x20;                      |

&#x20;                      v

&#x20;             Text Chunking

&#x20;                      |

&#x20;                      v

&#x20;             HuggingFace Embeddings

&#x20;                      |

&#x20;                      v

&#x20;                 ChromaDB

&#x20;               Vector Store

&#x20;                      |

&#x20;                      |

USER QUESTION --------+

&#x20;      |

&#x20;      v

Query Embedding

&#x20;      |

&#x20;      v

Similarity Retrieval

&#x20;      |

&#x20;      v

Relevant Document Chunks

&#x20;      |

&#x20;      v

Prompt + Retrieved Context

&#x20;      |

&#x20;      v

&#x20;     Gemini

&#x20;      |

&#x20;      v

Generated Answer

&#x20;      |

&#x20;      v

Answer + Source Citation

```



\---



\## 6. Project Structure



```text

RAG-Pipeline-LangChain-ChromaDB/

│

├── data/

│   └── documents/

│       └── urban\_company\_services.txt

│

├── src/

│   ├── ingest.py

│   ├── rag\_pipeline.py

│   └── chatbot.py

│

├── tests/

│

├── .gitignore

├── requirements.txt

├── README.md

└── PROJECT\_REPORT.md

```



The `.env` file is intentionally excluded from GitHub because it contains the private Gemini API key.



\---



\## 7. Knowledge Base



A sample Urban Company services document was created as the project knowledge base.



The document contains information about:



\- Home cleaning

\- Beauty services

\- Repair services

\- AC services

\- Service booking

\- Customer support

\- Cancellation

\- Safety



The document provides a controlled knowledge source for testing the RAG pipeline.



\---



\## 8. Document Ingestion



The ingestion process is implemented in:



`src/ingest.py`



The pipeline performs the following operations:



1\. Loads the knowledge document.

2\. Splits the document into smaller chunks.

3\. Generates embeddings for each chunk.

4\. Stores the embeddings in ChromaDB.

5\. Creates a persistent vector database inside the project directory.



The text splitter uses:



\- Chunk size: 500 characters

\- Chunk overlap: 50 characters



Chunk overlap helps preserve context between neighboring chunks.



\---



\## 9. Vector Database



ChromaDB is used as the vector database.



The generated vector database is stored locally in:



```text

chroma\_db/

```



The database stores the document

