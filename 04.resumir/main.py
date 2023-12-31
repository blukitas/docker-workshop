from PdfQA import PdfQA
from constants import EMB_SBERT_MPNET_BASE, LLM_FLAN_T5_BASE

# Configuration for PdfQA
config = {
    "persist_directory": None,
    "load_in_8bit": False,
    "embedding": EMB_SBERT_MPNET_BASE,
    "llm": LLM_FLAN_T5_BASE,
    "pdf_path": "./data/example.pdf",
}

# Initialize PdfQA
print("Initializing PdfQA")
pdfqa = PdfQA(config=config)
print("Initialized embeddings")
pdfqa.init_embeddings()
print("Initialized models")
pdfqa.init_models()

# Create Vector DB
print("vector db")
pdfqa.vector_db_pdf()

# Set up Retrieval QA Chain
print("retreival qa")
pdfqa.retreival_qa_chain()

# Query the model
# question = "how do you summarize the content of the book"
print("Answering questions")
with open("./data/questions.txt") as f:
    # Until I get to the end of the file, read by line
    answers = []
    for question in f:
        answers.append(f"question: {question}")
        answer, documents = pdfqa.answer_query(question)
        answers.append(f"answer: {answer}\n")
        answers.append(f"documents: {documents}\n")

    with open("./data/answers.txt", "w") as f:
        for i in answers:
            f.write(i)

# print(f"Question: {question}")
# print(f"answer: {answer}")
