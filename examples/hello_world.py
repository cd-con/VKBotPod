"""
hello_world.py
By cd-con

Example script for simple usage of VKBotPod library
15efd8568ae228a4e8967df7fe3150e20e49c390395cfd79886e46c0f739113438c8cd1de927d79b82264
"""

import bot

# Init bot class
pod = bot.LongPollBot("TOKEN", 123456)

# Add trigger and result message
# There can be several triggers
triggers = [bot.TextTrigger(text="hi", case_sensitive=False), bot.TextTrigger(text="hello", case_sensitive=False)]
message = bot.Message(text="Hello, %user_name%")

# Add handler
pod.add_Message_Handler(message, triggers)

# Run bot
if __name__ == "__main__":
    pod.run(debug=True)
