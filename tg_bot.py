import requests
import json



def send_pictures(token, chat_id, file_picture_names, text):

  media = []
  for number, i in enumerate(file_picture_names, start=1):
        media.append({
            "type": "photo",
            "media": f"attach://random-name-{number}"
    })
  media[0]["caption"] = text

  params = {
      "chat_id": chat_id,
      "media": json.dumps(media),
      "contentType": "application/json"
  }

  files = {}


  for number, i in enumerate(file_picture_names, start=1):
    files[f"random-name-{number}"] = open(i, "rb")


  send_text = f'https://api.telegram.org/bot{token}/sendMediaGroup'
  response = requests.post(send_text, params=params, files=files)
  response.raise_for_status()