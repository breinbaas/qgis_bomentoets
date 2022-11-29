# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TreeAssessment
                                 A QGIS plugin
 Toets bomen op keringen
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-11-28
        copyright            : (C) 2022 by Rob van Putten
        email                : breinbaasnl@gmail.com
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
    """Load TreeAssessment class from file TreeAssessment.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .tree_assessment import TreeAssessment
    return TreeAssessment(iface)
