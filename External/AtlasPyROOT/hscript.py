## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasPyROOT",
    "authors": ["Wim Lavrijsen <WLavrijsen@lbl.gov>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/AtlasROOT", version="AtlasROOT-02-*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-00-*", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("External/AtlasROOT", version="AtlasROOT-02-*", runtime=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-00-*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
