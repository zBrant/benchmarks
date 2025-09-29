TUNE=base
LABEL=primeiro-teste-m64
NUMBER=510
NAME=parest_r
SOURCES= source/base/auto_derivative_function.cc \
	 source/base/boost_threads.cc source/base/conditional_ostream.cc \
	 source/base/config.cc source/base/convergence_table.cc \
	 source/base/data_out_base.cc source/base/exceptions.cc \
	 source/base/flow_function.cc source/base/function.cc \
	 source/base/function_derivative.cc source/base/function_lib.cc \
	 source/base/function_lib_cutoff.cc source/base/function_parser.cc \
	 source/base/function_time.cc source/base/geometry_info.cc \
	 source/base/job_identifier.cc source/base/log.cc \
	 source/base/memory_consumption.cc source/base/multithread_info.cc \
	 source/base/parameter_handler.cc source/base/parsed_function.cc \
	 source/base/path_search.cc source/base/polynomial.cc \
	 source/base/polynomial_space.cc source/base/polynomials_abf.cc \
	 source/base/polynomials_bdm.cc source/base/polynomials_p.cc \
	 source/base/polynomials_raviart_thomas.cc source/base/quadrature.cc \
	 source/base/quadrature_lib.cc source/base/quadrature_selector.cc \
	 source/base/subscriptor.cc source/base/symmetric_tensor.cc \
	 source/base/table_handler.cc source/base/tensor.cc \
	 source/base/tensor_function.cc source/base/tensor_product_polynomials.cc \
	 source/base/thread_management.cc source/base/timer.cc \
	 source/base/utilities.cc source/dofs/dof_accessor.cc \
	 source/dofs/dof_faces.cc source/dofs/dof_handler.cc \
	 source/dofs/dof_levels.all_dimensions.cc \
	 source/dofs/dof_objects.all_dimensions.cc source/dofs/dof_objects.cc \
	 source/dofs/dof_renumbering.cc source/dofs/dof_tools.cc source/fe/fe.cc \
	 source/fe/fe_abf.cc source/fe/fe_data.cc source/fe/fe_dgp.cc \
	 source/fe/fe_dgp_monomial.cc source/fe/fe_dgp_nonparametric.cc \
	 source/fe/fe_dgq.cc source/fe/fe_nedelec.cc source/fe/fe_nedelec_1d.cc \
	 source/fe/fe_nedelec_2d.cc source/fe/fe_nedelec_3d.cc \
	 source/fe/fe_poly.cc source/fe/fe_poly_tensor.cc source/fe/fe_q.cc \
	 source/fe/fe_q_hierarchical.cc source/fe/fe_raviart_thomas.cc \
	 source/fe/fe_raviart_thomas_nodal.cc source/fe/fe_system.cc \
	 source/fe/fe_tools.all_dimensions.cc source/fe/fe_tools.cc \
	 source/fe/fe_values.cc source/fe/mapping.cc source/fe/mapping_c1.cc \
	 source/fe/mapping_cartesian.cc source/fe/mapping_q.cc \
	 source/fe/mapping_q1.cc source/fe/mapping_q1_eulerian.cc \
	 source/fe/mapping_q_eulerian.cc source/grid/grid_generator.cc \
	 source/grid/grid_in.cc source/grid/grid_out.all_dimensions.cc \
	 source/grid/grid_out.cc source/grid/grid_refinement.cc \
	 source/grid/grid_reordering.cc source/grid/grid_tools.cc \
	 source/grid/intergrid_map.cc source/grid/persistent_tria.cc \
	 source/grid/tria.all_dimensions.cc source/grid/tria.cc \
	 source/grid/tria_accessor.cc source/grid/tria_boundary.cc \
	 source/grid/tria_boundary_lib.cc source/grid/tria_faces.cc \
	 source/grid/tria_levels.cc source/grid/tria_objects.all_dimensions.cc \
	 source/grid/tria_objects.cc source/hp/dof_faces.cc \
	 source/hp/dof_handler.cc source/hp/dof_levels.all_dimensions.cc \
	 source/hp/dof_levels.cc source/hp/dof_objects.all_dimensions.cc \
	 source/hp/fe_collection.cc source/hp/fe_values.cc \
	 source/hp/mapping_collection.cc source/lac/block_matrix_array.cc \
	 source/lac/block_sparse_matrix.cc source/lac/block_sparse_matrix_ez.cc \
	 source/lac/block_sparsity_pattern.cc source/lac/block_vector.cc \
	 source/lac/chunk_sparse_matrix.cc source/lac/chunk_sparsity_pattern.cc \
	 source/lac/compressed_set_sparsity_pattern.cc \
	 source/lac/compressed_simple_sparsity_pattern.cc \
	 source/lac/compressed_sparsity_pattern.cc \
	 source/lac/constraint_matrix.cc source/lac/full_matrix.cc \
	 source/lac/lapack_full_matrix.cc source/lac/matrix_lib.cc \
	 source/lac/matrix_out.cc source/lac/petsc_block_sparse_matrix.cc \
	 source/lac/petsc_full_matrix.cc source/lac/petsc_matrix_base.cc \
	 source/lac/petsc_parallel_block_sparse_matrix.cc \
	 source/lac/petsc_parallel_block_vector.cc \
	 source/lac/petsc_parallel_sparse_matrix.cc \
	 source/lac/petsc_parallel_vector.cc source/lac/petsc_precondition.cc \
	 source/lac/petsc_solver.cc source/lac/petsc_sparse_matrix.cc \
	 source/lac/petsc_vector.cc source/lac/petsc_vector_base.cc \
	 source/lac/precondition_block.cc source/lac/precondition_block_ez.cc \
	 source/lac/solver.cc source/lac/solver_control.cc \
	 source/lac/sparse_decomposition.cc source/lac/sparse_direct.cc \
	 source/lac/sparse_ilu.cc source/lac/sparse_matrix.cc \
	 source/lac/sparse_matrix_ez.cc source/lac/sparse_mic.cc \
	 source/lac/sparse_vanka.cc source/lac/sparsity_pattern.cc \
	 source/lac/sparsity_tools.cc source/lac/swappable_vector.cc \
	 source/lac/tridiagonal_matrix.cc \
	 source/lac/trilinos_block_sparse_matrix.cc \
	 source/lac/trilinos_block_vector.cc source/lac/trilinos_precondition.cc* \
	 source/lac/trilinos_precondition_block.cc* source/lac/trilinos_solver.cc \
	 source/lac/trilinos_solver_block.cc \
	 source/lac/trilinos_sparse_matrix.cc* \
	 source/lac/trilinos_sparsity_pattern.cc* source/lac/trilinos_vector.cc* \
	 source/lac/trilinos_vector_base.cc source/lac/vector.cc \
	 source/lac/vector_memory.cc source/lac/vector_view.cc \
	 source/libparest/global_parameters.cc \
	 source/libparest/graphical_display.cc source/libparest/grid_transfer.cc \
	 source/libparest/message_log.cc source/libparest/statistics.cc \
	 source/libparest/top_level.cc source/libparest/utilities.cc \
	 source/me-tomography/boundary_sources_phantom.cc \
	 source/me-tomography/boundary_sources_planarz8.cc \
	 source/me-tomography/coefficient.cc source/me-tomography/evaluations.cc \
	 source/me-tomography/experiment_description.cc \
	 source/me-tomography/factories.cc source/me-tomography/forward.cc \
	 source/me-tomography/forward_solver_evaluators.cc \
	 source/me-tomography/forward_solver_parameters.cc \
	 source/me-tomography/geometry.cc source/me-tomography/me_parameters.cc \
	 source/me-tomography/me_slave.cc source/me-tomography/me_tomography.cc \
	 source/me-tomography/measurement_weights.cc \
	 source/me-tomography/measurements.cc \
	 source/me-tomography/problem_description.cc \
	 source/me-tomography/solver.cc \
	 source/me-tomography/state_discretization.cc \
	 source/me-tomography/synthetic_data.cc source/me-tomography/targets.cc \
	 source/multigrid/mg_base.cc source/multigrid/mg_dof_accessor.cc \
	 source/multigrid/mg_dof_handler.cc source/multigrid/mg_dof_tools.cc \
	 source/multigrid/mg_smoother.cc \
	 source/multigrid/mg_tools.all_dimensions.cc \
	 source/multigrid/mg_transfer_block.cc \
	 source/multigrid/mg_transfer_component.cc \
	 source/multigrid/mg_transfer_prebuilt.cc \
	 source/multigrid/multigrid.all_dimensions.cc source/numerics/data_out.cc \
	 source/numerics/data_out_faces.cc source/numerics/data_out_rotation.cc \
	 source/numerics/data_out_stack.cc source/numerics/data_postprocessor.cc \
	 source/numerics/derivative_approximation.cc \
	 source/numerics/error_estimator.cc source/numerics/fe_field_function.cc \
	 source/numerics/histogram.cc source/numerics/matrices.all_dimensions.cc \
	 source/numerics/matrices.cc source/numerics/solution_transfer.cc \
	 source/numerics/time_dependent.cc \
	 source/numerics/vectors.all_dimensions.cc source/numerics/vectors.cc \
	 source/libparest/master/master.cc \
	 source/libparest/master/newton_method.cc \
	 source/libparest/master/step_length_control.cc \
	 source/libparest/parallel/control.cc \
	 source/libparest/parallel/message_log.cc \
	 source/libparest/parallel/multiple_experiments.cc \
	 source/libparest/parallel/tools.cc source/libparest/parameter/base.cc \
	 source/libparest/parameter/bounds.cc \
	 source/libparest/parameter/factory.cc \
	 source/libparest/parameter/field.cc \
	 source/libparest/parameter/field_discretization.cc \
	 source/libparest/parameter/regularization.cc \
	 source/libparest/slave/factory.cc source/libparest/slave/slave.cc \
	 source/libparest/slave/stationary/boundary_values.cc \
	 source/libparest/slave/stationary/evaluations.cc \
	 source/libparest/slave/stationary/global_matrix.cc \
	 source/libparest/slave/stationary/grid_refinement.cc \
	 source/libparest/slave/stationary/measurements.cc \
	 source/libparest/slave/stationary/problem_description.cc \
	 source/libparest/slave/stationary/slave.cc \
	 source/libparest/slave/stationary/state_discretization.cc \
	 source/libparest/slave/stationary/synthetic_data.cc
