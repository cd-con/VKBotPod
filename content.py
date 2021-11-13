from vk_api.keyboard import VkKeyboard, VkKeyboardColor


class Message:
    """
        Message is an object, that helps you create a message

        :arg text: Message text
        :arg keyboard: keyboard object
        :arg is_inline: show keyboard in message
        """

    def __init__(self, text: str, keyboard=None):
        self.text = text
        self.keyboard = keyboard


class Button:
    def __init__(self, text, color=VkKeyboardColor.SECONDARY):
        self.text = text
        self.color = color


class Keyboard:
    def __init__(self, is_inline=False, is_onetime=False):
        self.buttons = {}
        self.is_inline = is_inline
        self.is_onetime = is_onetime

    def keyboard(self):
        keyboard = VkKeyboard(one_time=self.is_onetime)

        for button in self.buttons:
            keyboard.add_button(button.text, color=button.color)

        return keyboard

    def add_button(self, button=None):
        if button is None:
            raise ValueError("Button can't be equal to None")

        self.buttons[button.text] = self.button.color
