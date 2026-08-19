# AI-Based-Legal-Document-Analyzer-and-Question-Answering-System
AI-Based Legal Document Analyzer and Question Answering System using RAG, FAISS, Llama 3.3, Groq API, and NLP to analyze legal PDFs, detect clauses and risks, generate summaries, and answer document-based questions.
# AI-Based Legal Document Analyzer and Question Answering System

## 📌 Project Overview

The **AI-Based Legal Document Analyzer and Question Answering System** is an AI-powered web application designed to simplify the analysis of lengthy and complex legal documents.

The system allows users to upload legal documents in PDF format and automatically analyzes their contents. It extracts text, identifies important legal clauses, detects potential risks, generates summaries, and allows users to ask questions about the uploaded document using natural language.

The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant sections from the uploaded document before generating an answer. This helps provide document-specific responses and reduces irrelevant or unsupported answers.

---

## 🎯 Objectives

The main objectives of this project are:

- Develop an AI-based legal document analyzer.
- Extract text from legal PDF documents.
- Preprocess and clean extracted text.
- Divide documents into meaningful chunks.
- Generate semantic embeddings.
- Store embeddings using FAISS.
- Implement Retrieval-Augmented Generation (RAG).
- Integrate Llama 3.3 for question answering.
- Identify important legal clauses.
- Detect potential legal risks.
- Generate document summaries.
- Answer natural-language questions.
- Maintain document and question history.
- Generate downloadable PDF reports.

---

## ✨ Key Features

### 1. PDF Document Upload

Users can upload legal documents in PDF format through the web interface.

### 2. Text Extraction

The system uses **PyMuPDF** to extract text from uploaded PDF documents.

### 3. Text Preprocessing

Extracted text is cleaned and prepared for further analysis.

### 4. Text Chunking

Large documents are divided into smaller overlapping chunks to preserve contextual information.

### 5. Semantic Embeddings

The system uses the:

**BAAI/bge-small-en-v1.5**

embedding model to convert document chunks and user questions into numerical vector representations.

### 6. FAISS Vector Search

FAISS is used to store document embeddings and perform efficient similarity-based retrieval.

### 7. Legal Clause Detection

The system identifies important legal clauses such as:

- Payment
- Termination
- Confidentiality
- Liability
- Warranty
- Governing Law
- Intellectual Property
- Rights
- Obligations
- Force Majeure
- Dispute Resolution

### 8. Risk Detection

The system identifies potential legal risk indicators related to:

- Penalties
- Breaches
- Damages
- Liabilities
- Lawsuits
- Defaults
- Legal actions

### 9. Document Summarization

A concise summary is generated to help users quickly understand the overall document.

### 10. AI Question Answering

Users can ask natural-language questions about the uploaded document.

The system retrieves relevant document sections using FAISS and provides them as context to the Llama 3.3 model.

### 11. Database Management

SQLite is used to maintain:

- Document records
- Extracted chunks
- Detected clauses
- Identified risks
- Questions
- Generated answers
- Question history

### 12. PDF Report Generation

The system can generate downloadable PDF reports containing:

- Document summary
- Detected clauses
- Identified risks
- Analysis results
- Recommendations for further review

---

## 🏗️ System Architecture

The project follows the following processing pipeline:

PDF Upload  
↓  
Text Extraction using PyMuPDF  
↓  
Text Preprocessing  
↓  
Text Chunking  
↓  
Embedding Generation  
↓  
FAISS Vector Storage  
↓  
Semantic Retrieval  
↓  
Relevant Document Chunks  
↓  
Llama 3.3 through Groq API  
↓  
AI-Generated Answer

Along with the question-answering pipeline, the system also performs:

- Legal clause detection
- Risk detection
- Document summarization
- Database storage
- PDF report generation

---

## 🔄 Project Workflow

### Step 1: Upload Document

The user uploads a legal PDF document.

### Step 2: Extract Text

PyMuPDF extracts the textual content from the PDF.

### Step 3: Preprocess Text

The extracted text is cleaned and prepared for analysis.

### Step 4: Create Chunks

The document is divided into smaller overlapping chunks.

### Step 5: Generate Embeddings

The BAAI/bge-small-en-v1.5 model converts the chunks into semantic vectors.

### Step 6: Store Vectors

The generated vectors are stored in FAISS.

### Step 7: Analyze Legal Content

The system identifies important legal clauses and potential risks.

### Step 8: Ask a Question

The user enters a natural-language question.

### Step 9: Retrieve Relevant Information

The question is converted into an embedding and compared with the stored document vectors.

### Step 10: Generate Answer

The most relevant document sections are provided to Llama 3.3 through the Groq API.

### Step 11: Store Information

Document information, questions, answers, clauses, and risks are stored in SQLite.

### Step 12: Generate Report

The system generates a downloadable PDF report.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Web application backend |
| PyMuPDF | PDF text extraction |
| HuggingFace | Embedding model |
| BAAI/bge-small-en-v1.5 | Semantic embeddings |
| FAISS | Vector similarity search |
| RAG | Document-based question answering |
| Llama 3.3 | Large Language Model |
| Groq API | LLM API access |
| SQLite | Database |
| HTML | Frontend structure |
| CSS | Frontend styling |
| JavaScript | Frontend functionality |

---

## 📂 Project Structure

```text
AI-Legal-Document-Analyzer/
│
├── app.py
├── config.py
├── requirements.txt
│
├── ai/
│   ├── rag.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── analyzer.py
│
├── utils/
│   └── pdf_processor.py
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── upload.html
│   ├── analysis.html
│   ├── chat.html
│   ├── report.html
│   ├── search.html
│   ├── viewer.html
│   └── about.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
│
├── reports/
│
├── vector_db/
│
└── database.db
