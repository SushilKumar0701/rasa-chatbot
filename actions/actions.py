# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



# class ActionHelp(Action):

#     def name(self) -> Text:
#         return "action_loginhelp"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         buttons = [
#             {
#                 "payload": "/login",
#                 "title": "How to Login"
#             },
#             {
#                 "payload": "/forgot_password",
#                 "title": "Forgot password"
#             },
#             {
#                 "payload": "/change_password",
#                 "title": "Change password"
#             },
#             {
#                 "title": "Other help",
#                 "url": "https://www.integrichain.com/",
#                 "type": "web_url"
#             }
#         ]
#         dispatcher.utter_message(text="How can I help you?", buttons=buttons)

#         return []

class ActionHelp(Action):
    def name(self) -> Text:
        return "action_help"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "About Us",
                        "subtitle": "Integrichain",
                        "image_url": "https://mma.prnewswire.com/media/1218115/IntegriChain_Logo.jpg?p=facebook",
                        "buttons": [
                            {
                                "title": "About Company",
                                "payload": "/about_company",
                                "type": "postback"
                            },
                            {
                                "title": "Location",
                                "url": "https://goo.gl/maps/Jvn3X3ikNBW1cNWSA",
                                "type": "web_url"
                            },
                            {
                                "title": "Learn More",
                                "url": "https://www.integrichain.com/about-us/",
                                "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "About company Policy",
                        "subtitle": "Integrichain",
                        "image_url": "https://image.shutterstock.com/image-photo/compliance-rules-law-regulation-policy-260nw-1049316146.jpg",
                        "buttons": [
                            {
                                "title": "About Policy",
                                "payload": "/company_policy",
                                "type": "postback"
                            },
                            {
                                "title": "Want More",
                                "payload": "/more_policy",
                                "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Career in Integrichain",
                        "subtitle": "Integrichain",
                        "image_url": "https://thumbs.dreamstime.com/b/career-development-chart-hand-drawing-blackboard-56251425.jpg",
                        "buttons": [
                            {
                                "title": "Career",
                                "payload": "/career",
                                "type": "postback"
                            },
                            {
                                "title": "Click here",
                                "url": "https://www.integrichain.com/careers/",
                                "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        }
        dispatcher.utter_message(attachment=message)
        return []

class ActionMore(Action):
    def name(self) -> Text:
        return "action_morepolicy"

    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements":[
                    {
                        "title": "Policies",
                        "subtitle": "Integrichain",
                        "image_url": "https://thumbs.dreamstime.com/b/policy-procedure-illustration-traffic-sign-words-133548245.jpg",
                        "buttons": [
                            {
                                "title": "Leave Policy",
                                "payload": "/leave_policy",
                                "type": "postback"
                            },
                            {
                                "title": "Work from home policy",
                                "payload": "/wfh_policy",
                                "type": "postback"
                            },
                            {
                                "title": "Referral bonus policy",
                                "payload": "/referral_policy",
                                "type": "postback"
                            },
                            {
                                "title": "Employee Benefit Policy",
                                "payload": "/emp_policy",
                                "type": "postback"
                            },
                            {
                                "title": "Leave Travel allowance",
                                "payload": "/travel_policy",
                                "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Learn more about policy",
                        "subtitle": "Integrichain",
                        "image_url": "http://retaildesignblog.net/wp-content/uploads/2018/01/IntegriChain-office-by-Studio-IQL-Philadelphia-USA.jpg",
                        "buttons": [
                            {
                                "title": "Learn more",
                                "url": "https://www.integrichain.com/",
                                "type": "web_url"
                            }
                        ]
                    }
                ]
            }
        }
        dispatcher.utter_message(attachment=message)
        return []