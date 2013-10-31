## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasGSL",
    "authors": ["David Quarrie <David.Quarrie@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-00-*", public=True)
    ctx.use_pkg("LCG_Interfaces/GSL", version="v*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro_remove &{{GSL_linkopts [{default []} {notAsNeeded []} {asNeeded [-lgslcblas]}]}}
    ctx.hwaf_macro_remove("GSL_linkopts", (
      {"default": ""},
      {"notAsNeeded": ""},
      {"asNeeded": "-lgslcblas"},
    ))
    #### macro_append &{{GSL_linkopts [{default []} {notAsNeeded []} {asNeeded [${notAsNeeded_linkopt} -lgslcblas ${asNeeded_linkopt}]}]}}
    ctx.hwaf_macro_append("GSL_linkopts", (
      {"default": ""},
      {"notAsNeeded": ""},
      {"asNeeded": ["${notAsNeeded_linkopt}", "-lgslcblas", "${asNeeded_linkopt}"]},
    ))
    #### macro &{{GSL_export_paths [{default [${GSL_home}/bin ${GSL_home}/lib ${GSL_home}/include]}]}}
    ctx.hwaf_declare_macro("GSL_export_paths", (
      {"default": ["${GSL_home}/bin", "${GSL_home}/lib", "${GSL_home}/include"]},
    ), override=True)
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
