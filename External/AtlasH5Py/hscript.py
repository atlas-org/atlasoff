## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasH5Py",
    "authors": ["Sebastien Binet <binet@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", public=True)
    
    ## private dependencies
    ctx.use_pkg("AtlasFortranPolicy", version="AtlasFortranPolicy-*", private=True)
    ctx.use_pkg("External/AtlasCython", version="AtlasCython-*", private=True)
    ctx.use_pkg("External/AtlasNumPy", version="AtlasNumPy-*", private=True)
    ctx.use_pkg("External/AtlasHdf5", version="AtlasHdf5-*", private=True)
    ctx.use_pkg("TestPolicy", version="TestPolicy-*", private=True)
    
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
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=h5py file=pkgbuild_h5py.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{disable_package_on [platform=Darwin]})
    
    
    return # build

## EOF ##
