


from dotenv import load_dotenv
from flask import Flask, request, send_from_directory,send_file,jsonify
from flask_cors import CORS
load_dotenv()
import sys
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI 
agent = create_csv_agent(OpenAI(temperature=0), 
                         'server\csv\All_standards.csv', 
                         verbose=True)


print(agent.agent.llm_chain.prompt.template)
# agent.run("what is the standard name for  Gas and Vapor Detectors and Sensors ?")