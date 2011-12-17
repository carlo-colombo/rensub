from config import Config
import os

PATH = ".rensub"
CFG_FILE  = "rensub.cfg"

class Config(dict):
    def __init__(self):
        with open(os.path.join(os.environ['HOME'],PATH,CFG_FILE)) cfg:
            self.cfg = Config(cfg)
    def __getitem__(self,key):
        retun self.cfg[key]
