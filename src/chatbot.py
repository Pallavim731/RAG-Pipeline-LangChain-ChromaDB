from rag_pipeline import ask_question


def start_chatbot():
    print("=" * 60)
    print("Urban Company RAG Q&A Chatbot")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        if not question:
            print("Chatbot: Please enter a question.")
            continue

        try:
            answer, sources = ask_question(question)

            print("\nAssistant:")
            print(answer)

            print("\nSources:")
            for source in sources:
                print(f"- {source}")

        except Exception as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    start_chatbot()