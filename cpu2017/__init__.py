import sys, os, time, getopt, subprocess, tempfile

abspath = lambda d: os.path.abspath(os.path.join(d))

HOME = abspath(os.path.dirname(__file__))

postfix = '_base.sniper-x86_64'

def name_to_exe(name):
  return name.split('_')[0]+postfix

name_to_dir = {
  'perlbench_r': '500.perlbench_r',
  'gcc_r': '502.gcc_r',
  'bwaves_r': '503.bwaves_r',
  'mcf_r': '505.mcf_r',
  'cactuBSSN_r': '507.cactuBSSN_r',
  'namd_r': '508.namd_r',
  'parest_r': '510.parest_r',
  'povray_r': '511.povray_r',
  'lbm_r': '519.lbm_r',
  'omnetpp_r': '520.omnetpp_r',
  'wrf_r': '521.wrf_r',
  'xalancbmk_r': '523.xalancbmk_r',
  'x264_r': '525.x264_r',
  'blender_r': '526.blender_r',
  'cam4_r': '527.cam4_r',
  'deepsjeng_r': '531.deepsjeng_r',
  'imagick_r': '538.imagick_r',
  'leela_r': '541.leela_r',
  'nab_r': '544.nab_r',
  'exchange2_r': '548.exchange2_r',
  'fotonik3d_r': '549.fotonik3d_r',
  'roms_r': '554.roms_r',
  'xz_r': '557.xz_r',
  'perlbench_s': '600.perlbench_s',
  'gcc_s': '602.gcc_s',
  'bwaves_s': '603.bwaves_s',
  'mcf_s': '605.mcf_s',
  'cactuBSSN_s': '607.cactuBSSN_s',
  'lbm_s': '619.lbm_s',
  'omnetpp_s': '620.omnetpp_s',
  'wrf_s': '621.wrf_s',
  'xalancbmk_s': '623.xalancbmk_s',
  'x264_s': '625.x264_s',
  'cam4_s': '627.cam4_s',
  'pop2_s': '628.pop2_s',
  'deepsjeng_s': '631.deepsjeng_s',
  'imagick_s': '638.imagick_s',
  'leela_s': '641.leela_s',
  'nab_s': '644.nab_s',
  'exchange2_s': '648.exchange2_s',
  'fotonik3d_s': '649.fotonik3d_s',
  'roms_s': '654.roms_s',
  'xz_s': '657.xz_s',
  #'specrand_fs': '996.specrand_fs',
  #'specrand_fr': '997.specrand_fr',
  #'specrand_is': '998.specrand_is',
  #'specrand_ir': '999.specrand_ir',
}

