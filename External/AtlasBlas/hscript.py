## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasBlas",
    "authors": ["Sebastien Binet <binet@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("LCG_Interfaces/blas", version="*", public=True)
    
    ## private dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", private=True)
    
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{AtlasBlas_export_paths [{default [${blas_home}]}]}}
    ctx.hwaf_declare_macro("AtlasBlas_export_paths", (
      {"default": "${blas_home}"},
    ))
    #### macro &{{AtlasBlas_lcgcmt_lib [{default [${blas_home}/lib]}]}}
    ctx.hwaf_declare_macro("AtlasBlas_lcgcmt_lib", (
      {"default": "${blas_home}/lib"},
    ))
    #### macro &{{AtlasBlas_native_version [{default [${blas_native_version}]}]}}
    ctx.hwaf_declare_macro("AtlasBlas_native_version", (
      {"default": "${blas_native_version}"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{declare_installed_libraries [dir=$(AtlasBlas_lcgcmt_lib)]})
    
    
    return # build

## EOF ##
