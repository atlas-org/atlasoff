## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasZope",
    "authors": ["Sebastien Binet <binet@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{Zope_native_version [{default [3.3.0]}]}}
    ctx.hwaf_declare_macro("Zope_native_version", (
      {"default": "3.3.0"},
    ))
    #### macro &{{Zope_home [{default [${ATLAS_EXTERNAL}/ZopeInterface/${Zope_native_version}/${CMTCONFIG}]}]}}
    ctx.hwaf_declare_macro("Zope_home", (
      {"default": "${ATLAS_EXTERNAL}/ZopeInterface/${Zope_native_version}/${CMTCONFIG}"},
    ))
    ##### **** statement *hlib.IncludePathStmt (&{[none]})
    #### path_remove &{{PYTHONPATH [{default [/ZopeInterface/]}]}}
    ctx.hwaf_path_remove("PYTHONPATH", (
      {"default": "/ZopeInterface/"},
    ))
    #### path_prepend &{{PYTHONPATH [{default [${Zope_home}/lib/python${Python_version}/site-packages]}]}}
    ctx.hwaf_path_prepend("PYTHONPATH", (
      {"default": "${Zope_home}/lib/python${Python_version}/site-packages"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
