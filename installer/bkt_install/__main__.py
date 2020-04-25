# -*- coding: utf-8 -*-
'''
Created on 23.04.2020

@author: fstallmann
'''

from __future__ import absolute_import, print_function

import argparse


class BktInstaller(object):
    @staticmethod
    def install(args):
        from . import install
        install.install(args)

    @staticmethod
    def uninstall(args):
        from . import install
        install.uninstall(args)

    @staticmethod
    def configure(args):
        from . import config
        config.configure(args)


parser = argparse.ArgumentParser(prog="bkt_install", description='BKT install and configuration scripts')
subparsers = parser.add_subparsers(help='BKT Installer supports 3 modes: install, uninstall and configure')

parser_install = subparsers.add_parser('install', help='Installation and registration of BKT')
parser_install.add_argument('--register_only', action='store_true', help='Only register addin without creating or updating default configuration')
parser_install.add_argument('--apps', nargs='+', choices=["powerpoint", "excel", "word", "outlook", "visio"], default=['powerpoint'], help='Define list of application(s) in which BKT is activated by default')
parser_install.set_defaults(func=BktInstaller.install)

parser_uninstall = subparsers.add_parser('uninstall', help='Remove registration of BKT')
parser_uninstall.add_argument('--remove_config', action='store_true', help='Remove config.txt file')
parser_uninstall.set_defaults(func=BktInstaller.uninstall)

parser_configure = subparsers.add_parser('configure', help='Edit BKT configuration')
parser_configure.add_argument('--set_config', metavar=('KEY','VALUE'), nargs=2, action='append', help='Add or update KEY to VALUE in config.txt')
parser_configure.add_argument('--add_folders', metavar=('PATH1','PATH2'), nargs='+', help='Add feature folder (absolute path or path relative to bkt install folder) to config file')
parser_configure.add_argument('--remove_folders', metavar=('PATH1','PATH2'), nargs='+', help='Remove feature folder (absolute path or path relative to bkt install folder) from config file')
parser_configure.add_argument('--migrate_from', metavar='OLD_VERSION', help='Migrate config.txt from the given version to the current one')
parser_configure.set_defaults(func=BktInstaller.configure)

args = parser.parse_args()
args.func(args)