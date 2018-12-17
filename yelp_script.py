from yelpapi import YelpAPI
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')

MY_API_KEY = "uiVBSPKgvlwYBZFij9UnqGYDXlxWLI6q7muplXslfaBPIqqH07cgg8PeqP4aqDheV8VR0lVt7cvPRnfsBP67NkUsDRKQx5Af13EWpPcnttz_jmXX-R2Chh4PDCSqW3Yx"

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}




yelp_api = YelpAPI(MY_API_KEY)




def incrementAndUpdateOffSet(offset):
    return offset + 50

offSet = 0
results =[]

for state in states:
    print("Querying " + state + "...")
    location = states[state]
    offSet=0
    numberOfShopsProcessedThisBatch = 0
    BarberShopsToProcess = True

    while(BarberShopsToProcess and offSet < 1000):
        search_results = yelp_api.search_query(term='Barber Shop', location=location, offset=offSet)

        for business in search_results['businesses']:
            numberOfShopsProcessedThisBatch += 1
            id = business['id']
            name = business['name']
            address1 = business['location']['address1']
            address2 = business['location']['address2']
            city = business['location']['city']
            state = business['location']['state']
            zip = business['location']['zip_code']
            country = business['location']['country']
            phone = business['phone']
            is_closed = business['is_closed']
            results.append([id,name,address1,address2,city,state,zip,country,phone,is_closed])
        if numberOfShopsProcessedThisBatch == 0:
            BarberShopsToProcess = False
        else:
            offSet = incrementAndUpdateOffSet(offSet)
            numberOfShopsProcessedThisBatch = 0
            if offSet == 1000:
                print("Query limit reached for " + state + "...")

print("All states have been successfully queried!...")

with open('output.csv','w', 0) as fp: #create csv file
    print("Writing query results to output.csv...")
    a = csv.writer(fp, delimiter=',')
    a.writerows(results)

#print business['id'],business['name'],business['location']['address1'],business['location']['address2'],business['location']['city'],business['location']['state'],business['location']['zip_code'],business['location']['country'],business['phone'],business['is_closed']
#test0 = yelp_api.phone_search_query(phone='+17168455555')
#for result in test0['businesses']:
    #print str(result) + "\n"
