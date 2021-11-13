class Message:
    """
        Message is an object, that helps you create a message

        :arg text: Message text
        :arg keyboard: keyboard object
        :arg is_inline: show keyboard in message
        """

    def __init__(self, text: str, keyboard=None, is_inline=False):
        self.text = text
        self.keyboard = keyboard
        self.is_inline = is_inline