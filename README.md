# RAG Chatbot

A clean, document-based AI chatbot built using **Retrieval-Augmented Generation (RAG)**.

This project allows users to ask questions about information contained in a PDF document. The application retrieves the most relevant parts of the document and provides them as context to an LLM, which generates an answer based only on the retrieved information.

---

## Features

- 📄 PDF document processing
- ✂️ Text chunking with overlapping chunks
- 🧠 Semantic search using embeddings
- 🗄️ ChromaDB vector database
- 🤖 OpenAI-powered question answering
- 🎯 Relevance filtering for unrelated questions
- ⚡ Token-conscious retrieval
- 🌐 FastAPI backend
- 💬 Clean and minimal chatbot interface
- 🔐 Environment-based API key management

---

## How RAG Works

The application follows a Retrieval-Augmented Generation pipeline:

```text
                PDF DOCUMENT
                     │
                     ▼
              Extract PDF Text
                     │
                     ▼
               Text Chunking
                     │
                     ▼
              Generate Embeddings
                     │
                     ▼
                ChromaDB
                     │
                     │
                     │
              USER QUESTION
                     │
                     ▼
            Generate Query Embedding
                     │
                     ▼
              Similarity Search
                     │
                     ▼
             Relevance Check
                     │
             ┌───────┴───────┐
             │               │
          Relevant        Unrelated
             │               │
             ▼               ▼
       Retrieve Context   No LLM Call
             │               │
             ▼               ▼
          OpenAI          Return:
             │            "I couldn't find
             ▼             that information
           Answer           in the document."

           RAG-CHATBOT/
│
├── app/
│   ├── chunker.py          # Splits document text into chunks
│   ├── embeddings.py       # Generates text embeddings
│   ├── llm.py              # Handles LLM question answering
│   ├── main.py             # FastAPI application
│   ├── pdf_reader.py       # Extracts text from PDF files
│   ├── process_pdf.py      # Processes and stores PDF embeddings
│   ├── rag_test.py         # RAG testing
│   ├── retriever.py        # Performs semantic retrieval
│   ├── vector_store.py     # ChromaDB configuration
│   │
│   └── static/
│       ├── index.html      # Chatbot interface
│       ├── script.js       # Frontend logic
│       └── style.css       # UI styling
│
├── documents/              # Local PDF documents
├── chroma_db/              # Local vector database
├── .env                    # API keys (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

Tech Stack
Technology	     Purpose
Python	      Core programming language
FastAPI	       Backend API
ChromaDB	     Vector database
Sentence        Transformers	Text embeddings
OpenAI API     	Answer generation
PyPDF	PDF text    extraction
HTML	Frontend     structure
CSS	Frontend        styling
JavaScript	      Frontend interaction

How It Works
1. PDF Processing

The PDF is read and its text is extracted.

PDF
 ↓
Text
2. Text Chunking

The extracted text is divided into smaller overlapping chunks.

This allows the retrieval system to search smaller sections of the document instead of processing the entire document at once.

Example configuration:

chunk_size = 1000
overlap = 200
3. Embedding Generation

Each chunk is converted into a numerical vector representation called an embedding.

These embeddings allow the system to compare the semantic similarity between the user's question and document chunks.

4. Vector Storage

The embeddings are stored in ChromaDB.

Document Chunk
      ↓
   Embedding
      ↓
   ChromaDB
5. Question Retrieval

When the user asks a question:

User Question
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Most Relevant Chunks

The system retrieves the most relevant document sections.

6. Relevance Filtering

The system checks the similarity distance of the retrieved results.

If the closest result is too far away from the question, the system treats the question as unrelated to the document.

This prevents unnecessary LLM requests.

7. Answer Generation

If relevant context is found, it is passed to the OpenAI model along with the user's question.

The model is instructed to answer using only the provided document context.

Example
Question
What is reinforcement learning?
Retrieved Context

The system retrieves the relevant section from the document containing information about reinforcement learning.

Generated Answer
Reinforcement learning is a type of machine learning in which an
agent learns through trial and error by interacting with an
environment. It receives rewards or penalties based on its actions
and uses this feedback to maximize long-term success.
Handling Unrelated Questions

The chatbot also prevents unrelated questions from being unnecessarily sent to the LLM.

For example:

Question:
What is the recipe for making pizza?

If the document does not contain relevant information, the system returns:

I couldn't find that information in the document.

This relevance check helps reduce unnecessary API usage and keeps the chatbot grounded in the provided document.

API

The backend is built using FastAPI.

Health Check
GET /

Response:

{
  "message": "RAG Chatbot API is running"
}
Ask a Question
POST /ask

Request:

{
  "question": "What is reinforcement learning?"
}

Response:

{
  "question": "What is reinforcement learning?",
  "answer": "Reinforcement learning is a type of machine learning..."
}
Installation
1. Clone the Repository
git clone https://github.com/Yeshwanthnuvvula/RAG-CHATBOT.git
cd RAG-CHATBOT
2. Create a Virtual Environment
python -m venv venv

Activate it on macOS/Linux:

source venv/bin/activate

On Windows:

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure the OpenAI API Key

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

Never commit your .env file or expose your API key publicly.

5. Add a Document

Place your PDF inside:

documents/
6. Process the PDF

Run:

python app/process_pdf.py

This will:

Extract text from the PDF
Split the text into chunks
Generate embeddings
Store the embeddings in ChromaDB
7. Start the Application

Run:

uvicorn app.main:app --reload

Then open:

http://127.0.0.1:8000
Environment Variables

The application requires:

OPENAI_API_KEY

The .env file is intentionally excluded from Git using .gitignore.

Testing

The retrieval system can be tested directly using:

python -c "from app.retriever import get_context; print(get_context('What is reinforcement learning?'))"

Similarity distances can also be inspected using:

python -c "from app.retriever import search; r=search('What is reinforcement learning?'); print(r['distances'])"
Design Goals

The project focuses on three main principles:

1. Grounded Answers

The LLM receives retrieved document context and is instructed not to rely on outside knowledge.

2. Efficient Retrieval

Only relevant document chunks are passed to the LLM.

3. Reduced Unnecessary API Usage

Unrelated questions are filtered before making an LLM request.
Future Improvements

Possible future improvements include:

📚 Support for multiple documents
📤 PDF upload directly through the UI
🔎 Display retrieved sources
💬 Conversation history
🧹 Improved document management
📊 Retrieval evaluation
🚀 Cloud deployment
🔐 Authentication
⚙️ Configurable chunk size and retrieval parameters

Author

Yeshwanth Nuvvula

AI/ML Student | Interested in Artificial Intelligence, Machine Learning and Software Development

License

This project is intended for educational and portfolio purposes.
