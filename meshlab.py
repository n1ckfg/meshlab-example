# https://pymeshlab.readthedocs.io/en/latest/
# https://pymeshlab.readthedocs.io/en/latest/filter_list.html
# https://pymeshlab.readthedocs.io/en/latest/io_format_list.html

import pymeshlab as ml
from pathlib import Path
import sys

argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"

inputPath = argv[0]
samplePercentage = float(argv[1])   
inputFormat = argv[2]
outputFormat = argv[3]

pathList = Path(inputPath).glob('**/*.' + inputFormat)

for path in pathList:
    inputFileName = str(Path(path).resolve())
    outputFileName = Path(inputFileName).stem + "_resampled." + outputFormat.lower()
    
    ms = ml.MeshSet()
    ms.load_new_mesh(inputFileName)
    
    newSampleNum = int(ms.current_mesh().vertex_number() * samplePercentage)
    if (newSampleNum < 1):
        newSampleNum = 1
    
    ms.apply_filter("poisson_disk_sampling", samplenum=newSampleNum, subsample=True)
    ms.save_current_mesh(outputFileName)
  
