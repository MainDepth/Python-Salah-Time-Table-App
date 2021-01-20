import requests
import json
from tkinter import messagebox


def getApi(country,city):
    try:
        # connects to server
        url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method={2}&school={1}"
        request = requests.get(url)
        api = json.loads(request.content)
        return api
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Connection Error", "make sure you are\n connected to the internet")

def getTimingsApi2(country, city):
    # fetched timings data
    timingsAPI = getApi(country, city)["data"]["timings"]
    return timingsAPI


def getDateApi(country, city):
    #fetches date information
    dateApi = getApi(country, city)["data"]["date"]
    return dateApi

def getSalahTimes(country,city):
    fajr = "Fajr: " + getTimingsApi2(country,city)['Fajr']
    sunrise = "Sunrise: " + getTimingsApi2(country,city)['Sunrise']
    zuhr = "Zuhr: " + getTimingsApi2(country,city)['Dhuhr']
    asr = "Asr: " + getTimingsApi2(country,city)['Asr']
    sunset = "Sunset: " + getTimingsApi2(country,city)['Sunset']
    maghrib = "Maghrib: " + getTimingsApi2(country,city)['Maghrib']
    eisha = "Eisha: " + getTimingsApi2(country,city)['Isha']
    midnight = "Midnight: " + getTimingsApi2(country,city)['Midnight']
    prayerList = [fajr, sunrise, zuhr, asr, sunset, maghrib, eisha, midnight]
    return prayerList


def getDate(country, city,calendar, language):
    WeekDay = getDateApi(country, city)[calendar]["weekday"][language]
    Day = getDateApi(country,city)[calendar]["day"]
    Month = getDateApi(country,city)[calendar]["month"][language]
    Year = getDateApi(country,city)[calendar]["year"]
    return f"{WeekDay} {Day} {Month} {Year}"



def createDateList(country, city):
    # gregorian calendar
    GregorianDate=getDate(country, city,"gregorian","en")

    # hijri calendar in arabic
    HijriDateAR=getDate(country, city,"hijri","ar")

    # hijri date in english
    HijriDateEN=getDate(country, city,"hijri","en")

    listOfDates=[GregorianDate,HijriDateAR,HijriDateEN]
    return listOfDates