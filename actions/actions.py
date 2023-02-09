from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
# import json
# import logging
# import os
# import random
from rasa_sdk.executor import CollectingDispatcher

from typing import DefaultDict, Text, Callable, Dict, List, Any, Optional
from collections import defaultdict

from rasa_sdk import utils, Tracker, Action


class ActionPengajian(ActionQueryKnowledgeBase):
    def name(self) -> Text:
        return "action_query_pengajian"

    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("knowledge_base/pengajian.json")

        knowledge_base.set_representation_function_of_object(
            "pengajian", lambda obj: obj["nama"]
        )
        super().__init__(knowledge_base)
 
    def utter_attribute_value(
        self,
        dispatcher: CollectingDispatcher,
        object_name: Text,
        attribute_name: Text,
        attribute_value: Text,
    ):
        if attribute_value:
            dispatcher.utter_message(
                text=f"{attribute_value}."
            )
        else:
            dispatcher.utter_message(
                text=f"Mohon maaf, saya tidak tahu tentang {attribute_name} pada {object_name}."
            )
    
    async def utter_objects(
        self,
        dispatcher: CollectingDispatcher,
        object_type: Text,
        objects: List[Dict[Text, Any]],
    ):
        if objects:
            repr_function = await utils.call_potential_coroutine(
                self.knowledge_base.get_representation_function_of_object(object_type)
            )

            if len(objects) == 1:
                for i, obj in enumerate(objects, 1):
                    dispatcher.utter_message(text=f"{object_type} {repr_function(obj)}")
            else:
                dispatcher.utter_message(
                    text=f"Disini ada beberapa {object_type} seperti :",
                )
                for i, obj in enumerate(objects, 1):
                    dispatcher.utter_message(text=f"{i}: {repr_function(obj)}")
            
        else:
            dispatcher.utter_message(
                text=f"Maaf, saya kurang paham mengenai informasi {object_type} tersebut."
            )

class ActionSolat(ActionQueryKnowledgeBase):
    def name(self) -> Text:
        return "action_query_solat"

    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("knowledge_base/solat.json")

        knowledge_base.set_representation_function_of_object(
            "solat", lambda obj: obj["nama"]
        )
        super().__init__(knowledge_base)
 
    def utter_attribute_value(
        self,
        dispatcher: CollectingDispatcher,
        object_name: Text,
        attribute_name: Text,
        attribute_value: Text,
    ):
        if attribute_value:
            dispatcher.utter_message(
                text=f"{attribute_value}."
            )
        else:
            dispatcher.utter_message(
                text=f"Mohon maaf, saya tidak tahu tentang {attribute_name} pada {object_name}."
            )
    
    async def utter_objects(
        self,
        dispatcher: CollectingDispatcher,
        object_type: Text,
        objects: List[Dict[Text, Any]],
    ):
        if objects:
            repr_function = await utils.call_potential_coroutine(
                self.knowledge_base.get_representation_function_of_object(object_type)
            )

            if len(objects) == 1:
                for i, obj in enumerate(objects, 1):
                    dispatcher.utter_message(text=f"{object_type} {repr_function(obj)}")
            else:
                dispatcher.utter_message(
                    text=f"Ada beberapa {object_type} yang saya tahu seperti :",
                )
                for i, obj in enumerate(objects, 1):
                    dispatcher.utter_message(text=f"{i}: {repr_function(obj)}")
        else:
            dispatcher.utter_message(
                text=f"Maaf, saya kurang paham mengenai informasi {object_type} tersebut."
            )

class ActionPenyakit(ActionQueryKnowledgeBase):
    def name(self) -> Text:
        return "action_query_penyakit"

    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("knowledge_base/penyakit.json")

        knowledge_base.set_representation_function_of_object(
            "penyakit", lambda obj: obj["nama"]
        )
        super().__init__(knowledge_base)
 
    def utter_attribute_value(
        self,
        dispatcher: CollectingDispatcher,
        object_name: Text,
        attribute_name: Text,
        attribute_value: Text,
    ):
        print(object_name)
        print(attribute_name)
        if attribute_value:
            if type(attribute_value) is list:
                for i in attribute_value:
                    dispatcher.utter_message(
                        text=f"{i}."
                    )
            else:
                dispatcher.utter_message(
                    text=f"{attribute_value}."
                )
        else:
            dispatcher.utter_message(
                text=f"Mohon maaf, saya tidak tahu tentang {attribute_name} pada {object_name}."
            )
    
    async def utter_objects(
        self,
        dispatcher: CollectingDispatcher,
        object_type: Text,
        objects: List[Dict[Text, Any]],
    ):
        if objects:
            repr_function = await utils.call_potential_coroutine(
                self.knowledge_base.get_representation_function_of_object(object_type)
            )

            if len(objects) == 1:
                for i, obj in enumerate(objects, 1):
                    dispatcher.utter_message(text=f"{object_type} {repr_function(obj)}")
            else:
                dispatcher.utter_message(
                    text=f"Saya mengetahui tentang beberapa {object_type} seperti :",
                )
                for i, obj in enumerate(objects, 1):
                    dispatcher.utter_message(text=f"{i}: {repr_function(obj)}")
            
        else:
            dispatcher.utter_message(
                text=f"Maaf, saya kurang paham mengenai informasi {object_type} tersebut."
            )

