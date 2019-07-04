# sike_strat_draw
Tool to draw strategies for isogeny-based cryptography like SIKE protocol

Install :

"pip install sike_strat_draw"
or clone this repository and "pip install ." in sike_strat_draw directory

Dependencies :

The drawer module use a tool module named canvasvg in order to save drawing in a file.
This module can be downloaded here and installed with pip ("pip install ." in the canvas2svg directory) :
https://github.com/WojciechMula/canvas2svg/releases/tag/1.0.5
It can also be installed via PyPI : "pip install canvasvg"

Description :

Drawer class used to draw the strategy tree at each step, either an elliptic curve point doubling or an isogeny computation.
