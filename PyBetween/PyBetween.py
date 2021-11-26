from .APIHandler import APIHandler, APIUrl


class Between:

    # User
    class User:
        access_token = ""
        user_id = ""
        relationship_id = ""
        account_id = ""
        session_id = ""
        expires_at = 0

        def __init__(self):
            self.access_token = ""
            self.user_id = ""
            self.relationship_id = ""
            self.account_id = ""
            self.session_id = ""
            self.expires_at = 0

    # Thread
    class Thread:
        id = ""
        created_time = 0
        message_count = 0
        unread_count = 0
        chatroom_id = ""
        revision = 0

        def __init__(self):
            self.id = ""
            self.created_time = 0
            self.message_count = 0
            self.unread_count = 0
            self.chatroom_id = ""
            self.revision = 0

    class Threads:
        data = []
        count = 0

        def __init__(self):
            self.data = []
            self.count = 0

    # Message
    class Message:
        id = ""
        from_ = ""
        created_time = 0
        content = ""

        def __init__(self):
            self.id = ""
            self.from_ = ""
            self.created_time = 0
            self.content = ""

    class Messages:
        data = []
        count = 0
        revision = 0

        def __init__(self):
            self.data = []
            self.count = 0
            self.revision = 0

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        payload = {
            'email': self.email,
            'password': self.password

        }
        json_data = APIHandler(method='POST', url=APIUrl.AUTH, payload=payload)

        self.User.access_token = json_data['access_token']
        self.User.user_id = json_data['user_id']
        self.User.relationship_id = json_data['relationship_id']
        self.User.account_id = json_data['account_id']
        self.User.session_id = json_data['session_id']
        self.User.expires_at = json_data['expires_at']

        return True

    def get_threads(self):

        headers = {
            'X-BETWEEN-AUTHORIZATION': self.User.access_token
        }

        json_data = APIHandler(method='GET', url=APIUrl().get_url(endpoint=APIUrl.THREADS, param=self.User.user_id),
                               headers=headers)

        threads = []
        thread = []

        for data in json_data['data']:
            thread = self.Thread()

            thread.id = data["id"]
            thread.created_time = data["created_time"]
            thread.message_count = data["message_count"]
            thread.unread_count = data["unread_count"]
            thread.chatroom_id = data["chatroom_id"]
            thread.revision = data["revision"]

            threads.append(thread)

        self.Threads.data = threads
        self.Threads.count = json_data['count']

    def get_messages(self):
        headers = {
            'X-BETWEEN-AUTHORIZATION': self.User.access_token
        }

        json_data = APIHandler(method='GET', url=APIUrl().get_url(endpoint=APIUrl.MESSAGES,
                               param=self.Threads.data[0].id),
                               headers=headers)

        messages = []
        message = []

        for data in json_data['data']:
            message = self.Message()

            message.id = data["id"]
            message.from_ = data["from"]
            message.created_time = data["created_time"]
            message.content = data["content"]

            messages.append(message)

        self.Messages.data = messages
        self.Messages.count = json_data['count']
        self.Messages.revision = json_data['revision']

        return self.Messages

    def send_message(self, content):
        headers = {
            'X-BETWEEN-AUTHORIZATION': self.User.access_token
        }

        payload = {
            'content': content
        }

        APIHandler(method='POST', url=APIUrl().get_url(endpoint=APIUrl.SENDMESSAGE,
                   param=self.Threads.data[0].id),
                   headers=headers, payload=payload)

        return True
