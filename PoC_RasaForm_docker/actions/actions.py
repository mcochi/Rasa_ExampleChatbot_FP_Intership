from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

import requests
from codaio import Coda
import ssl

class ValidateRestaurantForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_restaurant_form"

    @staticmethod
    def cuisine_db() -> List[Text]:
        """Database of supported cuisines"""

        return ["caribbean", "chinese", "french"]

    def validate_cuisine_slot(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if slot_value.lower() in self.cuisine_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            #dispatcher.utter_message(text='Hellos!!!')
            return {"cuisine_slot": slot_value}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            dispatcher.utter_message(text="Sorry but we haven't got that class of food. We have Caribbean, Chinese and French food")
            return {"cuisine_slot": None}

# Testing Custom Actions
class ActionLaunchHelloWorld(Action):
    def name(self) -> Text:
        return "action_launch_hello_world"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        dispatcher.utter_message(text="Hello World!")
        return[]

# Testing api rest get
class ActionCallApi(Action):
    def name(self) -> Text:
        return "action_call_api"
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        
        #r = requests.get('http://192.168.1.34:3010')
        dispatcher.utter_message(text='r.text')
        return[]

# Testing store data on Coda

class ActionPostDinnerCoda(Action):
    def name(self) -> Text:
        return "action_post_dinner_coda"
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        
        dispatcher.utter_message(text='Storing Booking')
        cuisine = tracker.get_slot('cuisine_slot')
        numberofpeople = tracker.get_slot('num_people')
        API_KEY = '3bba5e87-358c-498c-9e19-01ee158fddd0'
        docid="hiDjxzDYZT"
        tabid = "grid-VaHaPUZKkn"
        columnid = "c-NXfRNP3U0x" #Tipo Comida
        columnind = "c-FOYgcNlXos" # Número de comensales
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
        
        coda = Coda(API_KEY)
        payload = {
                        'rows': [
                        {   
                    'cells': [
                        {'column': columnid, 'value': cuisine},
                        {'column': columnind, 'value': numberofpeople}
                        ],
                        },
                        ],
                    "keyColumns" : [
                        columnid
                        ]
        }
        coda.upsert_row(docid, tabid, payload)
        return[]
    