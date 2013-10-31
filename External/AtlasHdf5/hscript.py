## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasHdf5",
    "authors": ["Sebastien Binet <binet@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", public=True)
    
    ## private dependencies
    ctx.use_pkg("External/AtlasSzip", version="AtlasSzip-*", private=True)
    ctx.use_pkg("External/AtlasBzip2", version="AtlasBzip2-*", private=True)
    ctx.use_pkg("TestPolicy", version="TestPolicy-*", private=True)
    
    ## runtime dependencies
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro_append &{{AtlasHdf5_linkopts [{default [-lhdf5_cpp -lhdf5]}]}}
    ctx.hwaf_macro_append("AtlasHdf5_linkopts", (
      {"default": ["-lhdf5_cpp", "-lhdf5"]},
    ))
    #### macro_append &{{AtlasHdf5_linkopts [{default []} {Darwin [-lz -lsz]}]}}
    ctx.hwaf_macro_append("AtlasHdf5_linkopts", (
      {"default": ""},
      {"Darwin": ["-lz", "-lsz"]},
    ))
    ##### **** statement *hlib.IncludePathStmt (&{[none]})
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{include_path [extras=$(CMTINSTALLAREA)/$(CMTCONFIG)/include]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=hdf5 file=pkgbuild_hdf5.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{declare_runtime [extras="$(AtlasHdf5_root)/share *.ref *.h5]})
    
    ctx(
        features = "atlas_install_scripts",
        name     = "AtlasHdf5-install-scripts",
        target   = "AtlasHdf5-install-scripts",
        source   = ["scripts/*"],
    )
    return # build

## EOF ##
