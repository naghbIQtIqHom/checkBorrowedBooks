# -*- coding: utf-8 -*-
from optparse import OptionParser

def parseOption():
    parser = OptionParser()
    parser.add_option("-s", "--silent", action="store_true", dest="silence", default=False, help="サイレント。結果をしゃべらない。")
    parser.add_option("-l", "--library", action="store", type="string", dest="librarylist", default="all", help="調べる図書館リスト。allか図書館名を,区切りで渡す。")
    return parser.parse_args()

