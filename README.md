# Slides Recognition Tool
> Match the given frames from a lecture video to the original slides.

[![Language](https://img.shields.io/badge/language-python3-blue.svg?style=flat)](https://www.python.org)
[![Module](https://img.shields.io/badge/module-opencv-brightgreen.svg?style=flat)](https://pypi.org/project/opencv-python/)

Made as a part of Digital Signal Analysis Course (DSAA) Final Project alongwith two other team members [Arnav Juneja](https://github.com/vivacejr/) and [Preet Thakkar](https://github.com/preet021). Given two sets of images stored in folders named - `Slides` and `Frames` - the script will output the corresponding matching ppt slide for each frame.

## Dependencies
>All the dependencies are stored in `requirements.txt` file. 

Following command can help install those on Linux:

```sh
pip install -r requirements.txt
```

## Usage
> The `script.py` contains the code to classify the frames images.
- Run the following command on terminal:
```sh
python3 script.py <path-to-frames-folder> <path-to-slides-folder>
```
- This generates a result.txt file, containing a mapping of each frame to its corresponding slide.
- While the code runs, it also displays running accuracy on the data processed so far (as we have kept the names of images in some particular manner for now).
- `check.py` script can check the accuracy of the output stored in `results.txt` according to the present naming convention. This script can be changed according to the requirement.