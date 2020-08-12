from django.apps import AppConfig

from ai.settings import DISCRIPTION_FEATURES, MODELS_NAMES
#from ai.common.functions import UpdateAcceptableIntevals

class AIConfig(AppConfig):
    name = 'ai'

    def ready(self):
        pass
        """
        Filling DISCRIPTION_FEATURES with unical code by using ordinary continuous values.
        """
        """code = 1

        for model in MODELS_NAMES:
            for item in DISCRIPTION_FEATURES[model]:
                item['code'] = code

                code += 1
        """
        """
        Updating pair ranges. See the definition of the varable 
        RANGES_NUMERICAL_FEATURES in settings.py to find more inf.
        """
        #UpdateAcceptableIntevals()