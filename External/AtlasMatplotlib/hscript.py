## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasMatplotlib",
    "authors": ["Sebastien Binet <binet@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    
    ## private dependencies
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", private=True)
    ctx.use_pkg("LCG_Interfaces/pyanalysis", version="*", private=True)
    ctx.use_pkg("External/AtlasPyFwdBwdPorts", version="AtlasPyFwdBwdPorts-*", private=True)
    ctx.use_pkg("External/AtlasNumPy", version="AtlasNumPy-*", private=True)
    ctx.use_pkg("External/AtlasPyQt4", version="AtlasPyQt4-*", private=True)
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", private=True)
    ctx.use_pkg("External/AtlasPyTables", version="*", private=True)
    
    ## runtime dependencies
    ctx.use_pkg("External/AtlasPyFwdBwdPorts", version="AtlasPyFwdBwdPorts-*", runtime=True)
    ctx.use_pkg("External/AtlasPyTables", version="*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=rootplot file=pkgbuild_rootplot.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=rootpy file=pkgbuild_rootpy.py]})
    
    
    return # build

## EOF ##
