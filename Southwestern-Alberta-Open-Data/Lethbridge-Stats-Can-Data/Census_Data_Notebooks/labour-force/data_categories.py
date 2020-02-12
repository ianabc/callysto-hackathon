import pandas as pd
from ipywidgets import widgets, VBox, HBox, Button
from ipywidgets import Button, Layout, widgets
from IPython.display import display, Javascript, Markdown, HTML
import matplotlib.pyplot as plt
import zipfile
from io import BytesIO
from urllib.request import urlopen
import os, sys

#load "cufflinks" library under short name "cf"
import cufflinks as cf

#command to display graphics correctly in Jupyter notebook
cf.go_offline()

"""Override RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility """
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

"""Pandas settings""" 
pd.set_option('display.max_rows', 800)
pd.set_option('display.max_columns', 800)

# Fancy user interface to explore datasets
def rerun_cell( b ):
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,IPython.notebook.get_selected_index()+3)'))    

    
def run_4cell( b ):
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,IPython.notebook.get_selected_index()+5)'))    

style = {'description_width': 'initial'}


#**** DATA SUBSETS *****#
# Age data
age_data = [
'Total - Age groups and average age of the population - 100% data',
 '0 to 14 years',
 '0 to 4 years',
 '5 to 9 years',
 '10 to 14 years',
 '15 to 64 years',
 '15 to 19 years',
 '20 to 24 years',
 '25 to 29 years',
 '30 to 34 years',
 '35 to 39 years',
 '40 to 44 years',
 '45 to 49 years',
 '50 to 54 years',
 '55 to 59 years',
 '60 to 64 years',
 '65 years and over',
 '65 to 69 years',
 '70 to 74 years',
 '75 to 79 years',
 '80 to 84 years',
 '85 years and over',
 '85 to 89 years',
 '90 to 94 years',
 '95 to 99 years',
 '100 years and over']

age_distribution = [
 'Total - Distribution (%) of the population by broad age groups - 100% data',
 '0 to 14 years',
 '15 to 64 years',
 '65 years and over',
 '85 years and over',
 'Average age of the population',
 'Median age of the population'
]

# House size
house_data = [
'Total - Private households by household size - 100% data',
 '1 person',
 '2 persons',
 '3 persons',
 '4 persons',
 '5 or more persons',
 'Number of persons in private households',
 'Average household size'
]

# Marital status
marital_data = [
'Total - Marital status for the population aged 15 years and over - 100% data',
 'Married or living common law',
 'Married',
 'Living common law',
 'Not married and not living common law',
 'Never married',
 'Separated',
 'Divorced',
 'Widowed'
]

# Languages
languages_data =[
'Total - Knowledge of official languages for the total population excluding institutional residents - 100% data',
 'English only',
 'French only',
 'English and French',
 'Neither English nor French']

first_official_language_data=[
 'Total - First official language spoken for the total population excluding institutional residents - 100% data',
 'English',
 'French',
 'English and French',
 'Neither English nor French',
 'Official language minority (number)',
 'Official language minority (percentage)']


