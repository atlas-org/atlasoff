## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasSzip",
    "authors": ["Sebastien Binet <binet@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro_append &{{AtlasSzip_linkopts [{default [-lsz]}]}}
    ctx.hwaf_macro_append("AtlasSzip_linkopts", (
      {"default": "-lsz"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{include_path [extras=$(CMTINSTALLAREA)/$(CMTCONFIG)/include]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=szip file=pkgbuild_szip.py]})
    
    
    return # build

## EOF ##
