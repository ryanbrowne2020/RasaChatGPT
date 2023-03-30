import openai

KEY = "<your_api_key_here>"
openai.api_key = KEY

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

cognitive_prompt = ['What is the burden of cognitive training?', 
                    'How do you feel about your cognitive skills?'
                    ]

questionlist = cognitive_prompt

def interact_chatPGT_respondQ(usertext, question):
    global utter
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "Pretend you are my health coach, you are an expert in motivational psychology. I am an older adult, who has come to you to help me change my behaviour. You have just asked me the question'" + question + "' and I want you to respond to my answer"},
            {"role": "user", "content": usertext}
    ],
    max_tokens=260
    )
    utter = response.choices[0]["message"]["content"].strip()
    return utter

class AskForSlotAction1(Action):

    def name(self) -> Text:
        return "action_ask_firsttext"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=questionlist[0])

        return []

class AskForSlotAction2(Action):

    def name(self) -> Text:
        return "action_ask_nexttext"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        usertext = tracker.latest_message['text']
        question = questionlist[0]
        interact_chatPGT_respondQ(usertext, question)
        dispatcher.utter_message(utter)

        dispatcher.utter_message(text=questionlist[1])

        return []
    
class ActionFinished(Action):

    def name(self) -> Text:
        return "action_finished"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        usertext = tracker.latest_message['text']
        question = questionlist[1]
        interact_chatPGT_respondQ(usertext, question)
        dispatcher.utter_message(utter)

        return []