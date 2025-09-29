POST=base.sniper-x86_64
FILES=CPU2017/500.perlbench_r/exe/perlbench_r_$(POST) CPU2017/502.gcc_r/exe/gcc_r_$(POST) CPU2017/503.bwaves_r/exe/bwaves_r_$(POST) CPU2017/505.mcf_r/exe/mcf_r_$(POST) CPU2017/507.cactuBSSN_r/exe/cactuBSSN_r_$(POST) CPU2017/508.namd_r/exe/namd_r_$(POST) CPU2017/510.parest_r/exe/parest_r_$(POST) CPU2017/511.povray_r/exe/povray_r_$(POST) CPU2017/519.lbm_r/exe/lbm_r_$(POST) CPU2017/520.omnetpp_r/exe/omnetpp_r_$(POST) CPU2017/521.wrf_r/exe/wrf_r_$(POST) CPU2017/523.xalancbmk_r/exe/xalancbmk_r_$(POST) CPU2017/525.x264_r/exe/x264_r_$(POST) CPU2017/526.blender_r/exe/blender_r_$(POST) CPU2017/527.cam4_r/exe/cam4_r_$(POST) CPU2017/531.deepsjeng_r/exe/deepsjeng_r_$(POST) CPU2017/538.imagick_r/exe/imagick_r_$(POST) CPU2017/541.leela_r/exe/leela_r_$(POST) CPU2017/544.nab_r/exe/nab_r_$(POST) CPU2017/548.exchange2_r/exe/exchange2_r_$(POST) CPU2017/549.fotonik3d_r/exe/fotonik3d_r_$(POST) CPU2017/554.roms_r/exe/roms_r_$(POST) CPU2017/557.xz_r/exe/xz_r_$(POST) CPU2017/600.perlbench_s/exe/perlbench_s_$(POST) CPU2017/602.gcc_s/exe/gcc_s_$(POST) CPU2017/603.bwaves_s/exe/bwaves_s_$(POST) CPU2017/605.mcf_s/exe/mcf_s_$(POST) CPU2017/607.cactuBSSN_s/exe/cactuBSSN_s_$(POST) CPU2017/619.lbm_s/exe/lbm_s_$(POST) CPU2017/620.omnetpp_s/exe/omnetpp_s_$(POST) CPU2017/621.wrf_s/exe/wrf_s_$(POST) CPU2017/623.xalancbmk_s/exe/xalancbmk_s_$(POST) CPU2017/625.x264_s/exe/x264_s_$(POST) CPU2017/627.cam4_s/exe/cam4_s_$(POST) CPU2017/628.pop2_s/exe/pop2_s_$(POST) CPU2017/631.deepsjeng_s/exe/deepsjeng_s_$(POST) CPU2017/638.imagick_s/exe/imagick_s_$(POST) CPU2017/641.leela_s/exe/leela_s_$(POST) CPU2017/644.nab_s/exe/nab_s_$(POST) CPU2017/648.exchange2_s/exe/exchange2_s_$(POST) CPU2017/649.fotonik3d_s/exe/fotonik3d_s_$(POST) CPU2017/654.roms_s/exe/roms_s_$(POST) CPU2017/657.xz_s/exe/xz_s_$(POST) CPU2017/996.specrand_fs/exe/specrand_fs_$(POST) CPU2017/997.specrand_fr/exe/specrand_fr_$(POST) CPU2017/998.specrand_is/exe/specrand_is_$(POST) CPU2017/999.specrand_ir/exe/specrand_ir_$(POST)

include ../tools/hooks/buildconf.makefile

ifeq ($(USE_ICC),1)
  all:
	echo "Makefile.spec hardcoded to gcc but we're in icc mode, SPEC2017 benchmark suite will not be supported"
else
  all: deps compile $(FILES)
endif

include ../tools/scripts/env.makefile
export SPEC:=$(BENCHMARKS_ROOT)/cpu2017
export SPECPERLLIB:=$(SPEC)/bin:$(SPEC)/bin/lib
export PATH:=$(SPEC)/bin:$(PATH)

deps: CPU2017/999.specrand_ir/src/specrand-common/specrand.c
CPU2017/999.specrand_ir/src/specrand-common/specrand.c:
	@echo
	@echo SPEC CPU2017 sources not found. To build the CPU2017 benchmarks for Sniper, first run
	@echo benchmarks$$ ./install_cpu2017 PATH_TO_CPU2017_DVD
	@echo
	@false

