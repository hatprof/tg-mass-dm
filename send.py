from telethon.sync import TelegramClient

# Function to login to Telegram
def login(api_id, api_hash, phone_number):
    client = TelegramClient('session_name', api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        client.sign_in(phone_number, input('Enter the code: '))
    return client

# Function to send message to list of usernames
def send_message(client, username_file, message):
    with open(username_file, 'r') as file:
        usernames = file.readlines()
        for username in usernames:
            try:
                client.send_message(username.strip(), message)
                print(f"Message sent to {username.strip()} successfully!")
            except Exception as e:
                print(f"Failed to send message to {username.strip()}: {e}")

# Main function
def main():
    # Input your Telegram API credentials
    api_id = 'your_api_id'
    api_hash = 'your_api_hash'
    phone_number = 'your_phone_number'

    # Login to Telegram
    client = login(api_id, api_hash, phone_number)

    # Send message
    username_file = 'usernames.txt'  # Name of the text file containing usernames
    message = 'Your message here'  # Message to be sent
    send_message(client, username_file, message)

if __name__ == '__main__':
    main()
