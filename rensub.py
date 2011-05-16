#!/usr/bin/python
# -*- coding: utf-8 -*-
import re,os,sys,eml
import pdb

SUBS_FOLDERS=["/home/ilich/Scaricati"]
VIDEO_FOLDERS=["/home/ilich/download/torrent","/home/ilich/download/jd"]
#FORMATS=["avi","mkv","mp4"]

def find(r,directory,exclude=[]):
  for f in os.listdir(directory):
    m=r.match(f)
    if m and str(m.group())[-3:] not in exclude:
      yield m.group()
    

def make_pattern(serie,S,E,format=""):
  s=r".*%s.*0?%s\D\D?0?%s\D.*%s" % (serie,S,E,format)
  return re.compile(s,re.IGNORECASE)

def main(argv):
    if len(argv)>=4:
        p=make_pattern(*argv[1:4])
        current_folder = ""
        video_file = None
        for folder in VIDEO_FOLDERS:
            current_folder=folder
            l=[i for i in find(p,folder,["zip","srt","txt"])]
            if len(l)!=0:
                break  
        if len(l)==0:
            print "Video: no match found, please retry"
        elif len(l)==1:
            video_file=l[0]
        elif len(l)>1:
            for k,v in enumerate(l):
                print "%s %s (%s) " % (k, v, "directory" if os.path.isdir(os.path.join(folder,v)) else "file")
            video_file=l[int(raw_input("Many match, choose one: "))]
        full_path=os.path.join(folder,video_file)
        if (os.path.isdir(full_path)):
            l=find(p,full_path,["nfo"])
            if l:
                for k,v in enumerate(l):
                    print k," ",v
                video_file=l[int(raw_input("Choose one: "))]
                video_file=os.path.join(full_path, video_file)
            else:
                print "No file in the selected folder"
                video_file=None
        else:
            video_file=os.path.join(current_folder,video_file)
        if video_file:
            p=make_pattern(*argv[1:4],format="zip")
            current_subs_folder=""
            sub_file=None
            for s in SUBS_FOLDERS:
                current_subs_folder=s
                l=[i for i in find(p,s)]
                if len(l)!=0:
                    break
            if len(l)==0:
                print "Subtitle: no match found, please retry"
            elif len(l)==1:
                sub_file=l[0]
            else:
                for k,v in enumerate(l):
                    print k," ",v
                sub_file=l[int(raw_input( "Multiple match, please choose: "))]
            if sub_file:
                sub_file=os.path.join(current_subs_folder,sub_file)
    if sub_file and video_file:
        print video_file
        print sub_file
        renSubs.main(["empty", video_file , sub_file]+argv[4:])

if __name__=="__main__":
  main(sys.argv)