mother_tongue_data = [
 'Total - Mother tongue for the total population excluding institutional residents - 100% data',
 'Single responses',
 'Official languages',
 'English',
 'French',
 'Non-official languages',
 'Aboriginal languages',
 'Algonquian languages',
 'Blackfoot',
 'Cree-Montagnais languages',
 'Atikamekw',
 'Montagnais (Innu)',
 'Moose Cree',
 'Naskapi',
 'Northern East Cree',
 'Plains Cree',
 'Southern East Cree',
 'Swampy Cree',
 'Woods Cree',
 'Cree, n.o.s.',
 'Eastern Algonquian languages',
 'Malecite',
 "Mi'kmaq",
 'Ojibway-Potawatomi languages',
 'Algonquin',
 'Ojibway',
 'Oji-Cree',
 'Ottawa (Odawa)',
 'Algonquian languages, n.i.e.',
 'Athabaskan languages',
 'Northern Athabaskan languages',
 "Babine (Wetsuwet'en)",
 'Beaver',
 'Carrier',
 'Chilcotin',
 'Dene',
 'Dogrib (Tlicho)',
 "Gwich'in",
 'Sarsi (Sarcee)',
 'Sekani',
 'Slavey-Hare languages',
 'North Slavey (Hare)',
 'South Slavey',
 'Slavey, n.o.s.',
 'Tahltan languages',
 'Kaska (Nahani)',
 'Tahltan',
 'Tutchone languages',
 'Northern Tutchone',
 'Southern Tutchone',
 'Athabaskan languages, n.i.e.',
 'Haida',
 'Inuit languages',
 'Inuinnaqtun (Inuvialuktun)',
 'Inuktitut',
 'Inuit languages, n.i.e.',
 'Iroquoian languages',
 'Cayuga',
 'Mohawk',
 'Oneida',
 'Iroquoian languages, n.i.e.',
 'Kutenai',
 'Michif',
 'Salish languages',
 'Comox',
 'Halkomelem',
 'Lillooet',
 'Okanagan',
 'Shuswap (Secwepemctsin)',
 'Squamish',
 'Straits',
 'Thompson (Ntlakapamux)',
 'Salish languages, n.i.e.',
 'Siouan languages',
 'Dakota',
 'Stoney',
 'Siouan languages, n.i.e.',
 'Tlingit',
 'Tsimshian languages',
 'Gitxsan (Gitksan)',
 "Nisga'a",
 'Tsimshian',
 'Wakashan languages',
 'Haisla',
 'Heiltsuk',
 "Kwakiutl (Kwak'wala)",
 'Nuu-chah-nulth (Nootka)',
 'Wakashan languages, n.i.e.',
 'Aboriginal languages, n.o.s.',
 'Non-Aboriginal languages',
 'Afro-Asiatic languages',
 'Berber languages',
 'Kabyle',
 'Berber languages, n.i.e.',
 'Cushitic languages',
 'Bilen',
 'Oromo',
 'Somali',
 'Cushitic languages, n.i.e.',
 'Semitic languages',
 'Amharic',
 'Arabic',
 'Assyrian Neo-Aramaic',
 'Chaldean Neo-Aramaic',
 'Harari',
 'Hebrew',
 'Maltese',
 'Tigrigna',
 'Semitic languages, n.i.e.',
 'Afro-Asiatic languages, n.i.e.',
 'Austro-Asiatic languages',
 'Khmer (Cambodian)',
 'Vietnamese',
 'Austro-Asiatic languages, n.i.e',
 'Austronesian languages',
 'Bikol',
 'Cebuano',
 'Fijian',
 'Hiligaynon',
 'Ilocano',
 'Malagasy',
 'Malay',
 'Pampangan (Kapampangan, Pampango)',
 'Pangasinan',
 'Tagalog (Pilipino, Filipino)',
 'Waray-Waray',
 'Austronesian languages, n.i.e.',
 'Creole languages',
 'Haitian Creole',
 'Creole, n.o.s.',
 'Creole languages, n.i.e.',
 'Dravidian languages',
 'Kannada',
 'Malayalam',
 'Tamil',
 'Telugu',
 'Dravidian languages, n.i.e.',
 'Hmong-Mien languages',
 'Indo-European languages',
 'Albanian',
 'Armenian',
 'Balto-Slavic languages',
 'Baltic languages',
 'Latvian',
 'Lithuanian',
 'Slavic languages',
 'Belarusan',
 'Bosnian',
 'Bulgarian',
 'Croatian',
 'Czech',
 'Macedonian',
 'Polish',
 'Russian',
 'Serbian',
 'Serbo-Croatian',
 'Slovak',
 'Slovene (Slovenian)',
 'Ukrainian',
 'Slavic languages, n.i.e.',
 'Celtic languages',
 'Scottish Gaelic',
 'Welsh',
 'Celtic languages, n.i.e.',
 'Germanic languages',
 'Afrikaans',
 'Danish',
 'Dutch',
 'Frisian',
 'German',
 'Icelandic',
 'Norwegian',
 'Swedish',
 'Vlaams (Flemish)',
 'Yiddish',
 'Germanic languages, n.i.e.',
 'Greek',
 'Indo-Iranian languages',
 'Indo-Aryan languages',
 'Bengali',
 'Gujarati',
 'Hindi',
 'Kashmiri',
 'Konkani',
 'Marathi',
 'Nepali',
 'Oriya (Odia)',
 'Punjabi (Panjabi)',
 'Sindhi',
 'Sinhala (Sinhalese)',
 'Urdu',
 'Iranian languages',
 'Kurdish',
 'Pashto',
 'Persian (Farsi)',
 'Indo-Iranian languages, n.i.e.',
 'Italic (Romance) languages',
 'Catalan',
 'Italian',
 'Portuguese',
 'Romanian',
 'Spanish',
 'Italic (Romance) languages, n.i.e.',
 'Japanese',
 'Kartvelian languages',
 'Georgian',
 'Korean',
 'Mongolic languages',
 'Mongolian',
 'Niger-Congo languages',
 'Akan (Twi)',
 'Bamanankan',
 'Edo',
 'Ewe',
 'Fulah (Pular, Pulaar, Fulfulde)',
 'Ga',
 'Ganda',
 'Igbo',
 'Lingala',
 'Rundi (Kirundi)',
 'Kinyarwanda (Rwanda)',
 'Shona',
 'Swahili',
 'Wolof',
 'Yoruba',
 'Niger-Congo languages, n.i.e.',
 'Nilo-Saharan languages',
 'Dinka',
 'Nilo-Saharan languages, n.i.e.',
 'Sign languages',
 'American Sign Language',
 'Quebec Sign Language',
 'Sign languages, n.i.e',
 'Sino-Tibetan languages',
 'Chinese languages',
 'Cantonese',
 'Hakka',
 'Mandarin',
 'Min Dong',
 'Min Nan (Chaochow, Teochow, Fukien, Taiwanese)',
 'Wu (Shanghainese)',
 'Chinese, n.o.s.',
 'Chinese languages, n.i.e.',
 'Tibeto-Burman languages',
 'Burmese',
 'Karenic languages',
 'Tibetan',
 'Tibeto-Burman languages, n.i.e.',
 'Tai-Kadai languages',
 'Lao',
 'Thai',
 'Tai-Kadai languages, n.i.e',
 'Turkic languages',
 'Azerbaijani',
 'Turkish',
 'Uyghur',
 'Uzbek',
 'Turkic languages, n.i.e.',
 'Uralic languages',
 'Estonian',
 'Finnish',
 'Hungarian',
 'Uralic languages, n.i.e.',
 'Other languages, n.i.e.',
 'Multiple responses',
 'English and French',
 'English and non-official language',
 'French and non-official language',
 'English, French and non-official language']

