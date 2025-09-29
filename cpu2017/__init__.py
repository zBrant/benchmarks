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
  'specrand_fs': '996.specrand_fs',
  'specrand_fr': '997.specrand_fr',
  'specrand_is': '998.specrand_is',
  'specrand_ir': '999.specrand_ir',
}

name_to_input_index = {
    'perlbench_r': {
        'test': [],
        'train': [],
        'ref': ['checkspam', 'diffmail', 'splitmail'],
    },
    'perlbench_s': {
        'test': [],
        'train': [],
        'ref': ['checkspam', 'diffmail', 'splitmail'],
    },
    'gcc_r': {
        'test': [],
        'train': [],
        'ref': ['gcc-pp', 'gcc-smaller', 'ref32'],
    },
    'gcc_s': {
        'test': [],
        'train': [],
        'ref': ['gcc-pp'],
    },
    'mcf_r': {
        'test': [],
        'train': [],
        'ref': ['inp'],
    },
    'mcf_s': {
        'test': [],
        'train': [],
        'ref': ['inp'],
    },
    'omnetpp_r': {
        'test': [],
        'train': [],
        'ref': ['omnetpp'],
    },
    'omnetpp_s': {
        'test': [],
        'train': [],
        'ref': ['omnetpp'],
    },
    'xalancbmk_r': {
        'test': [],
        'train': [],
        'ref': ['t5', '100mb', 'xalanc'],
    },
    'xalancbmk_s': {
        'test': [],
        'train': [],
        'ref': ['t5', '100mb', 'xalanc'],
    },
    'x264_r': {
        'test': [],
        'train': [],
        'ref': ['BuckBunny'],
    },
    'x264_s': {
        'test': [],
        'train': [],
        'ref': ['BuckBunny'],
    },
    'deepsjeng_r': {
        'test': [],
        'train': [],
        'ref': ['ref'],
    },
    'deepsjeng_s': {
        'test': [],
        'train': [],
        'ref': ['ref'],
    },
    'leela_r': {
        'test': [],
        'train': [],
        'ref': ['ref'],
    },
    'leela_s': {
        'test': [],
        'train': [],
        'ref': ['ref'],
    },
    'exchange2_r': {
        'test': [],
        'train': [],
        'ref': ['6'],
    },
    'exchange2_s': {
        'test': [],
        'train': [],
        'ref': ['6'],
    },
    'xz_r': {
        'test': [],
        'train': [],
        'ref': ['cld.tar', 'cpu2006docs.tar', 'input.combined'],
    },
    'xz_s': {
        'test': [],
        'train': [],
        'ref': ['cpu2006docs.tar', 'cld.tar'],
    },
    'specrand_ir': {
        'test': [],
        'train': [],
        'ref': ['1255432124', '234923'],
    },
    'specrand_is': {
        'test': [],
        'train': [],,
        'ref': ['1255432124', '234923'],
    },
    'bwaves_r': {
        'test': [],
        'train': [],
        'ref': ['bwaves_1', 'bwaves_2', 'bwaves_3', 'bwaves_4'],
    },
    'bwaves_s': {
        'test': [],
        'train': [],
        'ref': ['bwaves_1', 'bwaves_2'],
    },
    'cactuBSSN_r': {
        'test': [],
        'train': [],
        'ref': ['spec_ref'],
    },
    'cactuBSSN_s': {
        'test': [],
        'train': [],
        'ref': ['spec_ref'],
    },
    'namd_r': {
        'test': [],
        'train': [],
        'ref': ['namd'],
    },
    'parest_r': {
	'test': [],
        'train': [],
        'ref': ['ref'],
    },
    'povray_r': {
        'test': [],
        'train': [],
        'ref': ['SPEC-benchmark-ref'],
    },
    'lbm_r': {
        'test': [],
        'train': [],
        'ref': ['100_100_130_ldc'],
    },
    'lbm_s': {
        'test': [],
        'train': [],
        'ref': ['200_200_260_ldc'],
    },
    'wrf_r': {
        'test': [],
        'train': [],
        'ref': ['namelist'],
    },
    'wrf_s': {
        'test': [],
        'train': [],
        'ref': ['namelist'],
    },
    'blender_r': {
        'test': [],
        'train': [],
        'ref': ['sh3_no_char'],
    },
    'cam4_r': {
        'test': [],
        'train': [],
        'ref': ['atm_in', 'drv_flds_in', 'drv_in'],
    },
    'cam4_s': {
        'test': [],
        'train': [],
        'ref': ['atm_in', 'drv_flds_in', 'drv_in'],
    },
    'pop2_s': {
        'test': [],
        'train': [],
        'ref': ['pop2_in'],
    },
    'imagick_r': {
        'test': [],
        'train': [],
        'ref': ['refrate_convert'],
    },
    'imagick_s': {
        'test': [],
        'train': [],
        'ref': ['refspeed_convert'],
    },
    'nab_r': {
        'test': [],
        'train': [],
        'ref': ['1am0'],
    },
    'nab_s': {
        'test': [],
        'train': [],
        'ref': ['3j1n'],
    },
    'fotonik3d_r': {
        'test': [],
        'train': [],
        'ref': ['fotonik3d'], # maybe wrong
    },
    'fotonik3d_s': {
        'test': [],
        'train': [],
        'ref': ['fotonik3d'], # maybe wrong
    },
    'roms_r': {
        'test': [],
        'train': [],
        'ref': ['ocean_benchmark2'],
    },
    'roms_s': {
        'test': [],
        'train': [],
        'ref': ['ocean_benchmark3'],
    },
    'specrand_fr': {
        'test': [],
        'train': [], 
        'ref': ['rand.234923'], # maybe wrong
    },
    'specrand_fs': {
        'test': [],
        'train': [],
        'ref': ['rand.234923'], # maybe wrong
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
      elif self.program == 'sphinx3':
        for datadir in (os.path.join('data',self.inputsize,'input'),):
          datadir = os.path.abspath(os.path.join(HOME,'CPU2006',name_to_dir[self.program],datadir))
          if not os.path.exists(datadir): raise Exception('Unable to find sphinx3-specific files')
          files = []
          for filename in os.listdir(datadir):
            if '.le.raw' in filename:
              files.append(filename.split('.le.raw')[0])
              destfilename = filename.split('.le.raw')[0]+'.raw'
              filename = os.path.abspath(os.path.join(datadir, filename))
              os.symlink(filename, os.path.join(rundir,os.path.basename(destfilename)))
          ctlfp = open(os.path.join(rundir,'ctlfile'), 'w')
          for f in sorted(files):
            ctlfp.write('%s %u\n' % (f, os.stat(os.path.join(rundir,f+'.raw')).st_size))
          ctlfp.close()
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
