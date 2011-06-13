import argparse
import rensub
import eml
import os
import shutil
from config import Config
                
class Rensub(argparse.Action):
    def __call__(self,parser, namespace, values, option_string=None):
        arg=namespace
        video_file, zip_file= rensub.main(["rensub",arg.show,arg.season,arg.episode])
        srt_file = eml.unzip(zip_file)
        if len(srt_file)>1:
            print "###################"
            for i,v in enumerate(srt_file):
                print i,v
            srt_file=srt_file[int(raw_input('Choose one: '))]
        else:
            srt_file=srt_file[0]
        eml.rename(video_file,srt_file)
        if arg.copy:
            shutils.copy(video_file,arg.copy)
            shutils.copy(srt_file,arg.copy)
        if arg.execute:
            os.popen(" ".join((arg.execute,video_file)))

class Copy(argparse.Action):
    def __call__(self,parser, namespace, values, option_string=None):
        print "copy"
        
class Exec(argparse.Action):
    def __call__(self,parser, namespace, values, option_string=None):
        print "execute"

parser = argparse.ArgumentParser(description='Subtitles utils')

subparsers = parser.add_subparsers()
rensub_parser = subparsers.add_parser('get')
config_parser = subparsers.add_parser('config')
manage_parser = subparsers.add_parser('manage')

rensub_parser.add_argument('show',help="string that can match the name of the show",action=Rensub)
rensub_parser.add_argument('season',nargs='?',type=int,help="season number",default=0)
rensub_parser.add_argument('episode',nargs='?',type=int,help="episode number",default=0)
rensub_parser.add_argument('-c','--copy',metavar='DESTINATION')
rensub_parser.add_argument('-e','--execute',metavar='PLAYER')

config_parser.add_argument('--video-folder','-v', nargs='+',action=Config,default=[])
config_parser.add_argument('--subtitle-folder','-s', nargs='+',action=Config,default=[])
config_parser.add_argument('--list-config','-l', nargs=0,action=Config.List)
#parser.add_argument('--config',help="starting configuration",action=Config,nargs=0)
#parser.add_argument('-n','--next',help="skip to next season, first episode",action='store_true')

if __name__=="__main__":
    parser.parse_args()

