from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import requests
import smtplib
from email.message import EmailMessage

load_dotenv()

def get_dog_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()  # Parse JSON response
    image_url = data['message']  # Get the image URL from the JSON
    print(f"Image URL: {image_url}")
        
    # # Download the image
    download_image(image_url, "random_dog.jpg")
    
    # Create list using / as delimiters
    url_parts = image_url.split('/')
    breed = url_parts[4]
    
    return breed

def download_image(image_url, filename):
    """Download an image from URL and save it locally"""
    try:
        print(f"Downloading image from: {image_url}")
        
        # Download the image
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Save the image
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"Image successfully downloaded and saved as: {filename}")
        
        # Get file size
        file_size = os.path.getsize(filename)
        print(f"File size: {file_size} bytes")
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
    except Exception as e:
        print(f"Error saving image: {e}")
    
def get_Gemini_response(dog_breed):
    client = genai.Client()
    
    prompt_content = "Write a sweet good morning paragraph to my girlfriend. Make up a dog name and center the message around the dog. The dog's breed is " + dog_breed + ".  The message should be short and sweet and should be around one paragraph."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_content,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
        ),
    )
    
    return response.text
def send_email(response_msg):

    # Email account credentials
    email_address = "jacobgale2003@gmail.com"
    app_password = "eyzb sbdk dcpm etfn"

    # Compose the email
    msg = EmailMessage()
    msg["Subject"] = "Good Morning Da Wuv"
    msg["From"] = email_address
    msg["To"] = "ashleygoldstein04@gmail.com"
    msg.set_content(response_msg)

    with open("random_dog.jpg", "rb") as img:
        img_data = img.read()
        msg.add_attachment(img_data, maintype="image", subtype="jpeg", filename="random_dog.jpg")
        
    # Send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_address, app_password)
        smtp.send_message(msg)

def main():
    breed = get_dog_image()
    response_msg = get_Gemini_response(breed)
    send_email(response_msg)
    

if __name__ == "__main__":
    main()
