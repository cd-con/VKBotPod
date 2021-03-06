import random

import bs4 as bs4
import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import logging


class LongPollBot:
    """
    LongPollBot uses for creating VK LongPoll bots for communities

    You should firstly init them, before you start make a bot

    Code example at /examples/hello_world.py

    :param token: Your VK community token
    """

    def __init__(self, token: str):
        self.event = None
        self.token = token
        self.handlers = {}

        self.no_handler_found_error = "This command does not exist!"

        self.vk = vk_api.VkApi(token=self.token)

    def run(self, debug=False):
        """
        Starts your bot.

        If debug mode is on, bot will stop on any error in thread.

        debug = False >> Production mode, bot will log all errors and don't stop on it

        :param debug: disable production mode
        :return Exception:
        """
        supported_handlers = [VkEventType.MESSAGE_NEW]
        handlers = {
            VkEventType.MESSAGE_NEW: self.__on_Message,
            VkEventType.USER_TYPING: self.__on_Typing  # indev
        }

        logging.basicConfig(filename="debug.log", level=logging.DEBUG)

        # TODO Make thread
        lp = VkLongPoll(self.vk)

        for event in lp.listen():
            self.event = event
            if debug:
                logging.debug("New event! Event type: " + str(event.type))

            if event.type in supported_handlers and event.to_me:
                if debug:
                    logging.debug("Event bypassed compatibility and event.to_me check")
                try:
                    handlers[event.type](event)
                except KeyError:
                    logging.error("KeyError! Such handler does not exists >> " + str(event.type))
                    if debug:
                        exit("App stopped due to error and debug = True. Watch debug.log to see full trace")

    def add_Message_Handler(self, message: object, triggers):
        for trigger in triggers:
            self.handlers[trigger.text] = message

    def __on_Message(self, *args):
        for arg in args:
            if arg.text is not None:
                try:
                    item = self.handlers[arg.text]
                    value = item.text
                except KeyError:
                    value = self.no_handler_found_error
                finally:
                    self.__send_Message(self.event.user_id, self.__fill_var(value))

    def __on_Typing(self, *args):
        print("User typing")

    def __send_Message(self, user_id, text):
        self.vk.method('messages.send', {'user_id': user_id,
                                         'message': text,
                                         'random_id': random.randint(111, 999)})

    def __fill_var(self, text: str):
        text = text.replace("%user_name%", self.get_username(self.event.user_id))
        return text

    def get_username(self, user_id):
        """
        Get username by VK ID
        :param user_id:
        :return: Username
        """
        request = requests.get("https://vk.com/id" + str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")

        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

        return user_name.split()[0]

    @staticmethod
    def _clean_all_tag_from_str(string_line):
        """
        ?????????????? ???????????? stringLine ???? ?????????? ?? ???? ????????????????????
        :param string_line: ?????????????????? ????????????
        :return: ?????????????????? ????????????
        """
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result
