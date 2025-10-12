TUNE=base
LABEL=primeiro-teste-m64
NUMBER=627
NAME=cam4_s
SOURCES= ESMF_BaseMod.F90 ESMF_BaseTimeMod.F90 ESMF_FractionMod.F90 \
	 ESMF_CalendarMod.F90 ESMF_TimeIntervalMod.F90 ESMF_Stubs.F90 \
	 ESMF_TimeMod.F90 ESMF_AlarmMod.F90 ESMF_ClockMod.F90 \
	 ESMF_AlarmClockMod.F90 ESMF_Mod.F90 cam_logfile.F90 \
	 debugutilitiesmodule.F90 decompmodule.F90 shr_kind_mod.F90 \
	 ghostmodule.F90 perf_utils.F90 shr_log_mod.F90 shr_mpi_mod.F90 \
	 shr_sys_mod.F90 shr_file_mod.F90 string_utils.F90 namelist_utils.F90 \
	 perf_mod.F90 mod_comm.F90 parutilitiesmodule.F90 mpishorthand.F90 \
	 abortutils.F90 units.F90 spmd_utils.F90 fv_control_mod.F90 \
	 pft_module.F90 dynamics_vars.F90 FVperf_module.F90 GPTLget_memusage.c \
	 GPTLprint_memusage.c GPTLutil.c MISR_simulator.F90 Meat.F90 pmgrid.F90 \
	 dycore.F90 pio_kinds.F90 pio_support.F90 pio_types.F90 pio_msg_mod.F90 \
	 alloc_mod.F90 pio_utils.F90 nf_mod.F90 pionfput_mod.F90 pionfatt_mod.F90 \
	 pio_spmd_utils.F90 calcdisplace_mod.F90 box_rearrange.F90 rearrange.F90 \
	 pionfread_mod.F90 iompi_mod.F90 pionfwrite_mod.F90 piodarray.F90 \
	 ionf_mod.F90 calcdecomp.F90 pio_mpi_utils.F90 piolib_mod.F90 \
	 pionfget_mod.F90 pio.F90 shr_timer_mod.F90 shr_string_mod.F90 \
	 shr_const_mod.F90 shr_cal_mod.F90 time_manager.F90 ppgrid.F90 \
	 physconst.F90 constituents.F90 commap.F90 infnan.F90 pspect.F90 \
	 rgrid.F90 spmd_dyn.F90 hycoef.F90 dyn_grid.F90 m_chars.F90 m_flow.F90 \
	 m_stdio.F90 m_mpif.F90 m_realkinds.F90 m_mpif90.F90 m_dropdead.F90 \
	 m_ioutil.F90 m_mpout.F90 m_die.F90 m_MergeSorts.F90 phys_grid.F90 \
	 ioFileMod.F90 cam_history_support.F90 cam_control_mod.F90 m_mall.F90 \
	 m_String.F90 m_rankMerge.F90 m_IndexBin_logical.F90 m_Permuter.F90 \
	 m_IndexBin_char.F90 m_IndexBin_integer.F90 m_SortingTools.F90 m_List.F90 \
	 m_TraceBack.F90 m_AttrVect.F90 m_GlobalMap.F90 m_FcComms.F90 \
	 m_MCTWorld.F90 m_GlobalSegMap.F90 m_AttrVectComms.F90 m_SparseMatrix.F90 \
	 m_SparseMatrixDecomp.F90 m_SparseMatrixComms.F90 m_Navigator.F90 \
	 m_GlobalToLocal.F90 m_SparseMatrixToMaps.F90 m_ConvertMaps.F90 \
	 m_ExchangeMaps.F90 m_Router.F90 m_Rearranger.F90 m_SparseMatrixPlus.F90 \
	 m_GeneralGrid.F90 m_Transfer.F90 m_inpak90.F90 m_GlobalSegMapComms.F90 \
	 m_Accumulator.F90 m_MatAttrVectMul.F90 m_GeneralGridComms.F90 \
	 mct_mod.F90 seq_comm_mct.F90 seq_drydep_mod.F90 seq_flds_mod.F90 \
	 seq_io_mod.F90 cam_pio_utils.F90 sat_hist.F90 solar_data.F90 \
	 shr_orb_mod.F90 shr_tInterp_mod.F90 shr_stream_mod.F90 shr_pcdf_mod.F90 \
	 shr_mct_mod.F90 shr_map_mod.F90 shr_ncread_mod.F90 shr_dmodel_mod.F90 \
	 shr_strdata_mod.F90 shr_scam_mod.F90 wrap_nf.F90 scamMod.F90 \
	 error_messages.F90 interpolate_data.F90 geopotential.F90 ref_pres.F90 \
	 phys_control.F90 physics_types.F90 time_utils.F90 repro_sum_mod.F90 \
	 phys_gmean.F90 mo_constants.F90 m_types.F90 mo_flbc.F90 \
	 chem_surfvals.F90 cam_history_buffers.F90 filenames.F90 cosp_share.F90 \
	 interp_mod.F90 cam_history.F90 advect_tend.F90 phys_buffer.F90 \
	 ghg_data.F90 radconstants.F90 radae.F90 quicksort.F90 radlw.F90 \
	 pkg_cldoptics.F90 phys_debug_util.F90 conv_water.F90 param_cldoptics.F90 \
	 mo_util.F90 rad_solar_var.F90 cmparray_mod.F90 radsw.F90 phys_prop.F90 \
	 rad_constituents.F90 wv_saturation.F90 modal_aer_opt.F90 \
	 aer_rad_props.F90 camsrfexch_types.F90 radiation_data.F90 \
	 cosp_constants.F90 cosp_utils.F90 radar_simulator_types.f90 \
	 cosp_types.F90 modis_simulator.F90 cosp_modis_simulator.F90 \
	 cosp_lidar.F90 cosp_misr_simulator.F90 llnl_stats.F90 lmd_ipsl_stats.F90 \
	 cosp_stats.F90 atmos_lib.f90 mrgrnk.f90 array_lib.f90 format_input.f90 \
	 math_lib.f90 optics_lib.f90 cosp_radar.F90 cosp_isccp_simulator.F90 \
	 cosp_simulator.F90 cosp.F90 cospsimulator_intr.F90 chemistry.F90 \
	 radheat.F90 radiation.F90 horizontal_interpolate.F90 polar_avg.F90 \
	 tracer_data.F90 prescribed_ghg.F90 prescribed_aero.F90 \
	 trb_mtn_stress.F90 phys_debug.F90 hb_diff.F90 upper_bc.F90 \
	 molec_diff.F90 diffusion_solver.F90 eddy_diff.F90 vertical_diffusion.F90 \
	 boundarydata.F90 cam3_ozone_data.F90 aoa_tracers.F90 iondrag.F90 \
	 cam3_aero_data.F90 tracers_suite.F90 tracers.F90 tropopause.F90 \
	 prescribed_volcaero.F90 prescribed_ozone.F90 aircraft_emit.F90 \
	 modal_aero_deposition.F90 aerodep_flx.F90 advnce.F90 drydep_mod.F90 \
	 wetdep.F90 dust_sediment_mod.F90 dust_intr.F90 progseasalts_intr.F90 \
	 scyc.F90 aerosol_intr.F90 history_scam.F90 xpavg_mod.F90 ncdio_atm.F90 \
	 metdata.F90 co2_data_flux.F90 co2_cycle.F90 buffer.F90 comsrf.F90 \
	 restart_physics.F90 pfixer.F90 ctem.F90 diag_module.F90 dyn_comp.F90 \
	 dyn_internal_state.F90 restart_dynamics.F90 cam_restart.F90 \
	 readinitial.F90 history_defaults.F90 error_function.F90 uw_conv.F90 \
	 uwshcu.F90 cldwat.F90 zm_conv.F90 hk_conv.F90 convect_shallow.F90 \
	 cloud_fraction.F90 cldwat2m_macro.F90 ndrop.F90 cldwat2m_micro.F90 \
	 microp_aero.F90 microp_driver.F90 pkg_cld_sediment.F90 stratiform.F90 \
	 inidat.F90 startup_initialconds.F90 inital.F90 check_energy.F90 \
	 dp_coupling.F90 fv_prints.F90 stepon.F90 ionosphere.F90 \
	 cloud_diagnostics.F90 cloud_rad_props.F90 tidal_diag.F90 \
	 constituent_burden.F90 cam_diagnostics.F90 flux_avg.F90 \
	 macrop_driver.F90 gw_drag.F90 zm_conv_intr.F90 convect_deep.F90 \
	 rayleigh_friction.F90 majorsp_diffusion.F90 sslt_rebin.F90 physpkg.F90 \
	 cam_comp.F90 seq_infodata_mod.F90 seq_cdata_mod.F90 runtime_opts.F90 \
	 cam_cpl_indices.F90 seq_timemgr_mod.F90 atm_comp_mct.F90 benergy.F90 \
	 binary_io.F90 bnddyi.F90 seq_flds_indices.F90 seq_diag_mct.F90 \
	 seq_rearr_mod.F90 map_ocnocn_mct.F90 mrg_x2s_mct.F90 ice_comp_mct.F90 \
	 mrg_x2o_mct.F90 seq_avdata_mod.F90 seq_hist_mod.F90 mrg_x2a_mct.F90 \
	 map_iceocn_mct.F90 seq_map_mod.F90 map_atmlnd_mct.F90 map_atmice_mct.F90 \
	 map_snoglc_mct.F90 map_atmocn_mct.F90 seq_domain_mct.F90 \
	 seq_rest_mod.F90 mrg_x2l_mct.F90 seq_frac_mct.F90 shr_flux_mod.F90 \
	 seq_flux_mct.F90 map_lndlnd_mct.F90 map_iceice_mct.F90 \
	 map_glcglc_mct.F90 lnd_comp_mct.F90 ocn_types.F90 ocn_comp.F90 \
	 ocn_comp_mct.F90 map_rofrof_mct.F90 map_atmatm_mct.F90 \
	 map_rofocn_mct.F90 shr_mem_mod.F90 map_snosno_mct.F90 mrg_x2g_mct.F90 \
	 mrg_x2i_mct.F90 glc_comp_mct.F90 ccsm_comp_mod.F90 ccsm_driver.F90 \
	 tp_core.F90 sw_core.F90 cd_core.F90 cldsav.F90 collective.c comm.c \
	 comspe.F90 cpslec.F90 d2a3dijk.F90 d2a3dikj.F90 dadadj.F90 datetime.F90 \
	 diag_dynvar_ic.F90 mean_module.F90 dryairm.F90 dsd.f90 mapz_module.F90 \
	 epvd.F90 esinti.F90 f_wrappers.c fft99.F90 fill_module.F90 fort.F90 \
	 gases.f90 gauaw_mod.F90 geopk.F90 get_zeits.c gffgch.F90 gptl.c \
	 gptl_papi.c group.c handles.c hirsbtpar.f90 hirsbt.f90 icarus.F90 \
	 initcom.F90 initindx.F90 intp_util.F90 iop_surf.F90 lidar_simulator.F90 \
	 list.c load_hydrometeor_classes.f90 m_AccumulatorComms.F90 \
	 m_AttrVectReduce.F90 m_StrTemplate.F90 m_FileResolv.F90 m_Filename.F90 \
	 m_Merge.F90 m_SpatialIntegralV.F90 m_SpatialIntegral.F90 m_zeit.F90 \
	 marsaglia.F90 mcshallow.F90 pio_quicksort.F90 mct_rearrange.F90 \
	 miesubs.F90 mo_msis_ubc.F90 mo_regrider.F90 mo_solar_parms.F90 mpi.c \
	 msise00.F90 p_d_adjust.F90 pack.c par_vecsum.F90 par_xsum.F90 \
	 pf_to_mr.F90 pio_msg_callbacks.F90 pio_msg_getput_callbacks.F90 \
	 pio_nf_utils.F90 pkez.F90 prec_scops.F90 puminterfaces.F90 qneg3.F90 \
	 qneg4.F90 radar_simulator.f90 recv.c redistributemodule.F90 req.c \
	 scops.F90 send.c sgexx.F90 shr_jlcp.c shr_msg_mod.F90 shr_vmath_fwrap.c \
	 shr_vmath_mod.F90 srchutil.F90 srfxfer.F90 sulchem.F90 te_map.F90 \
	 threadutil.c time.c topology.c tphysac.F90 tphysbc.F90 tphysidl.F90 \
	 trac2d.F90 trunc.F90 tsinti.F90 uv3s_update.F90 virtem.F90 vrtmap.F90 \
	 wrap_mpi.F90 wrf_error_fatal.F90 wrf_message.F90 zeff.f90 zenith.F90 \
	 netcdf/attr.c netcdf/dim.c netcdf/error.c netcdf/fort-attio.c \
	 netcdf/fort-control.c netcdf/fort-dim.c netcdf/fort-genatt.c \
	 netcdf/fort-geninq.c netcdf/fort-genvar.c netcdf/fort-lib.c \
	 netcdf/fort-misc.c netcdf/fort-v2compat.c netcdf/fort-var1io.c \
	 netcdf/fort-varaio.c netcdf/fort-vario.c netcdf/fort-varmio.c \
	 netcdf/fort-varsio.c netcdf/libvers.c netcdf/nc.c netcdf/ncx.c \
	 netcdf/posixio.c netcdf/putget.c netcdf/string.c netcdf/v1hpg.c \
	 netcdf/v2i.c netcdf/var.c netcdf/typeSizes.f90 netcdf/netcdf.f90 \
	 spec_qsort/spec_qsort.c
