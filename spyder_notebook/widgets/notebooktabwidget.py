# -*- coding: utf-8 -*-
#
# Copyright (c) Spyder Project Contributors
# Licensed under the terms of the MIT License

"""File implementing NotebookTabWidget."""

# Standard library imports
import sys

# Spyder imports
from spyder.widgets.tabs import Tabs


class NotebookTabWidget(Tabs):
    """Tabbed widget whose tabs display notebooks."""

    def __init__(self, parent, actions, menu, corner_widgets):
        """
        Constructor.

        Parameters
        ----------
        parent : QWidget
            Parent of the tabbed widget.
        actions : list of (QAction or QMenu or None) or None
            Items to be added to the context menu.
        menu : QMenu or None
            Context menu of the tabbed widget.
        corner_widgets : dict of (Qt.Corner, list of QWidget or int) or None
            Widgets to be placed in the top left and right corner of the
            tabbed widget. A button for browsing the tabs is always added to
            the top left corner.
        """
        super().__init__(parent, actions, menu, corner_widgets)

        if not sys.platform == 'darwin':
            # Don't set document mode to true on OSX because it generates
            # a crash when the console is detached from the main window
            # Fixes spyder-ide/spyder#561
            self.setDocumentMode(True)
