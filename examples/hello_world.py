"""
hello_world.py
By cd-con

Example script for simple usage of VKBotPod library

"""

import bot
import content
import trigger

# Init bot class
pod = bot.LongPollBot("YOUR TOKEN HERE")

# Add trigger and result message
# There can be several triggers
triggers = [trigger.TextTrigger(text="hi", case_sensitive=False), trigger.TextTrigger(text="hello", case_sensitive=False)]
message = content.Message(text="Hello, %user_name%")

# Add handler
pod.add_Message_Handler(message, triggers)

# Run bot
if __name__ == "__main__":
    pod.run(debug=True)
