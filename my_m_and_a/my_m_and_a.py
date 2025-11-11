import pandas as pd
import io
from enum import Enum
import re
from datetime import datetime

"""
Database schema

"gender" - 'string'
"firstname" - 'string', extract, all have, 2nd have to split
"Lastname" - 'string', extract, all have
"email" - 'string', extract, all have
"age" - 'string', all have
"city" - 'string', all have
"country" - 'string', they are ALL from the US
"created_at" - 'string', db thingy
"referral" - 'string', which company
"""

class Cols(Enum):
    gender = 'Gender'
    firstName = 'FirstName'
    lastName = 'LastName'
    email = 'Email'
    age = 'Age'
    city = 'City'
    country = 'Country'
    created_at = 'created_at'
    referral = 'referral'

db_rows = [col.value for col in Cols]
# db_rows = [Cols.gender, Cols.firstName, Cols.lastName, Cols.email, Cols.age, Cols.city, Cols.country, Cols.created_at, Cols.referral]

def clean_name(name):
    if not isinstance(name, str):
        return name
    name_quotes = name.replace('\\', '').replace('"', '')
    name_final = '\''.join([str.capitalize(part) for part in name_quotes.split('\'')])
    return name_final

def clean_email(email):
    if not isinstance(email, str):
        return email
    email_quotes = email.replace('\\"', '').replace('"', '')
    email_final = str.lower(email_quotes)
    return email_final

def clean_city(city):
    if not isinstance(city, str):
        return city
    city_parts = re.split('[_ -]', city)
    city_parts = [str.capitalize(part) for part in city_parts]
    city_final = ' '.join(city_parts)
    return city_final



def standardize_df1(df1: pd.DataFrame):

    df_dict = df1.to_dict('records')
    df_standard_list = []

    gender_table = {
        'Female': 'Female',
        'Male': 'Male',
        'F': 'Female',
        'M': 'Male',
        '1': 'Female',
        '0': 'Male'
    }

    for entry in df_dict:
        new_row = {key: '' for key in db_rows}

        entry_gender = gender_table[entry['Gender']]
        new_row[Cols.gender.value] = entry_gender

        if not pd.isna(entry['FirstName']):
            entry_firstname = clean_name(entry['FirstName'])
        else:
            entry_firstname = 'Nan'
        new_row[Cols.firstName.value] = entry_firstname

        entry_lastname = clean_name(entry['LastName'])
        new_row[Cols.lastName.value] = entry_lastname

        if entry['Email'] != 'forgottoask@woodinc':
            entry_email = clean_email(entry['Email'])
        else:
            entry_email = None
        new_row[Cols.email.value] = entry_email

        entry_age = str(entry['Age'])
        new_row[Cols.age.value] = entry_age

        entry_city = clean_city(entry['City'])
        new_row[Cols.city.value] = entry_city

        entry_country = 'United States of America'
        new_row[Cols.country.value] = entry_country

        entry_created_at = str(datetime.now())
        new_row[Cols.created_at.value] = entry_created_at

        entry_referral = 'Customer 1'
        new_row[Cols.referral.value] = entry_referral

        df_standard_list.append(new_row)

    df_standard = pd.DataFrame(df_standard_list)
    return df_standard

def standardize_df2(df2: pd.DataFrame):

    df_dict = df2.to_dict('records')
    df_standard_list = []

    gender_table = {
        'Female': 'Female',
        'Male': 'Male',
        'F': 'Female',
        'M': 'Male',
        '1': 'Female',
        '0': 'Male'
    }

    for entry in df_dict:
        new_row = {key: '' for key in db_rows}

        entry_gender = gender_table[entry[2]]
        new_row[Cols.gender.value] = entry_gender

        entry_firstname, entry_lastname = entry[3].split(' ', maxsplit=1)
        new_row[Cols.firstName.value] = clean_name(entry_firstname)
        new_row[Cols.lastName.value] = clean_name(entry_lastname)

        if not pd.isna(entry[4]):
            entry_email = clean_email(entry[4])
        else:
            entry_email = None
        new_row[Cols.email.value] = entry_email

        age_str = str(entry[0]).replace('"', '').replace('years', '').replace('year', '').replace('yo', '')
        entry_age = age_str[:2]
        new_row[Cols.age.value] = entry_age

        entry_city = clean_city(entry[1])
        new_row[Cols.city.value] = entry_city

        entry_country = 'United States of America'
        new_row[Cols.country.value] = entry_country

        entry_created_at = str(datetime.now())
        new_row[Cols.created_at.value] = entry_created_at

        entry_referral = 'Customer 2'
        new_row[Cols.referral.value] = entry_referral

        df_standard_list.append(new_row)

    df_standard = pd.DataFrame(df_standard_list)
    return df_standard

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def standardize_df3(df3: pd.DataFrame):

    # Preparations
    df_dict = df3.to_dict('records')
    df_standard_list = []

    gender_table = {
        'Female': 'Female',
        'Male': 'Male',
        'F': 'Female',
        'M': 'Male',
        '1': 'Female',
        '0': 'Male'
    }
    for entry in df_dict:
        new_row = {key: '' for key in db_rows}
        
        entry_gender = gender_table[entry['Gender'].split('_', 1)[1]]
        new_row[Cols.gender.value] = entry_gender

        entry_firstname, entry_lastname = remove_prefix(entry['Name'], 'string_').split(' ', maxsplit=1)
        new_row[Cols.firstName.value] = clean_name(entry_firstname)
        new_row[Cols.lastName.value] = clean_name(entry_lastname)

        if not pd.isna(entry['Email']):
            entry_email = clean_email(remove_prefix(entry['Email'], 'string_'))
        else:
            entry_email = None
        new_row[Cols.email.value] = entry_email

        entry_age = str(remove_prefix(entry['Age'].replace('"', ''), 'integer_').replace('years', '').replace('year', '').replace('yo', ''))[:2]
        new_row[Cols.age.value] = entry_age

        entry_city = clean_city(remove_prefix(entry['City'], 'string_'))
        new_row[Cols.city.value] = entry_city

        entry_country = 'United States of America'
        new_row[Cols.country.value] = entry_country

        entry_created_at = str(datetime.now())
        new_row[Cols.created_at.value] = entry_created_at

        entry_referral = 'Customer 3'
        new_row[Cols.referral.value] = entry_referral

        df_standard_list.append(new_row)

    df_standard = pd.DataFrame(df_standard_list)
    return df_standard



def my_m_and_a(content_database_1, content_database_2, content_database_3):
    df1 = pd.read_csv(content_database_1)
    df2 = pd.read_csv(content_database_2, sep=';', header=None)
    df3 = pd.read_csv(content_database_3, sep='\t', skiprows=1, header=None)
    df3.columns = ['Gender','Name','Email','Age','City','Country']

    df1_st = standardize_df1(df1)
    df2_st = standardize_df2(df2)
    df3_st = standardize_df3(df3)

    df_merged = pd.concat([df1_st, df2_st, df3_st], ignore_index=True)

    return df_merged


# with open('only_wood_customer_us_1.csv', 'r', encoding='utf-8') as f:
#     content_database_1 = f.read()
# with open('only_wood_customer_us_2.csv', 'r', encoding='utf-8') as f:
#     content_database_2 = f.read()  
# with open('only_wood_customer_us_3.csv', 'r', encoding='utf-8') as f:
#     content_database_3 = f.read()
    
# merged_csv = my_m_and_a(content_database_1, content_database_2, content_database_3)

# from my_ds_babel import csv_to_sql

# csv_to_sql(merged_csv, 'plastic_free_boutique.sql', 'customers')