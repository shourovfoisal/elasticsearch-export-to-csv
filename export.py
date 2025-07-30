from elasticsearch.helpers import scan
from config import es_client, index_name, columns, query
import pandas as pd
import os

def main():
    results = scan(
        client=es_client,
        query=query,
        index=index_name,
        scroll='2m',
        size=1000,
        preserve_order=True,
    )

    docs = []
    for i, doc in enumerate(results):
        docs.append(doc['_source'])

    if docs:
        column_order = list(docs[0].keys())

        # Sometimes, the first element's keys, which is:
        # column_order = list(docs[0].keys())
        # might not contain all the columns
        # as we can't expect every document to have data for every column
        if len(columns) > 0:
            dataframe = pd.DataFrame(docs)[columns] # we know the columns to expect
        else:
            dataframe = pd.DataFrame(docs)[column_order]    # we need to extract the columns from the first element
    else:
        dataframe = pd.DataFrame(docs)

    output_to_csv(dataframe)
    output_to_json(dataframe)

def output_to_csv(dataframe):
    os.makedirs("output", exist_ok=True)
    csv_export_path = os.path.join("output", "export.csv")
    dataframe.to_csv(csv_export_path, index=False)

def output_to_json(dataframe):
    os.makedirs("jsonoutput", exist_ok=True)
    json_export_path = os.path.join("jsonoutput", "export.json")
    dataframe.to_json(json_export_path, index=False)
    
main()