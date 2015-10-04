from db import Db
from gen import Generator
from parse import Parser
from sql import Sql
from rnd import Rnd
import sys
import sqlite3
import codecs

SENTENCE_SEPARATOR = '.'
WORD_SEPARATOR = ' '

def choose_mode():
    while True:
        print 'Choose parse or gen:'
        mode  = raw_input()
        if mode == 'parse' or mode == 'gen':
            return mode

def new_or_load():
    while True:
        print "Press 'n' for new or 'l' for load"
        response = raw_input()
        if response=='n' or response == 'l':
            return response

def main():
    
    #args = sys.argv

    #mode = choose_mode()

    response = new_or_load()
    
    depth = 1
    
    file_name = 'text/soldier_game.txt'
    #file_name = 'text/hitchhickers.txt'
    #file_name = 'text/soldier_game_short.txt'
    #file_name = 'text/soldier_game_short_segmented.txt'
    
    name  = 'soldierGame'
    #name  = 'hitchHikers'
    #name = 'soldierGameShort'
    #name = 'soldierGameShortSegmented'
    db_dir = 'db/'
    
    
    count = 1
        
    
    if response == 'n':
        usage = 'Usage: %s (parse <name> <depth> <path to txt file>|gen <name> <count>)' % ('parse', )

        db = Db(sqlite3.connect(db_dir + name + '.db'), Sql())
        #db = Db(sqlite3.connect(name + '.db'), Sql())
        db.setup(depth)
                
        txt = codecs.open(file_name, 'r', 'utf-8').read()
        Parser(name, db, SENTENCE_SEPARATOR, WORD_SEPARATOR).parse(txt)
    
    #elif mode == 'gen':
    #count = int(args[3])
    db = Db(sqlite3.connect(db_dir + name + '.db'), Sql())
    #db = Db(sqlite3.connect(name + '.db'), Sql())
    generator = Generator(name, db, Rnd())
    for i in range(0, count):
        print generator.generate(WORD_SEPARATOR)

    print''
    print''
    #else:
        #raise ValueError(usage)

















while True:
    main()
    

