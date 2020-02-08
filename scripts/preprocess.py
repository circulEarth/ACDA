# scripts/preprocess.py

# TODO add license

import csv
import data
import pandas

def process_data():
    """
    Process MLO data and save it to TODO
    Process UC San Diego data and save it to TODO
    """

    with open('data/mlo_co2.csv', 'w') as mlo_csv_file:
        csvwriter = csv.writer(mlo_csv_file)

        csvwriter.writerow(['Year', 'Month', 'Day', 'Decimal Date', 'Carbon Dioxide (ppm)'])

        # Load unprocessed mlo_data
        with open('data/preprocessed_data/mlo.txt', 'r') as file:
            raw_data = file.readlines()[49:]
            
            for row in raw_data:
                data = row.split()
                year = data[0]
                month = data[1]
                day = data[2]
                decimal = data[3] 
                ppm = data[4] if float(data[4]) != -999.99 else ''
                
                csvwriter.writerow([year, month, day, decimal, ppm])

    with open('data/ucsd_co2.csv', 'w') as ucsd_csv_file:
        csvwriter = csv.writer(ucsd_csv_file)

        csvwriter.writerow(['Year', 'Month', 'Decimal Date', 'Carbon Dioxide (ppm)'])
        
        # Load unprocessed ucsd data
        ucsd = pandas.read_csv('data/preprocessed_data/carbon-dioxide.csv')

        # Drop extra data
        ucsd.drop(['Seasonally Adjusted CO2 (ppm)', 'Carbon Dioxide Fit (ppm)', 
                    'Seasonally Adjusted CO2 Fit (ppm)'], axis=1)

        ucsd.to_csv(ucsd_csv_file, sep=',')


def pull_current():

    """
    Pull the most recent version of MLO data and 
     save it to XXX
    """

    pass
