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
            if '_B4' in imPath or '_B04' in imPath:
                red = imPath
            elif '_B8' in imPath or '_B08' in imPath:
                nir = imPath

    else:
        print('Unable to discover bands for satellite {}'.format(satellite))
    return(red, nir, swir)



def calc_ndvi(nir, red):
    """
    nir, red = arrays
    res = array
    """
    res = (nir-red)/(nir+red)
    # (count, row, col)  Rasterio needs count=1
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res

def calc_msavi(nir, red):
    res =  (2 * nir + 1- np.sqrt((2 * nir + 1)**2 - 8*(nir-red))) / 2
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res

def calc_ndbi(swir, nir):
    res = (swir-nir)/(swir+nir)
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res

def calc_ndwi(nir, swir):
    res = (nir-swir)/nir+swir
    res = res.reshape(1, res.shape[0], res.shape[1])
    return res