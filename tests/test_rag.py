from src.rag_pipeline import ask_question


def test_rag_returns_answer_and_sources():
    question = "What services are available for AC?"

    answer, sources = ask_question(question)

    assert answer
    assert isinstance(answer, str)
    assert isinstance(sources, list)
    assert len(sources) > 0