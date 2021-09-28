# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

py = pd.read_csv("C:\\Users\\ViJAY\\Desktop\\Questions\\python.txt", sep="\t")
nlp = pd.read_csv("C:\\Users\\ViJAY\\Desktop\\Questions\\nlp.txt", sep="\t")
dl = pd.read_csv("C:\\Users\\ViJAY\\Desktop\\Questions\\dl.txt", sep="\t")
ds = pd.read_csv("C:\\Users\\ViJAY\\Desktop\\Questions\\ds.txt", sep="\t")
ml = pd.read_csv("C:\\Users\\ViJAY\\Desktop\\Questions\\ml.txt", sep="\t")
stats = pd.read_csv("C:\\Users\\ViJAY\\Desktop\\Questions\\stats.txt", sep="\t")


class Actionreturninterview(Action):

    def name(self) -> Text:
        return "action_return_interview"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        try:
            topic = entities[0]['value']
            if topic=='python':
                que = py.python.values.tolist()
                for i in que:
                    dispatcher.utter_message(text=f"{i}")
        
            elif topic=='NLP':
                que = nlp.nlp.values.tolist()
                for i in que:
                    dispatcher.utter_message(text=f"{i}")

            elif topic=='ML':
                que = ml.ml.values.tolist()
                for i in que:
                    dispatcher.utter_message(text=f"{i}")
                    
            elif topic=='DL':
                que = dl.dl.values.tolist()
                for i in que:
                    dispatcher.utter_message(text=f"{i}")
                    
            elif topic=='DS':
                que = ds.ds.values.tolist()
                for i in que:
                    dispatcher.utter_message(text=f"{i}")
                    
            elif topic=='stats':
                que = stats.stats.values.tolist()
                for i in que:
                    dispatcher.utter_message(text=f"{i}")                    
        except:
            
            que = tracker.latest_message['text']
            que = que.split()
            que = '+'.join(que)

            url = f'https://www.google.com/search?q={que}&rlz=1C1CHBF_enIN926IN926&oq=kaggle&aqs=chrome.2.69i57j69i59j0i433i512j0i512l6.2219j0j15&sourceid=chrome&ie=UTF-8'
            driver = webdriver.Chrome('C:\\Users\\ViJAY\\Downloads\\chromedriver_win32\\chromedriver.exe')
            driver.get(url)

            a = driver.find_elements_by_xpath("//div[@class='yuRUbf']")
            for i in range(5):
                link = (a[i].find_element_by_tag_name('a').get_attribute('href'))
                dispatcher.utter_message(text=f"{link}")
                
        return []


class Actionreturndataset(Action):

    def name(self) -> Text:
        return "action_return_dataset"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        try:
            topic = entities[0]['value']
            if topic=='titanic':
                que = 'titanic'
                url = f'https://www.kaggle.com/search?q={que}'
                dispatcher.utter_message(text=f"Follow up this link for dataset \n{url}")
                          
        except:
            
            que = tracker.latest_message['text']
            que = que.split()
            que = '+'.join(que)
            url = f'https://www.kaggle.com/search?q={que}'
            dispatcher.utter_message(text=f"Follow up this link for dataset \n{url}")
                
        return []

           
