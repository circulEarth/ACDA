# scripts/preprocess.py

# TODO add license
# TODO add credit to ESRL

import csv
import data
import pandas

def process_all_data():
    process_mlo_data()
    process_uc_san_diego_data()
    # process_global_data()


def process_mlo_data():

    """
    Process data collected by the Earth Science Research Laboratory
        https://www.esrl.noaa.gov/gmd/ccgg/trends/data.html
    Data collected from the Mauna Loa Observatory in Mauna Loa, Hawaii

    Takes data in co2_weekly_mlo.txt and converts it into a CSV
    """

    with open('data/mlo_co2.csv', 'w') as mlo_csv_file:
        csvwriter = csv.writer(mlo_csv_file)

        csvwriter.writerow(['Year', 'Month', 'Day', 'Decimal Date', 'Carbon Dioxide (ppm)'])

        # Load unprocessed mlo_data
        with open('data/preprocessed_data/co2_weekly_mlo.txt', 'r') as file:
            raw_data = file.readlines()[49:]
            
            for row in raw_data:
                data = row.split()
                year = data[0]
                month = data[1]
                day = data[2]
                decimal = data[3] 
                ppm = data[4] if float(data[4]) != -999.99 else ''
                
                csvwriter.writerow([year, month, day, decimal, ppm])


def process_uc_san_diego_data():
    with open('data/ucsd_co2.csv', 'w') as ucsd_csv_file:
        csvwriter = csv.writer(ucsd_csv_file)

        csvwriter.writerow(['Year', 'Month', 'Decimal Date', 'Carbon Dioxide (ppm)'])
        
        # Load unprocessed ucsd data
        ucsd = pandas.read_csv('data/preprocessed_data/CarbonDioxide.csv')

        # Drop extra data
        ucsd.drop(['Seasonally Adjusted CO2 (ppm)', 'Carbon Dioxide Fit (ppm)', 
                    'Seasonally Adjusted CO2 Fit (ppm)'], axis=1)

        ucsd.to_csv(ucsd_csv_file, sep=',')


def fetch_current_mlo():

    """
    Pull the most recent version of MLO data and 
     save it to XXX
    """

    pass

def fetch_current_global():

    """
    Pull the most recent version of MLO data and 
     save it to XXX
    """

    pass
