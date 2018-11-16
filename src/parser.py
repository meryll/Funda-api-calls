import xml.etree.ElementTree as ET

#wazne elementy:
'''
AccountStatus
Objects
Paging
TotaalAantalObjecten
'''
ROOT = '{http://schemas.datacontract.org/2004/07/FundaAPI.Feeds.Entities}'
OBJECTS = 'Objects'
TOTAL_NUMBER_OF_OBJECTS = 'TotaalAantalObjecten'
REAL_ESTATE_AGENT_ID = 'MakelaarId'
REAL_ESTATE_AGENT = 'MakelaarNaam'

'''
Parsing REST API response. Returning only relevant information which is number of total objects
and names of real estate agents. 
todo: it would be a good idea to sort and counts real estate agents based on their's ID and not name.
For now I'm assuming that Name and ID are strictly correlated.
'''
def get (to_parse):
    root = ET.fromstring(to_parse)
    total_number_of_objects = int(root.find('{}{}'.format(ROOT, TOTAL_NUMBER_OF_OBJECTS)).text)

    objects = root.find('{}{}'.format(ROOT, OBJECTS))

    real_estate_agents = []
    for object in objects:
        agent_id = object.find('{}{}'.format(ROOT,REAL_ESTATE_AGENT_ID)).text
        agent_name = object.find('{}{}'.format(ROOT, REAL_ESTATE_AGENT)).text
        real_estate_agents.append(agent_name)

    return total_number_of_objects, real_estate_agents

