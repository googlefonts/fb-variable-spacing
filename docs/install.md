---
title  : Installing VariableSpacing
layout : default
---

VariableSpacing is packaged and distributed as a [RoboFont extension].
{: .lead }

* Table of Contents
{:toc}


Installing with Mechanic
------------------------

It is recommended to install VariableSpacing using [Mechanic], so it can automatically check for updates and install them.

1. Download the file `VariableSpacing.mechanic` from the repository.
2. Go to the Mechanic extension’s settings.
3. Use the plus button to add the `.mechanic` file to the list of [Single Extension Items].

[RoboFont extension]: http://robofont.com/documentation/extensions/
[Mechanic]: http://github.com/robofont-mechanic/mechanic-2
[Single Extension Items]: http://robofont.com/documentation/extensions/managing-extension-streams/#adding-single-extension-items


Installing manually
-------------------

The VariableSpacing extension can also be installed manually if you download the extension package.

Simply double-click the file `VariableSpacing.roboFontExt` to have it installed in RoboFont.

<div class="alert alert-primary" role="alert" markdown='1'>
If you install the extension manually, you will *not* be notified automatically about updates.
{: .card-text }
</div>


Installing from source
----------------------

VariableSpacing can be used directly from the source code if you download the repository.

This mode allows developers to make changes to the code while using and testing the tools in RoboFont.

1. Clone the repository using `git clone` (recommended) or download the source code.
2. In the RoboFont Preferences window, go to [Extensions > Start Up Scripts].
3. Add the file `VariableSpacing/code/Lib/start.py` to the list of start-up scripts.
4. Save the settings and restart RoboFont; VariableSpacing will now appear under the *Extensions* menu.

[Extensions > Start Up Scripts]: http://robofont.com/documentation/workspace/preferences-window/extensions/#start-up-scripts
