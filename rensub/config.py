import argparse
import shelve
from contextlib import closing
import os

PATH = ".rensub"
PREFIX = "__config_"
RENSUB_DB = "rensubDB"

def check():
    return os.path.exists(path())

def path(filename=""):
    return os.path.join(os.environ['HOME'],PATH,filename)
    
def folders(key):
    with ctx_shelve() as shelf:
        return shelf[key] if key in shelf and shelf[key] else []

def video_folders():
    return folders(PREFIX+"video_folder") 

def subtitle_folders():
    return folders(PREFIX+"subtitle_folder")
    
def link_folders():
    return folders(PREFIX+"link_folder")
    
def ctx_shelve():
    return closing(shelve.open(path(RENSUB_DB),'wu'))


class Config(argparse.Action):
    def __call__(self,parser, namespace, values, option_string=None):
        if not check():
            os.mkdir(path())
        with ctx_shelve() as shelf:
            key=PREFIX+self.dest
            if not  key in shelf:
                shelf[key]=set()
            filtered =list(map(os.path.abspath,list(filter(os.path.isdir, list(filter(os.path.exists,values))))))
            temp = shelf[key]
            temp.update(filtered)
            shelf[key]=temp
    
    class List(argparse.Action):
        def __call__(self,parser, namespace, values, option_string=None):
            with ctx_shelve() as shelf:
                for key in [k for k in list(shelf.keys()) if k.startswith(PREFIX)]:
                    print("*"*5,key.lstrip(PREFIX).replace("_"," "),"*"*10)
                    for config_value in shelf[key]:
                        print(config_value)

