from elasticsearch import Elasticsearch

es_client = Elasticsearch("http://localhost:9200")
index_name = "products-v1"
columns = ["id", "tags"]  # Choose columns. Leave empty array to choose all the columns.
query = {
    "_source": columns,
    "query": {
        "match_all": {}
    }
}