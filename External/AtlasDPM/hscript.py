## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasDPM",
    "authors": ["David Quarrie <David.Quarrie@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-*", public=True)
    
    ## private dependencies
    ctx.use_pkg("LCG_Interfaces/dpm", version="v*", private=True)
    
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    ## FIXME
    if 1:
        return
    
    ctx.hwaf_path_remove("PATH", (
      {"default": "/DPM/"},
      {"useDPM": ""},
    ))
    #### path_remove &{{LD_LIBRARY_PATH [{default [/DPM/]} {useDPM []}]}}
    ctx.hwaf_path_remove("LD_LIBRARY_PATH", (
      {"default": "/DPM/"},
      {"useDPM": ""},
    ))
    #### path_remove &{{LD_LIBRARY_PATH [{default [/AtlasDPM/]}]}}
    ctx.hwaf_path_remove("LD_LIBRARY_PATH", (
      {"default": "/AtlasDPM/"},
    ))
    #### path_prepend &{{LD_LIBRARY_PATH [{default []} {useDPM [${ATLASDPMROOT}/${CMTCONFIG}]}]}}
    ctx.hwaf_path_prepend("LD_LIBRARY_PATH", (
      {"default": ""},
      {"useDPM": "${ATLASDPMROOT}/${CMTCONFIG}"},
    ))
    #### macro_remove &{{dpm_linkopts [{default [-ldpm]} {useDPM []}]}}
    ctx.hwaf_macro_remove("dpm_linkopts", (
      {"default": "-ldpm"},
      {"useDPM": ""},
    ))
    ##### **** statement *hlib.MakeFragmentStmt (&{dpm_symlink})
    #### macro &{{AtlasDPM_pacman_post_install [{default [cmt make]}]}}
    ctx.hwaf_declare_macro("AtlasDPM_pacman_post_install", (
      {"default": ["cmt", "make"]},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
