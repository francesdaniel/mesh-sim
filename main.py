# Simulated RAG logic

def load_context():
    with open("context.txt", "r") as f:
        return f.read()

def simulate_rag(question):
    context = load_context()
    prompt = f"""
    Context:
    {context}

    Question: {question}
    Answer:"""
    return prompt

if __name__ == "__main__":
    print("Welcome to the Mini-RAG Simulator")
    question = input("Ask a question: ")
    response = simulate_rag(question)
    print("\n---\n" + response)
