# MedChat: Bridging AI and Medical Practice

MedChat won the Cohere RAG Hackathon held at the University of Waterloo! [News article](https://uwaterloo.ca/artificial-intelligence-institute/news/medchat-wins-cohere-retrieval-augmentation-generation).

## What MedChat Does
MedChat serves a dual purpose:

1. **Querying Medical Literature:** Using RAG om medical literature, MedChat allows easy interaction with medical literature, aiding healthcare providers in keeping up-to-date with the latest research findings, treatment protocols, and clinical guidelines.

2. **AI-Powered Diagnosis Assistance:** Beyond literature, MedChat integrates pre-trained medical models that assist in disease diagnosis. Doctors can submit MRI scans, X-rays and possibly other data, and MedChat can call other models to extract meaningful insights and diagnoses, offering a second opinion in medical diagnoses.

## How We Built MedChat

- **Utilizing Cohere API:** The backbone of MedChat is the Cohere API, including Cohere Chat for natural language processing, Classify for classifying user intent, and Rerank for optimizing response relevance.

- **Frontend Development with Streamlit:** We chose Streamlit for its simplicity.

- **Integrating Tensorflow for Running Medical Models:** The core functionality of disease diagnosis is powered by medical models run on Tensorflow. This integration allows MedChat to process complex medical data and provide accurate, AI-driven diagnostic suggestions.

## Challenges We Faced
A primary challenge in developing MedChat was:

- **Detecting User Intent Accurately:** To ensure that MedChat responds appropriately to the queries of medical professionals, a critical task was to accurately detect user intent. This involved discerning whether a query was seeking medical literature or a diagnosis, and then triggering the correct functions within the application. We did this using Cohere Classify, which is not scalable. Now that Cohere API supports Function calling, that would be a much better tool.

<img width="1791" alt="original" src="https://github.com/AreelKhan/MedChat/assets/20444505/b5a4bce0-c2ce-4429-bbba-59fe4d95cd29">

<img width="1791" alt="original (1)" src="https://github.com/AreelKhan/MedChat/assets/20444505/5d6377e6-5f09-4628-97a0-ffa95c8f1bdf">

<img width="3760" alt="original (2)" src="https://github.com/AreelKhan/MedChat/assets/20444505/06894c8c-6bb3-4a38-9abb-5663852f4741">
