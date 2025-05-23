from brainscore_vision import stimulus_set_registry
from brainscore_vision.data_helpers.s3 import load_stimulus_set_from_s3

BIBTEX = """@article{hendrycks2019benchmarking,
  title={Benchmarking neural network robustness to common corruptions and perturbations},
  author={Hendrycks, Dan and Dietterich, Thomas},
  journal={arXiv preprint arXiv:1903.12261},
  year={2019}
}"""

# stimulus set: imagenet_c.noise
stimulus_set_registry['imagenet_c.noise'] = lambda: load_stimulus_set_from_s3(
    identifier="imagenet_c.noise",
    bucket="brainscore-storage/brainio-brainscore",
    csv_sha1="56f445e058b4d825e7731711c824918812ed2d2d",
    zip_sha1="e3c46b81bfd8a522cadcd8a4bb0c67bb5ccb4c6a",
    csv_version_id="null",
    zip_version_id="null")

# stimulus set: imagenet_c.blur
stimulus_set_registry['imagenet_c.blur'] = lambda: load_stimulus_set_from_s3(
    identifier="imagenet_c.blur",
    bucket="brainscore-storage/brainio-brainscore",
    csv_sha1="e7a537bb2f3f94b9cd3819a529de9f4349e58bd2",
    zip_sha1="85bac6d7c9b9646b22480f65cf6f1486fcf4b488",
    csv_version_id="null",
    zip_version_id="null")

# stimulus set: imagenet_c.weather
stimulus_set_registry['imagenet_c.weather'] = lambda: load_stimulus_set_from_s3(
    identifier="imagenet_c.weather",
    bucket="brainscore-storage/brainio-brainscore",
    csv_sha1="02fa92430be754163ecd06ee9211c1edd8984207",
    zip_sha1="18ef85343b10a4a326b5fc0758b9ae1da58f7d90",
    csv_version_id="null",
    zip_version_id="null")

# stimulus set: imagenet_c.digital
stimulus_set_registry['imagenet_c.digital'] = lambda: load_stimulus_set_from_s3(
    identifier="imagenet_c.digital",
    bucket="brainscore-storage/brainio-brainscore",
    csv_sha1="1e9611b560333989d4673bfd019160a27842f89b",
    zip_sha1="a10e8d7eabce191d1f8e92983c08b4f0fe0f435d",
    csv_version_id="null",
    zip_version_id="null")
