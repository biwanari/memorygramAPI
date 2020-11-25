import pandas as pd

class Target:

    _dataProfileDict = {}

    def __init__(self, profileName, ide = None):
        self.profileName = profileName
        self.ide = ide

    def fillDictTarget(self, profileTarget = []):
        """
        Input = except a list of profile for one or more profile
        fill target profile with nameProfile as key and a list of possible handle
        data manipulation i.e. { "profilename" : [profile, followers, following, .....] }
        After setted target profile name, use list to invoke instance of class i.e. 
        Profile() has __class()__ for profile option in list...
        """
        if profileTarget != None:
            for i in range(len(profileTarget)):
                _dataProfileDict[profileTarget[i]] = [ 'Profile','ide','follower','following' ]
        
    def addOption(self,profile, nextOption):
        """
        Input: add option to target profile key in dict
        _dataProfileDict
        First select profile memorize as key, and digit nextOption as one option per time
        """
        if profile in d.keys():
            _dataProfileDict[profile].append(nextOption)
        
    def printDataDict(self):
        """
        print all information on target and equivalent option on itself
        into a printing and readable format
        """
        for k, v     in _dataProfileDict:
            print(f"""Profile: { k } 
                      Options: { v }  \n""")
    def createCsv(self):
        """
        Create a csv file with profile target and relative options.
        """
        pass