TUNE=base
LABEL=primeiro-teste-m64
NUMBER=654
NAME=roms_s
SOURCES= bbl.F90 bc_2d.F90 exchange_2d.F90 mod_param.F90 mod_kinds.F90 \
	 mod_grid.F90 mod_scalars.F90 mod_bbl.F90 mod_forces.F90 mod_ocean.F90 \
	 mod_sediment.F90 mod_parallel.F90 mod_iounits.F90 mod_strings.F90 \
	 mod_stepping.F90 mp_exchange.F90 bc_3d.F90 exchange_3d.F90 bc_bry2d.F90 \
	 bc_bry3d.F90 bulk_flux.F90 mod_mixing.F90 bvf_mix.F90 conv_2d.F90 \
	 conv_3d.F90 conv_bry2d.F90 conv_bry3d.F90 diag.F90 analytical.F90 \
	 distribute.F90 mod_ncparam.F90 mod_biology.F90 mod_eclight.F90 \
	 mod_boundary.F90 mod_clima.F90 mod_sources.F90 mod_netcdf.F90 \
	 strings.F90 forcing.F90 mod_coupling.F90 frc_adjust.F90 get_data.F90 \
	 mod_obs.F90 get_idata.F90 mod_tides.F90 nf_fread3d.F90 nf_fread4d.F90 \
	 gls_corstep.F90 tkebc_im.F90 gls_prestep.F90 hmixing.F90 ini_fields.F90 \
	 set_depth.F90 t3dbc_im.F90 u2dbc_im.F90 u3dbc_im.F90 v2dbc_im.F90 \
	 v3dbc_im.F90 zetabc.F90 initial.F90 ini_adjust.F90 mod_fourdvar.F90 \
	 state_addition.F90 state_copy.F90 metrics.F90 ocean_coupler.F90 \
	 mod_coupler.F90 roms_export.F90 roms_import.F90 omega.F90 rho_eos.F90 \
	 mod_eoscoef.F90 set_massflux.F90 stiffness.F90 wpoints.F90 \
	 mod_storage.F90 interp_floats.F90 lmd_bkpp.F90 shapiro.F90 lmd_skpp.F90 \
	 lmd_swfrac.F90 lmd_vmix.F90 main2d.F90 dotproduct.F90 obc_adjust.F90 \
	 oi_update.F90 radiation_stress.F90 mod_diags.F90 set_avg.F90 \
	 mod_average.F90 set_tides.F90 set_vbc.F90 step2d.F90 obc_volcons.F90 \
	 wetdry.F90 step_floats.F90 mod_floats.F90 vwalk_floats.F90 utility.F90 \
	 main3d.F90 biology.F90 my25_corstep.F90 my25_prestep.F90 rhs3d.F90 \
	 pre_step3d.F90 prsgrd.F90 t3dmix.F90 uv3dmix.F90 sediment.F90 \
	 sed_bed.F90 sed_bedload.F90 sed_fluxes.F90 sed_settling.F90 \
	 sed_surface.F90 set_zeta.F90 step3d_t.F90 mpdata_adiff.F90 step3d_uv.F90 \
	 wvelocity.F90 output.F90 set_data.F90 set_2dfld.F90 set_3dfld.F90 \
	 abort.F90 ocean_control.F90 back_cost.F90 cgradient.F90 nf_fread2d.F90 \
	 nf_fread2d_bry.F90 nf_fread3d_bry.F90 state_dotprod.F90 \
	 state_initialize.F90 state_scale.F90 cost_grad.F90 normalization.F90 \
	 nf_fwrite2d.F90 nf_fwrite3d.F90 white_noise.F90 nrutil.F90 packing.F90 \
	 posterior.F90 posterior_var.F90 state_product.F90 propagator.F90 \
	 random_ic.F90 sum_grad.F90 zeta_balance.F90 checkadj.F90 checkdefs.F90 \
	 checkerror.F90 checkvars.F90 close_io.F90 congrad.F90 def_avg.F90 \
	 def_var.F90 def_diags.F90 def_dim.F90 def_error.F90 def_floats.F90 \
	 def_gst.F90 def_hessian.F90 def_his.F90 def_impulse.F90 def_info.F90 \
	 def_ini.F90 def_lanczos.F90 def_mod.F90 def_norm.F90 def_rst.F90 \
	 def_station.F90 def_tides.F90 extract_obs.F90 extract_sta.F90 \
	 frc_weak.F90 gasdev.F90 get_2dfld.F90 get_2dfldr.F90 get_3dfld.F90 \
	 get_3dfldr.F90 get_bounds.F90 get_cycle.F90 get_date.F90 get_grid.F90 \
	 get_gst.F90 get_ngfld.F90 get_ngfldr.F90 get_state.F90 get_varcoords.F90 \
	 grid_coords.F90 interpolate.F90 ini_lanczos.F90 inp_par.F90 \
	 ran_state.F90 lubksb.F90 ludcmp.F90 mp_routines.F90 nf_fwrite2d_bry.F90 \
	 nf_fwrite3d_bry.F90 nf_fwrite4d.F90 obs_cost.F90 obs_depth.F90 \
	 obs_initial.F90 obs_read.F90 obs_write.F90 ran1.F90 regrid.F90 \
	 rep_matrix.F90 set_2dfldr.F90 set_3dfldr.F90 set_diags.F90 set_ngfld.F90 \
	 set_ngfldr.F90 set_scoord.F90 set_weights.F90 stats_modobs.F90 \
	 timers.F90 wrt_avg.F90 wrt_diags.F90 wrt_error.F90 wrt_floats.F90 \
	 wrt_gst.F90 wrt_hessian.F90 wrt_his.F90 wrt_impulse.F90 wrt_info.F90 \
	 wrt_ini.F90 wrt_rst.F90 wrt_station.F90 wrt_tides.F90 mod_arrays.F90 \
	 mod_nesting.F90 esmf_roms.F90 master.F90
