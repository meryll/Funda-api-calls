from src import api_call, parser
import time

DELAY_TIME_S = 60
MAX_NUMBER_OF_CALLS = 100


def delay():
    time.sleep(DELAY_TIME_S)


def get_objects(page_number, if_garden):
    xml_response = api_call.get(page_number=page_number, if_garden=if_garden)
    return parser.get(to_parse=xml_response)


def count(list_of_occurrences):
    counts = dict()
    for i in list_of_occurrences:
        counts[i] = counts.get(i, 0) + 1

    return counts


def convert_dict_to_array(dict):
    return [[k, v] for k, v in dict.items()]


def sort_based_on_occurrence(list_of_occurrences):
    dict_of_occurrence = count(list_of_occurrences)
    array_of_occurrences = convert_dict_to_array(dict_of_occurrence)
    sorted_array = sorted(array_of_occurrences, key=lambda x: x[1], reverse=True)
    return sorted_array


def get(if_garden, how_many):
    '''
    Getting the array of top <how many> real estate agents.
    1. Getting all object for 1st page.
    2. Getting objects for the rest of the pages unit we download all of the objects.
    '''

    init_number_of_objects, all_agents = get_objects(page_number=0, if_garden=if_garden)

    objects_left = init_number_of_objects
    page_number = 1

    while objects_left > 0:
        new_number_of_objects, agents_per_page = get_objects(page_number=page_number, if_garden=if_garden)

        if len(agents_per_page) == 0:
            objects_left = 0

        # If number of all objects listed has changed we have to also change number of objects left to download.
        # I'm asking rest api for objects sorted by date added so the newest objects would be at the last page.
        # But still it's a naive solution because listed object may be deleted and we might have already processed it.
        if init_number_of_objects != new_number_of_objects:
            objects_left += new_number_of_objects - init_number_of_objects

        # append list of real estate agents per page to list of all real estate agents
        all_agents += agents_per_page

        page_number += 1
        objects_left -= (len(agents_per_page))

        # If it's a 100 request make a delay as to avoid bottleneck and errors from API
        # Another (maybe even cleaner) way to do this it to check status code received from rest api
        # and if it's exception "Max number of requests reached" and add delay there.
        # but funda's rest api return 401 which can mean anything.
        if page_number % MAX_NUMBER_OF_CALLS == 0:
            delay()

    # since we have list of real estate agents for now we have to group them, count how many times each of them occurre.
    # and sort by the number of occurrences.
    sorted_agents = sort_based_on_occurrence(all_agents)
    return sorted_agents[:how_many]