from whatsfly import WhatsApp
# import time


def my_event_callback(client, event_data):
    ''' 
    Simple event callback to listen to incoming events/messages. 
    Whenever this function is called, it will retrieve the current incoming event or messages.
    '''
    print("Received event data:", event_data)




# for _ in range(100):  # Retry sending the message up to 100 times if it fails
#     message_sent = whatsapp.sendMessage(phone, message, False)

# time.sleep(5 * 60)  # Listen for messages for 5 minutes

# whatsapp.disconnect()

# def check_connection():


def whatsapp_connect():
    whatsapp = WhatsApp(on_event=my_event_callback)
    # whatsapp = WhatsApp()
    whatsapp.connect()

    return whatsapp

def send_message(whatsapp, phone: str, name: str, message: str):
    if whatsapp.loggedIn() and whatsapp.isConnected():
        message = message.replace("[name]", name)
        whatsapp.sendMessage(phone, message, False)
    else:
        print("Connection failed, trying again..")
        send_message(whatsapp, phone, name, message)

# def send_interface():
#     whatsapp = whatsapp_connect()
#     input("Continue?")
#     send_message(whatsapp, "966540450979", "الاخ الغالي احمد", "السلام عليكم [name] كل عام وانت بخير 🎉")
#     whatsapp.disconnect()