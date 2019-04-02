from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_nlu.components import Component

from .correction_functions import correct_user_input


class Autocorrect(Component):
    name = "autocorrect"
    provides = []
    requires = []
    defaults = {}
    language_list = None

    def __init__(self, component_config=None, nlp=None):

        self.nlp = nlp
        super(Autocorrect, self).__init__(component_config)

    def process(self, message, **kwargs):

        message.text = correct_user_input(message.text)

    def train(self, training_data, cfg, **kwargs):

        pass

    def persist(self, model_dir):

        pass

    @classmethod
    def load(cls, model_dir=None, model_metadata=None, cached_component=None,
             **kwargs):

        if cached_component:
            return cached_component
        else:
            component_config = model_metadata.for_component(cls.name)
            return cls(component_config)
