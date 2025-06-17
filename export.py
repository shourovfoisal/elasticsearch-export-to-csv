from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import pandas as pd
import os

es_client = Elasticsearch("http://localhost:9200")

DEV_INDEX = "products-v1-dev"
PRE_PROD_INDEX = "products-v1-pre-prod"

index_name = DEV_INDEX

query = {
    "query": {
        "match_all": {}
    }
}

results = scan(
    client=es_client,
    query=query,
    index=index_name,
    scroll='2m',
    size=1000,
    preserve_order=True
)

docs = []
for doc in results:
    docs.append(doc['_source'])

dataframe = pd.DataFrame(docs)
os.makedirs("output", exist_ok=True)
export_path = os.path.join("output", "export.csv")
dataframe.to_csv(export_path, index=False)

print(f"Export completed: {export_path}")
