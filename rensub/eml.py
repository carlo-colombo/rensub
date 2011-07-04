# -*- coding: utf-8 -*-
#/usr/bin/python
import os,zipfile,os.path,shutil

'''Extract, move, launch'''

def rename(avi,srt):
    '''avi and srt full path -> srt renamed file'''
    avidir,avifile=os.path.split(avi)
    srtdir=os.path.dirname(srt)
    temp=os.path.join(srtdir,".".join(avifile.split(".")[:-1]+["srt"]))
    os.rename(srt,temp)
    try:
        shutil.move(temp,avidir)
    finally:	  
        return temp

def unzip(zipped):
    '''zipped fullpath -> srt files
    unzipped files in the same directory,
    purge directory and non srt file'''
    z=zipfile.ZipFile(zipped)
    zipdir=os.path.dirname(zipped)
    files=[name for name in z.namelist() if not name.endswith(os.sep) and not name.startswith("__MAC") and name.endswith(".srt")]
    for name in files:
        out=open(os.path.join(zipdir,name),"wb")
        out.write(z.read(name))
        out.close()
    return [os.path.join(zipdir,f) for f in files]