from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import pandas as pd
import os

es_client = Elasticsearch("http://localhost:9200")
index_name = "products-v1"

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

if docs:
    column_order = list(docs[0].keys())
    print(column_order)
    dataframe = pd.DataFrame(docs)[column_order]
else:
    dataframe = pd.DataFrame(docs)

os.makedirs("output", exist_ok=True)
os.makedirs("jsonoutput", exist_ok=True)

csv_export_path = os.path.join("output", "export.csv")
json_export_path = os.path.join("jsonoutput", "export.json")

dataframe.to_csv(csv_export_path, index=False)
dataframe.to_json(json_export_path, index=False)