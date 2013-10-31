## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasBzip2",
    "authors": ["ATLAS Software Librarian <ATLAS-Software.Librarian@cern.ch>"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="*", public=True)
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro

    macro("AtlasBzip2_home", "${ATLAS_EXTERNAL}/bzip2/${AtlasBzip2_native_version}/${CMTCONFIG}")
    macro("AtlasBzip2_native_version", "1.0.5")

    macro("AtlasBzip2_incdir", "${AtlasBzip2_home}/include")
    macro("AtlasBzip2_libdir", "${AtlasBzip2_home}/lib")

    macro("LIBPATH_AtlasBzip2", "${AtlasBzip2_libdir}")
    macro("LIB_AtlasBzip2",     "bz2")

    macro("AtlasBzip2_export_paths", (
        {"default": ["${AtlasBzip2_incdir}",
                     "${AtlasBzip2_libdir}",
                     ]},
    ))

    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
