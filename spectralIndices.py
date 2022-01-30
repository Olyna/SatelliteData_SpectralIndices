#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:36:48 2019

@author: Gounari Olympia
"""

import numpy as np

def bandsForIndices(satellite, bandsInOneTile):
    """
    satellite = string or integer. Abbreviation of satellite mission name.
    bandsInOneTile = list of paths for the bands of a record.
    red, nir, swir = string. Paths for the corresponding band, for each
                    satellite.
    """
    # If it is about Landsat 8
    if str(satellite) == 'L8':
        for imPath in bandsInOneTile:
            if '_B4' in imPath:
                red = imPath
            elif '_B5' in imPath:
                nir = imPath
            elif '_B6' in imPath:
                swir = imPath
    # If it is about Landsat 5
    elif str(satellite) == 'L5':
        for imPath in bandsInOneTile:
            if '_B3' in imPath:
                red = imPath
            elif '_B4' in imPath:
                nir = imPath
            elif '_B5' in imPath:
                swir = imPath
    # If it is about Sentinel 2
    elif str(satellite) == 'S2':
        for imPath in bandsInOneTile:
            if '_B04' in imPath:
                red = imPath
            elif '_B08' in imPath:
                nir = imPath
        swir = None

    else:
        print('Unable to discover bands for satellite {}'.format(satellite))
    return(red, nir, swir)



def calc_ndvi(nir, red):
    """
    nir, red = arrays
    res = array
    """
    # BE CAREFULL! Without this convertion, doesn't work correctly !
    red = red.astype(np.float32)
    nir = nir.astype(np.float32)
    res = (nir-red)/(nir+red)
    # (count, row, col)  Rasterio needs count=1
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res


def calc_msavi(nir, red):
    res =  (2 * nir + 1- np.sqrt((2 * nir + 1)**2 - 8*(nir-red))) / 2
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res

def calc_ndbi(swir, nir):
    swir = swir.astype(np.float32)
    nir = nir.astype(np.float32)
    res = (swir-nir)/(swir+nir)
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res

def calc_ndwi(nir, swir):   
    nir = nir.astype(np.float32)
    swir = swir.astype(np.float32)
    res = (nir-swir)/(nir+swir)
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res

def calc_evi(nir, red, blue):
    res = 2.5 * ((nir-red) / (nir + 6*red - 7.5*blue + 1))
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res

def calc_ndti(swir1, swir2):
    swir1 = swir1.astype(np.float32)
    swir2 = swir2.astype(np.float32)
    res = (swir1-swir2)/(swir1+swir2)
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res

def calc_tvi(nir, red, green):
    res = 0.5 * (120*(nir-green) - 200*(red-green))
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res

def calc_ndvi8a4(nir2, red):
    red = red.astype(np.float32)
    nir2 = nir2.astype(np.float32)
    res = (nir2-red)/(nir2+red)
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res


def calc_ndvi8a5(nir2, re1):
    re1 = re1.astype(np.float32)
    nir2 = nir2.astype(np.float32)
    res = (nir2-re1)/(nir2+re1)
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res


def calc_ndvi8a6(nir2, re2):
    re2 = re2.astype(np.float32)
    nir2 = nir2.astype(np.float32)
    res = (nir2-re2)/(nir2+re2)
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res

def calc_ndvi65(re2, re1):
    re1 = re1.astype(np.float32)
    re2 = re2.astype(np.float32)
    res = (re2-re1)/(re2+re1)
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res


def calc_ndvi75(re3, re1):
    re1 = re1.astype(np.float32)
    re3 = re3.astype(np.float32)
    res = (re3-re1)/(re3+re1)
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res


def calc_ndvi76(re3, re2):
    re2 = re2.astype(np.float32)
    re3 = re3.astype(np.float32)
    res = (re3-re2)/(re3+re2)
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res
