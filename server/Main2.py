from dotenv import load_dotenv
from flask import Flask, request, send_from_directory,send_file,jsonify
from flask_cors import CORS
load_dotenv()

from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI

from langchain.agents import create_csv_agent
app = Flask(__name__)

CORS(app)
@app.route('/ask', methods=['POST'])
def question():
     file = "D:\summer\server\csv\movie.csv"
     agent = create_csv_agent(
     ChatOpenAI(temperature=0),
     file,
     agent_type=AgentType.OPENAI_FUNCTIONS,
     )
   
     data = request.get_json()
     question = data['question']
     res=agent.run(question)
     return jsonify( {"msg" :res} )
    
if __name__ == "__main__":
    app.run(debug=True)


