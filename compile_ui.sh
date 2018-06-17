#!/usr/bin/env bash
#workon deeplearning
rm -rf src/ui
rm resources_rc.py
mkdir src/ui
pyuic5 ui/cosmetic_properties_widget.ui > src/ui/cosmetic_properties_widget_ui.py
pyuic5 ui/simulation_widget.ui > src/ui/simulation_widget_ui.py
pyuic5 ui/physical_properties_widget.ui > src/ui/physical_properties_widget_ui.py
pyuic5 ui/main_window.ui > src/ui/main_window_ui.py
pyuic5 ui/starting_properties_widget.ui > src/ui/starting_properties_widget_ui.py
pyuic5 ui/cart_pole_graph_widget.ui > src/ui/cart_pole_graph_widget_ui.py
pyuic5 ui/about_dialog.ui > src/ui/about_dialog_ui.py
pyrcc5 -o resources_rc.py ui/resources.qrc