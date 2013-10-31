## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasLapack",
    "authors": ["Sebastien Binet <binet@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/AtlasBlas", version="AtlasBlas-*", public=True)
    ctx.use_pkg("LCG_Interfaces/lapack", version="*", public=True)
    
    ## private dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", private=True)
    
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{AtlasLapack_export_paths [{default [${lapack_home}]}]}}
    ctx.hwaf_declare_macro("AtlasLapack_export_paths", (
      {"default": "${lapack_home}"},
    ))
    #### macro &{{AtlasLapack_lcgcmt_lib [{default [${lapack_home}/lib]}]}}
    ctx.hwaf_declare_macro("AtlasLapack_lcgcmt_lib", (
      {"default": "${lapack_home}/lib"},
    ))
    #### macro &{{AtlasLapack_native_version [{default [${lapack_native_version}]}]}}
    ctx.hwaf_declare_macro("AtlasLapack_native_version", (
      {"default": "${lapack_native_version}"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{declare_installed_libraries [dir=$(AtlasLapack_lcgcmt_lib)]})
    
    
    return # build

## EOF ##
