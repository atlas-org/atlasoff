## -*- python -*-
## waf imports
import waflib.Logs as msg

#
# This glue package was written to help with profiling Athena
# jobs. To use it, you have to add
#
#   use AtlasGPerfTools AtlasGPerfTools-* External
#   macro_append MyPkg_use_linkopts " $(AtlasGPerfTools_linkopts_profiler)"
#
# to your requirements file, and surround the code you want to
# profile with:
#
#   ProfilerStart( "myJob.profile" );
#   ...
#   ProfilerStop();
#
# Usually it's a good idea to put the first line into some
# initialization, and the second one into some finalization
# function.
#

PACKAGE = {
    "name":    "External/AtlasGPerfTools",
    "authors": ["Attila Krasznahorkay <Attila.Krasznahorkay@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", public=True)
    ctx.use_pkg("External/AtlasLibUnwind", version="*", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    macro = ctx.hwaf_declare_macro

    macro("LIB_AtlasGPerfTools-tcmalloc",          "tcmalloc")
    macro("LIB_AtlasGPerfTools-tcmalloc-minimal",  "tcmalloc_minimal")
    macro("LIB_AtlasGPerfTools-tcmalloc-profiler", "tcmalloc_and_profiler")
    macro("LIB_AtlasGPerfTools-profiler",          "profiler")

    
    #### macro &{{AtlasGPerfTools_linkopts_tcmalloc [{default [-ltcmalloc]}]}}
    ctx.hwaf_declare_macro("AtlasGPerfTools_linkopts_tcmalloc", (
      {"default": "-ltcmalloc"},
    ))
    #### macro &{{AtlasGPerfTools_linkopts_tcmalloc_minimal [{default [-ltcmalloc_minimal]}]}}
    ctx.hwaf_declare_macro("AtlasGPerfTools_linkopts_tcmalloc_minimal", (
      {"default": "-ltcmalloc_minimal"},
    ))
    #### macro &{{AtlasGPerfTools_linkopts_tcmalloc_profiler [{default [-ltcmalloc_and_profiler]}]}}
    ctx.hwaf_declare_macro("AtlasGPerfTools_linkopts_tcmalloc_profiler", (
      {"default": "-ltcmalloc_and_profiler"},
    ))
    #### macro &{{AtlasGPerfTools_linkopts_profiler [{default [-lprofiler]}]}}
    ctx.hwaf_declare_macro("AtlasGPerfTools_linkopts_profiler", (
      {"default": "-lprofiler"},
    ))
    #### set &{{ATLAS_GPERFTOOLS_DIR [{default [${CMTINSTALLAREA}/${CMTCONFIG}/lib]}]}}
    ctx.hwaf_declare_macro("ATLAS_GPERFTOOLS_DIR", (
      {"default": "${CMTINSTALLAREA}/${CMTCONFIG}/lib"},
    ))
    ctx.hwaf_declare_runtime_env("ATLAS_GPERFTOOLS_DIR")
    #### macro &{{AtlasGPerfTools_linkopts [{default []} {use_gpt_tcmalloc [${AtlasGPerfTools_linkopts_tcmalloc}]} {use_gpt_tcmalloc_minimal [${AtlasGPerfTools_linkopts_tcmalloc_minimal}]} {use_gpt_tcmalloc_profiler [${AtlasGPerfTools_linkopts_tcmalloc_profiler}]} {use_gpt_profiler [${AtlasGPerfTools_linkopts_profiler}]} {none []}]}}
    ctx.hwaf_declare_macro("AtlasGPerfTools_linkopts", (
      {"default": ""},
      {"use_gpt_tcmalloc": "${AtlasGPerfTools_linkopts_tcmalloc}"},
      {"use_gpt_tcmalloc_minimal": "${AtlasGPerfTools_linkopts_tcmalloc_minimal}"},
      {"use_gpt_tcmalloc_profiler": "${AtlasGPerfTools_linkopts_tcmalloc_profiler}"},
      {"use_gpt_profiler": "${AtlasGPerfTools_linkopts_profiler}"},
      {"none": ""},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=gperftools file=pkgbuild_gperftools.py]})
    
    ctx(
        features = "atlas_install_scripts",
        name     = "AtlasGPerfTools-install-scripts",
        target   = "AtlasGPerfTools-install-scripts",
        source   = ["scripts/*"],
    )
    return # build

## EOF ##
