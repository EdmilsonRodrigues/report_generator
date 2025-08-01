"""
This is an application used to generate quality assurance reports for enteral
feeding products.
"""

import importlib.metadata
import sys

from PySide6 import QtWidgets


def main():
    # ###################### BRIEFCASE EXPLANATION #########################
    # Linux desktop environments use an app's .desktop file to integrate the
    # app in to their application menus. The .desktop file of this app will
    # include the StartupWMClass key, set to app's formal name. This helps
    # associate the app's windows to its menu item.
    #
    # For association to work, any windows of the app must have WMCLASS
    # property set to match the value set in app's desktop file. For PySide6,
    # this is set with setApplicationName().

    # Find the name of the module that was used to start the app
    app_module = sys.modules['__main__'].__package__
    # Retrieve the app's metadata
    metadata = importlib.metadata.metadata(app_module)

    QtWidgets.QApplication.setApplicationName(metadata['Formal-Name'])

    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec())
