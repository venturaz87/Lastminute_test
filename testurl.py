import json
import requests
import time
import datetime
import calendar
import csv

from datetime import timedelta, date

#Define function to increment the date day by day
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#Define start date and end date of your analysis
start_date = datetime.date(2016, 10, 16) #year,month,day
end_date = datetime.date(2016, 10, 17)

#Define a txt and a csv file where to store the variables of ALL the days
f_append = open('data_facebook_INCLUSIVE.txt','a')
c = csv.writer(open("data_facebook_EXCEL2.csv", "wb"), delimiter= "\t")

#Start the loop over the days
for single_date in daterange(start_date, end_date):

    #Convert datetime objects to strings (day, dayafter, end date)
    start_date_conv = single_date.strftime('%d/%m/%Y')
    dayafter_date_conv = (single_date + timedelta(1)).strftime('%d/%m/%Y')
    end_date_conv = end_date.strftime('%d/%m/%Y')

    #Convert dates to UNIX format
    input_date = str(calendar.timegm(time.strptime(start_date_conv, '%d/%m/%Y')))
    output_date = str(calendar.timegm(time.strptime(dayafter_date_conv, '%d/%m/%Y')))

    #Check the dates
    print(input_date, start_date_conv, output_date, dayafter_date_conv)

    #Open the URL containing your data
    url = 'https://graph.facebook.com/v2.7/10153077189041726/order_id_attributions?access_token=CAAHzp28RZAqUBAEzBVrNrdRkHc4qhOHedNjMp0HoFtXoI3zl7q3wUyp2r8QiihfZB76pm0AbZCwDhzq26SheZBbiIyCvHbMqdZAiJPwFJYwMTb10WIDSh6r1XA43AYLwvGB6ZAhAXzsqLvp7tBTLfSkZCvlgrTFSTenNGPlJ2FBwXjHoyOCVWPuufeJfrS8HbwZD&since='+input_date+'&until='+output_date+'&pixel_id=1072729222753588&fields=order_id&limit=2000'

    #Print the URL as a check
    print(url)
    data = requests.get(url)
    data.json()

    #Extract the values from the web as a json file and write them in a file
    with open('facebookWeb_'+input_date+'_'+output_date+'.json', 'w') as out_f:
        out_f.write(data.text)
    out_f.close()

    #Load the json file in python
    with open('facebookWeb_'+input_date+'_'+output_date+'.json') as data_json:
        data = json.load(data_json)
    #data_json.close()

    #Create a new file where to store the results on a DAYLY basis
    f = open('data_facebook_'+input_date+'_'+output_date+'.txt','w')

    #Loop over the length of the sample and get the variables you need
    d = data["data"]

    for i in range(len(d)):

        #Write on txt (day by day and inclusive) and csv (inclusive)
        f.write(d[i]["order_id"] + "\t" + "\n")
        f_append.write(d[i]["order_id"] + "\t" + "\n")
        c.writerow(d[i]["order_id"])
    #Close the files
    f.close()
f_append.close()
