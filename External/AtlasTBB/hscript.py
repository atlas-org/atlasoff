## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasTBB",
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
    
    
    
    ##### **** statement *hlib.IncludeDirsStmt (&{[none]})
    #### macro &{{AtlasTBB_linkopts [{default [-ltbb]}]}}
    ctx.hwaf_declare_macro("AtlasTBB_linkopts", (
      {"default": "-ltbb"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=tbb file=pkgbuild_tbb.py]})
    
    ctx(
        features = "atlas_application",
        name     = "test-tbb",
        target   = "test-tbb",
        source   = ["src/test-tbb.cxx"],
    )
    return # build

## EOF ##
