## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasLibUnwind",
    "authors": ["binet"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
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
    
    
    
    #### macro &{{AtlasLibUnwind_linkopts [{default [-L${CMTINSTALLAREA}/${CMTCONFIG}/lib -lunwind]}]}}
    ctx.hwaf_declare_macro("AtlasLibUnwind_linkopts", (
      {"default": ["-L${CMTINSTALLAREA}/${CMTCONFIG}/lib", "-lunwind"]},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=libunwind file=pkgbuild_libunwind.py]})
    
    
    return # build

## EOF ##
