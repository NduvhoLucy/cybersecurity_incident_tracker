class Incident:
    def __init__(self, title):
        self.title = title

class Report:
    def __init__(self, report_name):
        self.report_name = report_name

class ObjectFactory:
    @staticmethod
    def create_object(object_type, value):
        if object_type == "incident":
            return Incident(value)
        elif object_type == "report":
            return Report(value)
        else:
            raise ValueError(f"Unknown object type: {object_type}")

if __name__ == "__main__":
    factory = ObjectFactory()
    obj = factory.create_object("incident", "Unauthorized Access")
    print(obj.title)
