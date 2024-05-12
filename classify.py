import cohere
import os
from cohere import ClassifyExample

# get cohere api key from .env
from dotenv import load_dotenv
import os

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

INTENTS = {'General QA': 0, 'Diagnose Brain Tumour': 1, 'Blood Work': 2}

BRAIN_TUMOUR = "Diagnose Brain Tumour"
OTHER = "Other"

def get_user_intent(user_message):

  examples = [
    ClassifyExample(text="I need a tumour diagnoses on this brain scan.", label=BRAIN_TUMOUR),
    ClassifyExample(text="Can you make a diagnoses for this brain MRI?", label=BRAIN_TUMOUR),
    ClassifyExample(text="What is the cancer likelihood for this MRI scan of a patient's brain?", label=BRAIN_TUMOUR),
    ClassifyExample(text="What is the probability of positive tumour diagnosis for this brain MRI.", label=BRAIN_TUMOUR),
    ClassifyExample(text="I uploaded a brain scan, can you analyze and interpret it for me?", label=BRAIN_TUMOUR),
    ClassifyExample(text="What is the survival rate for stage 2 lung cancer", label=OTHER),
    ClassifyExample(text="What is the survival rate for brain tumour", label=OTHER),
    ClassifyExample(text="How is indigestion cured?", label=OTHER),
    ClassifyExample(text="What are the symptoms of diabetes?", label=OTHER),
  ]

  # Sends the classification request to the Cohere model
  user_intent = co.classify(
    model='large',
    inputs=[user_message],
    examples=examples
  )

  return user_intent.classifications[0].predictions