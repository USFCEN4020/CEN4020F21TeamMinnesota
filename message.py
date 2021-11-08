from os import path
import pickle

UNREAD_STATUS = "unread"
READ_STATUS = "read"


class Message:
    NEXT_MESSAGE_ID_FILE_NAME = "next_message_id.pickle"
    next_message_id = 0

    def __init__(self, sender_username, content, date):
        self.sender_username = sender_username
        self.content = content
        self.date = date
        self.status = UNREAD_STATUS
        self.id = None

    # Loads the NEXT_MESSAGE_ID_FILE_NAME file, if it doesn't exists it creates a new one.
    @staticmethod
    def load_next_message_id_file():
        if not path.isfile(Message.NEXT_MESSAGE_ID_FILE_NAME):
            Message.update_next_message_id_file()

        with open(Message.NEXT_MESSAGE_ID_FILE_NAME, "rb") as next_message_id_file:
            Message.next_message_id = pickle.load(next_message_id_file)

    # Creates the next_message_id file and dumps Message.next_message_id.
    @staticmethod
    def update_next_message_id_file():
        with open(Message.NEXT_MESSAGE_ID_FILE_NAME, "wb") as next_message_id_file:
            pickle.dump(Message.next_message_id, next_message_id_file)
