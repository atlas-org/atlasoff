## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasCOOL",
    "authors": ["RD Schaffer <R.D.Schaffer@cern.ch>"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-00-*", public=True)
    ctx.use_pkg("LCG_Interfaces/COOL", version="v*", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("External/AtlasReflex", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    ctx.hwaf_declare_macro('COOL_DISABLE_CORALCONNECTIONPOOLCLEANUP', "YES")
    ctx.hwaf_declare_runtime_env("COOL_DISABLE_CORALCONNECTIONPOOLCLEANUP")
    
    ctx.hwaf_apply_tag("NEEDS_PYCOOL")

    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
