from stix2 import CustomObject, properties

allowed_anomaly_class = ["excessive permissions", "missing permissions", "segregation of duty"]

@CustomObject('x-anomaly', [
    ('anomaly_class', properties.StringProperty(required=True)),
    ('roles', properties.ListProperty(properties.StringProperty(required=False))),
    ('permissions', properties.ListProperty(properties.StringProperty(required=False)))
])
class Anomaly(object):
    def __init__(self, anomaly_class=None, **kwargs):
         if anomaly_class and anomaly_class not in allowed_anomaly_class:
            raise ValueError("'%s' is not a recognized class of anomaly." % anomaly_class)



class AnomalyParser:
    def parseExcessive(roles, permissions):
        anomaly = Anomaly(anomaly_class="excessive permissions",
                          roles=roles,
                          permissions=permissions)
        return anomaly

    def parseMissing(roles, permissions):
        anomaly = Anomaly(anomaly_class="missing permissions",
                          roles=roles,
                          permissions=permissions)
        return anomaly

    def parseSegregation(roles, permissions):
        anomaly = Anomaly(anomaly_class="segregation of duty",
                          roles=roles,
                          permissions=permissions)
        return anomaly

