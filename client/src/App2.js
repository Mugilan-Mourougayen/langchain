import { useState } from 'react';
import './App.css';
import axios from 'axios';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Button from 'react-bootstrap/Button';
import "bootstrap/dist/css/bootstrap.min.css"
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Offcanvas from 'react-bootstrap/Offcanvas';
import Container from 'react-bootstrap/Container';

function App() {

  const [file, setFile] = useState()
  const [question, setQuestion] = useState()
  const [answer, setAnswer] = useState()
  const [chistory,setChistory]=useState()

const ask=()=>{
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question: question })
};
fetch('http://localhost:5000/ask', requestOptions)
    .then(response => response.json())
    .then(data =>{
      
      

      setAnswer(data.msg)
      console.log(data)
    });
    
}
  function handleChange(event) {
    setFile(event.target.files[0])
  }
  function handletxtChange(event) {
    setQuestion(event.target.value)
  }
  
  const upload=()=> {
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
      <Container>
      <Row>
        <Col sm={8}>
          <div>
          <Form controlId="formFileMultiple" style={{width:"50%"}}>
          <Row>
            <Col>
        <Form.Control type="file" multiple onChange={handleChange}/>
            </Col>
            <Col>
            <Button onClick={upload}>Upload</Button>
            </Col>

          </Row>
      </Form>

      

      <br/>
        <br/>
        <br/>
        <Form controlId="formFileMultiple" style={{width:"100%"}}>
          <Row>
            <Col xs={9}>
            <Form.Control  type="text" placeholder="question" onChange={handletxtChange} style={{marginLeft:"50px"}}/>
            </Col>
            <Col>
            <Button onClick={ask} variant="success">Ask</Button>
            </Col>

          </Row>
      </Form>
<br/>
<br/>
        
        
        {answer? 


      <InputGroup style={{width:"95%"}}>
        <Form.Control as="textarea" value={answer}aria-label="With textarea" />
        <InputGroup.Text onClick={() => {
          navigator.clipboard.writeText(answer);}}>
          Copy</InputGroup.Text>
      </InputGroup>
          : null}

          </div>
        </Col>
        <Col sm={4}>
       hello
        </Col>
      </Row>
    </Container>
   
        
 
      </header>
    </div>
  );
}

export default App;
