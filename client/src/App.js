import { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {

  const [file, setFile] = useState()
  const [question, setQuestion] = useState()
  const [answer, setAnswer] = useState()

const ask=()=>{
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question: question })
};
fetch('http://localhost:5000/ask', requestOptions)
    .then(response => response.json())
    .then(data =>{
      console.log(data)
      setAnswer(data.msg)});
}
  function handleChange(event) {
    setFile(event.target.files[0])
  }
  function handletxtChange(event) {
    setQuestion(event.target.value)
  }
  
  function handleSubmit(event) {
    event.preventDefault()
    const url = 'http://localhost:5000/';
    const formData = new FormData();
    formData.append('file', file);
    formData.append('fileName', file.name);
    const config = {
      headers: {
        'content-type': 'multipart/form-data',
      },
    };
    axios.post(url, formData, config).then((response) => {
      console.log(response.data);
    });

  }



  return (
    <div className="App">
      <header className="App-header">
      <form onSubmit={handleSubmit}>
          <h1>React File Upload</h1>
          <input type="file" onChange={handleChange}/>
          <button type="submit">Upload</button>
        </form>
        <br/>
        <br/>
        <br/>
        <input type="text" onChange={handletxtChange}/>
        <button onClick={ask}>Upload</button>

        {answer? answer: null}
      </header>
    </div>
  );
}

export default App;