class ActionObat(ActionQueryKnowledgeBase):
    def name(self) -> Text:
        return "action_query_obat"

    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("knowledge_base/obat.json")

        knowledge_base.set_representation_function_of_object(
            "obat", lambda obj: obj["nama"]
        )
        super().__init__(knowledge_base)
 
    def utter_attribute_value(
        self,
        dispatcher: CollectingDispatcher,
        object_name: Text,
        attribute_name: Text,
        attribute_value: Text,
    ):
        if attribute_value:
            dispatcher.utter_message(
                text=f"{attribute_value}."
            )
        else:
            dispatcher.utter_message(
                text=f"Mohon maaf, saya tidak tahu tentang {attribute_name} pada {object_name}."
            )
    
    async def utter_objects(
        self,
        dispatcher: CollectingDispatcher,
        object_type: Text,
        objects: List[Dict[Text, Any]],
    ):
        if objects:
            repr_function = await utils.call_potential_coroutine(
                self.knowledge_base.get_representation_function_of_object(object_type)
            )

            if len(objects) == 1:
                for i, obj in enumerate(objects, 1):
                    dispatcher.utter_message(text=f"{object_type} {repr_function(obj)}")
            else:
                dispatcher.utter_message(
                    text=f"Ada beberapa {object_type} yang saya tahu seperti :",
                )
                for i, obj in enumerate(objects, 1):
                    dispatcher.utter_message(text=f"{i}: {repr_function(obj)}")
        else:
            dispatcher.utter_message(
                text=f"Maaf, saya kurang paham mengenai informasi {object_type} tersebut."
            )

class ActionKegiatan(ActionQueryKnowledgeBase):
    def name(self) -> Text:
        return "action_query_kegiatan"

    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("knowledge_base/kegiatan.json")

        knowledge_base.set_representation_function_of_object(
            "kegiatan", lambda obj: obj["nama"]
        )
        super().__init__(knowledge_base)
 
    async def utter_objects(
        self,
        dispatcher: CollectingDispatcher,
        object_type: Text,
        objects: List[Dict[Text, Any]],
    ):
        if objects:
            dispatcher.utter_message(
                text=f"Sekarang Saatnya :",
            )
        
            repr_function = await utils.call_potential_coroutine(
                self.knowledge_base.get_representation_function_of_object(object_type)
            )
            for i, obj in enumerate(objects, 1):
                dispatcher.utter_message(text=f"{repr_function(obj)}")
        else:
            dispatcher.utter_message(
                text=f"Tidak ada {object_type}."
            )

class ActionUlangTahun(ActionQueryKnowledgeBase):
    def name(self) -> Text:
        return "action_query_ulang_tahun"

    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("knowledge_base/personal.json")

        knowledge_base.set_representation_function_of_object(
            "personal", lambda obj: obj["nama_orang"]
        )
        super().__init__(knowledge_base)
 
    async def utter_objects(
        self,
        dispatcher: CollectingDispatcher,
        object_type: Text,
        objects: List[Dict[Text, Any]],
    ):
        if objects:
            print(objects[0]['lagu_favorit'])
            dispatcher.utter_message(
                text=f"selamat ulang tahun untuk:",
            )
        
            repr_function = await utils.call_potential_coroutine(
                self.knowledge_base.get_representation_function_of_object(object_type)
            )
            for i, obj in enumerate(objects, 1):
                dispatcher.utter_message(text=f"{repr_function(obj)}")

            dispatcher.utter_message(
                text=f"Semoga selalu sehat dan bahagia.",
            )
        else:
            dispatcher.utter_message(
                text=f"Tidak ada yang '{object_type}'."
            )

class ActionLaguKesukaan(ActionQueryKnowledgeBase):
    def name(self) -> Text:
        return "action_query_lagu_kesukaan"

    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("knowledge_base/personal.json")

        knowledge_base.set_representation_function_of_object(
            "personal", lambda obj: obj["nama_orang"]
        )
        super().__init__(knowledge_base)
    
    async def utter_objects(
        self,
        dispatcher: CollectingDispatcher,
        object_type: Text,
        objects: List[Dict[Text, Any]],
    ):
        if objects:
            data = objects[0]['lagu_favorit']
            print(objects)
            dispatcher.utter_message(
                text=f"Mau putar lagu yang mana:",
            )
            for i, obj in enumerate(data, 1):
                dispatcher.utter_message(text=f"{i}: {obj}")
        else:
            dispatcher.utter_message(
                text=f"Maaf saya tidak tahu {object_type} anda."
            )

class ActionAskAgain(Action):

    def name(self) -> Text:
        return "action_ask_again"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        object_type = tracker.get_slot("object_type")
        if not object_type:
            dispatcher.utter_message(text=f"Maaf, saya tidak mengerti tentang {object_type}.")
        else:
            dispatcher.utter_message(text=f"Langsung tanyakan saja jika ada pertanyaan tentang {object_type} lagi, atau ingin menanyakan tentang hal lain?")
        return []