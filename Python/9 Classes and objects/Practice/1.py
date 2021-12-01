# create class programmer for storing information of programmers working at Microsoft


class Programmer:
    company = "Microsoft"

    def __init__(self, name, work):
        self.name = name
        self.work = work

    def getInfo(self):
        print(f"Name of programmer is {self.name} working on {self.work} in {self.company} ")


deep = Programmer("Deep", "GitHub")
harsh = Programmer("Harsh", "Salesforce")

deep.getInfo()
harsh.getInfo()