name_to_input_index = {
  'perlbench_r': {
    'refrate': ['splitmail.in', 'checkspam.pl', 'diffmail.in', 'checkspam.in'],
    'all': [],
    'test': [],
    'train': []
  },
  'gcc_r': {
    'refrate': ['gcc-smaller.c', 'gcc-pp.c', 'control', 'ref32.c'],
    'all': [],
    'test': [],
    'train': []
  },
  'bwaves_r': {
    'refrate': ['bwaves_1.in', 'bwaves_3.in', 'bwaves_4.in', 'bwaves_2.in', 'control'],
    'all': [],
    'test': [],
    'train': []
  },
  'mcf_r': {
    'refrate': ['control', 'inp.in'],
    'all': [],
    'test': [],
    'train': []
  },
  'cactuBSSN_r': {
    'refrate': ['control', 'spec_ref.par'],
    'all': [],
    'test': [],
    'train': []
  },
  'namd_r': {
    'refrate': ['namd.in'],
    'all': [],
    'test': [],
    'train': []
  },
  'parest_r': {
    'refrate': ['ref.prm'],
    'all': [],
    'test': [],
    'train': []
  },
  'povray_r': {
    'refrate': ['SPEC-benchmark-ref.ini', 'SPEC-benchmark-ref.pov'],
    'all': [],
    'test': [],
    'train': []
  },
  'lbm_r': {
    'refrate': ['lbm.in', '100_100_130_ldc.of'],
    'all': [],
    'test': [],
    'train': []
  },
  'omnetpp_r': {
    'refrate': ['omnetpp.ini', 'control'],
    'all': [],
    'test': [],
    'train': []
  },
  'wrf_r': {
    'refrate': ['control', 'namelist.input'],
    'all': [],
    'test': [],
    'train': []
  },
  'xalancbmk_r': {
    'refrate': ['100mb.xsd', 't5.xml', 'xalanc.xsl', 'ref.lst'],
    'all': [],
    'test': [],
    'train': []
  },
  'x264_r': {
    'refrate': ['control', 'BuckBunny.264'],
    'all': [],
    'test': [],
    'train': []
  },
  'blender_r': {
    'refrate': ['sh3_no_char.blend', 'control'],
    'all': [],
    'test': [],
    'train': []
  },
  'cam4_r': {
    'refrate': ['drv_flds_in', 'atm_in', 'drv_in'],
    'all': [],
    'test': [],
    'train': []
  },
  'deepsjeng_r': {
    'refrate': ['ref.txt'],
    'all': [],
    'test': [],
    'train': []
  },
  'imagick_r': {
    'refrate': ['control', 'refrate_input.tga'],
    'all': [],
    'test': [],
    'train': []
  },
  'leela_r': {
    'refrate': ['ref.sgf'],
    'all': [],
    'test': [],
    'train': []
  },
  'nab_r': {
    'refrate': ['control'],
    'all': [],
    'test': [],
    'train': []
  },
  'exchange2_r': {
    'refrate': ['control'],
    'all': [],
    'test': [],
    'train': []
  },
  'fotonik3d_r': {
    'refrate': ['power2.dat', 'OBJ.dat.xz', 'power1.dat', 'yee.dat', 'TEwaveguide.m', 'incident_W3PC.def', 'PSI.dat', 'trans_W3PC.def'],
    'all': [],
    'test': [],
    'train': []
  },
  'roms_r': {
    'refrate': ['ocean_benchmark2.in.x'],
    'all': [],
    'test': [],
    'train': []
  },
  'xz_r': {
    'refrate': ['control'],
    'all': [],
    'test': [],
    'train': []
  },
  'perlbench_s': {
    'refspeed': ['splitmail.in', 'checkspam.pl', 'diffmail.in', 'checkspam.in'],
    'all': [],
    'test': [],
    'train': []
  },
  'gcc_s': {
    'refspeed': ['gcc-pp.c', 'control'],
    'all': [],
    'test': [],
    'train': []
  },
  'bwaves_s': {
    'refspeed': ['bwaves_1.in', 'bwaves_2.in', 'control'],
    'all': [],
    'test': [],
    'train': []
  },
  'mcf_s': {
    'refspeed': ['control', 'inp.in'],
    'all': [],
    'test': [],
    'train': []
  },
  'cactuBSSN_s': {
    'refspeed': ['control', 'spec_ref.par'],
    'all': [],
    'test': [],
    'train': []
  },
  'lbm_s': {
    'refspeed': ['lbm.in', '200_200_260_ldc.of'],
    'all': [],
    'test': [],
    'train': []
  },
  'omnetpp_s': {
    'refspeed': ['omnetpp.ini', 'control'],
    'all': [],
    'test': [],
    'train': []
  },
  'wrf_s': {
    'refspeed': ['control', 'namelist.input'],
    'all': [],
    'test': [],
    'train': []
  },
  'xalancbmk_s': {
    'refspeed': ['100mb.xsd', 't5.xml', 'xalanc.xsl', 'ref.lst'],
    'all': [],
    'test': [],
    'train': []
  },
  'x264_s': {
    'refspeed': ['control', 'BuckBunny.264'],
    'all': [],
    'test': [],
    'train': []
  },
  'cam4_s': {
    'refspeed': ['drv_flds_in', 'atm_in', 'drv_in'],
    'all': [],
    'test': [],
    'train': []
  },
  'pop2_s': {
    'refspeed': ['pop2_in', 'dlnd_in', 'nyf.gxgxs.T62.stream.txt', 'glc_modelio.nml', 'dlnd_sno_in', 'seq_maps.rc', 'nyf.ncep.T62.stream.txt', 'dice_ice_in', 'datm_atm_in', 'gx3v7_tavg_contents', 'dice_in', 'datm_in', 'cpl_modelio.nml', 'dlnd_rof_in', 'nyf.giss.T62.stream.txt', 'ice_modelio.nml', 'pop2_in.org', 'drv_in.in', 'runoff.1x1.stream.txt', 'dlnd_lnd_in', 'ssmi_ifrac.clim.x0.5.txt', 'ocn_modelio.nml', 'lnd_modelio.nml', 'atm_modelio.nml'],
    'all': [],
    'test': [],
    'train': []
  },
  'deepsjeng_s': {
    'refspeed': ['ref.txt'],
    'all': [],
    'test': [],
    'train': []
  },
  'imagick_s': {
    'refspeed': ['refspeed_input.tga', 'control'],
    'all': [],
    'test': [],
    'train': []
  },
  'leela_s': {
    'refspeed': ['ref.sgf'],
    'all': [],
    'test': [],
    'train': []
  },
  'nab_s': {
    'refspeed': ['control'],
    'all': [],
    'test': [],
    'train': []
  },
  'exchange2_s': {
    'refspeed': ['control'],
    'all': [],
    'test': [],
    'train': []
  },
  'fotonik3d_s': {
    'refspeed': ['power2.dat', 'incident_W3PC_25nm.def', 'trans_W3PC_25nm.def', 'OBJ.dat.xz', 'power1.dat', 'yee.dat', 'TEwaveguide.m', 'PSI.dat'],
    'all': [],
    'test': [],
    'train': []
  },
  'roms_s': {
    'refspeed': ['ocean_benchmark3.in.x'],
    'all': [],
    'test': [],
    'train': []
  },
  'xz_s': {
    'refspeed': ['control'],
    'all': [],
    'test': [],
    'train': []
  },
}

