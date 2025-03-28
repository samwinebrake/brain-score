from brainscore_vision import model_registry
from brainscore_vision.model_helpers.brain_transformation import ModelCommitment
from .model import get_model, get_layers

model_registry["mvimgnet_ss_05"] = lambda: ModelCommitment(
    identifier="mvimgnet_ss_05",
    activations_model=get_model("mvimgnet_ss_05"),
    layers=get_layers("mvimgnet_ss_05"),
)
