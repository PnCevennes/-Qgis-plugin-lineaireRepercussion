# -*- coding: utf-8 -*-
"""
/***************************************************************************
 lineaireRepercussion
                                 A QGIS plugin
 Appel des fonctions sql de répercussion des changements sur le plan de circulation
                             -------------------
        begin                : 2015-07-08
        copyright            : (C) 2015 by PnC
        email                : amandine.sahl@cevennes-parcnational.fr
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load lineaireRepercussion class from file lineaireRepercussion.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .lineaire_repercussion import lineaireRepercussion
    return lineaireRepercussion(iface)
