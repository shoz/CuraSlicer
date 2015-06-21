# -*- coding: utf-8 -*-

from CuraSlicer import profile
from CuraSlicer import sliceEngine
from CuraSlicer import objectScene
from CuraSlicer import meshLoader

def commandlineProgressCallback(progress):
    if progress >= 0:
        print 'Preparing: %d%%' % (progress * 100)

prof = sys.argv[0]
stl = sys.argv[1]
output = sys.argv[2]

def main():
    profile.loadPreferences(prof)
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
