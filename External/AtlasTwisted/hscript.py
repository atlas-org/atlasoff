## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasTwisted",
    "authors": ["Sebastien Binet <binet@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    ctx.use_pkg("External/AtlasZope", version="AtlasZope-*", public=True)
    ctx.use_pkg("External/AtlasPyCrypto", version="AtlasPyCrypto-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{Twisted_native_version [{default [2.5.0]}]}}
    ctx.hwaf_declare_macro("Twisted_native_version", (
      {"default": "2.5.0"},
    ))
    #### macro &{{Twisted_home [{default [${ATLAS_EXTERNAL}/Twisted/${Twisted_native_version}/${CMTCONFIG}]}]}}
    ctx.hwaf_declare_macro("Twisted_home", (
      {"default": "${ATLAS_EXTERNAL}/Twisted/${Twisted_native_version}/${CMTCONFIG}"},
    ))
    ##### **** statement *hlib.IncludePathStmt (&{[none]})
    #### path_remove &{{PATH [{default [/Twisted/]}]}}
    ctx.hwaf_path_remove("PATH", (
      {"default": "/Twisted/"},
    ))
    #### path_prepend &{{PATH [{default [${Twisted_home}/bin]}]}}
    ctx.hwaf_path_prepend("PATH", (
      {"default": "${Twisted_home}/bin"},
    ))
    #### path_remove &{{PYTHONPATH [{default [/Twisted/]}]}}
    ctx.hwaf_path_remove("PYTHONPATH", (
      {"default": "/Twisted/"},
    ))
    #### path_prepend &{{PYTHONPATH [{default [${Twisted_home}/lib/python${Python_version}/site-packages]}]}}
    ctx.hwaf_path_prepend("PYTHONPATH", (
      {"default": "${Twisted_home}/lib/python${Python_version}/site-packages"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
