# -*- coding: utf-8 -*-

from CuraSlicer import profile
from CuraSlicer import sliceEngine
from CuraSlicer import objectScene
from CuraSlicer import meshLoader
import sys

def commandlineProgressCallback(progress):
    if progress >= 0:
        pass

def slicing(prof_filename, stl_filename, output_filename):
    profile.loadProfile(prof_filename)
    scene = objectScene.Scene()
    scene.updateMachineDimensions()
    engine = sliceEngine.Engine(commandlineProgressCallback)
    for m in meshLoader.loadMeshes(stl_filename):
        scene.add(m)
    engine.runEngine(scene)
    engine.wait()
    with open(output_filename, "wb") as f:
        result = engine.getResult()
        gcode = result.getGCode()
        printtime = result.getPrintTime()
        while True:
            data = gcode.read()
            if len(data) == 0:
                break
            f.write(data)
    print 'GCode file saved : %s' % output_filename
    print 'Printtime', printtime
    engine.cleanup()
    return printtime