EXEBASE=cam4_s
NEED_MATH=
BENCHLANG=F C

BENCH_CFLAGS     = -DNO_SHR_VMATH -DCO2A -DPERGRO -DPLON=144 -DPLAT=96 -DPLEV=26 -DPCNST=3 -DPCOLS=4 -DPTRM=1 -DPTRN=1 -DPTRK=1 -DSTAGGERED -D_NETCDF -DNO_R16 -I. -Iinclude -Inetcdf/include -DUSE_COSP -DSPEC_AUTO_BYTEORDER=0x12345678
BENCH_FFLAGS     =  -I. -Iinclude -Inetcdf/include
BENCH_FPPFLAGS   = -DNO_SHR_VMATH -DCO2A -DPERGRO -DPLON=144 -DPLAT=96 -DPLEV=26 -DPCNST=3 -DPCOLS=4 -DPTRM=1 -DPTRN=1 -DPTRK=1 -DSTAGGERED -D_NETCDF -DNO_R16 -I. -Iinclude -Inetcdf/include -DUSE_COSP -w -DHIDE_MPI -D_MPISERIAL -DNO_MPI2
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
PORTABILITY      = -DSPEC_CASE_FLAG
SPECLANG         = /usr/bin/
absolutely_no_locking = 0
action           = buildsetup
allow_label_override = 0
backup_config    = 1
baseexe          = cam4_s
basepeak         = 1
benchdir         = benchspec
benchmark        = 627.cam4_s
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
commandexe       = cam4_s_base.primeiro-teste-m64
commandfile      = speccmds.cmd
commandoutfile   = speccmds.out
commandstdoutfile = speccmds.stdout
comparedir       = compare
compareerrfile   = compare.err
comparefile      = compare.cmd
compareoutfile   = compare.out
comparestdoutfile = compare.stdout
compile_error    = 0
compwhite        = 1
configdir        = config
configfile       = default.cfg
configpath       = /home/kratos/specs/2017/config/default.cfg
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
fake             = 0
feedback         = 1
flag_url_base    = https://www.spec.org/auto/cpu2017/Docs/benchmarks/flags/
floatcompare     = 
force_monitor    = 0
from_runcpu      = 2
fw_bios          = virtualbox
hostname         = six-seven
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
hw_ncores        = 5
hw_ncpuorder     = 1-5 chips
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
logfile          = /home/kratos/specs/2017/tmp/CPU2017.002/templogs/preenv.fpspeed.002.1
logname          = /home/kratos/specs/2017/tmp/CPU2017.002/templogs/preenv.fpspeed.002.1
lognum           = 002.1
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
name             = cam4_s
nansupport       = 
need_math        = 
no_input_handler = close
no_monitor       = 
noratios         = 0
note_preenv      = 1
notes_plat_sysinfo_000 = 
notes_plat_sysinfo_005 =  Sysinfo program /home/kratos/specs/2017/bin/sysinfo
notes_plat_sysinfo_010 =  Rev: r6365 of 2019-08-21 295195f888a3d7edb1e6e46a485a0011
notes_plat_sysinfo_015 =  running on six-seven Sat Oct 11 18:48:53 2025
notes_plat_sysinfo_020 = 
notes_plat_sysinfo_025 =  SUT (System Under Test) info as seen by some common utilities.
notes_plat_sysinfo_030 =  For more information on this section, see
notes_plat_sysinfo_035 =     https://www.spec.org/cpu2017/Docs/config.html\#sysinfo
notes_plat_sysinfo_040 = 
notes_plat_sysinfo_045 =  From /proc/cpuinfo
notes_plat_sysinfo_050 =     model name : AMD Ryzen 7 5700X3D 8-Core Processor
notes_plat_sysinfo_055 =        1  "physical id"s (chips)
notes_plat_sysinfo_060 =        5 "processors"
notes_plat_sysinfo_065 =     cores, siblings (Caution: counting these is hw and system dependent. The following
notes_plat_sysinfo_070 =     excerpts from /proc/cpuinfo might not be reliable.  Use with caution.)
notes_plat_sysinfo_075 =        cpu cores : 5
notes_plat_sysinfo_080 =        siblings  : 5
notes_plat_sysinfo_085 =        physical 0: cores 0 1 2 3 4
notes_plat_sysinfo_090 = 
notes_plat_sysinfo_095 =  From lscpu:
notes_plat_sysinfo_100 =       Architecture:                            x86_64
notes_plat_sysinfo_105 =       CPU op-mode(s):                          32-bit, 64-bit
notes_plat_sysinfo_110 =       Address sizes:                           48 bits physical, 48 bits virtual
notes_plat_sysinfo_115 =       Byte Order:                              Little Endian
notes_plat_sysinfo_120 =       CPU(s):                                  5
notes_plat_sysinfo_125 =       On-line CPU(s) list:                     0-4
notes_plat_sysinfo_130 =       Vendor ID:                               AuthenticAMD
notes_plat_sysinfo_135 =       Model name:                              AMD Ryzen 7 5700X3D 8-Core Processor
notes_plat_sysinfo_140 =       CPU family:                              25
notes_plat_sysinfo_145 =       Model:                                   33
notes_plat_sysinfo_150 =       Thread(s) per core:                      1
notes_plat_sysinfo_155 =       Core(s) per socket:                      5
notes_plat_sysinfo_160 =       Socket(s):                               1
notes_plat_sysinfo_165 =       Stepping:                                2
notes_plat_sysinfo_170 =       BogoMIPS:                                5999.99
notes_plat_sysinfo_175 =       Flags:                                   fpu vme de pse tsc msr pae mce cx8 apic sep
notes_plat_sysinfo_180 =       mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt
notes_plat_sysinfo_185 =       rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid tsc_known_freq
notes_plat_sysinfo_190 =       pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c
notes_plat_sysinfo_195 =       rdrand hypervisor lahf_lm cmp_legacy cr8_legacy abm sse4a misalignsse 3dnowprefetch
notes_plat_sysinfo_200 =       vmmcall fsgsbase bmi1 avx2 bmi2 invpcid rdseed adx clflushopt sha_ni arat debug_swap
notes_plat_sysinfo_205 =       Hypervisor vendor:                       KVM
notes_plat_sysinfo_210 =       Virtualization type:                     full
notes_plat_sysinfo_215 =       L1d cache:                               160 KiB (5 instances)
notes_plat_sysinfo_220 =       L1i cache:                               160 KiB (5 instances)
notes_plat_sysinfo_225 =       L2 cache:                                2.5 MiB (5 instances)
notes_plat_sysinfo_230 =       L3 cache:                                480 MiB (5 instances)
notes_plat_sysinfo_235 =       NUMA node(s):                            1
notes_plat_sysinfo_240 =       NUMA node0 CPU(s):                       0-4
notes_plat_sysinfo_245 =       Vulnerability Gather data sampling:      Not affected
notes_plat_sysinfo_250 =       Vulnerability Ghostwrite:                Not affected
notes_plat_sysinfo_255 =       Vulnerability Indirect target selection: Not affected
notes_plat_sysinfo_260 =       Vulnerability Itlb multihit:             Not affected
notes_plat_sysinfo_265 =       Vulnerability L1tf:                      Not affected
notes_plat_sysinfo_270 =       Vulnerability Mds:                       Not affected
notes_plat_sysinfo_275 =       Vulnerability Meltdown:                  Not affected
notes_plat_sysinfo_280 =       Vulnerability Mmio stale data:           Not affected
notes_plat_sysinfo_285 =       Vulnerability Reg file data sampling:    Not affected
notes_plat_sysinfo_290 =       Vulnerability Retbleed:                  Not affected
notes_plat_sysinfo_295 =       Vulnerability Spec rstack overflow:      Vulnerable: Safe RET, no microcode
notes_plat_sysinfo_300 =       Vulnerability Spec store bypass:         Not affected
notes_plat_sysinfo_305 =       Vulnerability Spectre v1:                Mitigation; usercopy/swapgs barriers and
notes_plat_sysinfo_310 =       __user pointer sanitization
notes_plat_sysinfo_315 =       Vulnerability Spectre v2:                Mitigation; Retpolines; STIBP disabled; RSB
notes_plat_sysinfo_320 =       filling; PBRSB-eIBRS Not affected; BHI Not affected
notes_plat_sysinfo_325 =       Vulnerability Srbds:                     Not affected
notes_plat_sysinfo_330 =       Vulnerability Tsx async abort:           Not affected
notes_plat_sysinfo_335 = 
notes_plat_sysinfo_340 =  /proc/cpuinfo cache data
notes_plat_sysinfo_345 =     cache size : 512 KB
notes_plat_sysinfo_350 = 
notes_plat_sysinfo_355 =  From numactl --hardware  WARNING: a numactl 'node' might or might not correspond to a
notes_plat_sysinfo_360 =  physical chip.
notes_plat_sysinfo_365 =    available: 1 nodes (0)
notes_plat_sysinfo_370 =    node 0 cpus: 0 1 2 3 4
notes_plat_sysinfo_375 =    node 0 size: 8593 MB
notes_plat_sysinfo_380 =    node 0 free: 807 MB
notes_plat_sysinfo_385 =    node distances:
notes_plat_sysinfo_390 =    node   0
notes_plat_sysinfo_395 =      0:  10
notes_plat_sysinfo_400 = 
notes_plat_sysinfo_405 =  From /proc/meminfo
notes_plat_sysinfo_410 =     MemTotal:        8799764 kB
notes_plat_sysinfo_415 =     HugePages_Total:       0
notes_plat_sysinfo_420 =     Hugepagesize:       2048 kB
notes_plat_sysinfo_425 = 
notes_plat_sysinfo_430 =  /usr/bin/lsb_release -d
notes_plat_sysinfo_435 =     Ubuntu 24.04.3 LTS
notes_plat_sysinfo_440 = 
notes_plat_sysinfo_445 =  From /etc/*release* /etc/*version*
notes_plat_sysinfo_450 =     debian_version: trixie/sid
notes_plat_sysinfo_455 =     os-release:
notes_plat_sysinfo_460 =        PRETTY_NAME="Ubuntu 24.04.3 LTS"
notes_plat_sysinfo_465 =        NAME="Ubuntu"
notes_plat_sysinfo_470 =        VERSION_ID="24.04"
notes_plat_sysinfo_475 =        VERSION="24.04.3 LTS (Noble Numbat)"
notes_plat_sysinfo_480 =        VERSION_CODENAME=noble
notes_plat_sysinfo_485 =        ID=ubuntu
notes_plat_sysinfo_490 =        ID_LIKE=debian
notes_plat_sysinfo_495 =        HOME_URL="https://www.ubuntu.com/"
notes_plat_sysinfo_500 = 
notes_plat_sysinfo_505 =  uname -a:
notes_plat_sysinfo_510 =     Linux six-seven 6.14.0-33-generic \#33~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Fri Sep 19
notes_plat_sysinfo_515 =     17:02:30 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
notes_plat_sysinfo_520 = 
notes_plat_sysinfo_525 =  Kernel self-reported vulnerability status:
notes_plat_sysinfo_530 = 
notes_plat_sysinfo_535 =  gather_data_sampling:                     Not affected
notes_plat_sysinfo_540 =  ghostwrite:                               Not affected
notes_plat_sysinfo_545 =  indirect_target_selection:                Not affected
notes_plat_sysinfo_550 =  itlb_multihit:                            Not affected
notes_plat_sysinfo_555 =  CVE-2018-3620 (L1 Terminal Fault):        Not affected
notes_plat_sysinfo_560 =  Microarchitectural Data Sampling:         Not affected
notes_plat_sysinfo_565 =  CVE-2017-5754 (Meltdown):                 Not affected
notes_plat_sysinfo_570 =  mmio_stale_data:                          Not affected
notes_plat_sysinfo_575 =  reg_file_data_sampling:                   Not affected
notes_plat_sysinfo_580 =  retbleed:                                 Not affected
notes_plat_sysinfo_585 =  spec_rstack_overflow:                     Vulnerable: Safe RET, no microcode
notes_plat_sysinfo_590 =  CVE-2018-3639 (Speculative Store Bypass): Not affected
notes_plat_sysinfo_595 =  CVE-2017-5753 (Spectre variant 1):        Mitigation: usercopy/swapgs barriers and __user
notes_plat_sysinfo_600 =                                            pointer sanitization
notes_plat_sysinfo_605 =  CVE-2017-5715 (Spectre variant 2):        Mitigation: Retpolines; STIBP: disabled; RSB
notes_plat_sysinfo_610 =                                            filling; PBRSB-eIBRS: Not affected; BHI: Not
notes_plat_sysinfo_615 =                                            affected
notes_plat_sysinfo_620 =  srbds:                                    Not affected
notes_plat_sysinfo_625 =  tsx_async_abort:                          Not affected
notes_plat_sysinfo_630 = 
notes_plat_sysinfo_635 =  run-level 5 Oct 10 16:07
notes_plat_sysinfo_640 = 
notes_plat_sysinfo_645 =  SPEC is set to: /home/kratos/specs/2017
notes_plat_sysinfo_650 =     Filesystem     Type  Size  Used Avail Use% Mounted on
notes_plat_sysinfo_655 =     /dev/sda2      ext4   98G   32G   62G  35% /
notes_plat_sysinfo_660 = 
notes_plat_sysinfo_665 =  From /sys/devices/virtual/dmi/id
notes_plat_sysinfo_670 =      BIOS:    innotek GmbH VirtualBox 12/01/2006
notes_plat_sysinfo_675 =      Vendor:  innotek GmbH
notes_plat_sysinfo_680 =      Product: VirtualBox
notes_plat_sysinfo_685 =      Product Family: Virtual Machine
notes_plat_sysinfo_690 = 
notes_plat_sysinfo_695 =  Cannot run dmidecode; consider saying (as root)
notes_plat_sysinfo_700 =     chmod +s /usr/sbin/dmidecode
notes_plat_sysinfo_705 = 
notes_plat_sysinfo_710 =  (End of data from sysinfo program)
notes_wrap_columns = 0
notes_wrap_indent =   
num              = 627
obiwan           = 
os_exe_ext       = 
output_format    = txt,html,cfg,pdf,csv
output_root      = 
outputdir        = output
parallel_test    = 0
parallel_test_submit = 0
parallel_test_workloads = 
path             = /home/kratos/specs/2017/benchspec/CPU/627.cam4_s
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
rebuild          = 0
reftime          = reftime
reportable       = 0
resultdir        = result
review           = 0
run              = all
runcpu           = /home/kratos/specs/2017/bin/harness/runcpu --action buildsetup --noreportable --nopower --runmode speed --tune base --size refspeed fpspeed --nopreenv --note-preenv --logfile /home/kratos/specs/2017/tmp/CPU2017.002/templogs/preenv.fpspeed.002.1 --lognum 002.1 --from_runcpu 2
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
srcsource        = /home/kratos/specs/2017/benchspec/CPU/527.cam4_r/src
stagger          = 10
strict_rundir_verify = 1
sw_avail         = Ago-2025
sw_base_ptrsize  = 64-bit
sw_compiler001   = C/C++/Fortran: Version 11.4.0 of GCC, the
sw_compiler002   = GNU Compiler Collection
sw_file          = ext4
sw_os001         = Ubuntu 22.04.5 LTS
sw_os002         = 6.14.0-33-generic
sw_other         = None
sw_peak_ptrsize  = Not Applicable
sw_state         = 
sysinfo_hash_bits = 256
sysinfo_program  = specperl /home/kratos/specs/2017/bin/sysinfo
sysinfo_program_hash = sysinfo:SHA:1b187da62efa5d65f0e989c214b6a257d16a31d3cf135973c9043da741052207
table            = 1
teeout           = 0
test_date        = Oct-2025
test_sponsor     = My Test
tester           = My Test
threads          = 4
top              = /home/kratos/specs/2017
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
OUTPUT_RMFILES   = cam4_validate.txt
