import threading

from sqlalchemy import Column, String

from InsaneRobot.modules.sql import BASE, SESSION


class InsaneChats(BASE):
    __tablename__ = "Insane_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


InsaneChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_Insane(chat_id):
    try:
        chat = SESSION.query(InsaneChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_Insane(chat_id):
    with INSERTION_LOCK:
        Insanechat = SESSION.query(InsaneChats).get(str(chat_id))
        if not Insanechat:
            Insanechat = InsaneChats(str(chat_id))
        SESSION.add(Insanechat)
        SESSION.commit()


def rem_Insane(chat_id):
    with INSERTION_LOCK:
        Insanechat = SESSION.query(InsaneChats).get(str(chat_id))
        if Insanechat:
            SESSION.delete(Insanechat)
        SESSION.commit()
