from requests import get

TIMES_JSON = "https://www.balldontlie.io/api/v1/teams"

def get_times():
    '''## keys desta funçao ##
        for i in get_times():
            print(i.keys())'''
    times = get(TIMES_JSON).json()
    return times['data']


