import requests
import secret_consts

def get_all_data():
    GET_URL = 'https://getpocket.com/v3/get'
    kwargs = {'consumer_key': secret_consts.consumer_key,
              'access_token': secret_consts.access_token,
              'detailType': 'complete'}
    
    r = requests.post(GET_URL, data=kwargs)
    return r