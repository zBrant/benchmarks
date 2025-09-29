TUNE=base
LABEL=primeiro-teste-m64
NUMBER=628
NAME=pop2_s
SOURCES= netcdf/attr.c netcdf/dim.c netcdf/error.c netcdf/fort-attio.c \
	 netcdf/fort-control.c netcdf/fort-dim.c netcdf/fort-genatt.c \
	 netcdf/fort-geninq.c netcdf/fort-genvar.c netcdf/fort-lib.c \
	 netcdf/fort-misc.c netcdf/fort-v2compat.c netcdf/fort-var1io.c \
	 netcdf/fort-varaio.c netcdf/fort-vario.c netcdf/fort-varmio.c \
	 netcdf/fort-varsio.c netcdf/libvers.c netcdf/nc.c netcdf/ncx.c \
	 netcdf/posixio.c netcdf/putget.c netcdf/string.c netcdf/v1hpg.c \
	 netcdf/v2i.c netcdf/var.c netcdf/netcdf.f90 netcdf/typeSizes.f90 \
	 fort.F90 mpi.c send.c recv.c collective.c req.c list.c handles.c comm.c \
	 group.c time.c pack.c m_IndexBin_char.F90 m_IndexBin_integer.F90 \
	 m_IndexBin_logical.F90 m_List.F90 m_MergeSorts.F90 m_Filename.F90 \
	 m_FcComms.F90 m_Permuter.F90 m_SortingTools.F90 m_String.F90 \
	 m_StrTemplate.F90 m_chars.F90 m_die.F90 m_dropdead.F90 m_FileResolv.F90 \
	 m_flow.F90 m_inpak90.F90 m_ioutil.F90 m_mall.F90 m_mpif.F90 m_mpif90.F90 \
	 m_mpout.F90 m_rankMerge.F90 m_realkinds.F90 m_stdio.F90 m_TraceBack.F90 \
	 m_zeit.F90 get_zeits.c m_MCTWorld.F90 m_AttrVect.F90 m_GlobalMap.F90 \
	 m_GlobalSegMap.F90 m_GlobalSegMapComms.F90 m_Accumulator.F90 \
	 m_SparseMatrix.F90 m_Navigator.F90 m_AttrVectComms.F90 \
	 m_AttrVectReduce.F90 m_AccumulatorComms.F90 m_GeneralGrid.F90 \
	 m_GeneralGridComms.F90 m_SpatialIntegral.F90 m_SpatialIntegralV.F90 \
	 m_MatAttrVectMul.F90 m_Merge.F90 m_GlobalToLocal.F90 m_ExchangeMaps.F90 \
	 m_ConvertMaps.F90 m_SparseMatrixDecomp.F90 m_SparseMatrixToMaps.F90 \
	 m_SparseMatrixComms.F90 m_SparseMatrixPlus.F90 m_Router.F90 \
	 m_Rearranger.F90 m_Transfer.F90 alloc_mod.F90 box_rearrange.F90 \
	 iompi_mod.F90 ionf_mod.F90 mct_rearrange.F90 nf_mod.F90 piodarray.F90 \
	 pio.F90 pio_kinds.F90 piolib_mod.F90 pio_mpi_utils.F90 pionfatt_mod.F90 \
	 pionfget_mod.F90 pionfput_mod.F90 pionfread_mod.F90 pio_nf_utils.F90 \
	 pionfwrite_mod.F90 pio_quicksort.F90 pio_spmd_utils.F90 pio_support.F90 \
	 pio_types.F90 pio_utils.F90 pnetcdfversion.c rearrange.F90 topology.c \
	 dead_data_mod.F90 dead_mct_mod.F90 dead_mod.F90 ESMF_AlarmClockMod.F90 \
	 ESMF_AlarmMod.F90 ESMF_BaseMod.F90 ESMF_BaseTimeMod.F90 \
	 ESMF_CalendarMod.F90 ESMF_ClockMod.F90 ESMF_FractionMod.F90 ESMF_Mod.F90 \
	 ESMF_Stubs.F90 ESMF_TimeIntervalMod.F90 ESMF_TimeMod.F90 f_wrappers.c \
	 GPTLget_memusage.c GPTLprint_memusage.c GPTLutil.c mct_mod.F90 Meat.F90 \
	 perf_mod.F90 perf_utils.F90 seq_cdata_mod.F90 seq_comm_mct.F90 \
	 seq_drydep_mod.F90 seq_flds_indices.F90 seq_flds_mod.F90 \
	 seq_infodata_mod.F90 seq_io_mod.F90 seq_timemgr_mod.F90 shr_cal_mod.F90 \
	 shr_const_mod.F90 shr_dmodel_mod.F90 shr_file_mod.F90 shr_flux_mod.F90 \
	 shr_jlcp.c shr_kind_mod.F90 shr_log_mod.F90 shr_map_mod.F90 \
	 shr_mct_mod.F90 shr_mem_mod.F90 shr_mpi_mod.F90 shr_msg_mod.F90 \
	 shr_ncread_mod.F90 shr_orb_mod.F90 shr_pcdf_mod.F90 shr_scam_mod.F90 \
	 shr_strdata_mod.F90 shr_stream_mod.F90 shr_string_mod.F90 \
	 shr_sys_mod.F90 shr_timer_mod.F90 shr_tInterp_mod.F90 shr_vmath_fwrap.c \
	 shr_vmath_mod.F90 threadutil.c wrf_error_fatal.F90 wrf_message.F90 \
	 atm_comp_mct.F90 datm_comp_mod.F90 datm_shr_mod.F90 dlnd_comp_mod.F90 \
	 lnd_comp_mct.F90 dice_comp_mod.F90 ice_comp_mct.F90 POP_BlocksMod.F90 \
	 POP_BroadcastMod.F90 POP_CommMod.F90 POP_ConfigMod.F90 \
	 POP_ConstantsMod.F90 POP_DistributionMod.F90 POP_DomainSizeMod.F90 \
	 POP_ErrorMod.F90 POP_FieldMod.F90 POP_FinalMod.F90 POP_GridDimMod.F90 \
	 POP_GridHorzMod.F90 POP_GridVertMod.F90 POP_HaloMod.F90 \
	 POP_IOUnitsMod.F90 POP_InitMod.F90 POP_KindsMod.F90 POP_MCT_vars_mod.F90 \
	 POP_RedistributeMod.F90 POP_ReductionsMod.F90 POP_SolversMod.F90 \
	 advection.F90 baroclinic.F90 barotropic.F90 blocks.F90 broadcast.F90 \
	 budget_diagnostics.F90 cfc11_mod.F90 cfc_mod.F90 check_mod.F90 \
	 co2calc.F90 communicate.F90 constants.F90 current_meters.F90 \
	 diag_bsf.F90 diagnostics.F90 diags_on_lat_aux_grid.F90 distribution.F90 \
	 domain.F90 domain_size.F90 drifters.F90 ecosys_mod.F90 ecosys_parms.F90 \
	 exit_mod.F90 forcing.F90 forcing_ap.F90 forcing_coupled.F90 \
	 forcing_fields.F90 forcing_pt_interior.F90 forcing_s_interior.F90 \
	 forcing_sfwf.F90 forcing_shf.F90 forcing_tools.F90 forcing_ws.F90 \
	 gather_scatter.F90 global_reductions.F90 grid.F90 history.F90 \
	 hmix_aniso.F90 hmix_del2.F90 hmix_del4.F90 hmix_gm.F90 \
	 hmix_gm_submeso_share.F90 horizontal_mix.F90 hydro_sections.F90 \
	 iage_mod.F90 ice.F90 initial.F90 io.F90 io_binary.F90 io_ccsm.F90 \
	 io_netcdf.F90 io_pio.F90 io_tools.F90 io_types.F90 kinds_mod.F90 \
	 mix_submeso.F90 movie.F90 ms_balance.F90 msg_mod.F90 named_field_mod.F90 \
	 ocn_communicator.F90 ocn_comp_mct.F90 operators.F90 output.F90 \
	 overflows.F90 passive_tracer_tools.F90 passive_tracers.F90 \
	 pressure_grad.F90 prognostic.F90 qflux_mod.F90 registry.F90 restart.F90 \
	 spacecurve_mod.F90 state_mod.F90 step_mod.F90 surface_hgt.F90 \
	 sw_absorption.F90 tavg.F90 tidal_mixing.F90 time_management.F90 \
	 timers.F90 topostress.F90 tracer_types.F90 vertical_mix.F90 \
	 vmix_const.F90 vmix_kpp.F90 vmix_rich.F90 glc_comp_mct.F90 \
	 ccsm_driver.F90 map_atmatm_mct.F90 map_atmice_mct.F90 map_atmlnd_mct.F90 \
	 map_atmocn_mct.F90 map_glcglc_mct.F90 map_iceice_mct.F90 \
	 map_iceocn_mct.F90 map_lndlnd_mct.F90 map_ocnocn_mct.F90 \
	 map_rofocn_mct.F90 map_rofrof_mct.F90 map_snoglc_mct.F90 \
	 map_snosno_mct.F90 mrg_x2a_mct.F90 mrg_x2g_mct.F90 mrg_x2i_mct.F90 \
	 mrg_x2l_mct.F90 mrg_x2o_mct.F90 mrg_x2s_mct.F90 seq_avdata_mod.F90 \
	 seq_diag_mct.F90 seq_domain_mct.F90 seq_flux_mct.F90 seq_frac_mct.F90 \
	 seq_hist_mod.F90 seq_rearr_mod.F90 seq_rest_mod.F90
