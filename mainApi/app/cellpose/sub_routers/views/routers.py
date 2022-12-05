import asyncio
import concurrent
import os
import pydantic
from pydantic import BaseModel
import string
from tokenize import String
from PIL import Image
from fastapi.responses import JSONResponse, FileResponse
from fastapi.encoders import jsonable_encoder
from fastapi import (
    Request,
    Response,
    Body,
    APIRouter,
    Depends,
    status,
    UploadFile,
    File, Form, HTTPException
)
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List
import aiofiles
import jsons

import numpy as np
import time, os, sys
from urllib.parse import urlparse
import matplotlib.pyplot as plt
import matplotlib as mpl
#matplotlib inline
mpl.rcParams['figure.dpi'] = 300
from cellpose import utils, io
from cellpose import models
from cellpose.io import imread

from mainApi.app.auth.auth import get_current_user
from mainApi.app.db.mongodb import get_database
from mainApi.app.images.sub_routers.tile.models import AlignNaiveRequest, TileModelDB, AlignedTiledModel, NamePattenModel, MergeImgModel, ExperimentModel
from mainApi.app.images.utils.align_tiles import align_tiles_naive, align_ashlar
from mainApi.app.images.utils.file import save_upload_file, add_image_tiles, convol2D_processing
from mainApi.app.images.utils.experiment import add_experiment, get_experiment_data
from mainApi.app.images.utils.folder import get_user_cache_path, clear_path
from mainApi.app.auth.models.user import UserModelDB, PyObjectId
from mainApi.config import STATIC_PATH, CURRENT_STATIC
import tifftools

router = APIRouter(
    prefix="/view",
    tags=["view"],
)

# model = models.Cellpose(model_type='cyto')

# model = models.Cellpose(gpu=False, model_type='cyto')

# Upload Image file
@router.post("/updown_image",
             response_description="pageup/down Image",
             status_code=status.HTTP_201_CREATED,
             response_model=List[TileModelDB])
async def updown_image(request: Request,
                         clear_previous: bool = Form(False),
                             current_user: UserModelDB = Depends(get_current_user),
                             db: AsyncIOMotorDatabase = Depends(get_database)) -> List[TileModelDB]:
    # model_type='cyto' or 'nuclei' or 'cyto2'
    # model = models.Cellpose(model_type='cyto')

    # list of files
    # PUT PATH TO YOUR FILES HERE!
    files = ['http://www.cellpose.org/static/images/img02.png']

    imgs = [imread(f) for f in files]
    nimg = len(imgs)

    io.save_to_png(imgs, "img2")

    # define CHANNELS to run segementation on
    # grayscale=0, R=1, G=2, B=3
    # channels = [cytoplasm, nucleus]
    # if NUCLEUS channel does not exist, set the second channel to 0
    channels = [[0, 0]]
    # IF ALL YOUR IMAGES ARE THE SAME TYPE, you can give a list with 2 elements
    # channels = [0,0] # IF YOU HAVE GRAYSCALE
    # channels = [2,3] # IF YOU HAVE G=cytoplasm and B=nucleus
    # channels = [2,1] # IF YOU HAVE G=cytoplasm and R=nucleus

    # if diameter is set to None, the size of the cells is estimated on a per image basis
    # you can set the average cell `diameter` in pixels yourself (recommended)
    # diameter can be a list or a single number for all images

    # masks, flows, styles, diams = model.eval(imgs, diameter=None, channels=channels)
    # # I will download images from website
    # urls = ['http://www.cellpose.org/static/images/img02.png',
    #         'http://www.cellpose.org/static/images/img03.png',
    #         'http://www.cellpose.org/static/images/img05.png']
    # files = []
    # for url in urls:
    #     parts = urlparse(url)
    #     filename = os.path.basename(parts.path)
    #     if not os.path.exists(filename):
    #         sys.stderr.write('Downloading: "{}" to {}\n'.format(url, filename))
    #         utils.download_url_to_file(url, filename)
    #     files.append(filename)
    #
    # # REPLACE FILES WITH YOUR IMAGE PATHS
    # # files = ['img0.tif', 'img1.tif']
    # channels = [[0, 0]]
    # # view 1 image
    # img = io.imread(files[-1])
    # masks, flows, styles, diams = model.eval(imgs, diameter=None, channels=channels)
    # # masks, flows, styles, diams = model.eval(img, diameter=None, channels=chan)
    #
    # # save results so you can load in gui
    # io.masks_flows_to_seg(img, masks, flows, diams, files[-1], chan)
    #
    # # save results as png
    # io.save_to_png(img, masks, flows, files[-1])
    # plt.figure(figsize=(2, 2))
    # plt.imshow(img)
    # plt.axis('off')
    # plt.show()
    # current_user_path = os.path.join(STATIC_PATH, str(PyObjectId(current_user.id)))
    # if not os.path.exists(current_user_path):
    #     os.makedirs(current_user_path)
    # else:
    #     for f in os.listdir(current_user_path):
    #         os.remove(os.path.join(current_user_path, f))
    #     res = await db['tile-image-cache'].delete_many({"user_id": PyObjectId(current_user.id)})
    #
    # imgs = [imread(f) for f in files]
    # nimg = len(imgs)
    # io.save_to_png(imgs, masks, flows, image_names)
    # for each_file in files:
    #     file_path = os.path.join(current_user_path, each_file.filename)
    #     async with aiofiles.open(file_path, 'wb') as f:
    #         content = await each_file.read()
    #         nimg = len(content)
    #         channels = [[0, 0]]
    #         masks, flows, styles, diams = model.eval(imgs, diameter=None, channels=channels)
    #         await f.write(content)

    return JSONResponse({"success": "success"})