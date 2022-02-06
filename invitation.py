# dictionary of countries with list of country data as value
# each list will have a person dictionary with relevent information

import requests

unfiltered_data = requests.get(f'https://ct-mock-tech-assessment.herokuapp.com/').json()

data_list = []
for info in unfiltered_data['partners']:
    data_list.append(info)

class Conference:
    def __init__(self):
        pass
    # Get a list of countries in the conference
    def countries():
        country_list = []
        for country in data_list:
            if country['country']:
                country_list.append(country['country'])
        return set(country_list)
    c_list = list(countries())

    # List comprehension to get data for specific country
    # list of attendees for USA
    us_attendees = list([x for x in data_list if x['country'] == 'United States'])
    # list of attendees for Ireland
    ireland_attendees = list([x for x in data_list if x['country'] == 'Ireland'])
    # list of attendees for Spain
    spain_attendees = list([x for x in data_list if x['country'] == 'Spain'])
    # list of attendees for Mexico
    mexico_attendees = list([x for x in data_list if x['country'] == 'Mexico'])
    # list of attendees for Canada
    canada_attendees = list([x for x in data_list if x['country'] == 'Canada'])
    # list of attendees for Singapore
    singapore_attendees = list([x for x in data_list if x['country'] == 'Singapore'])
    # list of attendees for Japan
    japan_attendees = list([x for x in data_list if x['country'] == 'Japan'])
    # list of attendees for United Kingdom
    uk_attendees = list([x for x in data_list if x['country'] == 'United Kingdom'])
    # list of attendees for France
    france_attendees = list([x for x in data_list if x['country'] == 'France'])
    
    # Create a list containing attendees from all countries 
    list_of_all_attendees = [us_attendees,ireland_attendees,spain_attendees,mexico_attendees,canada_attendees,singapore_attendees,japan_attendees,uk_attendees,france_attendees]

    # Get the date that is most common from the list of dates for a country
    def get_dates(list_of_dates):
        # Create an empty list to store dates for each country
        usa_dates, ireland_dates, spain_dates, mexico_dates, canada_dates, singapore_dates, japan_dates, uk_dates, france_dates = [],[],[],[],[],[],[],[],[]
        
        for dates in list_of_dates:
            if(dates['country'] == 'United States'):
                usa_dates.append(dates['availableDates'])
                common_date_list = [el for sublist in usa_dates for el in sublist]
                us_best_date = max(common_date_list, key=common_date_list.count)
            if(dates['country'] == 'Ireland'):
                ireland_dates.append(dates['availableDates'])
                common_date_list = [el for sublist in ireland_dates for el in sublist]
                ireland_best_date = max(common_date_list, key=common_date_list.count)
            if(dates['country'] == 'Spain'):
                spain_dates.append(dates['availableDates'])
                common_date_list = [el for sublist in spain_dates for el in sublist]
                spain_best_date = max(common_date_list, key=common_date_list.count)
            if(dates['country'] == 'Mexico'):
                mexico_dates.append(dates['availableDates'])
                common_date_list = [el for sublist in mexico_dates for el in sublist]
                mexico_best_date = max(common_date_list, key=common_date_list.count)
            if(dates['country'] == 'Canada'):
                canada_dates.append(dates['availableDates'])
                common_date_list = [el for sublist in canada_dates for el in sublist]
                canada_best_date = max(common_date_list, key=common_date_list.count)
            if(dates['country'] == 'Singapore'):
                singapore_dates.append(dates['availableDates'])
                common_date_list = [el for sublist in singapore_dates for el in sublist]
                singapore_best_date = max(common_date_list, key=common_date_list.count)
            if(dates['country'] == 'Japan'):
                japan_dates.append(dates['availableDates'])
                common_date_list = [el for sublist in japan_dates for el in sublist]
                japan_best_date = max(common_date_list, key=common_date_list.count)
            if(dates['country'] == 'United Kingdom'):
                uk_dates.append(dates['availableDates'])
                common_date_list = [el for sublist in uk_dates for el in sublist]
                uk_best_date = max(common_date_list, key=common_date_list.count)
            if(dates['country'] == 'France'):
                france_dates.append(dates['availableDates'])
                common_date_list = [el for sublist in france_dates for el in sublist]
                france_best_date = max(common_date_list, key=common_date_list.count)

        # print(f'US: {us_best_date}, Ireland: {ireland_best_date}, Spain: {spain_best_date}, Mexico: {mexico_best_date}, Canada: {canada_best_date}, Singapore: {singapore_best_date}, Japan: {japan_best_date}, UK: {uk_best_date}, France: {france_best_date}')
        all_dates = []
        all_dates.append(('United States',us_best_date)), all_dates.append(('Ireland',ireland_best_date)), all_dates.append(('Spain',spain_best_date)), 
        all_dates.append(('Mexico',mexico_best_date)), all_dates.append(('Canada',canada_best_date)), all_dates.append(('Singapore',singapore_best_date)), 
        all_dates.append(('Japan',japan_best_date)), all_dates.append(('United Kingdom',uk_best_date)), all_dates.append(('France',france_best_date))
        return(all_dates)

    #  Get the best date for each country
    best_date = get_dates(data_list)

    # Get list of people who can attend the meeting for the best date across available date
    us_emails,ireland_emails,spain_emails,mexico_emails,canada_emails,singapore_emails,japan_emails,uk_emails,france_emails = [],[],[],[],[],[],[],[],[]
    for country in c_list:
        if country == 'United States':
            for person in us_attendees:
                if best_date[0][1] in person['availableDates']:
                    us_emails.append(person['email'])
        if country == 'Ireland':
            for person in ireland_attendees:
                if best_date[1][1] in person['availableDates']:
                    ireland_emails.append(person['email'])
        if country == 'Spain':
            for person in spain_attendees:
                if best_date[2][1] in person['availableDates']:
                    spain_emails.append(person['email'])
        if country == 'Mexico':
            for person in mexico_attendees:
                if best_date[3][1] in person['availableDates']:
                    mexico_emails.append(person['email'])
        if country == 'Canada':
            for person in canada_attendees:
                if best_date[4][1] in person['availableDates']:
                    canada_emails.append(person['email'])
        if country == 'Singapore':
            for person in singapore_attendees:
                if best_date[5][1] in person['availableDates']:
                    singapore_emails.append(person['email'])
        if country == 'Japan':
            for person in japan_attendees:
                if best_date[6][1] in person['availableDates']:
                    japan_emails.append(person['email'])
        if country == 'United Kingdom':
            for person in uk_attendees:
                if best_date[7][1] in person['availableDates']:
                    uk_emails.append(person['email'])
        if country == 'France':
            for person in france_attendees:
                if best_date[8][1] in person['availableDates']:
                    france_emails.append(person['email'])
    
    us_attendee_count = len(us_emails)
    ireland_attendee_count = len(ireland_emails)
    spain_attendee_count = len(spain_emails)
    mexico_attendee_count = len(mexico_emails)
    canada_attendee_count = len(canada_emails)
    singapore_attendee_count = len(singapore_emails)
    japan_attendee_count = len(japan_emails)
    uk_attendee_count = len(uk_emails)
    france_attendee_count = len(france_emails)

    # Creating dictionary of people who can attend meeting for each country
    usa_attendee_dict = {'United States': {'start_date': best_date[0][1], 'attendee_count': us_attendee_count, 'attendees': us_emails}}
    ireland_attendee_dict = {'Ireland': {'start_date': best_date[1][1], 'attendee_count': ireland_attendee_count, 'attendees': ireland_emails}}
    spain_attendee_dict = {'Spain': {'start_date': best_date[2][1], 'attendee_count': spain_attendee_count, 'attendees': spain_emails}}
    mexico_attendee_dict = {'Mexico': {'start_date': best_date[3][1], 'attendee_count': mexico_attendee_count, 'attendees': mexico_emails}}
    canada_attendee_dict = {'Canada': {'start_date': best_date[4][1], 'attendee_count': canada_attendee_count, 'attendees': canada_emails}}
    singapore_attendee_dict = {'Singapore': {'start_date': best_date[5][1], 'attendee_count': singapore_attendee_count, 'attendees': singapore_emails}}
    japan_attendee_dict = {'Japan': {'start_date': best_date[6][1], 'attendee_count': japan_attendee_count, 'attendees': japan_emails}}
    uk_attendee_dict = {'United Kingdom': {'start_date': best_date[7][1], 'attendee_count': uk_attendee_count, 'attendees': uk_emails}}
    france_attendee_dict = {'France': {'start_date': best_date[8][1], 'attendee_count': france_attendee_count, 'attendees': france_emails}}

    # Create a new dictionary and add country dictionaries
    country_dict_list = [usa_attendee_dict, ireland_attendee_dict, spain_attendee_dict, mexico_attendee_dict, canada_attendee_dict, singapore_attendee_dict, japan_attendee_dict, uk_attendee_dict, france_attendee_dict]
    sorted_dict = {}
    for i in country_dict_list:
        def update_dict(d, x):
            d.update({key:value for key, value in x.items() if key not in d})
        update_dict(sorted_dict, i)

    # Create a post request
    @classmethod
    def send_post(info_to_post):
        url = f'https://ct-mock-tech-assessment.herokuapp.com/'
        try:
            response = requests.post(url, data={'data': info_to_post})
            if response:
                print(response)
                print(response.text)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(" = "*100)
            print(e)
            print(" = "*100)
            print(" ~~> Please make sure you're sending the request to correct URL ")

class Run():
    Conference.send_post()