import config
import argparse

class Manage(argparse.Action):
    def __call__(self,parser, namespace, values, option_string=None):
        with config.ctx_shelve() as shelf:
            for k,v in shelf.items():
                if not k.startswith(config.PREFIX):
                    print k,v