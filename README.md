\# RAG Pipeline with LangChain, ChromaDB and Gemini



\## Project Overview



This project implements a \*\*Retrieval-Augmented Generation (RAG) pipeline\*\* using LangChain, ChromaDB, Hugging Face embeddings, and Google Gemini.



The system loads information from a document, converts it into smaller chunks, creates vector embeddings, stores them in ChromaDB, retrieves relevant information for a user's question, and uses Gemini to generate an answer based only on the retrieved context.



The project also provides a simple command-line Q\&A chatbot with source citations.



\---



\## Objectives



\- Build a complete RAG pipeline.

\- Load and process a document corpus.

\- Split documents into smaller chunks.

\- Generate vector embeddings.

\- Store embeddings in ChromaDB.

\- Retrieve relevant documents for a question.

\- Generate answers using an LLM.

\- Provide source citations with answers.

\- Build an interactive Q\&A chatbot.

\- Keep API credentials secure using environment variables.



\---



\## Technologies Used



\- \*\*Python\*\*

\- \*\*LangChain\*\*

\- \*\*ChromaDB\*\*

\- \*\*Google Gemini\*\*

\- \*\*Hugging Face Sentence Transformers\*\*

\- \*\*sentence-transformers/all-MiniLM-L6-v2\*\*

\- \*\*python-dotenv\*\*



\---



\## System Architecture



```text

&#x20;               Knowledge Document

&#x20;                      |

&#x20;                      v

&#x20;               Document Loading

&#x20;                      |

&#x20;                      v

&#x20;                Text Chunking

&#x20;                      |

&#x20;                      v

&#x20;             Hugging Face Embeddings

&#x20;                      |

&#x20;                      v

&#x20;                   ChromaDB

&#x20;                Vector Database

&#x20;                      |

&#x20;                      v

&#x20;                 User Question

&#x20;                      |

&#x20;                      v

&#x20;                  Retriever

&#x20;                      |

&#x20;                      v

&#x20;             Relevant Context

&#x20;                      |

&#x20;                      v

&#x20;                Gemini LLM

&#x20;                      |

&#x20;                      v

&#x20;                Generated Answer

&#x20;                      |

&#x20;                      v

&#x20;              Source Citations

```



\---



\## Project Structure



```text

RAG-Pipeline-LangChain-ChromaDB/

│

├── data/

│   └── documents/

│       └── urban\_company\_services.txt

│

├── src/

│   ├── chatbot.py

│   ├── ingest.py

│   └── rag\_pipeline.py

│

├── tests/

│

├── .gitignore

└── README.md

```



\---



\## Knowledge Base



The current knowledge base contains information about Urban Company services, including:



\- Home cleaning

\- Beauty services

\- Repair services

\- AC services

\- Service booking

\- Customer support

\- Cancellation

\- Safety



The document is stored at:



```text

data/documents/urban\_company\_services.txt

```



\---



\## How the RAG Pipeline Works



\### 1. Document Ingestion



The `ingest.py` script loads the knowledge document.



\### 2. Text Chunking



The document is divided into smaller chunks using a recursive text splitter.



\### 3. Embedding Generation



Each chunk is converted into a numerical vector using:



```text

sentence-transformers/all-MiniLM-L6-v2

```



\### 4. Vector Storage



The generated embeddings are stored in \*\*ChromaDB\*\*.



\### 5. Retrieval



When a user asks a question, the retriever searches ChromaDB and selects the most relevant document chunks.



\### 6. Context Construction



The retrieved chunks are combined into a context for the language model.



\### 7. Answer Generation



Google Gemini receives the retrieved context and user question.



The prompt instructs Gemini to answer using only the provided context.



\### 8. Source Citation



The application displays the source document used to generate the answer.



\---



\## Installation



\### 1. Clone the repository



```bash

git clone https://github.com/Pallavim731/RAG-Pipeline-LangChain-ChromaDB.git

cd RAG-Pipeline-LangChain-ChromaDB

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



\### 3. Activate the environment on Windows



```cmd

venv\\Scripts\\activate

```



\### 4. Install dependencies



```bash

pip install langchain langchain-community langchain-chroma langchain-google-genai chromadb python-dotenv pypdf langchain-text-splitters sentence-transformers langchain-huggingface