compile:
	make -C CPU2017/500.perlbench_r/src
	make -C CPU2017/502.gcc_r/src
	make -C CPU2017/503.bwaves_r/src
	make -C CPU2017/505.mcf_r/src
	make -C CPU2017/507.cactuBSSN_r/src
	make -C CPU2017/508.namd_r/src
	make -C CPU2017/510.parest_r/src
	make -C CPU2017/511.povray_r/src
	make -C CPU2017/519.lbm_r/src
	make -C CPU2017/520.omnetpp_r/src
	make -C CPU2017/521.wrf_r/src
	make -C CPU2017/523.xalancbmk_r/src
	make -C CPU2017/525.x264_r/src
	make -C CPU2017/526.blender_r/src
	make -C CPU2017/527.cam4_r/src
	make -C CPU2017/531.deepsjeng_r/src
	make -C CPU2017/538.imagick_r/src
	make -C CPU2017/541.leela_r/src
	make -C CPU2017/544.nab_r/src
	make -C CPU2017/548.exchange2_r/src
	make -C CPU2017/549.fotonik3d_r/src
	make -C CPU2017/554.roms_r/src
	make -C CPU2017/557.xz_r/src
	make -C CPU2017/600.perlbench_s/src
	make -C CPU2017/602.gcc_s/src
	make -C CPU2017/603.bwaves_s/src
	make -C CPU2017/605.mcf_s/src
	make -C CPU2017/607.cactuBSSN_s/src
	make -C CPU2017/619.lbm_s/src
	make -C CPU2017/620.omnetpp_s/src
	make -C CPU2017/621.wrf_s/src
	make -C CPU2017/623.xalancbmk_s/src
	make -C CPU2017/625.x264_s/src
	make -C CPU2017/627.cam4_s/src
	make -C CPU2017/628.pop2_s/src
	make -C CPU2017/631.deepsjeng_s/src
	make -C CPU2017/638.imagick_s/src
	make -C CPU2017/641.leela_s/src
	make -C CPU2017/644.nab_s/src
	make -C CPU2017/648.exchange2_s/src
	make -C CPU2017/649.fotonik3d_s/src
	make -C CPU2017/654.roms_s/src
	make -C CPU2017/657.xz_s/src

