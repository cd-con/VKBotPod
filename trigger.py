class TextTrigger:
    """
    TextTrigger is an object, that helps you handle new message incoming event

    :arg text: Trigger on some text
    :arg case_sensitive: Should trigger to be case sensitive
    :arg is_logging: Log trigger activation
    """

    def __init__(self, text: str, case_sensitive=False, is_logging=False):
        self.text = text
        self.case_sense = case_sensitive
        self.is_logging = is_logging