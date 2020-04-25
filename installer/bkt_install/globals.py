# -*- coding: utf-8 -*-
'''
Created on 25.02.2019

@author: fstallmann
'''

from __future__ import absolute_import, print_function

import os

# install bkt-framework with additional config
INSTALL_BASE = os.path.normpath(os.path.join(os.path.realpath(os.getcwd()), ".."))
FEATURE_BASE = os.path.join(INSTALL_BASE, 'features')

default_config=dict(
        feature_folders=[
            os.path.join(FEATURE_BASE, 'toolbox'),
            os.path.join(FEATURE_BASE, 'ppt_thumbnails'),
            os.path.join(FEATURE_BASE, 'ppt_notes'),
            os.path.join(FEATURE_BASE, 'ppt_shapetables'),
            os.path.join(FEATURE_BASE, 'ppt_circlify'),
        ],
        shape_library_folders = '',
        shape_libraries =  '',
        chart_library_folders = '',
        chart_libraries =  ''
    )