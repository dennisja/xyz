from typing import List

from flask_mail import Mail, Message


class EmailClient:
    @classmethod
    def init_app(self, app):
        self.__client = Mail(app=app)

    # TODO: instead of passing str and receiver, define a message class that will contain relevant info
    # to the send function
    def send(self, body: str, receiver):
        message = Message(
            sender="MNotify <noreply@mnotify.com>", recipients=[receiver], html=body
        )
        self.__client.send(message)
