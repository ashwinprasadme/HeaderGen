from keras.mixed_precision import policy as policy
from keras.saving.saved_model import base_serialization as base_serialization, constants as constants, save_impl as save_impl, serialized_attributes as serialized_attributes
from keras.utils import generic_utils as generic_utils

class LayerSavedModelSaver(base_serialization.SavedModelSaver):
    @property
    def object_identifier(self): ...
    @property
    def python_properties(self): ...
    def objects_to_serialize(self, serialization_cache): ...
    def functions_to_serialize(self, serialization_cache): ...

def get_serialized(obj): ...

class InputLayerSavedModelSaver(base_serialization.SavedModelSaver):
    @property
    def object_identifier(self): ...
    @property
    def python_properties(self): ...
    def objects_to_serialize(self, serialization_cache): ...
    def functions_to_serialize(self, serialization_cache): ...

class RNNSavedModelSaver(LayerSavedModelSaver):
    @property
    def object_identifier(self): ...

class VocabularySavedModelSaver(LayerSavedModelSaver):
    @property
    def python_properties(self): ...
