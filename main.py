import pyautogui
import time
import pyperclip
from openai import OpenAI
client = OpenAI( api_key="Enter API KEY")
def is_last_message_from_sender(chat_log):
    messages = chat_log.strip().splitlines()
    if not messages:
        return False

    last_message = messages[-1]
    return "]" in last_message and ":" in last_message
    
 #click at chrome icon
pyautogui.click(948,1064)    
time.sleep(1)  
last_processed_chat = ""        
while True:
    #drag the mouse from cordinates to select text
    pyautogui.moveTo(463,161)
    pyautogui.dragTo(1293,967,duration=1.0,button='left')
    #copy text to clipboard
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    pyautogui.click(496,199)
    # store the text in variable from clipboard
    chat_history=pyperclip.paste(578,976)
    if chat_history == last_processed_chat:
        time.sleep(2)
        continue

    last_processed_chat = chat_history
    print("Checking chat...")
    print(chat_history)
    # print text to verify
    print(chat_history)
    if is_last_message_from_sender(chat_history):
        completion=client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system","content":"you are a person named ganesh who speakes hindi as well as english, you are  from india  and you are a coder.you analyze chat history and respond like  ganesh.output should be next chat response mrssages only"},
                    {"role":"user","content":chat_history}    ]
        )
        response=completion.choices[0].message.content
        pyperclip.copy(response)
        #click at coordinates
        pyautogui.click()
        time.sleep(1)
        #paste the text
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)
        #press Enter
        pyautogui.press('enter')
