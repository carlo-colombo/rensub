import argparse
import rensub
import eml
import os
import shutil
from config import Config
                
class Rensub(argparse.Action):
    def __call__(self,parser, namespace, values, option_string=None):
        video_file, zip_file= rensub.main(["rensub"]+values+(3-len(values))*[0])
        if video_file and zip_file:
            print video_file, zip_file
            srt_file = eml.unzip(zip_file)
            if len(srt_file)>1:
                print "###################"
                for i,v in enumerate(srt_file):
                    print i,v
                srt_file=srt_file[int(raw_input('Choose one: '))]
            else:
                srt_file=srt_file[0]
            eml.rename(video_file,srt_file)
            setattr(namespace, "video_file",video_file)
            setattr(namespace, "srt_file",srt_file)
        else:
            parser.exit()

parser = argparse.ArgumentParser(description='Subtitles utils')

subparsers = parser.add_subparsers()
rensub_parser = subparsers.add_parser('get')
config_parser = subparsers.add_parser('config')
manage_parser = subparsers.add_parser('manage')

rensub_parser.add_argument('-c','--copy',metavar='DESTINATION')
rensub_parser.add_argument('-e','--execute',metavar='PLAYER')
rensub_parser.add_argument('show',help="string that can match the name of the show",action=Rensub,nargs='+')

#config
config_parser.add_argument('--video-folder','-v', nargs='+',action=Config,default=[])
config_parser.add_argument('--subtitle-folder','-s', nargs='+',action=Config,default=[])
config_parser.add_argument('--list-config','-l', nargs=0,action=Config.List)

def main():
    ns = parser.parse_args()
    if "copy" in ns and ns.copy:
        shutil.copy(ns.video_file,ns.copy)
        shutil.copy(ns.srt_file,ns.copy)
    if "execute" in ns and ns.execute:
        os.popen(" ".join((ns.execute,ns.video_file)))

if __name__=="__main__":
    main()

