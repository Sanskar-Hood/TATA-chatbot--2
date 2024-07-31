import os
from langchain_community.vectorstores import Vectara
from langchain_community.vectorstores.vectara import (
    RerankConfig,
    SummaryConfig,
    VectaraQueryConfig,
)
from langchain_community.document_loaders import PyPDFLoader

# Setup environment variables
VECTARA_API_KEY = "zwt_vwKISv4ZM-x7LDQmKq4X_yuKGMQ80sgIYLohtw"
VECTARA_CUSTOMER_ID = "3204614218"
VECTARA_CORPUS_ID = "2"

os.environ["VECTARA_CUSTOMER_ID"] = VECTARA_CUSTOMER_ID
os.environ["VECTARA_CORPUS_ID"] = VECTARA_CORPUS_ID
os.environ["VECTARA_API_KEY"] = VECTARA_API_KEY

# Load Tiago documents
loader = PyPDFLoader("tiago_merged.pdf")
documents = loader.load()

# Create Vectara instance for Tiago
vectara_tiago = Vectara.from_documents(documents, embedding=None)

# Configure Vectara query for Tiago
summary_config = SummaryConfig(is_enabled=True, max_results=7, response_lang="eng")
rerank_config = RerankConfig(reranker="mmr", rerank_k=50, mmr_diversity_bias=0.2)
config = VectaraQueryConfig(
    k=10, lambda_val=0.005, rerank_config=rerank_config, summary_config=summary_config
)

bot_tiago = vectara_tiago.as_chat(config)

def tiago_bot_query(query):
    return bot_tiago.invoke(query)["answer"]
