from pathlib import Path

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DOCUMENT_PATH = BASE_DIR / "data" / "documents" / "urban_company_services.txt"
CHROMA_PATH = BASE_DIR / "chroma_db"


def build_vector_database():
    print("Loading document...")

    loader = TextLoader(str(DOCUMENT_PATH), encoding="utf-8")
    documents = loader.load()

    print(f"Loaded {len(documents)} document(s).")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("Creating embeddings...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Storing vectors in ChromaDB...")

    vector_store = Chroma(
        collection_name="urban_company_services",
        embedding_function=embeddings,
        persist_directory=str(CHROMA_PATH),
    )

    vector_store.add_documents(chunks)

    print("ChromaDB indexing completed successfully.")
    print(f"Database location: {CHROMA_PATH}")


if __name__ == "__main__":
    build_vector_database()