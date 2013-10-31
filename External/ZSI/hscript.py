## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/ZSI",
    "authors": ["Chun Lik Tan <clat@hep.ph.bham.ac.uk>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-00-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### set &{{ZSI_VERSION [{default [2.1-a1]}]}}
    ctx.hwaf_declare_macro("ZSI_VERSION", (
      {"default": "2.1-a1"},
    ))
    ctx.hwaf_declare_runtime_env("ZSI_VERSION")
    #### path_remove &{{PYTHONPATH [{default [/ZSI/]}]}}
    ctx.hwaf_path_remove("PYTHONPATH", (
      {"default": "/ZSI/"},
    ))
    #### path_remove &{{PATH [{default [/ZSI/]}]}}
    ctx.hwaf_path_remove("PATH", (
      {"default": "/ZSI/"},
    ))
    #### path_prepend &{{PYTHONPATH [{default [${ATLAS_EXTERNAL}/ZSI/${ZSI_VERSION}/lib/python]}]}}
    ctx.hwaf_path_prepend("PYTHONPATH", (
      {"default": "${ATLAS_EXTERNAL}/ZSI/${ZSI_VERSION}/lib/python"},
    ))
    #### path_prepend &{{PATH [{default [${ATLAS_EXTERNAL}/ZSI/${ZSI_VERSION}/bin]}]}}
    ctx.hwaf_path_prepend("PATH", (
      {"default": "${ATLAS_EXTERNAL}/ZSI/${ZSI_VERSION}/bin"},
    ))
    #### macro &{{ZSI_home [{default [${ATLAS_EXTERNAL}/ZSI]}]}}
    ctx.hwaf_declare_macro("ZSI_home", (
      {"default": "${ATLAS_EXTERNAL}/ZSI"},
    ))
    #### macro &{{ZSI_native_version [{default [${ZSI_VERSION}]}]}}
    ctx.hwaf_declare_macro("ZSI_native_version", (
      {"default": "${ZSI_VERSION}"},
    ))
    #### macro &{{ZSI_export_paths [{default [${ATLAS_EXTERNAL}/ZSI/${ZSI_VERSION}/lib/python]}]}}
    ctx.hwaf_declare_macro("ZSI_export_paths", (
      {"default": "${ATLAS_EXTERNAL}/ZSI/${ZSI_VERSION}/lib/python"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