clean:
	make -C CPU2017/500.perlbench_r/src clean
	make -C CPU2017/502.gcc_r/src clean
	make -C CPU2017/503.bwaves_r/src clean
	make -C CPU2017/505.mcf_r/src clean
	make -C CPU2017/507.cactuBSSN_r/src clean
	make -C CPU2017/508.namd_r/src clean
	make -C CPU2017/510.parest_r/src clean
	make -C CPU2017/511.povray_r/src clean
	make -C CPU2017/519.lbm_r/src clean
	make -C CPU2017/520.omnetpp_r/src clean
	make -C CPU2017/521.wrf_r/src clean
	make -C CPU2017/523.xalancbmk_r/src clean
	make -C CPU2017/525.x264_r/src clean
	make -C CPU2017/526.blender_r/src clean
	make -C CPU2017/527.cam4_r/src clean
	make -C CPU2017/531.deepsjeng_r/src clean
	make -C CPU2017/538.imagick_r/src clean
	make -C CPU2017/541.leela_r/src clean
	make -C CPU2017/544.nab_r/src clean
	make -C CPU2017/548.exchange2_r/src clean
	make -C CPU2017/549.fotonik3d_r/src clean
	make -C CPU2017/554.roms_r/src clean
	make -C CPU2017/557.xz_r/src clean
	make -C CPU2017/600.perlbench_s/src clean
	make -C CPU2017/602.gcc_s/src clean
	make -C CPU2017/603.bwaves_s/src clean
	make -C CPU2017/605.mcf_s/src clean
	make -C CPU2017/607.cactuBSSN_s/src clean
	make -C CPU2017/619.lbm_s/src clean
	make -C CPU2017/620.omnetpp_s/src clean
	make -C CPU2017/621.wrf_s/src clean
	make -C CPU2017/623.xalancbmk_s/src clean
	make -C CPU2017/625.x264_s/src clean
	make -C CPU2017/627.cam4_s/src clean
	make -C CPU2017/628.pop2_s/src clean
	make -C CPU2017/631.deepsjeng_s/src clean
	make -C CPU2017/638.imagick_s/src clean
	make -C CPU2017/641.leela_s/src clean
	make -C CPU2017/644.nab_s/src clean
	make -C CPU2017/648.exchange2_s/src clean
	make -C CPU2017/649.fotonik3d_s/src clean
	make -C CPU2017/654.roms_s/src clean
	make -C CPU2017/657.xz_s/src clean
	rm -rf CPU2017/*/exe

%/exe:
	install -d $@


CPU2017/500.perlbench_r/exe/perlbench_r_$(POST): CPU2017/500.perlbench_r/src/perlbench_r CPU2017/500.perlbench_r/exe
	cp $< $@
CPU2017/502.gcc_r/exe/gcc_r_$(POST): CPU2017/502.gcc_r/src/gcc_r CPU2017/502.gcc_r/exe
	cp $< $@
CPU2017/503.bwaves_r/exe/bwaves_r_$(POST): CPU2017/503.bwaves_r/src/bwaves_r CPU2017/503.bwaves_r/exe
	cp $< $@
CPU2017/505.mcf_r/exe/mcf_r_$(POST): CPU2017/505.mcf_r/src/mcf_r CPU2017/505.mcf_r/exe
	cp $< $@
CPU2017/507.cactuBSSN_r/exe/cactuBSSN_r_$(POST): CPU2017/507.cactuBSSN_r/src/cactuBSSN_r CPU2017/507.cactuBSSN_r/exe
	cp $< $@
CPU2017/508.namd_r/exe/namd_r_$(POST): CPU2017/508.namd_r/src/namd_r CPU2017/508.namd_r/exe
	cp $< $@
CPU2017/510.parest_r/exe/parest_r_$(POST): CPU2017/510.parest_r/src/parest_r CPU2017/510.parest_r/exe
	cp $< $@
CPU2017/511.povray_r/exe/povray_r_$(POST): CPU2017/511.povray_r/src/povray_r CPU2017/511.povray_r/exe
	cp $< $@
CPU2017/519.lbm_r/exe/lbm_r_$(POST): CPU2017/519.lbm_r/src/lbm_r CPU2017/519.lbm_r/exe
	cp $< $@
CPU2017/520.omnetpp_r/exe/omnetpp_r_$(POST): CPU2017/520.omnetpp_r/src/omnetpp_r CPU2017/520.omnetpp_r/exe
	cp $< $@
CPU2017/521.wrf_r/exe/wrf_r_$(POST): CPU2017/521.wrf_r/src/wrf_r CPU2017/521.wrf_r/exe
	cp $< $@
CPU2017/523.xalancbmk_r/exe/xalancbmk_r_$(POST): CPU2017/523.xalancbmk_r/src/xalancbmk_r CPU2017/523.xalancbmk_r/exe
	cp $< $@
CPU2017/525.x264_r/exe/x264_r_$(POST): CPU2017/525.x264_r/src/x264_r CPU2017/525.x264_r/exe
	cp $< $@
CPU2017/526.blender_r/exe/blender_r_$(POST): CPU2017/526.blender_r/src/blender_r CPU2017/526.blender_r/exe
	cp $< $@
CPU2017/527.cam4_r/exe/cam4_r_$(POST): CPU2017/527.cam4_r/src/cam4_r CPU2017/527.cam4_r/exe
	cp $< $@
CPU2017/531.deepsjeng_r/exe/deepsjeng_r_$(POST): CPU2017/531.deepsjeng_r/src/deepsjeng_r CPU2017/531.deepsjeng_r/exe
	cp $< $@
CPU2017/538.imagick_r/exe/imagick_r_$(POST): CPU2017/538.imagick_r/src/imagick_r CPU2017/538.imagick_r/exe
	cp $< $@
CPU2017/541.leela_r/exe/leela_r_$(POST): CPU2017/541.leela_r/src/leela_r CPU2017/541.leela_r/exe
	cp $< $@
CPU2017/544.nab_r/exe/nab_r_$(POST): CPU2017/544.nab_r/src/nab_r CPU2017/544.nab_r/exe
	cp $< $@
CPU2017/548.exchange2_r/exe/exchange2_r_$(POST): CPU2017/548.exchange2_r/src/exchange2_r CPU2017/548.exchange2_r/exe
	cp $< $@
CPU2017/549.fotonik3d_r/exe/fotonik3d_r_$(POST): CPU2017/549.fotonik3d_r/src/fotonik3d_r CPU2017/549.fotonik3d_r/exe
	cp $< $@
CPU2017/554.roms_r/exe/roms_r_$(POST): CPU2017/554.roms_r/src/roms_r CPU2017/554.roms_r/exe
	cp $< $@
CPU2017/557.xz_r/exe/xz_r_$(POST): CPU2017/557.xz_r/src/xz_r CPU2017/557.xz_r/exe
	cp $< $@
CPU2017/600.perlbench_s/exe/perlbench_s_$(POST): CPU2017/600.perlbench_s/src/perlbench_s CPU2017/600.perlbench_s/exe
	cp $< $@
CPU2017/602.gcc_s/exe/gcc_s_$(POST): CPU2017/602.gcc_s/src/gcc_s CPU2017/602.gcc_s/exe
	cp $< $@
CPU2017/603.bwaves_s/exe/bwaves_s_$(POST): CPU2017/603.bwaves_s/src/bwaves_s CPU2017/603.bwaves_s/exe
	cp $< $@
CPU2017/605.mcf_s/exe/mcf_s_$(POST): CPU2017/605.mcf_s/src/mcf_s CPU2017/605.mcf_s/exe
	cp $< $@
CPU2017/607.cactuBSSN_s/exe/cactuBSSN_s_$(POST): CPU2017/607.cactuBSSN_s/src/cactuBSSN_s CPU2017/607.cactuBSSN_s/exe
	cp $< $@
CPU2017/619.lbm_s/exe/lbm_s_$(POST): CPU2017/619.lbm_s/src/lbm_s CPU2017/619.lbm_s/exe
	cp $< $@
CPU2017/620.omnetpp_s/exe/omnetpp_s_$(POST): CPU2017/620.omnetpp_s/src/omnetpp_s CPU2017/620.omnetpp_s/exe
	cp $< $@
CPU2017/621.wrf_s/exe/wrf_s_$(POST): CPU2017/621.wrf_s/src/wrf_s CPU2017/621.wrf_s/exe
	cp $< $@
CPU2017/623.xalancbmk_s/exe/xalancbmk_s_$(POST): CPU2017/623.xalancbmk_s/src/xalancbmk_s CPU2017/623.xalancbmk_s/exe
	cp $< $@
CPU2017/625.x264_s/exe/x264_s_$(POST): CPU2017/625.x264_s/src/x264_s CPU2017/625.x264_s/exe
	cp $< $@
CPU2017/627.cam4_s/exe/cam4_s_$(POST): CPU2017/627.cam4_s/src/cam4_s CPU2017/627.cam4_s/exe
	cp $< $@
CPU2017/628.pop2_s/exe/pop2_s_$(POST): CPU2017/628.pop2_s/src/pop2_s CPU2017/628.pop2_s/exe
	cp $< $@
CPU2017/631.deepsjeng_s/exe/deepsjeng_s_$(POST): CPU2017/631.deepsjeng_s/src/deepsjeng_s CPU2017/631.deepsjeng_s/exe
	cp $< $@
CPU2017/638.imagick_s/exe/imagick_s_$(POST): CPU2017/638.imagick_s/src/imagick_s CPU2017/638.imagick_s/exe
	cp $< $@
CPU2017/641.leela_s/exe/leela_s_$(POST): CPU2017/641.leela_s/src/leela_s CPU2017/641.leela_s/exe
	cp $< $@
CPU2017/644.nab_s/exe/nab_s_$(POST): CPU2017/644.nab_s/src/nab_s CPU2017/644.nab_s/exe
	cp $< $@
CPU2017/648.exchange2_s/exe/exchange2_s_$(POST): CPU2017/648.exchange2_s/src/exchange2_s CPU2017/648.exchange2_s/exe
	cp $< $@
CPU2017/649.fotonik3d_s/exe/fotonik3d_s_$(POST): CPU2017/649.fotonik3d_s/src/fotonik3d_s CPU2017/649.fotonik3d_s/exe
	cp $< $@
CPU2017/654.roms_s/exe/roms_s_$(POST): CPU2017/654.roms_s/src/roms_s CPU2017/654.roms_s/exe
	cp $< $@
CPU2017/657.xz_s/exe/xz_s_$(POST): CPU2017/657.xz_s/src/xz_s CPU2017/657.xz_s/exe
	cp $< $@
CPU2017/996.specrand_fs/exe/specrand_fs_$(POST): CPU2017/996.specrand_fs/src/specrand_fs CPU2017/996.specrand_fs/exe
	cp $< $@
CPU2017/997.specrand_fr/exe/specrand_fr_$(POST): CPU2017/997.specrand_fr/src/specrand_fr CPU2017/997.specrand_fr/exe
	cp $< $@
CPU2017/998.specrand_is/exe/specrand_is_$(POST): CPU2017/998.specrand_is/src/specrand_is CPU2017/998.specrand_is/exe
	cp $< $@
CPU2017/999.specrand_ir/exe/specrand_ir_$(POST): CPU2017/999.specrand_ir/src/specrand_ir CPU2017/999.specrand_ir/exe
	cp $< $@
