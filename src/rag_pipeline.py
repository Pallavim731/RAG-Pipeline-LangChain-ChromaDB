import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROMA_DIR = os.path.join(BASE_DIR, "chroma_db")


# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Load ChromaDB
vectorstore = Chroma(
    collection_name="urban_company_services",
    persist_directory=CHROMA_DIR,
    embedding_function=embeddings,
)


# Create retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)


# RAG prompt
prompt = ChatPromptTemplate.from_template(
    """
You are a helpful customer support assistant.

Answer the question using ONLY the information provided
in the context below.

If the answer is not available in the context, say:
"I don't have enough information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""
)


def ask_question(question):
    # Retrieve relevant documents
    documents = retriever.invoke(question)

    # Combine retrieved content
    context = "\n\n".join(
        document.page_content for document in documents
    )

    # Create prompt
    formatted_prompt = prompt.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    # Generate answer
    response = llm.invoke(formatted_prompt)

    # Clean Gemini response
    answer = response.content

    if isinstance(answer, list):
        answer = "\n".join(
            item.get("text", "")
            for item in answer
            if isinstance(item, dict) and item.get("type") == "text"
        )

    # Collect source information
    sources = []

    for document in documents:
        source = document.metadata.get(
            "source",
            "Unknown source"
        )

        if source not in sources:
            sources.append(source)

    return answer, sources


if __name__ == "__main__":
    question = input("Ask a question: ")

    answer, sources = ask_question(question)

    print("\nAnswer:")
    print(answer)

    print("\nSources:")

    for source in sources:
        print(f"- {source}")