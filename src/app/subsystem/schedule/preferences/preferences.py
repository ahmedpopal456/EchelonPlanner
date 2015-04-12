class Preferences(object):

    def __init__(self):
        # string of days that the user wants off. ex.: "----FSD" wants a long weeked
        self.daysOff = None
        # list of time slots that the user wants to have.
        # options are:
        #   "morning" before 12
        #   "afternoon" between 12 and 5
        #   "evening" after 5
        # ex.: ["morning", "evening"]
        # the user only wants courses before 12 and after 5
        self.timeOfDay = None
        # list of locations that the user wants
        # can be "SGW", "LOY", "Online"
        self.location = None


    """
    method that creates a set of preferences
    """
    @staticmethod
    def createPreferences(daysOff = "MTWJFSD", timeOfDay = [], location = []):
        myPrefs = Preferences()

        #TODO: make sure that what is received changes into the proper format as defined above!
        myPrefs.daysOff = daysOff
        myPrefs.timeOfDay = timeOfDay
        myPrefs.location = location

        return myPrefs