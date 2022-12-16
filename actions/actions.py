# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import logging
import json
from typing import Dict, Text, Any, List
from rasa_sdk import Tracker
from rasa_sdk import Action
from rasa.core import run
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
    ActionReverted,
)
logger = logging.getLogger(__name__)

class ActionFaqs(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        return "action_faqs"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in [
            "deep_learning",
            "machine_learning",
            "cnn_nn",
            "rnn_nn",
            "lstm_nn",
            "gan_nn",
            "rbfn_nn",
            "mlp_nn",           
            "som_nn",
            "dbn_nn",
            "rbm_nn",
            "autoencoders"
            ]:
            dispatcher.utter_message(template=f"utter_{intent}")

        return []

# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