EXEBASE=sroms
NEED_MATH=
BENCHLANG=F

BENCH_CFLAGS     = -I.
BENCH_FFLAGS     = -I.
BENCH_FPPFLAGS   = -w -m literal-single.pm -m c-comment.pm -I. -DBENCHMARK -DNestedGrids=1 -DNO_GETTIMEOFDAY
CC               = $(SPECLANG)gcc     -std=c99   -m64
CC_VERSION_OPTION = -v
CXX              = $(SPECLANG)g++     -std=c++03 -m64
CXX_VERSION_OPTION = -v
EXTRA_OPTIMIZE   = -fopenmp -DSPEC_OPENMP
EXTRA_PORTABILITY = -DSPEC_LP64
FC               = $(SPECLANG)gfortran           -m64
FC_VERSION_OPTION = -v
OPTIMIZE         = -g -O3 -march=native -fno-unsafe-math-optimizations  -fno-tree-loop-vectorize
OS               = unix
SPECLANG         = /usr/bin/
absolutely_no_locking = 0
abstol           = 1e-07
action           = build
allow_label_override = 0
backup_config    = 1
baseexe          = sroms
basepeak         = 1
benchdir         = benchspec
benchmark        = 654.roms_s
binary           = 
bindir           = exe
builddir         = build
bundleaction     = 
bundlename       = 
calctol          = 1
changedhash      = 0
check_version    = 0
clean_between_builds = no
command_add_redirect = 1
commanderrfile   = speccmds.err
commandexe       = sroms_base.primeiro-teste-m64
commandfile      = speccmds.cmd
commandoutfile   = speccmds.out
commandstdoutfile = speccmds.stdout
comparedir       = compare
compareerrfile   = compare.err
comparefile      = compare.cmd
compareoutfile   = compare.out
comparestdoutfile = compare.stdout
compile_error    = 0
compwhite        = 
configdir        = config
configfile       = my-first-run.cfg
configpath       = /home/kratos/cpu2017/config/my-first-run.cfg
copies           = 1
current_range    = 
datadir          = data
default_size     = ref
default_submit   = $command
delay            = 0
deletebinaries   = 0
deletework       = 0
dependent_workloads = 0
device           = 
difflines        = 10
dirprot          = 511
discard_power_samples = 0
enable_monitor   = 1
endian           = 12345678
env_vars         = 0
expand_notes     = 0
expid            = 
exthash_bits     = 256
failflags        = 0
fake             = 1
feedback         = 1
flag_url_base    = https://www.spec.org/auto/cpu2017/Docs/benchmarks/flags/
floatcompare     = 
force_monitor    = 0
from_runcpu      = 2
fw_bios          = virtualbox
hostname         = watter
http_proxy       = 
http_timeout     = 30
hw_avail         = Ago-2025
hw_cpu_max_mhz   = 4100
hw_cpu_name      = AMD Ryzen 7 5700X3D
hw_cpu_nominal_mhz = 3000
hw_disk          = 1 TB SSD NVMe
hw_memory001     = 16 GB (1 x 16 GB DDR4-3200)
hw_memory002     = 'N GB (N x N GB nRxn PC4-nnnnX-X)'
hw_model         = 'Test Build'
hw_nchips        = 1
hw_ncores        = 8
hw_ncpuorder     = 1-9 chips
hw_nthreadspercore = 2
hw_ocache        = None
hw_other         = None
hw_pcache        = 64 KB I + 64 KB D on chip per core
hw_scache        = 512 KB I+D on chip per core
hw_tcache        = 96 MB I+D on chip
hw_vendor        = My Test
idle_current_range = 
idledelay        = 10
idleduration     = 60
ignore_errors    = 1
ignore_sigint    = 0
ignorecase       = 
info_wrap_columns = 50
inputdir         = input
inputgenerrfile  = inputgen.err
inputgenfile     = inputgen.cmd
inputgenoutfile  = inputgen.out
inputgenstdoutfile = inputgen.stdout
iteration        = -1
iterations       = 1
keeptmp          = 0
label            = primeiro-teste-m64
license_num      = 2017
line_width       = 1020
link_input_files = 1
locking          = 1
log              = CPU2017
log_line_width   = 1020
log_timestamp    = 0
logfile          = /home/kratos/cpu2017/tmp/CPU2017.008/templogs/preenv.fpspeed.008.1
logname          = /home/kratos/cpu2017/tmp/CPU2017.008/templogs/preenv.fpspeed.008.1
lognum           = 008.1
mail_reports     = all
mailcompress     = 0
mailmethod       = smtp
mailport         = 25
mailserver       = 127.0.0.1
mailto           = 
make             = specmake
make_no_clobber  = 0
makefile_template = Makefile.YYYtArGeTYYYspec
makeflags        = --jobs=8
max_average_uncertainty = 1
max_hum_limit    = 0
max_report_runs  = 3
max_unknown_uncertainty = 1
mean_anyway      = 1
meter_connect_timeout = 30
meter_errors_default = 5
meter_errors_percentage = 5
min_report_runs  = 2
min_temp_limit   = 20
minimize_builddirs = 0
minimize_rundirs = 0
name             = roms_s
nansupport       = 
need_math        = 
no_input_handler = close
no_monitor       = 
noratios         = 0
note_preenv      = 1
notes_plat_sysinfo_000 = 
notes_plat_sysinfo_005 =  Sysinfo program /home/kratos/cpu2017/bin/sysinfo
notes_plat_sysinfo_010 =  Rev: r6365 of 2019-08-21 295195f888a3d7edb1e6e46a485a0011
notes_plat_sysinfo_015 =  running on watter Sat Sep 27 22:21:00 2025
notes_plat_sysinfo_020 = 
notes_plat_sysinfo_025 =  SUT (System Under Test) info as seen by some common utilities.
notes_plat_sysinfo_030 =  For more information on this section, see
notes_plat_sysinfo_035 =     https://www.spec.org/cpu2017/Docs/config.html\#sysinfo
notes_plat_sysinfo_040 = 
notes_plat_sysinfo_045 =  From /proc/cpuinfo
notes_plat_sysinfo_050 =     model name : AMD Ryzen 7 5700X3D 8-Core Processor
notes_plat_sysinfo_055 =        1  "physical id"s (chips)
notes_plat_sysinfo_060 =        8 "processors"
notes_plat_sysinfo_065 =     cores, siblings (Caution: counting these is hw and system dependent. The following
notes_plat_sysinfo_070 =     excerpts from /proc/cpuinfo might not be reliable.  Use with caution.)
notes_plat_sysinfo_075 =        cpu cores : 8
notes_plat_sysinfo_080 =        siblings  : 8
notes_plat_sysinfo_085 =        physical 0: cores 0 1 2 3 4 5 6 7
notes_plat_sysinfo_090 = 
notes_plat_sysinfo_095 =  From lscpu:
notes_plat_sysinfo_100 =       Architecture:                         x86_64
notes_plat_sysinfo_105 =       CPU op-mode(s):                       32-bit, 64-bit
notes_plat_sysinfo_110 =       Address sizes:                        48 bits physical, 48 bits virtual
notes_plat_sysinfo_115 =       Byte Order:                           Little Endian
notes_plat_sysinfo_120 =       CPU(s):                               8
notes_plat_sysinfo_125 =       On-line CPU(s) list:                  0-7
notes_plat_sysinfo_130 =       Vendor ID:                            AuthenticAMD
notes_plat_sysinfo_135 =       Model name:                           AMD Ryzen 7 5700X3D 8-Core Processor
notes_plat_sysinfo_140 =       CPU family:                           25
notes_plat_sysinfo_145 =       Model:                                33
notes_plat_sysinfo_150 =       Thread(s) per core:                   1
notes_plat_sysinfo_155 =       Core(s) per socket:                   8
notes_plat_sysinfo_160 =       Socket(s):                            1
notes_plat_sysinfo_165 =       Stepping:                             2
notes_plat_sysinfo_170 =       BogoMIPS:                             6000.00
notes_plat_sysinfo_175 =       Flags:                                fpu vme de pse tsc msr pae mce cx8 apic sep
notes_plat_sysinfo_180 =       mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt
notes_plat_sysinfo_185 =       rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid tsc_known_freq
notes_plat_sysinfo_190 =       pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c
notes_plat_sysinfo_195 =       rdrand hypervisor lahf_lm cmp_legacy cr8_legacy abm sse4a misalignsse 3dnowprefetch
notes_plat_sysinfo_200 =       vmmcall fsgsbase bmi1 avx2 bmi2 invpcid rdseed adx clflushopt sha_ni arat debug_swap
notes_plat_sysinfo_205 =       Hypervisor vendor:                    KVM
notes_plat_sysinfo_210 =       Virtualization type:                  full
notes_plat_sysinfo_215 =       L1d cache:                            256 KiB (8 instances)
notes_plat_sysinfo_220 =       L1i cache:                            256 KiB (8 instances)
notes_plat_sysinfo_225 =       L2 cache:                             4 MiB (8 instances)
notes_plat_sysinfo_230 =       L3 cache:                             768 MiB (8 instances)
notes_plat_sysinfo_235 =       NUMA node(s):                         1
notes_plat_sysinfo_240 =       NUMA node0 CPU(s):                    0-7
notes_plat_sysinfo_245 =       Vulnerability Gather data sampling:   Not affected
notes_plat_sysinfo_250 =       Vulnerability Itlb multihit:          Not affected
notes_plat_sysinfo_255 =       Vulnerability L1tf:                   Not affected
notes_plat_sysinfo_260 =       Vulnerability Mds:                    Not affected
notes_plat_sysinfo_265 =       Vulnerability Meltdown:               Not affected
notes_plat_sysinfo_270 =       Vulnerability Mmio stale data:        Not affected
notes_plat_sysinfo_275 =       Vulnerability Reg file data sampling: Not affected
notes_plat_sysinfo_280 =       Vulnerability Retbleed:               Not affected
notes_plat_sysinfo_285 =       Vulnerability Spec rstack overflow:   Vulnerable: Safe RET, no microcode
notes_plat_sysinfo_290 =       Vulnerability Spec store bypass:      Not affected
notes_plat_sysinfo_295 =       Vulnerability Spectre v1:             Mitigation; usercopy/swapgs barriers and
notes_plat_sysinfo_300 =       __user pointer sanitization
notes_plat_sysinfo_305 =       Vulnerability Spectre v2:             Mitigation; Retpolines; STIBP disabled; RSB
notes_plat_sysinfo_310 =       filling; PBRSB-eIBRS Not affected; BHI Not affected
notes_plat_sysinfo_315 =       Vulnerability Srbds:                  Not affected
notes_plat_sysinfo_320 =       Vulnerability Tsx async abort:        Not affected
notes_plat_sysinfo_325 = 
notes_plat_sysinfo_330 =  /proc/cpuinfo cache data
notes_plat_sysinfo_335 =     cache size : 512 KB
notes_plat_sysinfo_340 = 
notes_plat_sysinfo_345 =  From numactl --hardware  WARNING: a numactl 'node' might or might not correspond to a
notes_plat_sysinfo_350 =  physical chip.
notes_plat_sysinfo_355 = 
notes_plat_sysinfo_360 =  From /proc/meminfo
notes_plat_sysinfo_365 =     MemTotal:       16376184 kB
notes_plat_sysinfo_370 =     HugePages_Total:       0
notes_plat_sysinfo_375 =     Hugepagesize:       2048 kB
notes_plat_sysinfo_380 = 
notes_plat_sysinfo_385 =  /usr/bin/lsb_release -d
notes_plat_sysinfo_390 =     Ubuntu 22.04.5 LTS
notes_plat_sysinfo_395 = 
notes_plat_sysinfo_400 =  From /etc/*release* /etc/*version*
notes_plat_sysinfo_405 =     debian_version: bookworm/sid
notes_plat_sysinfo_410 =     os-release:
notes_plat_sysinfo_415 =        PRETTY_NAME="Ubuntu 22.04.5 LTS"
notes_plat_sysinfo_420 =        NAME="Ubuntu"
notes_plat_sysinfo_425 =        VERSION_ID="22.04"
notes_plat_sysinfo_430 =        VERSION="22.04.5 LTS (Jammy Jellyfish)"
notes_plat_sysinfo_435 =        VERSION_CODENAME=jammy
notes_plat_sysinfo_440 =        ID=ubuntu
notes_plat_sysinfo_445 =        ID_LIKE=debian
notes_plat_sysinfo_450 =        HOME_URL="https://www.ubuntu.com/"
notes_plat_sysinfo_455 = 
notes_plat_sysinfo_460 =  uname -a:
notes_plat_sysinfo_465 =     Linux watter 6.8.0-79-generic \#79~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Fri Aug 15
notes_plat_sysinfo_470 =     16:54:53 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
notes_plat_sysinfo_475 = 
notes_plat_sysinfo_480 =  Kernel self-reported vulnerability status:
notes_plat_sysinfo_485 = 
notes_plat_sysinfo_490 =  gather_data_sampling:                     Not affected
notes_plat_sysinfo_495 =  itlb_multihit:                            Not affected
notes_plat_sysinfo_500 =  CVE-2018-3620 (L1 Terminal Fault):        Not affected
notes_plat_sysinfo_505 =  Microarchitectural Data Sampling:         Not affected
notes_plat_sysinfo_510 =  CVE-2017-5754 (Meltdown):                 Not affected
notes_plat_sysinfo_515 =  mmio_stale_data:                          Not affected
notes_plat_sysinfo_520 =  reg_file_data_sampling:                   Not affected
notes_plat_sysinfo_525 =  retbleed:                                 Not affected
notes_plat_sysinfo_530 =  spec_rstack_overflow:                     Vulnerable: Safe RET, no microcode
notes_plat_sysinfo_535 =  CVE-2018-3639 (Speculative Store Bypass): Not affected
notes_plat_sysinfo_540 =  CVE-2017-5753 (Spectre variant 1):        Mitigation: usercopy/swapgs barriers and __user
notes_plat_sysinfo_545 =                                            pointer sanitization
notes_plat_sysinfo_550 =  CVE-2017-5715 (Spectre variant 2):        Mitigation: Retpolines; STIBP: disabled; RSB
notes_plat_sysinfo_555 =                                            filling; PBRSB-eIBRS: Not affected; BHI: Not
notes_plat_sysinfo_560 =                                            affected
notes_plat_sysinfo_565 =  srbds:                                    Not affected
notes_plat_sysinfo_570 =  tsx_async_abort:                          Not affected
notes_plat_sysinfo_575 = 
notes_plat_sysinfo_580 =  run-level 5 Sep 14 23:57
notes_plat_sysinfo_585 = 
notes_plat_sysinfo_590 =  SPEC is set to: /home/kratos/cpu2017
notes_plat_sysinfo_595 =     Filesystem     Type  Size  Used Avail Use% Mounted on
notes_plat_sysinfo_600 =     /dev/sda3      ext4   78G   30G   44G  41% /
notes_plat_sysinfo_605 = 
notes_plat_sysinfo_610 =  From /sys/devices/virtual/dmi/id
notes_plat_sysinfo_615 =      BIOS:    innotek GmbH VirtualBox 12/01/2006
notes_plat_sysinfo_620 =      Vendor:  innotek GmbH
notes_plat_sysinfo_625 =      Product: VirtualBox
notes_plat_sysinfo_630 =      Product Family: Virtual Machine
notes_plat_sysinfo_635 = 
notes_plat_sysinfo_640 =  Cannot run dmidecode; consider saying (as root)
notes_plat_sysinfo_645 =     chmod +s /usr/sbin/dmidecode
notes_plat_sysinfo_650 = 
notes_plat_sysinfo_655 =  (End of data from sysinfo program)
notes_wrap_columns = 0
notes_wrap_indent =   
num              = 654
obiwan           = 
os_exe_ext       = 
output_format    = txt,html,cfg,pdf,csv
output_root      = 
outputdir        = output
parallel_test    = 0
parallel_test_submit = 0
parallel_test_workloads = 
path             = /home/kratos/cpu2017/benchspec/CPU/654.roms_s
plain_train      = 1
platform         = 
power            = 0
preENV_LD_LIBRARY_PATH = %{gcc_dir}/lib64/:%{gcc_dir}/lib/:/lib64
preENV_OMP_STACKSIZE = 120M
preenv           = 0
prefix           = 
prepared_by      = Watta
ranks            = 1
rawhash_bits     = 256
rebuild          = 1
reftime          = reftime
reltol           = 1e-07
reportable       = 0
resultdir        = result
review           = 0
run              = all
runcpu           = /home/kratos/cpu2017/bin/harness/runcpu --configfile my-first-run.cfg --action build --fake --noreportable --nopower --runmode speed --tune base --size refspeed fpspeed --nopreenv --note-preenv --logfile /home/kratos/cpu2017/tmp/CPU2017.008/templogs/preenv.fpspeed.008.1 --lognum 008.1 --from_runcpu 2
rundir           = run
runmode          = speed
safe_eval        = 1
save_build_files = 
section_specifier_fatal = 1
setprocgroup     = 1
setup_error      = 0
sigint           = 2
size             = refspeed
size_class       = ref
skipabstol       = 
skipobiwan       = 
skipreltol       = 
skiptol          = 
smarttune        = base
specdiff         = specdiff
specrun          = specinvoke
srcalt           = 
srcdir           = src
srcsource        = /home/kratos/cpu2017/benchspec/CPU/554.roms_r/src
stagger          = 10
strict_rundir_verify = 1
sw_avail         = Ago-2025
sw_base_ptrsize  = 64-bit
sw_compiler001   = C/C++/Fortran: Version 11.4.0 of GCC, the
sw_compiler002   = GNU Compiler Collection
sw_file          = ext4
sw_os001         = Ubuntu 22.04.5 LTS
sw_os002         = 6.8.0-79-generic
sw_other         = None
sw_peak_ptrsize  = Not Applicable
sw_state         = 
sysinfo_hash_bits = 256
sysinfo_program  = specperl /home/kratos/cpu2017/bin/sysinfo
sysinfo_program_hash = sysinfo:SHA:1b187da62efa5d65f0e989c214b6a257d16a31d3cf135973c9043da741052207
table            = 1
teeout           = 1
test_date        = Sep-2025
test_sponsor     = My Test
tester           = My Test
threads          = 4
top              = /home/kratos/cpu2017
train_single_thread = 0
train_with       = train
tune             = base
uid              = 1000
unbuffer         = 1
uncertainty_exception = 5
update           = 0
update_url       = http://www.spec.org/auto/cpu2017/updates/
use_submit_for_compare = 0
use_submit_for_speed = 0
username         = kratos
verbose          = 5
verify_binaries  = 1
version          = 1.000503
voltage_range    = 
worklist         = list
OUTPUT_RMFILES   = ocean_benchmark1.log
