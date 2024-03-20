from brainscore_vision.model_helpers.check_submission import check_models
import functools
import os
import torchvision.models
from brainscore_vision.model_helpers.activations.pytorch import PytorchWrapper
from brainscore_vision.model_helpers.activations.pytorch import load_preprocess_images
from pathlib import Path
from brainscore_vision.model_helpers import download_weights
import torch

# This is an example implementation for submitting resnet-50 as a pytorch model

# Attention: It is important, that the wrapper identifier is unique per model!
# The results will otherwise be the same due to brain-scores internal result caching mechanism.
# Please load your pytorch model for usage in CPU. There won't be GPUs available for scoring your model.
# If the model requires a GPU, contact the brain-score team directly.
from brainscore_vision.model_helpers.check_submission import check_models


def get_model_list():
    return ['bp_resnet50_julios']


def get_model(name):
    assert name == 'bp_resnet50_julios'
    model = torch.load('brainscore_vision/models/bp_resnet50_julios/bp_export.pt')
    # download_weights(
    # bucket='brainscore-vision', 
    # folder_path='models/resnet50-deepdive-2',
    # filename_version_sha=[('ckpt.pth', 'C722T4BityNPpazdXWiAeu8pGBxKIudb', '0186929df5d04451995d94cd332a3603a00594fe')],
    # save_directory=Path(__file__).parent)
    # ckpt_path = os.path.join(os.path.dirname(__file__), 'ckpt.pth')
    # state_dict = torch.load(ckpt_path, map_location=torch.device('cpu'))
    # model.load_state_dict(state_dict)
    
    preprocessing = functools.partial(load_preprocess_images, image_size=224)
    print(preprocessing)
    wrapper = PytorchWrapper(identifier='bp_resnet50_julios', model=model, preprocessing=preprocessing)
    wrapper.image_size = 224
    return wrapper


def get_layers(name):
    assert name == 'bp_resnet50_julios'
    return ['layer1', 'layer2', 'layer3', 'layer4']  


def get_bibtex(model_identifier):
    return """xx"""


if __name__ == '__main__':
    check_models.check_base_models(__name__)