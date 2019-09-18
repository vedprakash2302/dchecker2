import time
import json
import traceback
import logging
from urllib.parse import urlencode
from urllib.request import urlopen


def vivo_sparql_query(query,
                      baseURL="http://sparql.vivo.ufl.edu/VIVO/sparql",
                      format="application/sparql-results+json", debug=False):
    """
    Given a SPARQL query string return result set of the SPARQL query.  Default
    is to call the UF VIVO SPAQRL endpoint and receive results in JSON format
    """

    prefix = """
    PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd:     <http://www.w3.org/2001/XMLSchema#>
    PREFIX owl:     <http://www.w3.org/2002/07/owl#>
    PREFIX swrl:    <http://www.w3.org/2003/11/swrl#>
    PREFIX swrlb:   <http://www.w3.org/2003/11/swrlb#>
    PREFIX vitro:   <http://vitro.mannlib.cornell.edu/ns/vitro/0.7#>
    PREFIX bibo:    <http://purl.org/ontology/bibo/>
    PREFIX dcelem:  <http://purl.org/dc/elements/1.1/>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX event:   <http://purl.org/NET/c4dm/event.owl#>
    PREFIX foaf:    <http://xmlns.com/foaf/0.1/>
    PREFIX geo:     <http://aims.fao.org/aos/geopolitical.owl#>
    PREFIX pvs:     <http://vivoweb.org/ontology/provenance-support#>
    PREFIX ero:     <http://purl.obolibrary.org/obo/>
    PREFIX scires:  <http://vivoweb.org/ontology/scientific-research#>
    PREFIX skos:    <http://www.w3.org/2004/02/skos/core#>
    PREFIX ufVivo:  <http://vivo.ufl.edu/ontology/vivo-ufl/>
    PREFIX vitro:   <http://vitro.mannlib.cornell.edu/ns/vitro/public#>
    PREFIX vivo:    <http://vivoweb.org/ontology/core#>
    PREFIX core:    <http://vivoweb.org/ontology/core#>
    """
    params = {
        "default-graph": "",
        "should-sponge": "soft",
        "query": prefix+query,
        "debug": "on",
        "timeout": "7000",  # 7 seconds
        "format": format,
        "save": "display",
        "fname": ""
    }
    querypart = urlencode(params).encode("utf-8")
    if debug:
        print("Base URL " + baseURL)
        print("Query: " + querypart)
    start = 2.0
    retries = 10
    count = 0
    while True:
        try:
            response = urlopen(baseURL, querypart).read()
            break
        except Exception as e:
            logging.exception(("OH DAMN."))
            count = count + 1
            if count > retries:
                break
            sleep_seconds = start**count
            print("<!-- Failed query. Count = "+str(count) +
                  " Will sleep now for "+str(sleep_seconds) +
                  " seconds and retry -->")
            time.sleep(sleep_seconds)  # increase the wait time with each retry
    try:
        return json.loads(response)
    except:
        return None
