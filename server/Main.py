from flask import Flask, request, send_from_directory,send_file,jsonify
from flask_cors import CORS
import os
import openai
import sys
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
# ----------------------

from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

embedding = OpenAIEmbeddings()
persist_directory = './chroma'
CORS(app)
UPLOAD_FOLDER = 'D:\summer\server\collections'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
vectordb = None
# ----------------------------------------


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1500,
    chunk_overlap = 150
)
# ---------------------------------------------
@app.route('/', methods=['POST'])
def home():
        global vectordb
        if 'file' not in request.files:
            return "no file"
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"})
        try:
            upload_folder = app.config['UPLOAD_FOLDER']
            file_path = os.path.abspath(os.path.join(upload_folder, file.filename))
            file.save(file_path)
            # -------------------
            loader = PyPDFLoader(file_path) 
            pages = loader.load()
            # ------------------
            splits = text_splitter.split_documents(pages)
            # -------------------
            
            vectordb = Chroma.from_documents(
            documents=splits,
            embedding=embedding,
            persist_directory=persist_directory
            )
      
            vectordb.persist()
            # 
            return jsonify( {"msg" :"uploaded sucess"  } )
        except Exception as e:
            print("Error:", str(e), file=sys.stderr)
            return jsonify({"error": "An error occurred while processing the PDF file"})
# ---------------------------------------------------

@app.route('/ask', methods=['POST'])
def question():
     global vectordb
     vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding
)
     llm = OpenAI(temperature=0)
     compressor = LLMChainExtractor.from_llm(llm)
    #  retriever = SelfQueryRetriever.from_llm(
    #  llm,
    #  vectordb,
    #  verbose=True
    #  )
    # -----------------------
    #  compression_retriever = ContextualCompressionRetriever(
    #    base_compressor=compressor,
    #     base_retriever=vectordb.as_retriever()
    #   )
    #  question = "What is the boy name"
    #  compressed_docs = compression_retriever.get_relevant_documents(question)
    #  print("helooo",file=sys.stderr)
    #  print( compressed_docs, file=sys.stderr)

    #  return jsonify({"msg": compressed_docs[0].page_content})
    # -------------------------------
     qa_chain = RetrievalQA.from_chain_type(
     llm,
     retriever=vectordb.as_retriever(),
     chain_type="refine"
) 
     data = request.get_json()
     question = data['question']
     result = qa_chain({"query": question})
     return jsonify( {"msg" :result["result"]} )
    
if __name__ == "__main__":
    app.run(debug=True)





    "\n\nThe standard name for CO Gas Test Kit for Gas and Vapour is UL 80079-20-1 Explosive Atmospheres - Part 20-1: Material Characteristics for Gas and Vapour Classification - Test Methods and Data (Ed. 1), as specified in the UL 130 Standard Method of Test for Ignition Resistance of Loose Fill Insulation (Cigarette Method) / Méthode Normalisée d’Essai de Résistance à l’Allumage de l’Isolant Thermique Cellulosique à Bourrage Lâche (Méthode de la Cigarette) (Ed. 3), UL 123 Standard for Oxy-Fuel Gas Torches (Ed. 11), UL 124 Outline of Investigation for Hand-Operated Pumps for Flammable and Combustible Liquids (Ed. 4), UL 124 Standard Method of Test for the Evaluation of Protective Coverings for Foamed Plastic / Méthode d’essai normalisée évaluation des revêtements protecteurs des mousses plastiques (Ed. 1), UL 124 STANDARD METHOD OF TEST FOR THE EVALUATION OF THERMAL BARRIERS, UL 13"
