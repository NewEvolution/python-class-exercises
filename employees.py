class Company(object):

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def getStartDate(self):
        return self.start_date
