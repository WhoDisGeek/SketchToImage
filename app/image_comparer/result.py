import numpy as np
import argparse
import imutils
import cv2
import os
import numpy as np
import sys
from numpy import dot
from numpy.linalg import norm
import operator
import shutil

targetdir = '/home/prime/Django-Projects/SketchToImage/media/feature_vectors/target'
gandir = '/home/prime/Django-Projects/SketchToImage/media/feature_vectors/gen'


def main():
    ganvectors = {}

    for gansubdir, gandirs, ganfiles in os.walk(gandir):
        for ganfile in ganfiles:
            ganpath = os.path.join(gansubdir, ganfile)

            with open(ganpath) as f:
                ganlines = f.read().splitlines()

            for x in range(0, len(ganlines)):
                ganlines[x] = float(ganlines[x])

            similaritylist = []
            for targetsubdir, targetdirs, targetfiles in os.walk(targetdir):
                for targetfile in targetfiles:
                    targetpath = os.path.join(targetsubdir, targetfile)

                    with open(targetpath) as f:
                        targetlines = f.read().splitlines()

                    for x in range(0, len(targetlines)):
                        targetlines[x] = float(targetlines[x])

                    similaritylist.append(dot(targetlines, ganlines) / (norm(targetlines) * norm(ganlines)))
            end = ganfile.find('.')
            ganvectors[ganfile[0:end] + '.png'] = max(similaritylist)

    sortvector = sorted(ganvectors.items(), key=operator.itemgetter(1), reverse=True)
    retlist = []
    for i in range(5):
        print('similar images file name..')
        print(sortvector[i][0])
        retlist.append(sortvector[i][0])
    return retlist