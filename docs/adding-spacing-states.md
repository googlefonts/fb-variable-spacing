---
title  : Adding spacing states to a font
layout : default
---

How to add 'tight' and 'loose' spacing states to an existing UFO source in RoboFont.
{: .lead }

* Table of Contents
{:toc}

##### 1. Open the tool

- Open the file [`variableSpacingTool.py`](http://github.com/gferreira/VariableSpacing/blob/master/code/Lib/variableSpacing/dialogs/variableSpacingTool.py) in the Scripting Window.
- Run the script to open the **SpacingStates tool**.

<div class="alert alert-primary" role="alert" markdown='1'>
If you have [installed the VariableSpacing extension](../install), you can open the tool from the menu *Extensions > VariableSpacing > SpacingStates*.
{: .card-text }
</div>

##### 2. Create default state

Click on the **new** button to create a new empty spacing state in the font. 

Since this is the first spacing state in the font, it will be named `default`.

##### 3. Save default state

- Select the `default` state in the list.
- Click on the **save** button to save the font’s current spacing and kerning into the `default` spacing state.

##### 4. Create tight state

Click on the **new** button to create a new empty spacing state in the font. 

Since this is the second spacing state in the font, it will be named `tight`.

##### 5. Adjust tight spacing

Edit the widths and margins in the font to produce the `tight` extreme of the spacing axis.

The tight margins can be set using the [SetMargins tool](../set-margins-tool), or manually in the Space Center.

Should the opaque shapes of adjacent glyphs be allowed to touch each other? In other words, should the tight margins be positive, zero, or negative? It is up to the designer to decide based on the typeface style.

##### 6. Adjust tight kerning

After the tight glyph margins have been set, adjust the kerning values of the font accordingly.

Kerning groups and kerning pairs should remain the same, only the **kerning values** should change.

##### 7. Save tight state

Make sure to save the tight spacing state to the lib after editing it.

- Select the `tight` state in the list.
- Click on the **save** button to save the font’s current spacing and kerning into the tight spacing state.

##### 8. Create loose state

Optionally, repeat steps 4-7 to create the `loose` extreme of the spacing axis.

##### 9. Continue editing

You can switch between the various spacing states at any time and continue editing.

Don’t forget to save the current spacing state to the lib before loading another one.

Also, make sure to select the correct lib: be careful not to save the tight state into the `default` lib, for example.