home_language_data = [
 'Total - Language spoken most often at home for the total population excluding institutional residents - 100% data',
 'Single responses',
 'Official languages',
 'English',
 'French',
 'Non-official languages',
 'Aboriginal languages',
 'Algonquian languages',
 'Blackfoot',
 'Cree-Montagnais languages',
 'Atikamekw',
 'Montagnais (Innu)',
 'Moose Cree',
 'Naskapi',
 'Northern East Cree',
 'Plains Cree',
 'Southern East Cree',
 'Swampy Cree',
 'Woods Cree',
 'Cree, n.o.s.',
 'Eastern Algonquian languages',
 'Malecite',
 "Mi'kmaq",
 'Ojibway-Potawatomi languages',
 'Algonquin',
 'Ojibway',
 'Oji-Cree',
 'Ottawa (Odawa)',
 'Algonquian languages, n.i.e.',
 'Athabaskan languages',
 'Northern Athabaskan languages',
 "Babine (Wetsuwet'en)",
 'Beaver',
 'Carrier',
 'Chilcotin',
 'Dene',
 'Dogrib (Tlicho)',
 "Gwich'in",
 'Sarsi (Sarcee)',
 'Sekani',
 'Slavey-Hare languages',
 'North Slavey (Hare)',
 'South Slavey',
 'Slavey, n.o.s.',
 'Tahltan languages',
 'Kaska (Nahani)',
 'Tahltan',
 'Tutchone languages',
 'Northern Tutchone',
 'Southern Tutchone',
 'Athabaskan languages, n.i.e.',
 'Haida',
 'Inuit languages',
 'Inuinnaqtun (Inuvialuktun)',
 'Inuktitut',
 'Inuit languages, n.i.e.',
 'Iroquoian languages',
 'Cayuga',
 'Mohawk',
 'Oneida',
 'Iroquoian languages, n.i.e.',
 'Kutenai',
 'Michif',
 'Salish languages',
 'Comox',
 'Halkomelem',
 'Lillooet',
 'Okanagan',
 'Shuswap (Secwepemctsin)',
 'Squamish',
 'Straits',
 'Thompson (Ntlakapamux)',
 'Salish languages, n.i.e.',
 'Siouan languages',
 'Dakota',
 'Stoney',
 'Siouan languages, n.i.e.',
 'Tlingit',
 'Tsimshian languages',
 'Gitxsan (Gitksan)',
 "Nisga'a",
 'Tsimshian',
 'Wakashan languages',
 'Haisla',
 'Heiltsuk',
 "Kwakiutl (Kwak'wala)",
 'Nuu-chah-nulth (Nootka)',
 'Wakashan languages, n.i.e.',
 'Aboriginal languages, n.o.s.',
 'Non-Aboriginal languages',
 'Afro-Asiatic languages',
 'Berber languages',
 'Kabyle',
 'Berber languages, n.i.e.',
 'Cushitic languages',
 'Bilen',
 'Oromo',
 'Somali',
 'Cushitic languages, n.i.e.',
 'Semitic languages',
 'Amharic',
 'Arabic',
 'Assyrian Neo-Aramaic',
 'Chaldean Neo-Aramaic',
 'Harari',
 'Hebrew',
 'Maltese',
 'Tigrigna',
 'Semitic languages, n.i.e.',
 'Afro-Asiatic languages, n.i.e.',
 'Austro-Asiatic languages',
 'Khmer (Cambodian)',
 'Vietnamese',
 'Austro-Asiatic languages, n.i.e',
 'Austronesian languages',
 'Bikol',
 'Cebuano',
 'Fijian',
 'Hiligaynon',
 'Ilocano',
 'Malagasy',
 'Malay',
 'Pampangan (Kapampangan, Pampango)',
 'Pangasinan',
 'Tagalog (Pilipino, Filipino)',
 'Waray-Waray',
 'Austronesian languages, n.i.e.',
 'Creole languages',
 'Haitian Creole',
 'Creole, n.o.s.',
 'Creole languages, n.i.e.',
 'Dravidian languages',
 'Kannada',
 'Malayalam',
 'Tamil',
 'Telugu',
 'Dravidian languages, n.i.e.',
 'Hmong-Mien languages',
 'Indo-European languages',
 'Albanian',
 'Armenian',
 'Balto-Slavic languages',
 'Baltic languages',
 'Latvian',
 'Lithuanian',
 'Slavic languages',
 'Belarusan',
 'Bosnian',
 'Bulgarian',
 'Croatian',
 'Czech',
 'Macedonian',
 'Polish',
 'Russian',
 'Serbian',
 'Serbo-Croatian',
 'Slovak',
 'Slovene (Slovenian)',
 'Ukrainian',
 'Slavic languages, n.i.e.',
 'Celtic languages',
 'Scottish Gaelic',
 'Welsh',
 'Celtic languages, n.i.e.',
 'Germanic languages',
 'Afrikaans',
 'Danish',
 'Dutch',
 'Frisian',
 'German',
 'Icelandic',
 'Norwegian',
 'Swedish',
 'Vlaams (Flemish)',
 'Yiddish',
 'Germanic languages, n.i.e.',
 'Greek',
 'Indo-Iranian languages',
 'Indo-Aryan languages',
 'Bengali',
 'Gujarati',
 'Hindi',
 'Kashmiri',
 'Konkani',
 'Marathi',
 'Nepali',
 'Oriya (Odia)',
 'Punjabi (Panjabi)',
 'Sindhi',
 'Sinhala (Sinhalese)',
 'Urdu',
 'Iranian languages',
 'Kurdish',
 'Pashto',
 'Persian (Farsi)',
 'Indo-Iranian languages, n.i.e.',
 'Italic (Romance) languages',
 'Catalan',
 'Italian',
 'Portuguese',
 'Romanian',
 'Spanish',
 'Italic (Romance) languages, n.i.e.',
 'Japanese',
 'Kartvelian languages',
 'Georgian',
 'Korean',
 'Mongolic languages',
 'Mongolian',
 'Niger-Congo languages',
 'Akan (Twi)',
 'Bamanankan',
 'Edo',
 'Ewe',
 'Fulah (Pular, Pulaar, Fulfulde)',
 'Ga',
 'Ganda',
 'Igbo',
 'Lingala',
 'Rundi (Kirundi)',
 'Kinyarwanda (Rwanda)',
 'Shona',
 'Swahili',
 'Wolof',
 'Yoruba',
 'Niger-Congo languages, n.i.e.',
 'Nilo-Saharan languages',
 'Dinka',
 'Nilo-Saharan languages, n.i.e.',
 'Sign languages',
 'American Sign Language',
 'Quebec Sign Language',
 'Sign languages, n.i.e',
 'Sino-Tibetan languages',
 'Chinese languages',
 'Cantonese',
 'Hakka',
 'Mandarin',
 'Min Dong',
 'Min Nan (Chaochow, Teochow, Fukien, Taiwanese)',
 'Wu (Shanghainese)',
 'Chinese, n.o.s.',
 'Chinese languages, n.i.e.',
 'Tibeto-Burman languages',
 'Burmese',
 'Karenic languages',
 'Tibetan',
 'Tibeto-Burman languages, n.i.e.',
 'Tai-Kadai languages',
 'Lao',
 'Thai',
 'Tai-Kadai languages, n.i.e',
 'Turkic languages',
 'Azerbaijani',
 'Turkish',
 'Uyghur',
 'Uzbek',
 'Turkic languages, n.i.e.',
 'Uralic languages',
 'Estonian',
 'Finnish',
 'Hungarian',
 'Uralic languages, n.i.e.',
 'Other languages, n.i.e.',
 'Multiple responses',
 'English and French',
 'English and non-official language',
 'French and non-official language',
 'English, French and non-official language']


