#!/usr/bin/env python

import os
import sys
import subprocess
import git
import csv
import datetime


def main(argv):

    print "Begin process at " + str(datetime.datetime.now())
    ##call ls to have all the files '.gz' : ls | grep ".gz"
    subprocess.call('ls | grep ".gz" > all_files.txt', shell=True)
    all_tgz_files = open('all_files.txt','r')
    ##create csv header
    with open('result_search_bad_tag.csv', 'w') as csvfile:
        result_writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        result_writer.writerow(['Mm Day', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'])

    with open('result_search_white_spaces.csv', 'w') as csvfile:
        result_writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        result_writer.writerow(['Mm Day', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'])

    for tgz_file in all_tgz_files:
        file_bad_tag = "file_bad_tag.txt"
        error_bad_tag = 'zgrep "faultString: org.xml.sax.SAXException: Bad envelope tag:  html" '+tgz_file.strip()+' > '+file_bad_tag
        filterErrors(tgz_file.strip(), error_bad_tag, file_bad_tag, 'result_search_bad_tag.csv')

        file_white_spaces = "file_white_spaces.txt"
        error_white_spaces = 'zgrep "faultString: org.xml.sax.SAXParseException: White spaces are required between publicId and systemId." '+tgz_file.strip()+' > '+file_white_spaces
        filterErrors(tgz_file.strip(), error_white_spaces, file_white_spaces, 'result_search_white_spaces.csv')

    all_tgz_files.close()
    subprocess.call('rm all_files.txt', shell=True)
    print "End process at " + str(datetime.datetime.now())

def filterErrors(tgz_file, processs_to_call, file_to_process, csv_to_open):
    dict_of_days_hours = {}
    list_horaires_jours = [0]*24
    subprocess.call(processs_to_call, shell=True)
    output_file = open(file_to_process,'r')
    list_agg = list()
    previous_date = ""
    for line in output_file:
        heure = ""
        if line.split(' ')[1] == "":
            heure = line.split(' ')[3].split(':')[0]
        else:
            heure = line.split(' ')[2].split(':')[0]
        if len(list_agg) == 0 or heure in list_agg:
            list_agg.append(heure)
        else:
            list_horaires_jours[int(list_agg[0])] = len(list_agg)
            list_agg = list()
            list_agg.append(heure)
        now_date = ""
        if line.split(' ')[1] == "":
            now_date = line.split(' ')[0] + " " +line.split(' ')[2]
        else:
            now_date = line.split(' ')[0] + " " +line.split(' ')[1]
        if previous_date == "" or not now_date in previous_date:
            previous_date = now_date
            list_horaires_jours = [0]*24
            dict_of_days_hours[now_date] = list_horaires_jours
    output_file.close()
    subprocess.call('rm '+file_to_process, shell=True)

    if len(list_agg) != 0:
        list_horaires_jours[int(list_agg[0])] = len(list_agg)
        dict_of_days_hours[now_date] = list_horaires_jours

    for key in dict_of_days_hours:
        if "Sep" in key or "May" in key or "Apr" in key:
            print tgz_file
            print key
            print dict_of_days_hours.get(key)

    with open(csv_to_open, 'a') as csvfile:
        result_writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for key in dict_of_days_hours:
            result_writer.writerow([key, dict_of_days_hours.get(key)[0], dict_of_days_hours.get(key)[1], dict_of_days_hours.get(key)[2], dict_of_days_hours.get(key)[3], dict_of_days_hours.get(key)[4], dict_of_days_hours.get(key)[5], dict_of_days_hours.get(key)[6], dict_of_days_hours.get(key)[7], dict_of_days_hours.get(key)[8], dict_of_days_hours.get(key)[9], dict_of_days_hours.get(key)[10], dict_of_days_hours.get(key)[11], dict_of_days_hours.get(key)[12], dict_of_days_hours.get(key)[13], dict_of_days_hours.get(key)[14], dict_of_days_hours.get(key)[15], dict_of_days_hours.get(key)[16], dict_of_days_hours.get(key)[17], dict_of_days_hours.get(key)[18], dict_of_days_hours.get(key)[19],dict_of_days_hours.get(key)[20], dict_of_days_hours.get(key)[21], dict_of_days_hours.get(key)[22], dict_of_days_hours.get(key)[23]])


if __name__ == "__main__":
    main(sys.argv[1:])