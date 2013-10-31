## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/pyAMI",
    "authors": ["Noel Dawe <noel.dawe@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    ctx.use_pkg("External/ZSI", version="ZSI-*", public=True)
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", public=True)
    ctx.use_pkg("External/AtlasPyFwdBwdPorts", version="AtlasPyFwdBwdPorts-*", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("External/ZSI", version="ZSI-*", runtime=True)
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=pyAMI file=pkgbuild_pyAMI.py]})
    
    
    return # build

## EOF ##
