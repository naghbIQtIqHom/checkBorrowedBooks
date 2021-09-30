# -*- coding: utf-8 -*-

from musashino import MusashinoLibrary
from suginami import SuginamiLibrary
from nerima import NerimaLibrary

from secret import accountData
from urlData import libraryUrl
from speakStatus import speakStatus
from options import parseOption
import sys

def checkLendAndReservedBooks(name, data, user, password):
    library = eval(data["class"])(data["url"], user, password)
    library.setUp()
    library.login()
    rents = library.rentlist()
    reserves = library.reserveBooks()
    library.logout()
    library.tearDown()
    return rents, reserves

def speakCurrentStatus(name, rentData):
    rents = rentData[name]['rents']
    reserves = rentData[name]['reserves']
    narrator = speakStatus()
    narrator.rentBooks(name, rents)
    narrator.reserveBooks(name, reserves)
    narrator.endThatsit(name)

def getRentAndReserveData(name, data):
    rents = {}
    reserves = {}
    try:
        user = accountData[name]["user"]
        password = accountData[name]["password"]
        rents, reserves = checkLendAndReservedBooks(name, data, user, password)
    except Exception as e:
        tb = sys.exc_info()[2]
        print("{0} で何かエラー\n{1}\n{2}\n{3}".format(name, e.with_traceback(tb),sys.exc_info()[0],sys.exc_info()[1]))
    return rents, reserves

def getAllRentBooksFromAllLibrary(libraris):
    rentData = {}
    for name in libraries:
        if name in libraryUrl.keys():
            print("=== {0} ===".format(name))
            data = libraryUrl[name]
            rents, reserves = getRentAndReserveData(name, data)
            rentData[name] = { 'rents' : rents, 'reserves' : reserves }
    return rentData

if __name__ == "__main__":
    (options, args) = parseOption()

    rentData = {}
    if options.librarylist == "all":
        libraries = libraryUrl.keys()
        rents = getAllRentBooksFromAllLibrary(libraries)
        rentData.update(rents)
    else:
        libraries = [x.strip() for x in options.librarylist.split(',')]
        rents = getAllRentBooksFromAllLibrary(libraries)
        rentData.update(rents)

    if not options.silence:
        if options.librarylist == "all":
            libraries = libraryUrl.keys()
            for name in libraries:
                speakCurrentStatus(name, rentData)
        else:
            libraries = [x.strip() for x in options.librarylist.split(',')]
            for name in libraries:
                speakCurrentStatus(name, rentData)
