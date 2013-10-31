## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasDCACHE",
    "authors": ["David Quarrie <David.Quarrie@cern.ch>"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-*", public=True)
    ctx.use_pkg("LCG_Interfaces/dcache_client", version="", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{dache_use [{default []} {useDCACHE [dcache_client v* LCG_Interfaces]}]}}
    ctx.hwaf_declare_macro("dache_use", (
      {"default": ""},
      {"useDCACHE": ["dcache_client", "v*", "LCG_Interfaces"]},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
