import logging
import os

from .vivotools import vivo_sparql_query
from .utils import echo, sparql_variable_rename


class QueryHandler:

    def __init__(self):
        pass

    def query_iterator(self, endpoint, path):
        """Loops over a list of SPARQL queries and sends them to an endpoint.
        Keyword arguments:
        endpoint -- an accessible SPARQL endpoint
        """
        report = ""
        all_queries = os.listdir(path)
        all_queries.sort()
        echo("Queries that will be run:", "yellow")
        echo(all_queries, "yellow")
        echo("", "white")
        for query_file in all_queries:
            with open(path + query_file, 'r') as query_file_path:
                logging.info("Opened query file %s", query_file)
                if query_file == 'Duplicated_UFIDs.rq' \
                        or query_file == 'Duplicated_Gatorlinks.rq' \
                        or query_file == 'Count_Name_Prefixes.rq':
                    result = self.run_query_new(query_file_path.read(), endpoint)
                    report += result
                    echo(report, "blue")
                else:
                    result = self.run_query(query_file_path.read(), endpoint, query_file)
                    report += result
                    echo(report, "blue")

        return report

    def run_query(self, query, endpoint, query_file):
        """Query a SPARQL endpoint and return reportable results in text format.
        Keyword arguments:
        query -- a SPARQL query file on disk
        endpoint -- an open SPARQL endpoint
        query_file -- the SPARQL query file name
        """
        logging.info("Sending query %s", query_file)
        data = vivo_sparql_query(query, baseURL=endpoint)

        # WARNING (2019-04-04) [taeber] This looks like bad logic. By redefining
        # `report` with each header, only the last header actual determines what
        # gets returned.
        for var in data["head"]["vars"]:
            bindings = data["results"]["bindings"]
            num_errors = len(bindings)

            if num_errors == 0:
                report = "{0}\t\t{1}\n".format(num_errors,
                                               sparql_variable_rename(var))
                continue

            if num_errors == 1:
                if bindings[0][var.encode("ascii", "ignore")]["value"] == "0":
                    # Whenever a COUNT query returns 0, report no errors.
                    report = "{0}\t\t{1}\n".format(0, sparql_variable_rename(var))
                    continue

            report = "{0}\t\t{1}\n".format(num_errors, sparql_variable_rename(var))
            for error_record in bindings:
                error_value = error_record[var.encode('ascii', 'ignore')]["value"]
                # insert variable name and error value
                report += "\t\t\t{0}\n".format(error_value)

        return report

    def run_query_new(self, query, endpoint):
        """Query a SPARQL endpoint and return reportable results in text format.
        Modified for specific queries.
        Keyword arguments:
        query -- a SPARQL query file on disk
        endpoint -- an open SPARQL endpoint
        """
        result = ""
        data = vivo_sparql_query(query, baseURL=endpoint)
        # print data
        # if (not(any(data["results"]["bindings"])))
        if len(data["results"]["bindings"]) == 0:
            result = "0 \t\t" + (sparql_variable_rename(data["head"]["vars"][0])) + "\n"
            return result
        else:
            result += str(len(data["results"]["bindings"])/2) + " \
                " + (sparql_variable_rename(data["head"]["vars"][0])) + "\n"
            for var in data["head"]["vars"]:
                result += ("\t"+sparql_variable_rename(var)) + "\t\t\t"
            result += "\n"
            for item in data["results"]["bindings"]:
                for var in data["head"]["vars"]:
                    result += "\t" + item[var]["value"] + "\t"
                result += "\n"
            # print result
            return result
