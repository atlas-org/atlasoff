## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/sqlalchemy",
    "authors": ["Peter Waller <peter.waller@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{sqlalchemy_home [{default [${ATLAS_EXTERNAL}/sqlalchemy]}]}}
    ctx.hwaf_declare_macro("sqlalchemy_home", (
      {"default": "${ATLAS_EXTERNAL}/sqlalchemy"},
    ))
    #### macro &{{sqlalchemy_native_version [{default [0.6.0]}]}}
    ctx.hwaf_declare_macro("sqlalchemy_native_version", (
      {"default": "0.6.0"},
    ))
    #### macro &{{SQLA_PATH [{default [${sqlalchemy_home}/${sqlalchemy_native_version}/lib/python2.5/site-packages]}]}}
    ctx.hwaf_declare_macro("SQLA_PATH", (
      {"default": "${sqlalchemy_home}/${sqlalchemy_native_version}/lib/python2.5/site-packages"},
    ))
    #### macro &{{sqlalchemy_export_paths [{default [${SQLA_PATH}]}]}}
    ctx.hwaf_declare_macro("sqlalchemy_export_paths", (
      {"default": "${SQLA_PATH}"},
    ))
    #### path_remove &{{PYTHONPATH [{default [/sqlalchemy/]}]}}
    ctx.hwaf_path_remove("PYTHONPATH", (
      {"default": "/sqlalchemy/"},
    ))
    #### path_append &{{PYTHONPATH [{default [${SQLA_PATH}]}]}}
    ctx.hwaf_path_append("PYTHONPATH", (
      {"default": "${SQLA_PATH}"},
    ))
    ##### **** statement *hlib.IncludePathStmt (&{[none]})
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