```



\---



\## Environment Configuration



Create a `.env` file in the project root:



```text

GEMINI\_API\_KEY=your\_gemini\_api\_key\_here

```



Never commit the `.env` file to GitHub.



The `.gitignore` file excludes:



```text

.env

venv/

chroma\_db/

\_\_pycache\_\_/

\*.pyc

```



\---



\## Build the Vector Database



From the project root, run:



```cmd

python src\\ingest.py

```



This loads the document, creates embeddings, and stores them in ChromaDB.



\---



\## Run the RAG Pipeline



From the project root:



```cmd

python src\\rag\_pipeline.py

```



Example:



```text

Ask a question: What services are available for AC?



Answer:

Based on the provided context, the services available for AC include:



\* AC cleaning

\* AC repair

\* AC installation

\* AC uninstallation

\* Gas-related services



Sources:

\- urban\_company\_services.txt

```



\---



\## Run the Interactive Chatbot



Move into the `src` directory:



```cmd

cd src

python chatbot.py

```



The chatbot supports continuous questions until the user enters:



```text

exit

```



Example:



```text

============================================================

Urban Company RAG Q\&A Chatbot

Type 'exit' to quit.

============================================================



You: What services are available for AC?



Assistant:

Based on the provided context, the services available for AC include:

\- AC cleaning

\- AC repair

\- AC installation

\- AC uninstallation

\- Gas-related services



Sources:

\- urban\_company\_services.txt

```



\---



\## RAG Safety / Grounding



The system is designed to reduce unsupported answers.



The prompt instructs the LLM to:



1\. Use only the retrieved document context.

2\. Avoid inventing information.

3\. State that there is not enough information when the answer is unavailable in the provided documents.



Example fallback:



```text

I don't have enough information in the provided documents.

```



\---



\## Testing



The chatbot can be tested using questions such as:



```text

What home cleaning services are available?

```



```text

What services are available for AC?

```



```text

How can a customer book a service?

```



```text

What is the cancellation policy?

```



An out-of-context question can also be used to verify the fallback response.



\---



\## Challenges Faced



\### Groq API Authentication



The original project requirement specified a Groq LLM. GroqCloud authentication was unavailable during development, so the LLM layer was implemented using Google Gemini.



The RAG architecture remains the same because the LLM is separated from the document retrieval layer.



\### Gemini Model Availability



The initially selected Gemini model was unavailable for new users. The application was updated to use the currently available Gemini model.



\### Response Formatting



The Gemini integration returned structured response content. Additional handling was added to extract the text cleanly before displaying the answer.



\### API Key Security



The Gemini API key is stored in `.env` and excluded from Git using `.gitignore`.



\---



\## Key Features



\- Document-based question answering

\- Semantic search

\- Vector database using ChromaDB

\- Hugging Face embeddings

\- Gemini-powered response generation

\- Source citations

\- Interactive command-line chatbot

\- Context-grounded responses

\- API key protection

\- Modular Python implementation



\---



\## Future Enhancements



\- Add support for multiple PDF and TXT documents.

\- Add a web interface using Streamlit or Flask.

\- Add conversation memory.

\- Add automated RAG evaluation using Ragas.

\- Add document upload functionality.

\- Add metadata filtering.

\- Add a REST API.

\- Add Docker support.

\- Add automated testing and CI/CD.



\---



\## Internship Assignment Alignment



This project addresses the major requirements of the RAG assignment:



| Requirement | Implementation |

|---|---|

| RAG pipeline | Implemented |

| LangChain | Used |

| ChromaDB | Used |

| Document corpus | Implemented |

| Embeddings | Hugging Face Sentence Transformers |

| LLM | Google Gemini |

| Q\&A chatbot | Implemented |

| Source citations | Implemented |

| Context-grounded answers | Implemented |

| API key security | `.env` + `.gitignore` |



\---



\## Conclusion



The project demonstrates a complete Retrieval-Augmented Generation workflow from document ingestion to grounded question answering.



The combination of LangChain, ChromaDB, Hugging Face embeddings, and Gemini provides a modular foundation that can be extended into a production-style RAG application.



\## Author



\*\*Pallavi C M\*\*



Information Science \& Engineering

