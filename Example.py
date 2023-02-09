from Anomaly_Parser import AnomalyParser

if __name__ == '__main__':

    print(AnomalyParser.parseExcessive(["employee"], ["HR data"]).serialize(pretty=True))
    print(AnomalyParser.parseMissing(["employee"], ["employee data"]).serialize(pretty=True))
    print(AnomalyParser.parseSegregation(["employee"], ["grant loan", "apply for loan"]).serialize(pretty=True))
