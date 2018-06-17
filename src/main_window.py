import json
from PyQt5.QtCore import Qt, pyqtSlot, QDir, QFile, QIODevice, QTextStream, QSettings
from PyQt5.QtWidgets import QMainWindow, QDockWidget, QMessageBox, QFileDialog, QDialog, QAction

from src.model.document import Document
from src.ui.main_window_ui import Ui_MainWindow
from src.widgets.about_dialog import AboutDialog
from src.widgets.cart_pole_graph_widget import CartPoleGraphWidget
from src.widgets.cosmetic_properties_widget import CosmeticPropertiesWidget
from src.widgets.physical_properties_widget import PhysicalPropertiesWidget
from src.widgets.simulation_widget import SimulationWidget
from src.widgets.starting_properties_widget import StartingPropertiesWidget


class MainWindow(QMainWindow):
    MAX_RECENT_FILES_LENGTH = 10

    def __init__(self):
        super().__init__()

        # Create the document
        self._document = Document()
        self._settings = QSettings('settings.ini', QSettings.IniFormat)
        self._recentFileActions = []

        # Init the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.updateWindowTitle()
        self.initDockWidgets()
        self.initDialogs()

        # Inject the data
        self.ui.cartPoleWidget.cosmeticProperties = self._document._cosmeticProperties
        self.ui.cartPoleWidget.environment = self._document._environment

        # Load the settings
        if not self.loadSettings():
            self.showMaximized()

        # Setup signals
        self._document.systemStepped.connect(self.onEnvironmentStepped)
        self._document.systemResetted.connect(self.onEnvironmentResetted)
        self._document.simulationStateChanged.connect(self.onSimulationStateChanged)
        self._document.changed.connect(self.onDocumentChanged)
        self._cosmeticPropertiesWidget.modelChanged.connect(self.onCosmeticChanged)
        self._physicalPropertiesWidget.modelChanged.connect(self.onEnvironmentChanged)
        self._startingPropertiesWidget.modelChanged.connect(self.onStartingChanged)
        self._simulationWidget.integratorChanged.connect(self.onIntegratorChanged)
        self._simulationWidget.agentChanged.connect(self.onAgentChanged)
        self.ui.cartPoleWidget.keyPressed.connect(self.onCartPoleWidgetKeyPressed)

    @pyqtSlot(object)
    def onCartPoleWidgetKeyPressed(self, event):
        if event.key() == Qt.Key_Left:
            self._document._agent._force = -10
        elif event.key() == Qt.Key_Right:
            self._document._agent._force = 10
        elif event.key() == Qt.Key_R:
            self._document.reset()

    def initDockWidgets(self):
        # Instance the widgets
        self._cosmeticPropertiesWidget = CosmeticPropertiesWidget()
        self._physicalPropertiesWidget = PhysicalPropertiesWidget()
        self._startingPropertiesWidget = StartingPropertiesWidget()
        self._simulationWidget = SimulationWidget()
        self._cartPoleGraphWidget = CartPoleGraphWidget()

        # Create the containers of the widget that can be docked
        cosmeticPropertiesDockWidget = QDockWidget()
        physicalPropertiesDockWidget = QDockWidget()
        startingPropertiesDockWidget = QDockWidget()
        simulationDockWidget = QDockWidget()
        cartPoleGraphDockWidget = QDockWidget()

        cosmeticPropertiesDockWidget.setObjectName("cosmeticDock")
        physicalPropertiesDockWidget.setObjectName("physicalDock")
        startingPropertiesDockWidget.setObjectName("startingDock")
        simulationDockWidget.setObjectName("simulationDock")
        cartPoleGraphDockWidget.setObjectName("cartPoleGraphDock")

        # Inject the widgets into the dock widgets
        cosmeticPropertiesDockWidget.setWidget(self._cosmeticPropertiesWidget)
        physicalPropertiesDockWidget.setWidget(self._physicalPropertiesWidget)
        startingPropertiesDockWidget.setWidget(self._startingPropertiesWidget)
        simulationDockWidget.setWidget(self._simulationWidget)
        cartPoleGraphDockWidget.setWidget(self._cartPoleGraphWidget)

        # Setup the titles
        cosmeticPropertiesDockWidget.setWindowTitle(self._cosmeticPropertiesWidget.windowTitle())
        physicalPropertiesDockWidget.setWindowTitle(self._physicalPropertiesWidget.windowTitle())
        startingPropertiesDockWidget.setWindowTitle(self._startingPropertiesWidget.windowTitle())
        simulationDockWidget.setWindowTitle(self._simulationWidget.windowTitle())
        cartPoleGraphDockWidget.setWindowTitle(self._cartPoleGraphWidget.windowTitle())

        # Add the dock widgets to the UI
        self.addDockWidget(Qt.LeftDockWidgetArea, cosmeticPropertiesDockWidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, physicalPropertiesDockWidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, startingPropertiesDockWidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, simulationDockWidget)
        self.addDockWidget(Qt.RightDockWidgetArea, cartPoleGraphDockWidget)

        # Inject the data into the widgets
        self._cosmeticPropertiesWidget.document = self._document._cosmeticProperties
        self._physicalPropertiesWidget.environment = self._document._environment
        self._physicalPropertiesWidget.cosmeticProperties = self._document._cosmeticProperties
        self._startingPropertiesWidget.environment = self._document._environment
        self._simulationWidget.document = self._document

        # Inject the dock actions in the View menu
        self.ui.menu_View.addAction(cosmeticPropertiesDockWidget.toggleViewAction())
        self.ui.menu_View.addAction(physicalPropertiesDockWidget.toggleViewAction())
        self.ui.menu_View.addAction(startingPropertiesDockWidget.toggleViewAction())
        self.ui.menu_View.addAction(simulationDockWidget.toggleViewAction())
        self.ui.menu_View.addAction(cartPoleGraphDockWidget.toggleViewAction())

    def initDialogs(self):
        self._aboutDialog = AboutDialog(self)
        self._saveDialog = QFileDialog(self)
        self._saveDialog.setWindowTitle("Save")
        self._saveDialog.setAcceptMode(QFileDialog.AcceptSave)
        self._saveDialog.setDirectory(QDir.homePath())
        self._saveDialog.setNameFilter("Cart Pole Environments (*.json)")
        self._saveDialog.setDefaultSuffix("json")

        self._openDialog = QFileDialog(self)
        self._openDialog.setWindowTitle("Open")
        self._openDialog.setAcceptMode(QFileDialog.AcceptOpen)
        self._openDialog.setDirectory(QDir.homePath())
        self._openDialog.setNameFilter("Cart Pole Environments (*.json)")
        self._openDialog.setDefaultSuffix("json")

    def loadSettings(self):
        geometry = self._settings.value('geometry', None)
        state = self._settings.value('windowState', None)

        # PyQt serializes empty lists as @Invalid so we need the toList method
        recentFiles = self.toList(self._settings.value('recentFiles', None))

        # Inject recent files into the menu
        for file in recentFiles:
            self.addRecentFileAction(file)

        if geometry is None or state is None:
            return False

        self.restoreGeometry(geometry)
        self.restoreState(state)
        return True

    def saveSettings(self):
        geometry = self.saveGeometry()
        state = self.saveState()
        self._settings.setValue('geometry', geometry)
        self._settings.setValue('windowState', state)
        self._settings.setValue('recentFiles', [action.data() for action in self._recentFileActions])

    def askSave(self):
        # If we have unsaved changes
        if self.isWindowModified():
            # Ask the user
            if QMessageBox.question(self, "CartPole", "You have unsaved changes. Save?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes) == QMessageBox.Yes:
                # If the user actually saves
                return self.save()

        return True

    def closeEvent(self, event):
        if self.askSave():
            self.saveSettings()
            super().closeEvent(event)
        else:
            event.ignore()

    def save(self):
        # If we do not have a file name, choose one
        if self._document._pathName is None:
            return self.saveAs()

        # Try to save
        if not self.internalSave(self._document._pathName):
            QMessageBox.critical(self, "Error", "Could not save %s!" % self._document._pathName)
            return False

        # Add recent file action
        self.addRecentFileAction(self._document._pathName)

        # Success, update the window title, and reset flags
        self.setWindowModified(False)
        self.ui.actionSave.setEnabled(False)
        return True

    def saveAs(self):
        result = self._saveDialog.exec()
        if result == QDialog.Rejected:
            return False

        fileName = self._saveDialog.selectedFiles()[0]

        # Try to save
        if not self.internalSave(fileName):
            return False

        # Setup the new name
        self._document._pathName = fileName

        # Add recent file action
        self.addRecentFileAction(self._document._pathName)

        # Success, update the window title, and reset flags
        self.updateWindowTitle()
        self.setWindowModified(False)
        self.ui.actionSave.setEnabled(False)
        return True

    # Opens a file.
    # If a fileName is passed, the user is not prompted with the file dialog (used for recent files).
    def open(self, fileName=None):
        if not self.askSave():
            return False

        # Prompt the user to select a file
        if fileName is None:
            result = self._openDialog.exec()
            if result == QDialog.Rejected:
                return False

            fileName = self._openDialog.selectedFiles()[0]

        # Try to read the document
        if not self.internalOpen(fileName):
            QMessageBox.critical(self, "Error", "Could not open %s!" % fileName)
            return False

        # Setup the new name
        self._document._pathName = fileName
        self.syncUI()

        # Add the recent file
        self.addRecentFileAction(fileName)

        # Success, update the window title, and reset flags
        self.updateWindowTitle()
        self.setWindowModified(False)
        self.ui.actionSave.setEnabled(False)
        return True

    def internalSave(self, pathName):
        try:
            f = QFile(pathName)
            if not f.open(QIODevice.WriteOnly):
                return False

            jsonDoc = json.dumps(
                self._document.toJson(),
                indent=4,
                separators=(',', ': ')
            )

            outputStream = QTextStream(f)
            outputStream << jsonDoc
            return True
        except Exception:
            return False

    def internalOpen(self, pathName):
        try:
            f = QFile(pathName)
            if not f.open(QIODevice.ReadOnly):
                return False

            inputStream = QTextStream(f)
            self._document.fromJson(json.loads(inputStream.readAll()))
            return True

        except Exception:
            return False

    def updateWindowTitle(self):
        if self._document._pathName is None:
            self.setWindowTitle("Untitled - CartPole [*]")
        else:
            self.setWindowTitle("%s - CartPole [*]" % self._document._pathName)

    def toList(self, value):
        """
        Module function to convert a value to a list.
        From: https://riverbankcomputing.com/pipermail/pyqt/2011-September/030480.html

        @param value value to be converted
        @return converted data
        """
        if value is None:
            return []
        elif not isinstance(value, list):
            return [value]
        else:
            return value

    def addRecentFileAction(self, path):
        # Dont add duplicate actions
        if path in [action.data() for action in self._recentFileActions]:
            return

        action = QAction()
        action.setData(path)
        action.setText(path)
        action.triggered.connect(lambda checked, _action=action: self.openRecentFile(_action))

        # Register the action
        self._recentFileActions.append(action)
        self.ui.menuRecent_files.addAction(action)

        # Keep the list length at a maximum
        if len(self._recentFileActions) > MainWindow.MAX_RECENT_FILES_LENGTH:
            self.ui.menuRecent_files.removeAction(self._recentFileActions.pop(0))

    @pyqtSlot()
    def on_actionSave_triggered(self):
        self.save()

    @pyqtSlot()
    def on_actionSave_as_triggered(self):
        self.saveAs()

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        self.open()

    @pyqtSlot()
    def on_actionClearRecentFiles_triggered(self):
        for action in self._recentFileActions:
            self.ui.menuRecent_files.removeAction(action)
        self._recentFileActions.clear()

    @pyqtSlot()
    def on_actionAbout_triggered(self):
        self._aboutDialog.show()

    @pyqtSlot()
    def openRecentFile(self, action):
        path = action.data()
        if not self.open(path):
            if QMessageBox.question(self, "Recent files", "Remove the file from the list?") == QMessageBox.Yes:
                self.ui.menuRecent_files.removeAction(action)
                self._recentFileActions.remove(action)

    @pyqtSlot()
    def onDocumentChanged(self):
        self.setWindowModified(True)
        self.ui.actionSave.setEnabled(True)

    @pyqtSlot()
    def onEnvironmentStepped(self):
        self._cartPoleGraphWidget.addPoint('position', self._document._environment._time, self._document._environment._position)
        self._cartPoleGraphWidget.addPoint('velocity', self._document._environment._time, self._document._environment._velocity)
        self._cartPoleGraphWidget.addPoint('angle', self._document._environment._time, self._document._environment._angle)
        self._cartPoleGraphWidget.addPoint('angularVelocity', self._document._environment._time, self._document._environment._angleVelocity)
        self._document.markModified()
        self.ui.cartPoleWidget.update()

        if self._document._environment.constraintsViolated():
            self._document.stop()


    @pyqtSlot()
    def onEnvironmentChanged(self):
        self._document.markModified()
        self.ui.cartPoleWidget.update()

    @pyqtSlot()
    def onEnvironmentResetted(self):
        self._document.markModified()
        self.ui.cartPoleWidget.update()
        self._cartPoleGraphWidget.clearAll()

    @pyqtSlot()
    def onIntegratorChanged(self):
        pass

    @pyqtSlot()
    def onAgentChanged(self):
        pass

    @pyqtSlot()
    def onStartingChanged(self):
        self._document.markModified()

    @pyqtSlot()
    def onSimulationStateChanged(self):
        self.ui.cartPoleWidget._displayFrameRate = self._document.isStarted()

    @pyqtSlot()
    def onCosmeticChanged(self):
        self._document.markModified()
        self.ui.cartPoleWidget.update()

    def syncUI(self):
        self._cosmeticPropertiesWidget.syncUI()
        self._physicalPropertiesWidget.syncUI()
        self._startingPropertiesWidget.syncUI()
        self._simulationWidget.syncUI()
        self.ui.cartPoleWidget.update()

