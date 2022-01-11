!pip install ibm_watson

!pip install pathlib

!pip install ruamel-yaml

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = ""
url = ""

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator= authenticator)
stt.set_service_url(url)

with open('/Users/eddie/recording.mp3', 'rb') as f:
    res = stt.recognize(audio=f, content_type = 'audio/mp3', model = 'en-US_NarrowbandModel').get_result()
    
#result1 = res['results']['alternatives'][0]['transcript']

print(res)
