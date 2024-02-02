#i_view32.exe .\*.jpg /resize=(1280,1024) /resample /aspectratio /convert=*.jpg /jpgq=90

import subprocess
import os

subprocess.call(['i_view32.exe', '.\*.jpg', '/resize=(1280,1024)', '/resample', '/aspectratio', '/convert=*.jpg', '/jpgq=90'])
