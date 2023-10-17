from dotenv import load_dotenv
from flask import Flask, request,jsonify
from flask_cors import CORS
load_dotenv()


from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(return_messages=True)
llm = OpenAI(temperature=0)
conversation = ConversationChain(
    llm=llm, 
    verbose=True, 
    memory=ConversationBufferMemory()
)

app = Flask(__name__)

CORS(app)
@app.route('/ask', methods=['GET'])
def question():
     data = request.get_json()
     question = data['question']
     res = conversation.predict("how many chaactes can you return as output") 
     
    #  res = conversation.predict(input=question) 
     
     return res 
    
if __name__ == "__main__":
    app.run(debug=True)


