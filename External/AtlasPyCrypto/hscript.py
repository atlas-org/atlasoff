## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasPyCrypto",
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
    
    
    
    #### macro &{{PyCrypto_native_version [{default [2.0.1]}]}}
    ctx.hwaf_declare_macro("PyCrypto_native_version", (
      {"default": "2.0.1"},
    ))
    #### macro &{{PyCrypto_home [{default [${ATLAS_EXTERNAL}/PyCrypto/${PyCrypto_native_version}/${CMTCONFIG}]}]}}
    ctx.hwaf_declare_macro("PyCrypto_home", (
      {"default": "${ATLAS_EXTERNAL}/PyCrypto/${PyCrypto_native_version}/${CMTCONFIG}"},
    ))
    #### macro &{{PyCrypto_pypath [{default [${PyCrypto_home}/lib/python${Python_version}/site-packages]}]}}
    ctx.hwaf_declare_macro("PyCrypto_pypath", (
      {"default": "${PyCrypto_home}/lib/python${Python_version}/site-packages"},
    ))
    ##### **** statement *hlib.IncludePathStmt (&{[none]})
    #### path_remove &{{PYTHONPATH [{default [/PyCrypto/]}]}}
    ctx.hwaf_path_remove("PYTHONPATH", (
      {"default": "/PyCrypto/"},
    ))
    #### path_prepend &{{PYTHONPATH [{default [${PyCrypto_pypath}]}]}}
    ctx.hwaf_path_prepend("PYTHONPATH", (
      {"default": "${PyCrypto_pypath}"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
