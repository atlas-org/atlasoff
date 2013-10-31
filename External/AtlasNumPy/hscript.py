## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasNumPy",
    "authors": ["Sebastien Binet <binet@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("LCG_Interfaces/pyanalysis", version="*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    ctx.use_pkg("External/AtlasBlas", version="AtlasBlas-*", public=True)
    ctx.use_pkg("External/AtlasLapack", version="AtlasLapack-*", public=True)
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", public=True)
    
    ## private dependencies
    ctx.use_pkg("AtlasFortranPolicy", version="AtlasFortranPolicy-*", private=True)
    ctx.use_pkg("TestPolicy", version="TestPolicy-*", private=True)
    ctx.use_pkg("External/AtlasNose", version="AtlasNose-*", private=True)
    
    ## runtime dependencies
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
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=uncertainties file=pkgbuild_uncertainties.py]})
    
    
    return # build

## EOF ##