EXEBASE=parest_r
NEED_MATH=
BENCHLANG=CXX

BENCH_FLAGS      = -Iinclude -I. -DSPEC_AUTO_SUPPRESS_OPENMP
CC               = $(SPECLANG)gcc     -std=c99   -m64
CC_VERSION_OPTION = -v
CXX              = $(SPECLANG)g++     -std=c++03 -m64
CXX_VERSION_OPTION = -v
EXTRA_PORTABILITY = -DSPEC_LP64
FC               = $(SPECLANG)gfortran           -m64
FC_VERSION_OPTION = -v
OPTIMIZE         = -g -O3 -march=native -fno-unsafe-math-optimizations  -fno-tree-loop-vectorize
OS               = unix
SPECLANG         = /usr/bin/
absolutely_no_locking = 0
action           = build
allow_label_override = 0
backup_config    = 1
baseexe          = parest_r
basepeak         = 1
benchdir         = benchspec
benchmark        = 510.parest_r
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
commandexe       = parest_r_base.primeiro-teste-m64
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
floatcompare     = 1
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
logfile          = /home/kratos/cpu2017/tmp/CPU2017.008/templogs/preenv.fprate.008.0
logname          = /home/kratos/cpu2017/tmp/CPU2017.008/templogs/preenv.fprate.008.0
lognum           = 008.0
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
name             = parest_r
nansupport       = 
need_math        = 
no_input_handler = close
no_monitor       = 
noratios         = 0
note_preenv      = 1
notes_plat_sysinfo_000 = 
notes_plat_sysinfo_005 =  Sysinfo program /home/kratos/cpu2017/bin/sysinfo
notes_plat_sysinfo_010 =  Rev: r6365 of 2019-08-21 295195f888a3d7edb1e6e46a485a0011
notes_plat_sysinfo_015 =  running on watter Sat Sep 27 22:20:32 2025
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
notes_plat_sysinfo_600 =     /dev/sda3      ext4   78G   30G   45G  41% /
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
num              = 510
obiwan           = 
os_exe_ext       = 
output_format    = txt,html,cfg,pdf,csv
output_root      = 
outputdir        = output
parallel_test    = 0
parallel_test_submit = 0
parallel_test_workloads = 
path             = /home/kratos/cpu2017/benchspec/CPU/510.parest_r
plain_train      = 1
platform         = 
power            = 0
preENV_LD_LIBRARY_PATH = %{gcc_dir}/lib64/:%{gcc_dir}/lib/:/lib64
preenv           = 0
prefix           = 
prepared_by      = Watta
ranks            = 1
rawhash_bits     = 256
rebuild          = 1
reftime          = reftime
reltol           = 
reportable       = 0
resultdir        = result
review           = 0
run              = all
runcpu           = /home/kratos/cpu2017/bin/harness/runcpu --configfile my-first-run.cfg --action build --fake --noreportable --nopower --runmode rate --tune base --size refrate fprate --nopreenv --note-preenv --logfile /home/kratos/cpu2017/tmp/CPU2017.008/templogs/preenv.fprate.008.0 --lognum 008.0 --from_runcpu 2
rundir           = run
runmode          = rate
safe_eval        = 1
save_build_files = 
section_specifier_fatal = 1
setprocgroup     = 1
setup_error      = 0
sigint           = 2
size             = refrate
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
srcsource        = /home/kratos/cpu2017/benchspec/CPU/510.parest_r/src
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
threads          = 1
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
version          = 1.000901
voltage_range    = 
worklist         = list
OUTPUT_RMFILES   = 001-m0.vtk 002-m0.vtk log me.prm statistics
