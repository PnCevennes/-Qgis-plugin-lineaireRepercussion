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
from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtWidgets import QDialog

from .ui_settingsdialog import Ui_db_connexion_form

class SettingsDialog(QDialog):
  def __init__(self, iface):
    QDialog.__init__(self, iface.mainWindow())
    # set up the user interface
    self.ui = Ui_db_connexion_form()
    self.ui.setupUi(self)

    # load settings
    settings = QSettings()
    self.ui.txt_db_host.setText(settings.value("/lineaireRepercussion/dbhost", "", type=str))
    self.ui.txt_db_port.setText(settings.value("/lineaireRepercussion/dbport", "5432", type=str))
    self.ui.txt_db_dbname.setText(settings.value("/lineaireRepercussion/dbname", "", type=str))
    self.ui.txt_db_user.setText(settings.value("/lineaireRepercussion/dbuser", "", type=str))
    self.ui.txt_db_password.setText(settings.value("/lineaireRepercussion/dbpassword", "", type=str))

  def accept(self):
    QDialog.accept(self)

    # save settings
    settings = QSettings()
    settings.setValue("/lineaireRepercussion/dbhost", self.ui.txt_db_host.text())
    settings.setValue("/lineaireRepercussion/dbport", self.ui.txt_db_port.text())
    settings.setValue("/lineaireRepercussion/dbname", self.ui.txt_db_dbname.text())
    settings.setValue("/lineaireRepercussion/dbuser", self.ui.txt_db_user.text())
    settings.setValue("/lineaireRepercussion/dbpassword", self.ui.txt_db_password.text())
