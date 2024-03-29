from importlib import reload
import variableSpacing.spacingAreas
reload(variableSpacing.spacingAreas)

from variableSpacing.spacingAreas import *

# --------
# settings
# --------

designspacePath = '/hipertipo/tools/VariableSpacing/demos/Roboto/Roboto.designspace'

L = dict(weight=400, spacing=0)

x, y = 30, 440
s    = 0.05
lh   = 1.1
upm  = 2048

txt = '''\
nhnmnuninjnln
noncnbndnpnqn
nanengnsnrnfntn
nvnwnknynxnzn
'''

parameters = {
    'scale'    : s,
    'location' : L,
    'glyphParameters' : {
        'color1'  : (0, 1, 0), # inner
        'color2'  : (1, 0, 0), # outer
        'color3'  : (1,),      # glyph
        'ySteps'  : 50,
        'yMin'    : 0,
        'yMax'    : 'xHeight',
        'xFactor' : 0.3,
        'dMax'    : 320, 
    }
}

# -----
# draw!
# -----

size('A4Landscape')
fill(1)
rect(0, 0, width(), height())

for txtLine in txt.split('\n'):
    S = SpacingAreasLine(designspacePath)
    S.setParameters(parameters)
    S.draw(txtLine, (x, y))
    translate(0, -upm*s*lh)

# saveImage('acefgrstzj_2.png')
