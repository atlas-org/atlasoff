## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasPOOL",
    "authors": ["Alexander Undrus <undrus@bnl.gov>",
                "RD Schaffer <R.D.Schaffer@cern.ch>",
                "Marcin.Nowak@cern.ch",
                ],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
    ctx.use_pkg("LCG_Interfaces/mysql", version="v*", public=True)
    ctx.use_pkg("Database/APR/POOLCore", version="POOLCore-*", public=True)
    ctx.use_pkg("Database/APR/CollectionBase", version="CollectionBase-*", public=True)
    ctx.use_pkg("Database/APR/CollectionUtilities", version="CollectionUtilities-*", public=True)
    ctx.use_pkg("Database/APR/StorageSvc", version="StorageSvc-*", public=True)
    ctx.use_pkg("Database/APR/PersistencySvc", version="PersistencySvc-*", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("LCG_Interfaces/mysql", version="v*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    ctx.hwaf_path_remove("LD_LIBRARY_PATH", (
      {"default": "/AtlasRAL/"},
    ))

    ctx.hwaf_declare_macro(
        "POOLDB_ROOTDEFS",
        "${INSTALL_AREA}/AtlasPOOL/AtlasRootHacks.h"
        )
    ctx.hwaf_declare_runtime_env("POOLDB_ROOTDEFS")

    # ctx.hwaf_declare_macro("install_command", (
    #   {"default": ["cp", "-R", "-H"]},
    # ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    ctx(
        features="atlas_install_headers",
        source="share/AtlasRootHacks.h",
        cwd="share",
        )
    
    return # build

## EOF ##
