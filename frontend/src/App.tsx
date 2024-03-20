


import React, { useState } from 'react';
import "./App.css";
import axios from 'axios';

const App: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [query, setQuery] = useState<string>('');
  const [response, setResponse] = useState<any>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setFile(event.target.files[0]);
    }
  };

  const handleQueryChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(event.target.value);
  };

  const handleSubmit = async () => {
    if (!file) {
      console.error('Please select a file.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const result = await axios.post('http://localhost:8000/predict', formData, {
        params: { query },
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      setResponse(result.data);
    } catch (error) {
      console.error('An error occurred:', error);
    }
  };

  return (
    <div>
      <h1>File Upload and Question Answering</h1>
      <input type="file" accept=".txt,.pdf,.csv" onChange={handleFileChange} />
      <br />
      <input type="text" value={query} onChange={handleQueryChange} placeholder="Enter your query" />
      <br />
      <button onClick={handleSubmit}>Submit</button>
      {response && (
        <div>
          <h2>Response</h2>
          <p>Content: {response.content}</p>
          <p>Word Count: {response.word_count}</p>
          <p>Answer: {response.answer}</p>
        </div>
      )}
    </div>
  );
};

export default App;


