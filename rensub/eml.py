# -*- coding: utf-8 -*-
#/usr/bin/python
import os,zipfile,os.path,shutil,sys,re

'''Extract, move, launch'''

def rename(avi,srt):
    '''avi and srt full path -> srt renamed file'''
    avidir,avifile=os.path.split(avi)
    srtdir=os.path.dirname(srt)
    temp=os.path.join(srtdir,".".join(avifile.split(".")[:-1]+["srt"]))
    os.rename(srt,temp)
    try:
        shutil.move(temp,avidir)
    except shutil.Error:
        print("Subtitle file already exists, not overwritten")
    except OSError:
        pass
    finally:      
        return os.path.join(avidir,os.path.split(temp)[1])

def unzip(zipped):
    '''zipped fullpath -> srt files
    unzipped files in the same directory,
    purge directory and non srt file'''
    z=zipfile.ZipFile(zipped)
    zipdir=os.path.dirname(zipped)
    #print z.namelist()
    files=[name for name in z.namelist() if not name.endswith(os.sep) and not name.startswith("__MAC") and name.endswith(".srt")]
    for name in files:
        out=open(os.path.join(zipdir,name),"wb")
        out.write(z.read(name))
        out.close()
    return [os.path.join(zipdir,f) for f in files]

def makeAll(avi,zipped):
    '''avi and zipped file fullpath -> renamed srt file
    unzip move and rename subtitle file'''
    files=unzip(zipped)
    #print files
    r=-5
    while (r<0 or r>=len(files)):
        if len(files)>1:
            for i in range(len(files)):
                print("%d: %s" % (i,files[i]))
            r=int(input("Scegli: "))    
        else:
            r=0
    
    return rename(avi,files[r])
    
def main(argv):
    if len(argv)>=3:
          avi=argv[1]
          zipped=argv[2]
          srt=makeAll(avi,zipped)
          if srt:
              print(avi,srt)
              if len(argv)==4:
                  print(os.popen(argv[3]+" "+avi))
              if len(argv)==5 and argv[3]=="copy":
                  shutil.copy(avi,argv[4])
                  srtpath=os.path.split(avi)[0]+os.sep+os.path.split(srt)[1]
                  shutil.copy(srtpath,argv[4])
                  print("Copied")
          else:
              print("Error: multiple file in zip.")
          
    else:
          print('''Use: python renSubs.py <full path avi file> <full path zip file>''')

if __name__ == '__main__':
  main(sys.argv)

    
    