inputmap = {
  'test': 'test',
  'train': 'train',
  'ref': 'ref',
  'large': 'train',
  'huge': 'ref',
}

def allbenchmarks():
  return map(lambda x: x[0], sorted(name_to_dir.items(), key=lambda x: x[1]))

def allinputs():
  return inputmap.keys()


class Program:

  def __init__(self, program, nthreads, inputsize, benchmark_options = []):
    origprogram = program
    if '_' in program:
      pgm = program.split('_', 1)
      program = pgm[0]
      origindex = pgm[1]
      index = origindex

      try:
        index = int(index)
      except ValueError, e:
        if program in name_to_input_index:
          inps = name_to_input_index[program]
          if inputsize in inps:
            idxs = inps[inputsize]
            if index in idxs:
              index = idxs.index(index)
    else:
      index = 0
    if program not in allbenchmarks():
      raise ValueError("Invalid benchmark %s" % program)
    if inputsize not in allinputs():
      raise ValueError("Invalid input size %s" % inputsize)
    if index != 0 and index >= len(name_to_input_index.get(program, {}).get(inputsize, [])):
      raise ValueError("Invalid program index (%s/%s)" % (origprogram, index))
    self.program = program
    self.nthreads = nthreads
    self.inputsize = inputmap[inputsize]
    self.index = index


  def ncores(self):
    return self.nthreads


  def run(self, graphitecmd, postcmd = ''):
    rc = 1 # Indicate failure if there are any problems
    origcwd = os.getcwd()
    rundir = None
    try:
      rundir = tempfile.mkdtemp()
      os.chdir(rundir)
      # Link in all of the binaries and data files
      for datadir in (os.path.join('data','all','input'), os.path.join('data',self.inputsize,'input'), 'exe', 'Spec'):
        datadir = os.path.abspath(os.path.join(HOME,'CPU2017',name_to_dir[self.program],datadir))
        if not os.path.exists(datadir):
          continue
        for filename in os.listdir(datadir):
          filename = os.path.abspath(os.path.join(datadir, filename))
          os.symlink(filename, os.path.join(rundir,os.path.basename(filename)))
      # Additional preparation for some benchmarks
      if self.program == 'wrf_r':
	    for datadir in (os.path.join('data','all','input','le','32'),):
          datadir = os.path.abspath(os.path.join(HOME,'CPU2017',name_to_dir[self.program],datadir))
          if not os.path.exists(datadir):
	        raise Exception('Unable to find wrf-specific files')
	      for filename in os.listdir(datadir):
	        filename = os.path.abspath(os.path.join(datadir, filename))
	        os.symlink(filename, os.path.join(rundir,os.path.basename(filename)))
      input_filenames = []
      for indir in ('all', self.inputsize):
        try:
          input_filenames += os.listdir(os.path.join(HOME,'CPU2017',name_to_dir[self.program],'data',indir,'input'))
        except OSError:
          pass
      omp_cmd = '%s/run_spec.pl --name %s --exe %s --size %s --index %s ' % (HOME, self.program, name_to_exe(self.program), self.inputsize, self.index) + ' '.join(map(lambda x: '--input %s' % x, sorted(input_filenames)))
      cmd_to_run = subprocess.Popen(omp_cmd, shell=True, stdout=subprocess.PIPE).communicate()[0].split(' ',1)
      cmd_to_run = ' '.join([os.path.join(rundir,cmd_to_run[0]),len(cmd_to_run) == 2 and cmd_to_run[1] or ''])
    except Exception as e:
      print ('Error: ' + str(e) + ' in %s' % __file__)
      os.chdir(origcwd)
      if rundir != None:
        os.system('rm -rf "%s"' % rundir)
      raise

    rc = run_bm(self.program, cmd_to_run, graphitecmd, env = '', postcmd = postcmd)
    os.chdir(origcwd)
    os.system('rm -rf "%s"' % rundir)
    return rc


  def rungraphiteoptions(self):
    return ''


def run(cmd):
  sys.stdout.flush()
  sys.stderr.flush()
  rc = os.system(cmd)
  rc >>= 8
  return rc

def run_bm(bm, cmd, submit, env, postcmd = ''):
  print '[CPU2017]', '[========== Running benchmark', bm, '==========]'
  cmd = env + ' ' + submit + ' ' + cmd + ' ' + postcmd
  print '[CPU2017]', 'Running \'' + cmd + '\':'
  print '[CPU2017]', '[---------- Beginning of output ----------]'
  rc = run(cmd)
  print '[CPU2017]', '[----------    End of output    ----------]'
  print '[CPU2017]', 'Done.'
  return rc
