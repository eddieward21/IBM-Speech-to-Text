!pip install ibm_watson

!pip install pathlib

!pip install ruamel-yaml

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = "ko1WCTeXR335j38HPOpP7GHtmFOyXg2I-J6Fz4t1m_Su"
url = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/6f75754d-f7e5-47f5-921c-1ff23a2f72be"

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator= authenticator)
stt.set_service_url(url)

with open('/Users/eddie/Desktop/258 E Clinton Ave.mp3', 'rb') as f:
    res = stt.recognize(audio=f, content_type = 'audio/mp3', model = 'en-US_NarrowbandModel').get_result()
    
#result1 = res['results']['alternatives'][0]['transcript']

print(res)
