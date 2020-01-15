# -*- coding: utf-8 -*-
"""
/***************************************************************************
 lineaireRepercussion
                                 A QGIS plugin
 Appel des fonctions sql de répercussion des changements sur le plan de circulation
                              -------------------
        begin                : 2015-07-08
        git sha              : $Format:%H$
        copyright            : (C) 2015 by PnC
        email                : amandine.sahl@cevennes-parcnational.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from __future__ import absolute_import
from builtins import range
from builtins import object
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, QSettings
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMessageBox, QProgressBar

# Import the code for the dialog
from .lineaire_repercussion_dialog import lineaireRepercussionDialog
import os.path


from qgis.gui import QgsMessageBar
from qgis.core import Qgis
import psycopg2
import time

class lineaireRepercussion(object):
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'lineaireRepercussion_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        # self.dlg = lineaireRepercussionDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Répercussion du linéaire')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'lineaireRepercussion')
        self.toolbar.setObjectName(u'lineaireRepercussion')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('lineaireRepercussion', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/lineaireRepercussion/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Répercussion du linéaire'),
            callback=self.run,
            parent=self.iface.mainWindow())

        icon_path = ':/plugins/lineaireRepercussion/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Paramètres'),
            callback=self.initParameters,
            parent=self.iface.mainWindow())



    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Répercussion du linéaire'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    def initParameters(self):
        from .settingsdialog import SettingsDialog
        dialog = SettingsDialog(self.iface)
        accepted = dialog.exec_()
        if not accepted:
            return False

    def run(self):
        msgBox = QMessageBox();
        msgBox.setWindowTitle(u"Répercussion des modification réalisées")
        msgBox.setInformativeText(u"Voulez-vous lancer la répercussion des changements du linéaire sur le plan de circulation ?")
        msgBox.setStandardButtons(QMessageBox.Ok |  QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Ok)
        ret = msgBox.exec_()
        
        progressMessageBar = self.iface.messageBar().createMessage(u"Répercussion du linéaire : Traitement en cours ....")
        progress = QProgressBar()
        progress.setMaximum(10)
        progressMessageBar.layout().addWidget(progress)
        self.iface.messageBar().pushWidget(progressMessageBar, Qgis.Info)

        if ret == QMessageBox.Ok:
            for i in range(10):
                time.sleep(1)
                progress.setValue(i + 1)
            self.runSql()
        else:
            self.iface.messageBar().clearWidgets()

    def runSql(self):
        settings = QSettings()
        dbhost = settings.value("/lineaireRepercussion/dbhost", "", type=str)
        dbname = settings.value("/lineaireRepercussion/dbname", "", type=str)
        dbuser = settings.value("/lineaireRepercussion/dbuser", "", type=str)
        dbpassword = settings.value("/lineaireRepercussion/dbpassword", "", type=str)
        dbport = settings.value("/lineaireRepercussion/dbport",5432, type=int)
        
        dns = "dbname='%s' host='%s' user='%s' password='%s' port=%s" % (dbname, dbhost, dbuser, dbpassword, dbport)
            
        try:
           conn = psycopg2.connect(dns)
        except Exception as err:
            self.iface.messageBar().clearWidgets()
            self.iface.messageBar().pushMessage("Erreur", "Connexion à la base de données impossible", level=Qgis.CRITICAL)
            return False

        try:
            cur = conn.cursor()
            sql = "SELECT modification_lineaire.repercussion_modification_lineaire();"
            cur.execute(sql)
            conn.commit()
            sql = "SELECT modification_lineaire.update_geometry_of_evenement_with_split();"
            cur.execute(sql)
            conn.commit()
            for notice in conn.notices:
                 self.iface.messageBar().clearWidgets()
                 self.iface.messageBar().pushMessage("Information", notice.decode('utf-8'), level=Qgis.INFO)
            sql = "SELECT modification_lineaire.update_geometry_of_evenement_without_split();"
            cur.execute(sql)
            conn.commit()
            for notice in conn.notices:
                self.iface.messageBar().clearWidgets()
                self.iface.messageBar().pushMessage("Information", notice.decode('utf-8'), level=Qgis.INFO)
            conn.close()
        except Exception as err:
            self.iface.messageBar().clearWidgets()
            self.iface.messageBar().pushMessage("Erreur", repr(err), level=Qgis.CRITICAL)
            conn.close()
        pass