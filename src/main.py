# -*- coding: utf-8 -*-

from musashino import MusashinoLibrary
from suginami import SuginamiLibrary
from secret import accountData
from urlData import libraryUrl
from speakStatus import speakStatus
import sys

def checkLendAndReservedBooks(name, data, user, password):
    library = eval(data["class"])(data["url"], user, password)
    library.setUp()
    library.login()
    rents = library.rentlist()
    reserves = library.reserveBooks()
    library.logout()
    library.tearDown()

    narrator = speakStatus()
    narrator.rentBooks(name, rents)
    narrator.reserveBooks(name, reserves)
    narrator.endThatsit(name)

if __name__ == "__main__":
    for name,data in libraryUrl.items():
        try:
            user = accountData[name]["user"]
            password = accountData[name]["password"]
            checkLendAndReservedBooks(name, data, user, password)
        except Exception as e:
            tb = sys.exc_info()[2]
            print("{0} で何かエラー\n{1}".format(name, e.with_traceback(tb)))
