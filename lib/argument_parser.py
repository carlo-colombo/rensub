import argparse

parser = argparse.ArgumentParser(description='Subtitles utils')
parser.add_argument('show',help="string that can match the name of the show")
parser.add_argument('season',nargs='?',type=int,help="season number",default=0)
parser.add_argument('episode',nargs='?',type=int,help="episode number",default=0)
parser.add_argument('-c','--copy',metavar='DESTINATION')
parser.add_argument('-e','--execute',metavar='PLAYER')
parser.add_argument('--config',help="starting configuration",action='store_true')
parser.add_argument('-n','--next',help="skip to next season, first episode",action='store_true')
args = parser.parse_args()
print args