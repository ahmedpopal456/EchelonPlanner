class Preferences(object):

    daysOff = ""
    timeOfDay = []
    location = []

    def __init__(self, daysOff=None, timeOfDay=None, location = None):

        #TODO: make sure that what is received changes into the proper format as defined above!

        # string of days that the user wants off. ex.: "----FSD" wants a long weekend
        if daysOff is not None:
            self.daysOff = daysOff
        else:
            self.daysOff = "-------"
        # list of time slots that the user wants to have.
        # options are:
        #   "morning" before 12
        #   "afternoon" between 12 and 5
        #   "evening" after 5
        # ex.: ["morning", "evening"]
        # the user only wants courses before 12 and after 5
        if timeOfDay is not None:
            self.timeOfDay = timeOfDay
        else:
            self.timeOfDay = ["morning", "afternoon", "evening"]
        # list of locations that the user wants
        # can be "SGW", "LOY", "Online"
        if location is not None:
            self.location = location
        else:
            self.location = ["SGW", "LOY", "Online"]



    # """
    # method that creates a set of preferences
    # """
    # @staticmethod
    # def createPreferences(daysOff = "-------", timeOfDay = ["morning", "afternoon", "evening"], location = []):
    #     myPrefs = Preferences()
    #
    #
    #     myPrefs.daysOff = daysOff
    #     myPrefs.timeOfDay = timeOfDay
    #     myPrefs.location = location
    #
    #     return myPrefs