labor_force_data = [
    
    'Total - Population aged 15 years and over by Labour force status - 25% sample data',
 'In the labour force',
 'Employed',
 'Unemployed',
 'Not in the labour force',
 'Participation rate',
 'Employment rate',
 'Unemployment rate']

work_activity_data  = [
 'Total population aged 15 years and over by work activity during the reference year - 25% sample data',
 'Did not work',
 'Worked',
 'Worked full year, full time',
 'Worked part year and/or part time']
 #'Average weeks worked in reference year']

class_of_worker = [
 'Total labour force aged 15 years and over by class of worker - 25% sample data',
 'Class of worker - not applicable',
 'All classes of workers',
 'Employee',
 'Self-employed']

occupation_data = [
 'Total labour force population aged 15 years and over by occupation - National Occupational Classification (NOC) 2016 - 25% sample data',
 'Occupation - not applicable',
 #'All occupations',
 '0 Management occupations',
 '1 Business, finance and administration occupations',
 '2 Natural and applied sciences and related occupations',
 '3 Health occupations',
 '4 Occupations in education, law and social, community and government services',
 '5 Occupations in art, culture, recreation and sport',
 '6 Sales and service occupations',
 '7 Trades, transport and equipment operators and related occupations',
 '8 Natural resources, agriculture and related production occupations',
 '9 Occupations in manufacturing and utilities']