EXEBASE=speed_pop2
NEED_MATH=
BENCHLANG=F C

BENCH_CFLAGS     =  -I. -Inetcdf/include -D_MPISERIAL -D_NETCDF -D_USEBOX -DCCSMCOUPLED=1 -DNO_SHR_VMATH -DBLCKX=50 -DBLCKY=4 -DMXBLCKS=58 -DNO_GETTIMEOFDAY  -DSPEC_AUTO_BYTEORDER=0x12345678
BENCH_FPPFLAGS   = -w  -I. -Inetcdf/include -D_MPISERIAL -D_NETCDF -D_USEBOX -DCCSMCOUPLED=1 -DNO_SHR_VMATH -DBLCKX=50 -DBLCKY=4 -DMXBLCKS=58 -DNO_GETTIMEOFDAY  -DSPEC_AUTO_BYTEORDER=0x12345678
CC               = $(SPECLANG)gcc     -std=c99   -m64
CC_VERSION_OPTION = -v
CPORTABILITY     = -DSPEC_CASE_FLAG
CXX              = $(SPECLANG)g++     -std=c++03 -m64
CXX_VERSION_OPTION = -v
EXTRA_OPTIMIZE   = -fopenmp -DSPEC_OPENMP
EXTRA_PORTABILITY = -DSPEC_LP64
FC               = $(SPECLANG)gfortran           -m64
FC_VERSION_OPTION = -v
FPORTABILITY     = -fconvert=big-endian
OPTIMIZE         = -g -O3 -march=native -fno-unsafe-math-optimizations  -fno-tree-loop-vectorize
OS               = unix
SPECLANG         = /usr/bin/
absolutely_no_locking = 0
action           = build
allow_label_override = 0
backup_config    = 1
baseexe          = speed_pop2
basepeak         = 1
benchdir         = benchspec
benchmark        = 628.pop2_s
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
commandexe       = speed_pop2_base.primeiro-teste-m64
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
name             = pop2_s
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
num              = 628
obiwan           = 
os_exe_ext       = 
output_format    = txt,html,cfg,pdf,csv
output_root      = 
outputdir        = output
parallel_test    = 0
parallel_test_submit = 0
parallel_test_workloads = 
path             = /home/kratos/cpu2017/benchspec/CPU/628.pop2_s
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
srcsource        = /home/kratos/cpu2017/benchspec/CPU/628.pop2_s/src
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
OUTPUT_RMFILES   = ocn.log
