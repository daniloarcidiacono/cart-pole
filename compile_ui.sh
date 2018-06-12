#!/usr/bin/env bash
#workon deeplearning
rm -rf src/ui
mkdir src/ui
pyuic5 ui/cosmetic_properties_widget.ui > src/ui/cosmetic_properties_widget_ui.py
pyuic5 ui/simulation_widget.ui > src/ui/simulation_widget_ui.py
pyuic5 ui/physical_properties_widget.ui > src/ui/physical_properties_widget_ui.py
pyuic5 ui/main_window.ui > src/ui/main_window_ui.py
pyuic5 ui/starting_properties_widget.ui > src/ui/starting_properties_widget_ui.py