industry_data = [
 'Total Labour Force population aged 15 years and over by Industry - North American Industry Classification System (NAICS) 2012 - 25% sample data',
 'Industry - NAICS2012 - not applicable',
 #'All industry categories',
 '11 Agriculture, forestry, fishing and hunting',
 '21 Mining, quarrying, and oil and gas extraction',
 '22 Utilities',
 '23 Construction',
 '31-33 Manufacturing',
 '41 Wholesale trade',
 '44-45 Retail trade',
 '48-49 Transportation and warehousing',
 '51 Information and cultural industries',
 '52 Finance and insurance',
 '53 Real estate and rental and leasing',
 '54 Professional, scientific and technical services',
 '55 Management of companies and enterprises',
 '56 Administrative and support, waste management and remediation services',
 '61 Educational services',
 '62 Health care and social assistance',
 '71 Arts, entertainment and recreation',
 '72 Accommodation and food services',
 '81 Other services (except public administration)',
 '91 Public administration']

place_of_work_data = [
 'Total - Place of work status for the employed labour force aged 15 years and over in private households - 25% sample data',
 'Worked at home',
 'Worked outside Canada',
 'No fixed workplace address',
 'Worked at usual place']

commuting_employed_data = [
 'Total - Commuting destination for the employed labour force aged 15 years and over in private households with a usual place of work - 25% sample data',
 'Commute within census subdivision (CSD) of residence',
 'Commute to a different census subdivision (CSD) within census division (CD) of residence',
 'Commute to a different census subdivision (CSD) and census division (CD) within province or territory of residence',
 'Commute to a different province or territory']

