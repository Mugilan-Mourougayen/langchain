


from dotenv import load_dotenv
from flask import Flask, request, send_from_directory,send_file,jsonify
from flask_cors import CORS
load_dotenv()
import sys
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI 
agent = create_csv_agent(OpenAI(temperature=0), 
                         'server\csv\All_standardss.csv', 
                         verbose=True)



question = """
What is the UL standard for Gas and Vapor Detectors and Sensors in March?
"""

prompt = f"""
Search the dataset for the UL standard name related to text.
Return the entire raw row as it is .
Text: `{question}`
"""

print(agent.agent.llm_chain.prompt.template)
agent.run(prompt)