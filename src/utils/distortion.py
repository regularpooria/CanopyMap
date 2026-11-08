from defisheye import Defisheye

# Correction parameters
img_kwargs = {"fov": 116, "pfov": 100, "dtype": "equalarea", "format": "fullframe"}


def de_fish_eye_image(path: str):
    obj = Defisheye(path, **img_kwargs)
    return obj.convert()
