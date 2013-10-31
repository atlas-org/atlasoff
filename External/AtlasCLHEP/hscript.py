## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasCLHEP",
    "authors": ["ATLAS Software Librarian <ATLAS-Software.Librarian@cern.ch>"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-00-*", public=True)
    ctx.use_pkg("LCG_Interfaces/CLHEP", version="v*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    ctx.hwaf_macro_remove("CLHEP_linkopts", (
      {"default": ""},
      {"notAsNeeded": ""},
      {"asNeeded": "CLHEP-Vector-${CLHEP_native_version}"},
    ))
    
    ctx.hwaf_macro_remove("LIB_CLHEP", (
      {"default": ""},
      {"notAsNeeded": ""},
      {"asNeeded": "CLHEP-Random-${CLHEP_native_version}"},
    ))
    
    ctx.hwaf_macro_append("LIB_CLHEP", (
      {"default": ""},
      {"notAsNeeded": ""},
      {"asNeeded": [#"${notAsNeeded_linkopt}", ## FIXME
                    "CLHEP-Vector-${CLHEP_native_version}",
                    "CLHEP-Random-${CLHEP_native_version}",
                    #"${asNeeded_linkopt}",    ## FIXME
                    ]},
    ))

    ctx.hwaf_declare_macro("DEFINES_CLHEP", (
      {"default": ["CLHEP_MAX_MIN_DEFINED", "CLHEP_ABS_DEFINED", "CLHEP_SQR_DEFINED"]},
    ))

    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
