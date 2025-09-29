TUNE=base
LABEL=primeiro-teste-m64
NUMBER=502
NAME=gcc_r
SOURCES= main.c cc1-checksum.c alias.c alloca.c alloc-pool.c argv.c \
	 attribs.c auto-inc-dec.c bb-reorder.c bid2dpd_dpd2bid.c bitmap.c \
	 bt-load.c c-lang.c c-errors.c c-lex.c c-pragma.c c-decl.c c-typeck.c \
	 c-convert.c c-aux-info.c c-common.c c-opts.c c-format.c c-semantics.c \
	 c-ppoutput.c c-objc-common.c c-dump.c c-parser.c c-gimplify.c \
	 c-pretty-print.c c-omp.c caller-save.c calls.c cfg.c cfganal.c \
	 cfgbuild.c cfgcleanup.c cfgexpand.c cfghooks.c cfglayout.c cfgloop.c \
	 cfgloopanal.c cfgloopmanip.c cfgrtl.c cgraph.c cgraphbuild.c \
	 cgraphunit.c combine.c combine-stack-adj.c concat.c convert.c coverage.c \
	 cp-demangle.c cp-demint.c cplus-dem.c cpp_directives.c cpp_lex.c \
	 cpp_errors.c cpp_expr.c cpp_charset.c cpp_macro.c cpp_traditional.c \
	 cpp_line-map.c cpp_symtab.c cpp_identifiers.c cpp_mkdeps.c cpp_pch.c \
	 cpp_directives-only.c crc32.c cse.c cselib.c dbxout.c dbgcnt.c dce.c \
	 ddg.c debug.c decContext.c decimal128.c decimal32.c decimal64.c \
	 decNumber.c df-byte-scan.c df-core.c df-problems.c df-scan.c dfp.c \
	 diagnostic.c dojump.c dominance.c domwalk.c double-int.c dse.c \
	 dwarf2asm.c dwarf2out.c dyn-string.c ebitmap.c emit-rtl.c et-forest.c \
	 except.c explow.c expmed.c expr.c fdmatch.c fibheap.c filename_cmp.c \
	 final.c fixed-value.c floatformat.c fold-const.c fopen_unlocked.c \
	 function.c fwprop.c gcse.c genrtl.c getopt1.c getopt.c getpwd.c \
	 getruntime.c ggc-common.c ggc-page.c gimple.c gimple-iterator.c \
	 gimple-low.c gimple-pretty-print.c gimplify.c graph.c graphds.c \
	 graphite.c graphite-blocking.c graphite-clast-to-gimple.c \
	 graphite-dependences.c graphite-interchange.c graphite-poly.c \
	 graphite-ppl.c graphite-scop-detection.c graphite-sese-to-poly.c \
	 gtype-desc.c haifa-sched.c hashtab.c hex.c hooks.c host-ieee128.c \
	 host-ieee32.c host-ieee64.c host-linux.c i386.c i386-c.c ifcvt.c \
	 incpath.c init-regs.c insn-attrtab.c insn-automata.c insn-emit.c \
	 insn-extract.c insn-modes.c insn-opinit.c insn-output.c insn-peep.c \
	 insn-preds.c insn-recog.c integrate.c ipa-cp.c ipa-inline.c ipa-prop.c \
	 ipa-pure-const.c ipa-reference.c ipa-struct-reorg.c ipa-type-escape.c \
	 ipa-utils.c ipa.c ira.c ira-build.c ira-costs.c ira-conflicts.c \
	 ira-color.c ira-emit.c ira-lives.c jump.c lambda-code.c lambda-mat.c \
	 lambda-trans.c langhooks.c lbasename.c lcm.c lists.c loop-doloop.c \
	 loop-init.c loop-invariant.c loop-iv.c loop-unroll.c loop-unswitch.c \
	 lower-subreg.c lrealpath.c lto-cgraph.c lto-streamer-in.c \
	 lto-streamer-out.c lto-section-in.c lto-section-out.c lto-symtab.c \
	 lto-opts.c lto-streamer.c lto-wpa-fixup.c make-relative-prefix.c \
	 make-temp-file.c partition.c matrix-reorg.c mcf.c md5.c mkstemps.c \
	 mode-switching.c modulo-sched.c objalloc.c obstack.c omega.c omp-low.c \
	 optabs.c options.c opts-common.c opts.c params.c passes.c physmem.c \
	 plugin.c pointer-set.c postreload-gcse.c postreload.c predict.c \
	 pretty-print.c print-rtl.c print-tree.c profile.c recog.c reg-stack.c \
	 regcprop.c regex.c reginfo.c regmove.c regrename.c regstat.c reload.c \
	 reload1.c reorg.c resource.c rtl-error.c rtl.c rtlanal.c rtlhooks.c \
	 safe-ctype.c sbitmap.c sched-deps.c sched-ebb.c sched-rgn.c sched-vis.c \
	 sdbout.c sel-sched-ir.c sel-sched-dump.c sel-sched.c sese.c sha1.c \
	 simplify-rtx.c sort.c spaces.c sparseset.c splay-tree.c sreal.c \
	 stack-ptr-mod.c statistics.c stmt.c stor-layout.c store-motion.c \
	 stringpool.c strsignal.c stub-objc.c targhooks.c timevar.c tracer.c \
	 tree-affine.c tree-call-cdce.c tree-cfg.c tree-cfgcleanup.c tree-chrec.c \
	 tree-complex.c tree-data-ref.c tree-dfa.c tree-dump.c tree-eh.c \
	 tree-if-conv.c tree-inline.c tree-into-ssa.c tree-iterator.c \
	 tree-loop-distribution.c tree-loop-linear.c tree-mudflap.c tree-nested.c \
	 tree-nrv.c tree-object-size.c tree-optimize.c tree-outof-ssa.c \
	 tree-parloops.c tree-phinodes.c tree-predcom.c tree-pretty-print.c \
	 tree-profile.c tree-scalar-evolution.c tree-sra.c \
	 tree-switch-conversion.c tree-ssa-address.c tree-ssa-alias.c \
	 tree-ssa-ccp.c tree-ssa-coalesce.c tree-ssa-copy.c tree-ssa-copyrename.c \
	 tree-ssa-dce.c tree-ssa-dom.c tree-ssa-dse.c tree-ssa-forwprop.c \
	 tree-ssa-ifcombine.c tree-ssa-live.c tree-ssa-loop-ch.c \
	 tree-ssa-loop-im.c tree-ssa-loop-ivcanon.c tree-ssa-loop-ivopts.c \
	 tree-ssa-loop-manip.c tree-ssa-loop-niter.c tree-ssa-loop-prefetch.c \
	 tree-ssa-loop-unswitch.c tree-ssa-loop.c tree-ssa-math-opts.c \
	 tree-ssa-operands.c tree-ssa-phiopt.c tree-ssa-phiprop.c tree-ssa-pre.c \
	 tree-ssa-propagate.c tree-ssa-reassoc.c tree-ssa-sccvn.c tree-ssa-sink.c \
	 tree-ssa-structalias.c tree-ssa-ter.c tree-ssa-threadedge.c \
	 tree-ssa-threadupdate.c tree-ssa-uncprop.c tree-ssa.c tree-ssanames.c \
	 tree-stdarg.c tree-tailcall.c tree-vect-generic.c tree-vect-patterns.c \
	 tree-vect-data-refs.c tree-vect-stmts.c tree-vect-loop.c \
	 tree-vect-loop-manip.c tree-vect-slp.c tree-vectorizer.c tree-vrp.c \
	 tree.c unlink-if-ordinary.c value-prof.c var-tracking.c varpool.c \
	 varasm.c varray.c vec.c vmsdbgout.c web.c xatexit.c xcoffout.c xexit.c \
	 xmalloc.c xmemdup.c xstrdup.c xstrerror.c xstrndup.c c-cppbuiltin.c \
	 c-pch.c cpp_files.c cpp_init.c cppdefault.c intl.c prefix.c strerror.c \
	 toplev.c vasprintf.c version.c builtins.c real.c mini-gmp.c \
	 spec_qsort/spec_qsort.c
