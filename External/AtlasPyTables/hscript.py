## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasPyTables",
    "authors": ["Sebastien Binet <binet@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    ctx.use_pkg("External/AtlasNumPy", version="AtlasNumPy-*", public=True)
    ctx.use_pkg("External/AtlasHdf5", version="AtlasHdf5-*", public=True)
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", public=True)
    
    ## private dependencies
    ctx.use_pkg("AtlasFortranPolicy", version="AtlasFortranPolicy-*", private=True)
    ctx.use_pkg("External/AtlasLzo", version="AtlasLzo-*", private=True)
    ctx.use_pkg("External/AtlasBzip2", version="AtlasBzip2-*", private=True)
    
    ## runtime dependencies
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    ##### **** statement *hlib.IncludeDirsStmt (&{[$(CMTINSTALLAREA)/$(CMTCONFIG)/include]})
    #### macro_append &{{make_pkgbuild_pytables_dependencies [{default [make_pkgbuild_numexpr]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_pytables_dependencies", (
      {"default": "make_pkgbuild_numexpr"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=numexpr file=pkgbuild_numexpr.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=pytables file=pkgbuild_pytables.py]})
    
    
    return # build

## EOF ##
