## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasCORAL",
    "authors": ["RD Schaffer <R.D.Schaffer@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-00-*", public=True)
    ctx.use_pkg("LCG_Interfaces/CORAL", version="v*", public=True)
    ctx.use_pkg("External/AtlasReflex", version="AtlasReflex-00-*", public=True)
    ctx.use_pkg("External/AtlasOracle", version="", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("External/AtlasReflex", version="AtlasReflex-00-*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    ## FIXME
    ctx.hwaf_declare_tag("NEEDS_CORAL_BASE", content=[])
    ctx.hwaf_declare_tag("NEEDS_CORAL_RELATIONAL_ACCESS", content=[])
    
    ctx.hwaf_apply_tag("NEEDS_CORAL_RELATIONAL_ACCESS")
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
