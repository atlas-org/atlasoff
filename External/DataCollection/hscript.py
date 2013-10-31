## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/DataCollection",
    "authors": [],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasCxxPolicy", version="AtlasCxxPolicy-*", public=True)
    ## FIXME
    #ctx.use_pkg("TDAQCPolicy/TDAQCPolicyExt", version="v*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{DataCollection_linkopts [{default [${tdaqc_linkopts}]}]}}
    ctx.hwaf_declare_macro("DataCollection_linkopts", (
      {"default": "${tdaqc_linkopts}"},
    ))
    #### macro_append &{{DataCollection_linkopts [{default [-leformat -leformat_write -lDataReader -leformat_old]}]}}
    ctx.hwaf_macro_append("DataCollection_linkopts", (
      {"default": ["-leformat", "-leformat_write", "-lDataReader", "-leformat_old"]},
    ))
    #### macro_append &{{DataCollection_linkopts [{default [-lRawFileName -lDataWriter -ldl -lers]}]}}
    ctx.hwaf_macro_append("DataCollection_linkopts", (
      {"default": ["-lRawFileName", "-lDataWriter", "-ldl", "-lers"]},
    ))
    #### path_remove &{{PYTHONPATH [{default [/tdaq-common/]}]}}
    ctx.hwaf_path_remove("PYTHONPATH", (
      {"default": "/tdaq-common/"},
    ))
    #### path_append &{{PYTHONPATH [{default [${tdaq-common_home}/installed/share/lib/python]}]}}
    ctx.hwaf_path_append("PYTHONPATH", (
      {"default": "${tdaq-common_home}/installed/share/lib/python"},
    ))
    #### path_append &{{PYTHONPATH [{default [${tdaq-common_home}/installed/${CMTCONFIG}/lib]}]}}
    ctx.hwaf_path_append("PYTHONPATH", (
      {"default": "${tdaq-common_home}/installed/${CMTCONFIG}/lib"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
