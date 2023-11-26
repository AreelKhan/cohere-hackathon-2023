import os

from langchain.schema import SystemMessage
from langchain.prompts import MessagesPlaceholder
from langchain.chat_models import ChatCohere
from langchain.docstore.document import Document
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.memory import ConversationBufferMemory
from typing import List
from classify import get_user_intent
from utils import BrainTumourDiagnosisAgent
from app import uploaded_files

COHERE_API_KEY = "leKGpK1kojv9JIOqduGjiJfevBphofbWMmfRyQrj"
#os.environ["COHERE_API_KEY"] = COHERE_API_KEY
MEMORY_KEY = 'key'

class MedicalChatBot:
    """
    Master Agent.
    """
    def __init__(self, api_key) -> None:


        self.llm = ChatCohere(model="large", temperature=0.0, streaming=True)

        self.prompt = AGENT_HERE.create_prompt(
            system_message=SystemMessage(content=SYSTEM_MESSAGE_PROMPT),
            extra_prompt_messages=[
                MessagesPlaceholder(variable_name=MEMORY_KEY),
            ],
        )

        self.memory = ConversationBufferMemory(
            memory_key=MEMORY_KEY,
            return_messages=True,
            input_key="input",
            output_key="output",
        )



    def query(self, message):

        # first we check the user intent
        intent = get_user_intent(message)

        if intent == "Diagnose Brain Tumour":
            # call brain diagnosis model
            test = BrainTumourDiagnosisAgent(image)
            test.diagnose()









