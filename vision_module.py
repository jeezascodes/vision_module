import requests


def get_image_text(base_64_image):
    key = 'AIzaSyAHDvJchYHbM84G4Me2HAGkodAQB99C-U0'
    payload = {'requests': [
        {
            'image': {
                "content": base_64_image
            },
            'features': [{'type': 'TEXT_DETECTION'}],
        },
    ]}

    r = requests.post(
        'https://vision.googleapis.com/v1/images:annotate?key=' + key, data=str(payload))
    res = r.json()

    if 'responses' in res and bool(res['responses'][0]):
            text = res['responses'][0]['textAnnotations']
            return list(map(lambda item: item['description'], text))
    else:
        return res

