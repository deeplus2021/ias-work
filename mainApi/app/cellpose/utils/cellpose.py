import sys, os, pathlib, warnings, datetime, tempfile, glob, time
import gc
from natsort import natsorted
from tqdm import tqdm, trange

import PyQt5
from PyQt5 import QtGui, QtCore, Qt, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QScrollBar, QSlider, QComboBox, QGridLayout, \
    QPushButton, QFrame, QCheckBox, QLabel, QProgressBar, QLineEdit, QMessageBox, QGroupBox
import pyqtgraph as pg
from pyqtgraph import GraphicsScene

import numpy as np
from scipy.stats import mode
import cv2
    
def update_plot():
    selected = 0
    X2 = 0
    resize = -1
    onechan = False
    loaded = False
    channel = [0, 1]
    current_point_set = []
    in_stroke = False
    strokes = []
    stroke_appended = True
    ncells = 0
    zdraw = []
    removed_cell = []
    cellcolors = np.array([255, 255, 255])[np.newaxis, :]
    # -- set menus to default -- #
    color = 0
    view = 0


    # -- zero out image stack -- #
    opacity = 128  # how opaque masks should be
    outcolor = [200, 200, 255, 200]
    NZ, Ly, Lx = 1, 512, 512
    saturation = [[0, 255] for n in range(NZ)]
    currentZ = 0
    flows = [[], [], [], [], [[]]]
    stack = np.zeros((1, Ly, Lx, 3))
    # masks matrix
    layerz = 0 * np.ones((Ly, Lx, 4), np.uint8)
    # image matrix with a scale disk
    radii = 0 * np.ones((Ly, Lx, 4), np.uint8)
    cellpix = np.zeros((1, Ly, Lx), np.uint32)
    outpix = np.zeros((1, Ly, Lx), np.uint32)
    ismanual = np.zeros(0, 'bool')
    filename = []
    loaded = False
    recompute_masks = False

    img = pg.ImageItem(viewbox=self.p0, parent=self)
    Ly, Lx, _ = stack[currentZ].shape
    if view == 0:
        image = stack[currentZ]
        img.setImage(image, autoLevels=False, lut=None)
        img.setLevels(saturation[currentZ])
    else:
        image = np.zeros((Ly, Lx), np.uint8)
        if len(flows) >= view - 1 and len(flows[view - 1]) > 0:
            image = flows[view - 1][currentZ]
        if view > 1:
            img.setImage(image, autoLevels=False, lut=bwr)
        else:
            img.setImage(image, autoLevels=False, lut=None)
        img.setLevels([0.0, 255.0])
    scale.setImage(radii, autoLevels=False)
    scale.setLevels([0.0, 255.0])
    # img.set_ColorMap(bwr)
    if NZ > 1 and orthobtn.isChecked():
        update_ortho()

    slider.setLow(saturation[currentZ][0])
    slider.setHigh(saturation[currentZ][1])
    win.show()
    show()