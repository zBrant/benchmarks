#!/usr/bin/env python3

import os, tomllib, copy, argparse, shutil, sys
from itertools import product

HOME_SNIPER = os.environ['GRAPHITE_ROOT']
HOME_BENCHMARKS = os.environ['BENCHMARKS_ROOT']
TASK_SPOOLER = 'tsp'

# these are the defaults values for each field
CFG_DEFAULT = { 
  "label": "default",
  "config": ["gainestown"],
  "slots": 4,
  "benchmarks": ["cpu2006", "parsec", "splash2", "cpu2017"],
  "apps": ["all"],
  "inputs": ["ref"],
  "n_cores": [4],
  "out_dir": ".",
  "instr": 100000000, #100M
  "force": False,
  "debug": False,
  "num_slots": 1,
}

sys.path.append(os.path.abspath(HOME_BENCHMARKS))

from suites import modules

def load_benchmark_apps():
  benchmarks = {}
  for module in sorted(modules):
    module = __import__(module)
    try:
      benchmarks[module.__name__] = ' '.join(module.allbenchmarks()).split(' ')
    except TypeError:
      print('INFO: %s not downloaded yet, run make to download its components.' % module.__name__)    
  return benchmarks


ALL_APPS = load_benchmark_apps() 


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('config', type=str, nargs=1, help='donuts configurations to the experiment')
  return parser.parse_args()


def parse_cfg_file(f):
  configs = []

  for config in f['runner']:
    cfg_dict = copy.deepcopy(CFG_DEFAULT)
    for key in config.keys():
      cfg_dict[key] = config[key]
    configs.append(cfg_dict)

  return configs


def add_app_to_spooler(benchmark, app_name, inpt, n_cores, config, out_dir, n_instr):
  cmd = f"{TASK_SPOOLER} {HOME_BENCHMARKS}/run-sniper -p {benchmark}-{app_name} -i {inpt} -n {n_cores} -c {config} -d {out_dir} -s stop-by-icount:{n_instr}"
  #os.system(cmd)
  print(cmd)


def run(config_file):
  cores = config_file['n_cores']
  benchmarks = config_file['benchmarks']
  configs = config_file['configs']
  inputs = config_file['inputs']
  apps = config_file['apps']
  n_instr = config_file['instr']
  out_dir = config_file['out_dir']
  label = config_file['label']

  slots = config_file['slots']
  os.system(f"{TASK_SPOOLER} -S {slots}")
    
  for benchmark in benchmarks:
    for config, n_cores, inpt, app in product(configs, cores, inputs, ALL_APPS[benchmark]):
      out_path = f"{out_dir}/results/{label}/{n_cores}/{benchmark}/{app}/{inpt}/{config}"
      add_app_to_spooler(benchmark, app, inpt, n_cores, config, out_path, n_instr)


def main():
  args = parse_args()

  try:
    if not os.path.isfile(args.config[0]): raise Exception("file not found")
    if not shutil.which(TASK_SPOOLER): raise Exception(f"task-spooler ({TASK_SPOOLER}) is not installed!")

    cfgs = None
    with open(args.config[0], 'rb') as f: cfgs = parse_cfg_file(tomllib.load(f))

    for cfg in cfgs: run(cfg)
  except Exception as e:
    print(f"An error occurred: {e}")


if __name__ == "__main__":
  main()
