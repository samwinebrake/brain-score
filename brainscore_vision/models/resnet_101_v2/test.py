import pytest
import brainscore_vision


@pytest.mark.travis_slow
def test_has_identifier():
    model = brainscore_vision.load_model('resnet_101_v2')
    assert model.identifier == 'resnet_101_v2'
