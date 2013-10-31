## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasEigen",
    "authors": [],


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
    
    
    
    ##### **** statement *hlib.IncludePathStmt (&{[none]})
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{include_path [extras=$(CMTINSTALLAREA)/$(CMTCONFIG)/include]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=eigen file=pkgbuild_eigen.py]})
    
    
    return # build

## EOF ##
