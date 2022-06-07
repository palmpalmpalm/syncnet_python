# #!/usr/bin/python
# #-*- coding: utf-8 -*-

# import time, pdb, argparse, subprocess, pickle, os, gzip, glob

# from SyncNetInstance import *

# # ==================== PARSE ARGUMENT ====================

# parser = argparse.ArgumentParser(description = "SyncNet");
# parser.add_argument('--initial_model', type=str, default="data/syncnet_v2.model", help='');
# parser.add_argument('--batch_size', type=int, default='20', help='');
# parser.add_argument('--vshift', type=int, default='15', help='');
# parser.add_argument('--data_dir', type=str, default='data/work', help='');
# parser.add_argument('--videofile', type=str, default='', help='');
# parser.add_argument('--reference', type=str, default='', help='');
# opt = parser.parse_args();

# setattr(opt,'avi_dir',os.path.join(opt.data_dir,'pyavi'))
# setattr(opt,'tmp_dir',os.path.join(opt.data_dir,'pytmp'))
# setattr(opt,'work_dir',os.path.join(opt.data_dir,'pywork'))
# setattr(opt,'crop_dir',os.path.join(opt.data_dir,'pycrop'))


# # ==================== LOAD MODEL AND FILE LIST ====================

# s = SyncNetInstance();

# s.loadParameters(opt.initial_model);
# print("Model %s loaded."%opt.initial_model);

# flist = glob.glob(os.path.join(opt.crop_dir,opt.reference,'0*.avi'))
# flist.sort()

# # ==================== GET OFFSETS ====================

# dists = []
# for idx, fname in enumerate(flist):
#     offset, conf, dist = s.evaluate(opt,videofile=fname)
#     dists.append(dist)
      
# # ==================== PRINT RESULTS TO FILE ====================

# with open(os.path.join(opt.work_dir,opt.reference,'activesd.pckl'), 'wb') as fil:
#     pickle.dump(dists, fil)

#!/usr/bin/python
#-*- coding: utf-8 -*-

# ================================================================================
# ================================================================================
# ================================================================================


import time, pdb, argparse, subprocess, pickle, os, gzip, glob
from typing import NamedTuple
from dataclasses import dataclass

from SyncNetInstance import *

# ==================== REPLACE ARGUMENTS WITH DATACLASS ====================

@dataclass
class opt:
    initial_model = "data/syncnet_v2.model"
    batch_size = 20
    vshift = 15
    data_dir = "data/work"
    videofile = ""
    reference = ""
    avi_dir = "data/work/pyavi"
    tmp_dir = "data/work/pytmp"
    work_dir = "data/work/pywork"
    crop_dir = "data/work/pycrop"
    
    

# ==================== LOAD MODEL AND FILE LIST ====================

s = SyncNetInstance();

s.loadParameters(opt.initial_model);
print("Model %s loaded."%opt.initial_model);



def get_offset(vidfile, data_dir, reference):
    opt.video_file = vidfile
    opt.reference = reference
    opt.data_dir = data_dir
    opt.avi_dir = os.path.join(data_dir,'pyavi')
    opt.crop_dir = os.path.join(data_dir,'pycrop')
    opt.tmp_dir = os.path.join(data_dir,'pytmp')
    opt.work_dir = os.path.join(data_dir,'pywork')
    
    
    flist = glob.glob(os.path.join(opt.crop_dir,opt.reference,'0*.avi'))
    flist.sort()

    for idx, fname in enumerate(flist):
        offset, conf, dist = s.evaluate(opt,videofile=fname)
        
    return offset
