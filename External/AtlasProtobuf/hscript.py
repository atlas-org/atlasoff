## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasProtobuf",
    "authors": ["Sebastien Binet", "Johannes Ebke"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    
    ## private dependencies
    ctx.use_pkg("TestPolicy", version="TestPolicy-*", private=True)
    
    ## runtime dependencies
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", runtime=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", runtime=True)
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
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=protobuf file=pkgbuild_protobuf.py]})
    
    
    return # build

## EOF ##
