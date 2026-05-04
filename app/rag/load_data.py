from langchain_community.document_loaders import TextLoader
import os

def load_documents():
    docs = []

    base_path = "data"

    # Load policies
    policies_path = os.path.join(base_path, "policies")
    for file in os.listdir(policies_path):
        loader = TextLoader(os.path.join(policies_path, file))
        docs.extend(loader.load())

    # Load logs
    logs_path = os.path.join(base_path, "logs")
    for file in os.listdir(logs_path):
        loader = TextLoader(os.path.join(logs_path, file))
        docs.extend(loader.load())

    return docs