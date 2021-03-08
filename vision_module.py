import requests
import json
from validate_curp import validate_curp

def get_image_text(base_64_image):
    key = 'YOUR_KEY'
    payload = {'requests': [
        {
            'image': {
                "content": base_64_image
            },
            'features': [{'type': 'TEXT_DETECTION'}],
        },
    ]}

    r = requests.post(
        'https://vision.googleapis.com/v1/images:annotate?key=' + key, data=json.dumps(payload))
    res = r.json()

    if 'responses' in res and 'textAnnotations' in res['responses'][0]:
        text = res['responses'][0]['textAnnotations']
        detected_curp = list(
            filter(lambda item: validate_curp(item['description']), text))

        return detected_curp[0]['description'] if bool(detected_curp) else None
    else:
        return None

