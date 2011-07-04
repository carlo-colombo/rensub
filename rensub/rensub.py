#!/usr/bin/python
# -*- coding: utf-8 -*-
import re,os,sys,eml, shelve
from contextlib import closing
import config

def find(r,directory,exclude=[]):
  for f in os.listdir(directory):
    m=r.match(f)
    if m and str(m.group())[-3:] not in exclude:
      yield m.group()
    

def make_pattern(serie,S,E,format=""):
  s=r".*%s.*0?%s\D\D?0?%s\D.*%s" % (serie,S,E,format)
  return re.compile(s,re.IGNORECASE)

def main(argv,as_library=True):
    with config.ctx_shelve() as ep:
        if len(argv)>=4:
            if ep.has_key(argv[1]) and argv[2:4]==[0,0]:
                argv[2:4]=list(ep[argv[1]])
                argv[3]=int(argv[3])+1
            p=make_pattern(*argv[1:4])
            current_folder = ""
            video_file = None
            for folder in config.video_folders():
                current_folder=folder
                l=[i for i in find(p,folder,["zip","srt","txt"])]
                if len(l)!=0:
                    break  
            if len(l)==0:
                raise Exception("Video: no match found, please retry")
            elif len(l)==1:
                video_file=l[0]
            elif len(l)>1:
                for k,v in enumerate(l):
                    print "%s %s (%s) " % (k, v,home+ "directory" if os.path.isdir(os.path.join(folder,v)) else "file")
                video_file=l[int(raw_input("Many match, choose one: "))]
            full_path=os.path.join(folder,video_file)
            if (os.path.isdir(full_path)):
                l=[i for i in find(p,full_path,["nfo"])]
                if l:
                    for k,v in enumerate(l):
                        print k," ",v
                    video_file=l[int(raw_input("Choose one: "))]
                    video_file=os.path.join(full_path, video_file)
                else:
                    raise Exception("Empty folder")
            
            video_file=os.path.join(current_folder,video_file)
            p=make_pattern(*argv[1:4],format="zip")
            current_subs_folder=""
            sub_file=None
            l=[]
            for s in config.subtitle_folders():
                current_subs_folder=s
                l=[i for i in find(p,s)]
                if len(l)!=0:
                    break
            if len(l)==0:
                raise Exception("Subtitle: no match found, please retry")
            elif len(l)==1:
                sub_file=l[0]
            else:
                for k,v in enumerate(l):
                    print k," ",v
                sub_file=l[int(raw_input( "Multiple match, please choose: "))]
            sub_file=os.path.join(current_subs_folder,sub_file)
            ep[argv[1]]=tuple(argv[2:4])
            if as_library:
                return video_file,sub_file
            else:
                print video_file
                print sub_file
                eml.main(["empty", video_file , sub_file]+argv[4:])
                

if __name__=="__main__":
    main(sys.argv,False)
