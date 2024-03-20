The repository contains code for a web application built with FastAPI and React. The application allows users to upload text files (.txt), PDF files (.pdf), or CSV files (.csv), ask questions about the content of the uploaded file, and receive answers based on the provided query.

Features Upload files: Users can upload text files, PDF files, or CSV files using the web interface. Ask questions: Users can enter a question about the content of the uploaded file. Receive answers: The application uses a pre-trained model to generate answers to user queries based on the content of the uploaded file. File Structure backend/main.py: FastAPI backend code that handles file upload, question answering, and API endpoints. frontend/src/App.tsx: React frontend code for the web application interface. frontend/src/App.css: CSS stylesheet for styling the frontend components. frontend/public/index.html: HTML template for the React application.

Dependencies FastAPI: Backend web framework for building APIs with Python. React: Frontend JavaScript library for building user interfaces. Pydantic: Data validation and settings management using Python type annotations. Transformers: Library for natural language processing using pre-trained models. Axios: HTTP client for making requests from the frontend to the backend server. Credits::: This project was inspired by the need for a simple and efficient way to extract information from text documents and provide answers to user queries.


Backend (FastAPI):

File Upload: Users can upload text files (.txt), PDF files (.pdf), or CSV files (.csv) using the FastAPI endpoint /predict.
Text Extraction: The content of the uploaded file is extracted using the get_file_content function.
Word Count: The number of words in the uploaded file is calculated.
Question Answering: Users can provide a query, and the model generates an answer based on the content of the uploaded file and the query.
Model Usage: The code uses the transformers library to load a pre-trained question answering model (AutoModelForQuestionAnswering) and its tokenizer (AutoTokenizer).
Response Model: The API response includes the file content, word count, and the generated answer.
Frontend (React):

File Selection: Users can select a file to upload.
Query Input: Users can enter a query for question answering.
Submit Button: When clicked, the form data (file and query) is sent to the backend for processing.
Response Display: The response from the backend (file content, word count, and answer) is displayed below the form.
Styling: The frontend is styled using CSS to improve visual presentation.
Documentation:



Backend Dependencies: FastAPI, Pydantic, GridFS, pymongo, textract, pandas, PyPDF2, transformers, torch.
Frontend Dependencies: React, Axios.



NOTE: you might need to install transformers and pytorch if you are running it on your local machine
Python Version: The backend code is written in Python 3.x.
 The frontend code requires Node.js to run React.
Package Managers: Python uses pip for package management, while Node.js uses npm or yarn.
