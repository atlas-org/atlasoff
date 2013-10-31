## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasOracle",
    "authors": ["Alexandre Vaniachine <vaniachine@anl.gov>",
                "RD Schaffer <R.D.Schaffer@cern.ch>",
                ],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-00-*", public=True)
    ctx.use_pkg("LCG_Interfaces/oracle", version="v*", public=True)
    ctx.use_pkg("LCG_Interfaces/pytools", version="*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):

    
    # instruct Oracle not to change floating point precision
    # this should eventually go to LCGCMT rather than ATLAS package
    ctx.hwaf_declare_macro("ORA_FPU_PRECISION", "EXTENDED", override=True)
    ctx.hwaf_declare_runtime_env("ORA_FPU_PRECISION")
    

    ctx.hwaf_path_remove("DYLD_LIBRARY_PATH", (
      {"default": ""},
      {"host-darwin": "/oracle/"},
    ))

    ctx.hwaf_path_append("DYLD_LIBRARY_PATH", (
      {"default": ""},
      {"host-darwin": "${oracle_home}/lib"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
