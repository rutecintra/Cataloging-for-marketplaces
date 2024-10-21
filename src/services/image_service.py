import requests
import os
from google.cloud import vision
import time

def download_image(image_url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    max_retries = 5
    backoff_factor = 2
    wait_time = 1 
    connect_timeout = 10
    read_timeout = 20

    for attempt in range(max_retries):

        try:

            response = requests.get(image_url, headers=headers, timeout=(connect_timeout, read_timeout))

            if response.status_code == 200:

                image_path = 'temp_image.jpg'

                with open(image_path, 'wb') as image_file:

                    image_file.write(response.content)

                return image_path
            
            else:

                print(f"Error downloading image (status {response.status_code}): {image_url}")
                return None
            
        except requests.exceptions.ConnectTimeout:

            print(f"Connection timeout when downloading image on attempt {attempt + 1} of {max_retries}. Waiting {wait_time} seconds before trying again...")
            time.sleep(wait_time)
            wait_time *= backoff_factor

        except requests.exceptions.ReadTimeout:

            print(f"Connection timeout when downloading image on attempt {attempt + 1} of {max_retries}. Waiting {wait_time} seconds before trying again...")
            time.sleep(wait_time)
            wait_time *= backoff_factor

        except requests.exceptions.RequestException as e:

            print(f"Error downloading image {image_url}: {e}")
            return None
        
    print(f"Failed to download image after {max_retries} attempts.")
    return None


def get_image_description(image_path):

    client = vision.ImageAnnotatorClient()

    with open(image_path, 'rb') as image_file:

        content = image_file.read()

    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = [label.description for label in response.label_annotations]
    description = ', '.join(labels)

    try:

        os.remove(image_path)

    except Exception as e:
        
        print(f"Error deleting image {image_path}: {e}")
    
    return description