# -*- coding: utf-8 -*-

from CuraSlicer import profile
from CuraSlicer import sliceEngine
from CuraSlicer import objectScene
from CuraSlicer import meshLoader
import sys

def commandlineProgressCallback(progress):
    if progress >= 0:
        print 'Preparing: %d%%' % (progress * 100)

prof = sys.argv[1]
stl = sys.argv[2]
output = sys.argv[3]

def main():
    profile.loadProfile(prof)
    scene = objectScene.Scene()
    scene.updateMachineDimensions()
    engine = sliceEngine.Engine(commandlineProgressCallback)
    for m in meshLoader.loadMeshes(stl):
        print m
        scene.add(m)
    engine.runEngine(scene)
    engine.wait()
    with open(output, "wb") as f:
        gcode = engine.getResult().getGCode()
        print len(gcode)
        while True:
            data = gcode.read()
            if len(data) == 0:
                break
            f.write(data)
    print 'GCode file saved : %s' % output
    engine.cleanup()

if __name__ == '__main__':
    main()
