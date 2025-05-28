from hashlib import md5
from requests import get
from datetime import datetime

class RestMarvel:
    timestamp = datetime.now().strftime('%Y-%m-%d%H:%M:S')
    pub_key = '6f610f2e1e9b3085a6c0c43b84f9b0b0'
    priv_key = '59a5dd33e4467d643f9cf85c1acf4ebc7fbe95dc'

    def hash_params(self):
        hash_md5 = md5()
        hash_md5.update(f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params = hash_md5.hexdigest()
        return hashed_params
    
    def get_heroes(self):
        params ={'ts':self.timestamp,'apikey':self.pub_key,'hash':self.hash_params()}
        results = get('https://gateway.marvel.com:443/v1/public/characters',params=params)
        
        data =results.json()
        print(data)
        print(data['status'])

mv=RestMarvel()
mv.get_heroes()
