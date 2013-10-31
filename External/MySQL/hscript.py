## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/MySQL",
    "authors": ["Alexandre Vaniachine <vaniachine@anl.gov>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-00-*", public=True)
    ctx.use_pkg("LCG_Interfaces/mysql", version="v*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    ##### **** statement *hlib.IncludeDirsStmt (&{[$(mysql_home)/include]})
    #### set &{{My_SQL [{default [${mysql_home}]}]}}
    ctx.hwaf_declare_macro("My_SQL", (
      {"default": "${mysql_home}"},
    ))
    ctx.hwaf_declare_runtime_env("My_SQL")
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
