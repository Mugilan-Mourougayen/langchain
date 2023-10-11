from dotenv import load_dotenv
from flask import Flask, request,jsonify
from flask_cors import CORS

load_dotenv()



from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType,Tool
import os
from langchain.utilities import OpenWeatherMapAPIWrapper
from langchain.utilities import SerpAPIWrapper
# os.environ["OPENAI_API_KEY"] = ""
# os.environ["OPENWEATHERMAP_API_KEY"] = ""
from langchain.chat_models import ChatOpenAI
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

llm = OpenAI(temperature=0)

weather = OpenWeatherMapAPIWrapper()
search = SerpAPIWrapper()
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events. You should ask targeted questions",
    ),
 Tool(
        name="weather",
        func=weather.run,
        description="useful for when you need to answer questions about weather , temperature and climatic change of a place",
    ),]


agent_kwargs = {
    "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
}
memory = ConversationBufferMemory(memory_key="memory", return_messages=True)
agent_chain = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True, agent_kwargs=agent_kwargs, memory=memory,
)












app = Flask(__name__)

CORS(app)
@app.route('/ask', methods=['POST'])
def question():
     data = request.get_json()
     question = data['question']
     res = agent_chain.run(question)
     
     return jsonify( {"msg" :res} )
    
if __name__ == "__main__":
    app.run(debug=True)