EXEBASE=cpugcc_r
NEED_MATH=yes
BENCHLANG=C

BENCH_FLAGS      = -I. -I./include -I./spec_qsort -DSPEC_502 -DSPEC_AUTO_SUPPRESS_OPENMP -DIN_GCC -DHAVE_CONFIG_H
CC               = $(SPECLANG)gcc     -std=c99   -m64
CC_VERSION_OPTION = -v
CXX              = $(SPECLANG)g++     -std=c++03 -m64
CXX_VERSION_OPTION = -v
EXTRA_COPTIMIZE  = -fno-strict-aliasing -fgnu89-inline
EXTRA_PORTABILITY = -DSPEC_LP64
FC               = $(SPECLANG)gfortran           -m64
FC_VERSION_OPTION = -v
OPTIMIZE         = -g -O3 -march=native -fno-unsafe-math-optimizations  -fno-tree-loop-vectorize
OS               = unix
SPECLANG         = /usr/bin/
absolutely_no_locking = 0
abstol           = 
action           = build
allow_label_override = 0
backup_config    = 1
baseexe          = cpugcc_r
basepeak         = 1
benchdir         = benchspec
benchmark        = 502.gcc_r
binary           = 
bindir           = exe
builddir         = build
bundleaction     = 
bundlename       = 
calctol          = 0
changedhash      = 0
check_version    = 0
clean_between_builds = no
command_add_redirect = 1
commanderrfile   = speccmds.err
commandexe       = cpugcc_r_base.primeiro-teste-m64
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
logfile          = /home/kratos/cpu2017/tmp/CPU2017.008/templogs/preenv.intrate.008.2
logname          = /home/kratos/cpu2017/tmp/CPU2017.008/templogs/preenv.intrate.008.2
lognum           = 008.2
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
name             = gcc_r
nansupport       = no
need_math        = yes
no_input_handler = close
no_monitor       = 
noratios         = 0
note_preenv      = 1
notes_plat_sysinfo_000 = 
notes_plat_sysinfo_005 =  Sysinfo program /home/kratos/cpu2017/bin/sysinfo
notes_plat_sysinfo_010 =  Rev: r6365 of 2019-08-21 295195f888a3d7edb1e6e46a485a0011
notes_plat_sysinfo_015 =  running on watter Sat Sep 27 22:21:18 2025
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
notes_plat_sysinfo_600 =     /dev/sda3      ext4   78G   31G   44G  41% /
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
num              = 502
obiwan           = 
os_exe_ext       = 
output_format    = txt,html,cfg,pdf,csv
output_root      = 
outputdir        = output
parallel_test    = 0
parallel_test_submit = 0
parallel_test_workloads = 
path             = /home/kratos/cpu2017/benchspec/CPU/502.gcc_r
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
runcpu           = /home/kratos/cpu2017/bin/harness/runcpu --configfile my-first-run.cfg --action build --fake --noreportable --nopower --runmode rate --tune base --size refrate intrate --nopreenv --note-preenv --logfile /home/kratos/cpu2017/tmp/CPU2017.008/templogs/preenv.intrate.008.2 --lognum 008.2 --from_runcpu 2
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
srcsource        = /home/kratos/cpu2017/benchspec/CPU/502.gcc_r/src
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
version          = 1.000503
voltage_range    = 
worklist         = list
OUTPUT_RMFILES   = 200.opts-O3_-finline-limit_50000.s scilab.opts-O3_-finline-limit_50000.s train01.opts-O3_-finline-limit_50000.s
