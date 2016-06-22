from abc import ABCMeta, abstractmethod
import logging


class MessageType():
    HELLO = 'hello'
    RECONNECT_URL = 'reconnect_url'
    TEXT = 'text'
    TEAM_JOIN = 'team_join'
    

class BaseMessage(object):
    __metaclass__ = ABCMeta

    def __init__(self, jsonObj):
        self.type = jsonObj['type']


class HelloMessage(BaseMessage):
    def __init__(self, jsonObj):
        super(HelloMessage, self).__init__(jsonObj)


class ReconnectUrlMessage(BaseMessage):
    def __init__(self, jsonObj):
        super(ReconnectUrlMessage, self).__init__(jsonObj)
        self.url = jsonObj['url']


class TextMessage(BaseMessage):
    def __init__(self, jsonObj):
        super(TextMessage, self).__init__(jsonObj)
        self.text = jsonObj['text']

    
class TeamJoinMessage(BaseMessage):
    def __init__(self, jsonObj):
        super(TeamJoinMessage, self).__init__(jsonObj)
        self.user_keys = jsonObj['user']
