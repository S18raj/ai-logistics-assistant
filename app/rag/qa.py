from app.rag.embeddings import create_vector_store
from app.llm.groq_llm import generate_answer

vector_store = create_vector_store()

def get_answer(query: str):

    docs = vector_store.similarity_search(query, k=3)

    context = "\n".join([d.page_content for d in docs])

    answer = generate_answer(context, query)

    return answer