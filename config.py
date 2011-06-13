import argparse
import shelve
from contextlib import closing
import os


class Config(argparse.Action):
    PATH = ".rensub"
    PREFIX = "__config_"
    RENSUB_DB = "rensubDB"
    
    @staticmethod
    def check():
        return os.path.exists(Config.path())
    
    @staticmethod
    def path():
        return os.path.join(os.environ['HOME'],Config.PATH)
    
    def __call__(self,parser, namespace, values, option_string=None):
        if not Config.check():
            os.mkdir(Config.path())
        with closing(shelve.open(os.path.join(Config.path(),Config.RENSUB_DB))) as shelf:
            key=Config.PREFIX+self.dest
            if not  key in shelf:
                shelf[key]=set()
            filtered =map(os.path.abspath,filter(os.path.isdir, filter(os.path.exists,values)))
            temp = shelf[key]
            temp.update(filtered)
            shelf[key]=temp
            for path in shelf[key]:
                print path
    
    class List(argparse.Action):
        def __call__(self,parser, namespace, values, option_string=None):
            with closing(shelve.open(os.path.join(Config.path(),Config.RENSUB_DB ))) as shelf:
                for key in filter(lambda k: k.startswith(Config.PREFIX),shelf.keys()):
                    print "*"*5,key.lstrip(Config.PREFIX).replace("_"," "),"*"*10
                    for config_value in shelf[key]:
                        print config_value