mode_commute_data = [
 'Total - Main mode of commuting for the employed labour force aged 15 years and over in private households with a usual place of work or no fixed workplace address - 25% sample data',
 'Car, truck, van - as a driver',
 'Car, truck, van - as a passenger',
 'Public transit',
 'Walked',
 'Bicycle',
 'Other method']

commuting_duration_data =[
 'Total - Commuting duration for the employed labour force aged 15 years and over in private households with a usual place of work or no fixed workplace address - 25% sample data',
 'Less than 15 minutes',
 '15 to 29 minutes',
 '30 to 44 minutes',
 '45 to 59 minutes',
 '60 minutes and over']

leave_for_work_data = [
 'Total - Time leaving for work for the employed labour force aged 15 years and over in private households with a usual place of work or no fixed workplace address - 25% sample data',
 'Between 5 a.m. and 5:59 a.m.',
 'Between 6 a.m. and 6:59 a.m.',
 'Between 7 a.m. and 7:59 a.m.',
 'Between 8 a.m. and 8:59 a.m.',
 'Between 9 a.m. and 11:59 a.m.',
 'Between 12 p.m. and 4:59 a.m.'
]

######### Combo datasets

work_force_dictionary ={
                 "Labour force": labor_force_data, 
                  "Class of worker":class_of_worker,
                  "Occupation data":occupation_data,
                  "Industry data": industry_data}

work_environment_dictionary = {"Place of work":place_of_work_data,
                              "Commuting":commuting_employed_data,
                              "Mode of commute":mode_commute_data,
                              "Commuting duration":commuting_duration_data,
                              "Leaving for work time":leave_for_work_data}

languages_dictionary={"Official languages":languages_data,
                       "First official language":first_official_language_data,
                       "Mother tongue": mother_tongue_data,
                       "Home language" : home_language_data}

personal_dictionary = {"Age":age_data,
                       "Age distribution": age_distribution,
                       "Household members": house_data,
                       "Marital status":marital_data}

if __name__ == '__main__':
    
    print("Setting up our environment...count until 20 :)")

    # Link to zipped data
    link_csv = "https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/prof/details/download-telecharger/comp/GetFile.cfm?Lang=E&FILETYPE=CSV&GEONO=069"
    
    # Unzip data in local directory
    r = urlopen(link_csv).read()
    z = zipfile.ZipFile(BytesIO(r))
    z.extractall()

    # Get CSV files only from extracted data sets
    import glob, os
    os.chdir("./")
    csv_file = []
    for file in glob.glob("*.csv"):
        csv_file.append(file)

     ######### Build widgets
    all_the_widgets = []

    # Button widget
    CD_button = widgets.Button(
        button_style='success',
        description="Preview Dataset", 
        layout=Layout(width='15%', height='30px'),
        style=style
    )    

    # Connect widget to function - run subsequent cells
    CD_button.on_click( rerun_cell )
    
    print("DONE! Ready to use notebook")