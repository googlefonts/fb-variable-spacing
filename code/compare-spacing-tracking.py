import sys, os

folder = os.getcwd()

try:
    import variableSpacing
except:
    variableSpacingPath = os.path.join(folder, 'Lib')
    sys.path.append(variableSpacingPath)
    import variableSpacing

from importlib import reload
import variableSpacing.spacingSetter
reload(variableSpacing.spacingSetter)

from variableSpacing.spacingSetter import *

# ---------
# functions
# ---------

def setup():
    blendMode('multiply')
    fill(1)
    rect(0, 0, height(), width())
    fill(0)
    font('Menlo')
    fontSize(9)

def drawColorCaptions(glyphBox=True, kerning=True, tracking=True):
    captions = {
        'glyph box' : colorBox,
        'kerning'   : colorKerning,
        'tracking'  : colorTracking,
    }
    x = width() / 2
    y = height() - 30
    col = 100
    _captions = {}
    if glyphBox:
        _captions['glyph box'] = captions['glyph box']
    if kerning:
        _captions['kerning']   = captions['kerning']
    if tracking:
        _captions['tracking']  = captions['tracking']
    with savedState():
        for label, color in _captions.items():
            fill(*color)    
            rect(x, y-4, 12, 12)
            fill(0)
            text(label, (x + 20, y))
            translate(col, 0)

def drawTracking(x, y, t, s, L, steps, lh, mode=0):
    _y = y
    for i in range(steps):
        if mode == 0:
            tracking = i * t -(t*2)
        elif mode == 1:
            tracking = 100 - (i * -t // 2)
        else:
            tracking = i * t // 2

        S.tracking = tracking
        S.draw(txt, (x, _y), s, L)
        text(str(tracking), (x-30, _y))
        _y -= S.fontInfo.unitsPerEm * s * lh

def drawSpacing(x, y, t, s, L, steps, lh, mode=0):
    _y = y
    for i in range(steps):
        if mode == 0:
            spac = (i-2) * t * 4 / (steps-1)
        elif mode == 1:
            spac = 100 - (i * -t * 2 / (steps-1))
        else:
            spac = i * t * 2 / (steps-1)
        L = dict(width=0, weight=400, spacing=spac, contrast=0, slant=0)
        S.draw(txt, (x, _y), s, L)
        text(str(int(spac)), (x-30, _y))
        _y -= S.fontInfo.unitsPerEm * s * lh

# --------
# settings
# --------

size('A4Landscape')
W, H = width(), height()
newDrawing()

designspacePath = '/hipertipo/tools/VariableSpacing/demos/Roboto/Roboto.designspace'

txt = 'AVATAR voxr.'

steps = 5
s     = 0.04
t     = -50
lh    = 1.25

savePDF = True
savePNG = False

x, y = 50, 0.8 * H

colorBox      = 1, 0, 1, 0.35
colorKerning  = 0, 1, 1, 0.35
colorTracking = 1, 1, 0, 0.35
colorMargins  = 0,

L = dict(width=0, weight=400, spacing=0, contrast=0, slant=0)

# -----
# draw!
# -----

S = SpacingSetter(designspacePath)
S.colorBox      = colorBox
S.colorKerning  = colorKerning
S.colorTracking = colorTracking
S.colorMargins  = colorMargins

## set 1: glyph boxes, no kerning

S.drawBoxes     = True
S.drawTracking  = True
S.drawWidths    = True
S.useKerning    = False
S.drawKerning   = False
newPage(W, H)
setup()
drawColorCaptions(kerning=False)
text('tracking (kerning off)', (x, height()-30))
drawTracking(x, y, t, s, L, steps, lh)

S.tracking = 0
newPage()
setup()
drawColorCaptions(kerning=False, tracking=False)
text('spacing axis (kerning off)', (x, height()-30))
drawSpacing(x, y, t, s, L, steps, lh)

## set 2: show kerning (and tracking), no glyph boxes

S.useKerning    = True
S.drawKerning   = True
S.drawTracking  = True
S.drawWidths    = True
S.drawBoxes     = False
newPage(W, H)
setup()
drawColorCaptions(glyphBox=False)
text('tracking (static kerning)', (x, height()-30))
drawTracking(x, y, t, s, L, steps, lh)

S.tracking = 0
newPage(W, H)
setup()
drawColorCaptions(glyphBox=False, tracking=False)
text('spacing axis (variable kerning)', (x, height()-30))
drawSpacing(x, y, t, s, L, steps, lh)

### set 3: black & white text

S.useKerning   = True
S.drawTracking = False
S.drawBoxes    = False
S.drawKerning  = False
S.drawWidths   = False

newPage(W, H)
setup()
text('tracking (static kerning)', (x, height()-30))
drawTracking(x, y, t, s, L, steps, lh, mode=1)

S.tracking = 0
newPage(W, H)
setup()
text('spacing axis (variable kerning)', (x, height()-30))
drawSpacing(x, y, t, s, L, steps, lh, mode=1)

newPage(W, H)
setup()
text('tracking (static kerning)', (x, height()-30))
drawTracking(x, y, t, s, L, steps, lh, mode=2)

S.tracking = 0
newPage(W, H)
setup()
text('spacing axis (variable kerning)', (x, height()-30))
drawSpacing(x, y, t, s, L, steps, lh, mode=2)




# -----------
# save images
# -----------

if savePDF:
    pdfPath = os.path.join(os.path.dirname(folder), 'imgs', 'spacing-axis-vs-tracking.pdf')
    saveImage(pdfPath)

if savePNG:
    pngPath = os.path.join(os.path.dirname(folder), 'imgs', 'spacing-axis-vs-tracking.png')
    saveImage(pngPath, multipage=True)
