## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasMKL",
    "authors": ["Sebastien Binet"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{AtlasMKL_native_version [{default [2013.3.163]}]}}
    ctx.hwaf_declare_macro("AtlasMKL_native_version", (
      {"default": "2013.3.163"},
    ))
    #### macro &{{AtlasMKL_composerxe_home [{default [/no-intel-composerxe]} {Linux [${SITEROOT}/sw/IntelSoftware/linux/x86_64/xe2013/composer_xe_${AtlasMKL_native_version}]}]}}
    ctx.hwaf_declare_macro("AtlasMKL_composerxe_home", (
      {"default": "/no-intel-composerxe"},
      {"Linux": "${SITEROOT}/sw/IntelSoftware/linux/x86_64/xe2013/composer_xe_${AtlasMKL_native_version}"},
    ))
    #### macro &{{AtlasMKL_home [{default [/no-intel-mkl]} {Linux [${AtlasMKL_composerxe_home}/mkl]}]}}
    ctx.hwaf_declare_macro("AtlasMKL_home", (
      {"default": "/no-intel-mkl"},
      {"Linux": "${AtlasMKL_composerxe_home}/mkl"},
    ))
    #### macro &{{AtlasMKL_compiler_home [{default [/no-intel-compiler]} {Linux [${AtlasMKL_composerxe_home}/compiler]}]}}
    ctx.hwaf_declare_macro("AtlasMKL_compiler_home", (
      {"default": "/no-intel-compiler"},
      {"Linux": "${AtlasMKL_composerxe_home}/compiler"},
    ))
    #### macro &{{AtlasMKL_export_paths [{default [${AtlasMKL_incdir} ${AtlasMKL_libdir} ${AtlasMKL_compiler_libdir}]}]}}
    ctx.hwaf_declare_macro("AtlasMKL_export_paths", (
      {"default": ["${AtlasMKL_incdir}", "${AtlasMKL_libdir}", "${AtlasMKL_compiler_libdir}"]},
    ))
    #### macro &{{AtlasMKL_platform [{default []} {Linux&64 [intel64]} {Linux&32 [ia32]}]}}
    ctx.hwaf_declare_macro("AtlasMKL_platform", (
      {"default": ""},
      {("Linux", "64"): "intel64"},
      {("Linux", "32"): "ia32"},
    ))
    #### macro &{{AtlasMKL_bin [{default [${AtlasMKL_home}/bin/ia32]} {64 [${AtlasMKL_home}/bin/intel64]}]}}
    ctx.hwaf_declare_macro("AtlasMKL_bin", (
      {"default": "${AtlasMKL_home}/bin/ia32"},
      {"64": "${AtlasMKL_home}/bin/intel64"},
    ))
    #### macro &{{AtlasMKL_incdir [{default []} {Linux&64 [${AtlasMKL_home}/include]} {Linux&32 [${AtlasMKL_home}/include]}]}}
    ctx.hwaf_declare_macro("AtlasMKL_incdir", (
      {"default": ""},
      {("Linux", "64"): "${AtlasMKL_home}/include"},
      {("Linux", "32"): "${AtlasMKL_home}/include"},
    ))
    ##### **** statement *hlib.IncludeDirsStmt (&{[$(AtlasMKL_incdir)]})
    #### macro &{{AtlasMKL_libdir [{default []} {Linux&64 [${AtlasMKL_home}/lib/intel64]} {Linux&32 [${AtlasMKL_home}/lib/ia32]}]}}
    ctx.hwaf_declare_macro("AtlasMKL_libdir", (
      {"default": ""},
      {("Linux", "64"): "${AtlasMKL_home}/lib/intel64"},
      {("Linux", "32"): "${AtlasMKL_home}/lib/ia32"},
    ))
    #### macro &{{AtlasMKL_compiler_libdir [{default []} {Linux&32 [${AtlasMKL_compiler_home}/lib/ia32]} {Linux&64 [${AtlasMKL_compiler_home}/lib/intel64]}]}}
    ctx.hwaf_declare_macro("AtlasMKL_compiler_libdir", (
      {"default": ""},
      {("Linux", "32"): "${AtlasMKL_compiler_home}/lib/ia32"},
      {("Linux", "64"): "${AtlasMKL_compiler_home}/lib/intel64"},
    ))
    #### set &{{ATLASMKLLIBDIR [{default [${AtlasMKL_libdir}]}]}}
    ctx.hwaf_declare_macro("ATLASMKLLIBDIR", (
      {"default": "${AtlasMKL_libdir}"},
    ))
    ctx.hwaf_declare_runtime_env("ATLASMKLLIBDIR")
    #### set &{{ATLASMKLLIBDIR_PRELOAD [{default [${AtlasMKL_compiler_libdir}]}]}}
    ctx.hwaf_declare_macro("ATLASMKLLIBDIR_PRELOAD", (
      {"default": "${AtlasMKL_compiler_libdir}"},
    ))
    ctx.hwaf_declare_runtime_env("ATLASMKLLIBDIR_PRELOAD")
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
