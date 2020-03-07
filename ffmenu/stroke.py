#!/usr/bin/env fontforge -lang=py

import fontforge

def updateGlyph(font, glyph):
    bg = glyph.background
    print("    glyph.background = %s" % bg)
    fg = glyph.foreground
    print("    glyph.foreground = %s" % fg)
    if not bg.isEmpty():
        width = glyph.width

        glyph.activeLayer = 'Fore'

        # save
        anchorPoints = glyph.anchorPoints

        glyph.activeLayer = 'Fore'
        pen = glyph.glyphPen()

        glyph.activeLayer = 'Back'
        glyph.draw(pen)

        pen = None              # done

        glyph.activeLayer = 'Fore'

        glyph.stroke('circular', 96, 'round', 'round')
        #     glyph.stroke("circular",width[,linecap,linejoin,flags])
        #     glyph.stroke("eliptical",width,minor-width,angle[,linecap,linejoin,flags])
        #     glyph.stroke("caligraphic",width,height,angle[,flags])
        #     glyph.stroke("polygon",contour[,flags])
        glyph.removeOverlap()
        glyph.addExtrema()
        glyph.width = width

        # restore
        for anchorPoint in anchorPoints:
            glyph.addAnchorPoint(*anchorPoint)

activeFont = fontforge.activeFont()

if activeFont == None:
    raise Exception('No active font.')

codes = [code for code in activeFont.selection]
print("codes = %s" % codes)

for code in codes:
    print("code = %s" % code)
    glyph = activeFont[code]
    print("glyph = %s" % glyph)
    updateGlyph(activeFont, glyph)
