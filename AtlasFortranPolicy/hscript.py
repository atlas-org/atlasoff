## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "AtlasFortranPolicy",
    "authors": ["Christian Arnault <arnault@lal.in2p3.fr>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-*", public=True)
    ctx.use_pkg("External/AtlasCompilers", version="AtlasCompilers-*", public=True)
    ctx.use_pkg("GaudiPolicy", version="v*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):

    macro = ctx.hwaf_declare_macro
    tag =   ctx.hwaf_declare_tag
    
    ## FIXME:
    tag("NO_GFO", content=[])
    
    #### tag &{gcc34 [useG77]}
    tag(
        "gcc34",
        content=["useG77"]
    )
    #### macro &{{for [{default [gfortran]} {gcc41 [gfortran]} {gcc43 [gfortran]} {gcc45 [gfortran]} {gcc46 [gfortran]} {gcc47 [gfortran]} {gcc48 [gfortran]} {target-clang3 [gfortran]} {Darwin [gfortran]} {useG77 [g77]}]}}
    macro("for", (
      {"default": "gfortran"},
      {"gcc41": "gfortran"},
      {"gcc43": "gfortran"},
      {"gcc45": "gfortran"},
      {"gcc46": "gfortran"},
      {"gcc47": "gfortran"},
      {"gcc48": "gfortran"},
      {"target-clang3": "gfortran"},
      {"Darwin": "gfortran"},
      {"useG77": "g77"},
    ), override=True)
    

    ctx.hwaf_macro_append("FCFLAGS", (
      {"default": ""},
      {("x86_64", "gcc", "32"): "-m32"},
    ))

    ctx.hwaf_macro_append("shlibbuilder", (
      {"default": ""},
      {("x86_64", "gcc", "32"): "-m32"},
    ))

    macro("GFORTRAN_UNBUFFERED_ALL", "y")
    ctx.hwaf_declare_runtime_env("GFORTRAN_UNBUFFERED_ALL")
    
    ctx.hwaf_macro_remove("FCFLAGS", (
      {"default": ""},
      {"Linux": "-O2"},
    ))

    ctx.hwaf_macro_remove("FCFLAGS", (
      {"default": ""},
      {"Linux": "-fdollar-ok"},
    ))

    ctx.hwaf_macro_remove("FCFLAGS", (
      {"default": ""},
      {"Linux": "-ff90"},
    ))

    ctx.hwaf_macro_remove("FCFLAGS", (
      {"default": ""},
      {"Linux": "-w"},
    ))

    macro("cpp_fortran_macro", (
      {"default": ""},
      {"32": "-DFVOIDP=INTEGER*4"},
      {"64": "-DFVOIDP=INTEGER*8"},
    ))

    ctx.hwaf_macro_append("FCFLAGS", (
      {"default": ""},
      {"Linux": ["-pipe", "-fno-automatic", "-fno-second-underscore", "-ffixed-line-length-132", "-Wall", "-W", "-Wno-unused", "-Wsurprising", "-fPIC", "${cpp_fortran_macro}"]},
      {"Darwin": ["-ffixed-line-length-132", "-Wall", "-W", "-Wsurprising", "-Wno-unused", "-fPIC", "${cpp_fortran_macro}"]},
    ))

    ctx.hwaf_macro_append("FCFLAGS", (
      {"default": ""},
      {("gcc", "dbg"): "-fbounds-check"},
    ))

    ctx.hwaf_macro_append("FCFLAGS", (
      {"default": ""},
      {"noWerror": ""},
      {"applyWerror": "-Werror"},
    ))

    ## FIXME
    macro("fortran_linkopts_prefix", (
      {"default": ""},
      {"notAsNeeded": ""},
      {"asNeeded": ["-Wl,--no-as-needed"]},
    ))

    ## FIXME
    macro("fortran_linkopts_postfix", (
      {"default": ""},
      {"notAsNeeded": ""},
      {"asNeeded": ["-Wl,--as-needed"]},
    ))

    macro("FCLINKFLAGS", (
      {"default": "-fPIC"},
      {"Darwin": ""},
      {"useG77": ["${fortran_linkopts_prefix}", "g2c", "${fortran_linkopts_postfix}", "nsl", "crypt", "dl"]},
    ), override=True)

    ## FIXME
    ctx.hwaf_macro_append("componentshr_linkopts", (
      {"default": ""},
      {"Linux": ["-Wl,--hash-style=both"]},
    ))

    ## FIXME
    ctx.hwaf_macro_append("libraryshr_linkopts", (
      {"default": ""},
      {"Linux": ["-Wl,--hash-style=both"]},
    ))

    ## FIXME
    ctx.hwaf_macro_append("application_linkopts", (
      {"default": ""},
      {"Linux": ["-Wl,--hash-style=both"]},
    ))

    tag("HAS_PGI32", content=["HAS_PGI"])
    tag("HAS_PGI41", content=["HAS_PGI"])
    tag("HAS_PGI51", content=["HAS_PGI"])
    tag("HAS_PGI52", content=["HAS_PGI"])
    tag("HAS_PGI",   content=["HAS_PGI_RUNTIME", "HAS_FORTRAN_RUNTIME", "HAS_FORTRAN"])
    tag("HAS_G95",   content=["HAS_FORTRAN",     "HAS_G95_RUNTIME"])
    tag("HAS_GFO",   content=["HAS_FORTRAN",     "HAS_GFO_RUNTIME"])

    tag("HAS_PGI_RUNTIME", content=["HAS_FORTRAN_RUNTIME"])
    tag("HAS_G95_RUNTIME", content=["HAS_FORTRAN_RUNTIME"])
    tag("HAS_GFO_RUNTIME", content=["HAS_FORTRAN_RUNTIME"])

    macro("SLES9_HAS_GFO", (
      {"default": "NO_GFO"},
      {"SLES9": "NO_GFO"},
      {"CERN": "HAS_GFO"},
      {"BNL": "HAS_GFO"},
      {"LBNL": "HAS_PGI32"},
      {"STANDALONE": "HAS_GFO"},
    ))
    ctx.hwaf_apply_tag("${SLES9_HAS_GFO}")

    macro("f90_native_version", (
      {"default": ""},
      {"HAS_PGI32": "32"},
      {"HAS_PGI41": "41"},
      {"HAS_PGI51": "51"},
    ))
    macro("PGI", (
      {"default": ""},
      {"CERN": "/afs/cern.ch/sw/fortran/pgi/pgi${f90_native_version}"},
      {"BNL": "/usr/pgi"},
      {"LBNL": "/usr/local/pkg/pgi${f90_native_version}"},
    ))

    macro("G95", (
      {"default": ""},
      {"CERN": "/afs/cern.ch/sw/fortran/g95-install"},
    ))

    macro("AtlasFortranPolicy_native_version", (
      {"default": ""},
      {"HAS_GFO": "gcc-v-4.2.0-20060924"},
    ))

    macro("gfo_base_cmd", (
      {"default": "${ATLASFORTRANPOLICYROOT}/cmt/setup_gfo_base.sh"},
    ))

    macro("GFO_BASE", (
      {"default": "${ATLAS_EXTERNAL}/fortran/${AtlasFortranPolicy_native_version}/gfortran32"},
      {("slc4", "gcc-3.2.3"): "${ATLAS_EXTERNAL}/fortran/${AtlasFortranPolicy_native_version}/gfortran32"},
      {"gcc43": "${gfo_base_cmd}"},
      {"gcc45": "${gfo_base_cmd}"},
      {"gcc46": "${gfo_base_cmd}"},
      {"gcc47": "${gfo_base_cmd}"},
      {"gcc48": "${gfo_base_cmd}"},
      {"target-clang3": "${gfo_base_cmd}"},
      {"slc4": "/usr"},
      {"slc5": "/usr"},
      {"slc6": "/usr"},
      {"Darwin": "/usr"},
      {("x86_64", "gcc"): "${ATLAS_EXTERNAL}/fortran/${AtlasFortranPolicy_native_version}/gfortran64"},
    ))
    #### macro &{{GFO_LIBS [{default [lib]} {slc4&64 [lib64]} {slc5&64 [lib64]} {slc6&64 [lib64]}]}}
    macro("GFO_LIBS", (
      {"default": "lib"},
      {("slc4", "64"): "lib64"},
      {("slc5", "64"): "lib64"},
      {("slc6", "64"): "lib64"},
    ))
    #### macro &{{GFO [{default []} {slc4&gcc-3.2.3 [${GFO_BASE}/irun]} {slc4 [${GFO_BASE}]} {slc5 [${GFO_BASE}]} {slc6 [${GFO_BASE}]} {slc7 [${GFO_BASE}]} {target-clang3 [${GFO_BASE}]} {Darwin [${GFO_BASE}/local/gfortran]} {CERN [${GFO_BASE}/irun]} {BNL [${GFO_BASE}/irun]} {STANDALONE [${GFO_BASE}/irun]}]}}
    macro("GFO", (
      {"default": ""},
      {("slc4", "gcc-3.2.3"): "${GFO_BASE}/irun"},
      {"slc4": "${GFO_BASE}"},
      {"slc5": "${GFO_BASE}"},
      {"slc6": "${GFO_BASE}"},
      {"slc7": "${GFO_BASE}"},
      {"target-clang3": "${GFO_BASE}"},
      {"Darwin": "${GFO_BASE}/local/gfortran"},
      {"CERN": "${GFO_BASE}/irun"},
      {"BNL": "${GFO_BASE}/irun"},
      {"STANDALONE": "${GFO_BASE}/irun"},
    ))
    #### macro &{{gfo_asNeeded_linkopt [{default []} {Darwin []} {notAsNeeded []} {asNeeded [-Wl,--as-needed]}]}}
    macro("gfo_asNeeded_linkopt", (
      {"default": ""},
      {"Darwin": ""},
      {"notAsNeeded": ""},
      {"asNeeded": ["-Wl,--as-needed"]},
    ))
    #### macro &{{gfo_notAsNeeded_linkopt [{default []} {Darwin []} {notAsNeeded []} {asNeeded [-Wl,--no-as-needed]}]}}
    macro("gfo_notAsNeeded_linkopt", (
      {"default": ""},
      {"Darwin": ""},
      {"notAsNeeded": ""},
      {"asNeeded": ["-Wl,--no-as-needed"]},
    ))
    #### macro &{{FORTRAN_libset [{default []} {HAS_PGI32 [${PGI}/linux86/lib/event_init.o ${PGI}/linux86/lib/libpgf90.a ${PGI}/linux86/lib/libpgf90_rpm1.a ${PGI}/linux86/lib/libpgf902.a ${PGI}/linux86/lib/libpgf90rtl.a ${PGI}/linux86/lib/libpgftnrtl.a ${PGI}/linux86/lib/libpgc.a]} {HAS_PGI41 [${PGI}/linux86/lib/libpgf90.a ${PGI}/linux86/lib/libpgf90_rpm1.a ${PGI}/linux86/lib/libpgf902.a ${PGI}/linux86/lib/libpgf90rtl.a ${PGI}/linux86/lib/libpgftnrtl.a ${PGI}/linux86/lib/libpgc.a]} {HAS_PGI51 [${PGI}/linux86/lib/libpgf90.a ${PGI}/linux86/lib/libpgf90_rpm1.a ${PGI}/linux86/lib/libpgf902.a ${PGI}/linux86/lib/libpgf90rtl.a ${PGI}/linux86/lib/libpgftnrtl.a ${PGI}/linux86/lib/libpgc.a]} {HAS_PGI52 [${PGI}/lib/libpgf90.a ${PGI}/lib/libpgf90_rpm1.a ${PGI}/lib/libpgf902.a ${PGI}/lib/libpgf90rtl.a ${PGI}/lib/libpgftnrtl.a ${PGI}/lib/libnspgc.a ${PGI}/lib/libpgc.a]} {HAS_GFO&gcc43 [${gfo_notAsNeeded_linkopt} ${GFO}/${GFO_LIBS}/libgfortran.so ${gfo_asNeeded_linkopt}]} {HAS_GFO&gcc45 [${gfo_notAsNeeded_linkopt} ${GFO}/${GFO_LIBS}/libgfortran.so ${gfo_asNeeded_linkopt}]} {HAS_GFO&gcc46 [${gfo_notAsNeeded_linkopt} `${for} -print-file-name=libgfortran.so` ${gfo_asNeeded_linkopt}]} {HAS_GFO&gcc47 [${gfo_notAsNeeded_linkopt} `${for} -print-file-name=libgfortran.so` ${gfo_asNeeded_linkopt}]} {HAS_GFO&gcc48 [${gfo_notAsNeeded_linkopt} `${for} -print-file-name=libgfortran.so` ${gfo_asNeeded_linkopt}]} {HAS_GFO&target-clang3 [${gfo_notAsNeeded_linkopt} `${for} -print-file-name=libgfortran.so` ${gfo_asNeeded_linkopt}]} {HAS_GFO&slc4 [${GFO}/${GFO_LIBS}/libgfortran.so.1]} {HAS_GFO&slc5 [${GFO}/${GFO_LIBS}/libgfortran.so.1]} {HAS_GFO&slc6 [${GFO}/${GFO_LIBS}/libgfortran.so.1]} {HAS_GFO&Darwin [${GFO}/${GFO_LIBS}/libgfortran.dylib]} {HAS_GFO [${GFO}/${GFO_LIBS}/libgfortranbegin.a ${GFO}/${GFO_LIBS}/libgfortran.a]} {HAS_G95 [${G95}/lib/gcc-lib/i686-pc-linux-gnu/4.0.1/libf95.a]}]}}
    macro("FORTRAN_libset", (
      {"default": ""},
      {"HAS_PGI32": ["${PGI}/linux86/lib/event_init.o", "${PGI}/linux86/lib/libpgf90.a", "${PGI}/linux86/lib/libpgf90_rpm1.a", "${PGI}/linux86/lib/libpgf902.a", "${PGI}/linux86/lib/libpgf90rtl.a", "${PGI}/linux86/lib/libpgftnrtl.a", "${PGI}/linux86/lib/libpgc.a"]},
      {"HAS_PGI41": ["${PGI}/linux86/lib/libpgf90.a", "${PGI}/linux86/lib/libpgf90_rpm1.a", "${PGI}/linux86/lib/libpgf902.a", "${PGI}/linux86/lib/libpgf90rtl.a", "${PGI}/linux86/lib/libpgftnrtl.a", "${PGI}/linux86/lib/libpgc.a"]},
      {"HAS_PGI51": ["${PGI}/linux86/lib/libpgf90.a", "${PGI}/linux86/lib/libpgf90_rpm1.a", "${PGI}/linux86/lib/libpgf902.a", "${PGI}/linux86/lib/libpgf90rtl.a", "${PGI}/linux86/lib/libpgftnrtl.a", "${PGI}/linux86/lib/libpgc.a"]},
      {"HAS_PGI52": ["${PGI}/lib/libpgf90.a", "${PGI}/lib/libpgf90_rpm1.a", "${PGI}/lib/libpgf902.a", "${PGI}/lib/libpgf90rtl.a", "${PGI}/lib/libpgftnrtl.a", "${PGI}/lib/libnspgc.a", "${PGI}/lib/libpgc.a"]},
      {("HAS_GFO", "gcc43"): ["${gfo_notAsNeeded_linkopt}", "${GFO}/${GFO_LIBS}/libgfortran.so", "${gfo_asNeeded_linkopt}"]},
      {("HAS_GFO", "gcc45"): ["${gfo_notAsNeeded_linkopt}", "${GFO}/${GFO_LIBS}/libgfortran.so", "${gfo_asNeeded_linkopt}"]},
      {("HAS_GFO", "gcc46"): ["${gfo_notAsNeeded_linkopt}", "`${for}", "-print-file-name=libgfortran.so`", "${gfo_asNeeded_linkopt}"]},
      {("HAS_GFO", "gcc47"): ["${gfo_notAsNeeded_linkopt}", "`${for}", "-print-file-name=libgfortran.so`", "${gfo_asNeeded_linkopt}"]},
      {("HAS_GFO", "gcc48"): ["${gfo_notAsNeeded_linkopt}", "`${for}", "-print-file-name=libgfortran.so`", "${gfo_asNeeded_linkopt}"]},
      {("HAS_GFO", "target-clang3"): ["${gfo_notAsNeeded_linkopt}", "`${for}", "-print-file-name=libgfortran.so`", "${gfo_asNeeded_linkopt}"]},
      {("HAS_GFO", "slc4"): "${GFO}/${GFO_LIBS}/libgfortran.so.1"},
      {("HAS_GFO", "slc5"): "${GFO}/${GFO_LIBS}/libgfortran.so.1"},
      {("HAS_GFO", "slc6"): "${GFO}/${GFO_LIBS}/libgfortran.so.1"},
      {("HAS_GFO", "Darwin"): "${GFO}/${GFO_LIBS}/libgfortran.dylib"},
      {"HAS_GFO": ["${GFO}/${GFO_LIBS}/libgfortranbegin.a", "${GFO}/${GFO_LIBS}/libgfortran.a"]},
      {"HAS_G95": "${G95}/lib/gcc-lib/i686-pc-linux-gnu/4.0.1/libf95.a"},
    ))
    #### macro &{{HAS_GFO_export [{default []} {HAS_GFO&slc4 []} {HAS_GFO&slc5 []} {HAS_GFO&slc6 []} {HAS_GFO [${GFO}/bin ${GFO}/include ${GFO}/${GFO_LIBS} ${GFO}/libexec]}]}}
    macro("HAS_GFO_export", (
      {"default": ""},
      {("HAS_GFO", "slc4"): ""},
      {("HAS_GFO", "slc5"): ""},
      {("HAS_GFO", "slc6"): ""},
      {"HAS_GFO": ["${GFO}/bin", "${GFO}/include", "${GFO}/${GFO_LIBS}", "${GFO}/libexec"]},
    ))
    ##### **** statement *hlib.PatternStmt (&{fortran_macro macro <name>_platform  HAS_FORTRAN <value> ; macro <name>  Linux $(<name>_platform) Darwin $(<name>_platform)})
    ##### **** statement *hlib.PatternStmt (&{pgi_gfo_g95_macro macro <name>_platform  HAS_PGI <pgivalue> HAS_GFO <gforvalue> HAS_G95 <g95value> ; macro <name>  Linux $(<name>_platform) Darwin $(<name>_platform)})
    ##### **** statement *hlib.PatternStmt (&{fortran_runtime_macro macro <name>_platform  HAS_FORTRAN_RUNTIME <value> ; macro <name>  Linux $(<name>_platform) Darwin $(<name>_platform)})
    #### macro &{{gfortran_path [{default [${GFO}/bin/]} {Darwin []}]}}
    macro("gfortran_path", (
      {"default": "${GFO}/bin/"},
      {"Darwin": ""},
    ))
    #### path_remove &{{PATH [{default []} {Linux [/pacific/]}]}}
    ctx.hwaf_path_remove("PATH", (
      {"default": ""},
      {"Linux": "/pacific/"},
    ))
    #### path_remove &{{PATH [{default []} {Linux [/pgi/]}]}}
    ctx.hwaf_path_remove("PATH", (
      {"default": ""},
      {"Linux": "/pgi/"},
    ))
    #### path_remove &{{PATH [{default []} {Linux [/gfortran/]}]}}
    ctx.hwaf_path_remove("PATH", (
      {"default": ""},
      {"Linux": "/gfortran/"},
    ))
    #### macro_append &{{for90 [{default []} {x86_64&gcc&32 [-m32]} {x86_64&gcc&64 [-m64]}]}}
    ctx.hwaf_macro_append("for90", (
      {"default": ""},
      {("x86_64", "gcc", "32"): "-m32"},
      {("x86_64", "gcc", "64"): "-m64"},
    ))
    #### macro_append &{{f90flags [{default []} {x86_64&gcc&32 [-march=pentium -Wa,-32]} {x86_64&gcc&64 [-Wa,-64]}]}}
    ctx.hwaf_macro_append("f90flags", (
      {"default": ""},
      {("x86_64", "gcc", "32"): ["-march=pentium", "-Wa,-32"]},
      {("x86_64", "gcc", "64"): ["-Wa,-64"]},
    ))
    #### macro_append &{{f90flags [{default []} {dbg [-fbounds-check]}]}}
    ctx.hwaf_macro_append("f90flags", (
      {"default": ""},
      {"dbg": "-fbounds-check"},
    ))
    #### macro &{{gcc_s [{default []} {gcc41 []} {useG77&x86_64&32 [-lgcc_s_32]} {Darwin []} {useG77 [-lgcc_s]}]}}
    macro("gcc_s", (
      {"default": ""},
      {"gcc41": ""},
      {("useG77", "x86_64", "32"): "-lgcc_s_32"},
      {"Darwin": ""},
      {"useG77": "-lgcc_s"},
    ))
    #### macro &{{fortran90_fragment [{default []} {HAS_FORTRAN [fortran90]}]}}
    macro("fortran90_fragment", (
      {"default": ""},
      {"HAS_FORTRAN": "fortran90"},
    ))
    #### macro &{{fortran90_library_fragment [{default []} {HAS_FORTRAN [fortran90_library]}]}}
    macro("fortran90_library_fragment", (
      {"default": ""},
      {"HAS_FORTRAN": "fortran90_library"},
    ))
    ##### **** statement *hlib.MakeFragmentStmt (&{$(fortran90_fragment)})
    ##### **** statement *hlib.MakeFragmentStmt (&{$(fortran90_library_fragment)})
    #### macro &{{AtlasFortranPolicy_linkopts [{default [${f90_linkopts} ${f77_linkopts}]}]}}
    macro("AtlasFortranPolicy_linkopts", (
      {"default": ["${f90_linkopts}", "${f77_linkopts}"]},
    ))
    #### macro &{{AtlasFortranPolicy_export_paths [{default [${FORTRAN_libset}]} {HAS_GFO [${HAS_GFO_export}]}]}}
    macro("AtlasFortranPolicy_export_paths", (
      {"default": "${FORTRAN_libset}"},
      {"HAS_GFO": "${HAS_GFO_export}"},
    ))
    ##### **** statement *hlib.PatternStmt (&{relative_fincludes -global macro old_dir  useG77 `echo $(<package>_project)/$(<package>_project_release) | sed -e s#//#/#g'` ; macro old_base useG77 `echo $(<package>_cmtpath) | sed -e s#/$(old_dir)##'` ; macro sedcmd  useG77 's#$(old_base)## -e s#^/## -e s#/$## -e s#[^/]*#..#g' ; macro new_base useG77 `echo $(<package>_root)/cmt | sed -e $(sedcmd)` ; macro part_fincludes useG77 `( echo $(includes) | sed -e s#$(old_base)#$(new_base)#g')` ; macro new_fincludes  useG77 `$(ATLASFORTRANPOLICYROOT)/cmt/patch_fincludes.sh $(<package>_cmtpath) $(<package>_root)` ; macro fincludes $(includes) useG77 `cmt show macro_value new_fincludes`})
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{pgi_gfo_g95_macro [name=f90_home pgivalue="$(PGI)/bin gforvalue="$(gfortran_path) g95value="$(G95)/bin]})
    ##### **** statement *hlib.ApplyPatternStmt (&{pgi_gfo_g95_macro [name=for90 pgivalue="pgf90 gforvalue="$(f90_home)gfortran g95value="i686-pc-linux-gnu-g95]})
    ##### **** statement *hlib.ApplyPatternStmt (&{fortran_macro [name=f90pp value="$(for) -E -P $(fincludes) ]})
    ##### **** statement *hlib.ApplyPatternStmt (&{fortran_macro [name=f90flags value= -O3 -fno-second-underscore -fPIC]})
    ##### **** statement *hlib.ApplyPatternStmt (&{fortran_macro [name=f90ppflags value= -pipe -fno-second-underscore -Wall -W -Wsurprising -fPIC ]})
    ##### **** statement *hlib.ApplyPatternStmt (&{fortran_macro [name=f90comp value="$(for90) -c $(includes) $(f90flags) $(pp_f90flags)]})
    ##### **** statement *hlib.ApplyPatternStmt (&{fortran_macro [name=f90link value="$(for90) $(f90linkflags)]})
    ##### **** statement *hlib.ApplyPatternStmt (&{pgi_gfo_g95_macro [name=f90_system_linkopts pgivalue="-lm -lgcc -lc -lgcc $(f77_linkopts) gforvalue="-lm $(gcc_s) -lgcc -lc $(gcc_s) -lgcc $(f77_linkopts) g95value="-lm -lgcc -lc -lgcc $(f77_linkopts)]})
    ##### **** statement *hlib.ApplyPatternStmt (&{fortran_runtime_macro [name=f90_linkopts value="$(FORTRAN_libset) $(f90_system_linkopts)]})
    
    
    return # build

## EOF ##
