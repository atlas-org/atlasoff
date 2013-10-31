## -*- python -*-
## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "Database/IOVDbSvc",
    "authors": ["Antoine Perus <perus@lal.in2p3.fr>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/AtlasCOOL", version="AtlasCOOL-*", public=True)
    ctx.use_pkg("External/GaudiInterface", version="GaudiInterface-*", public=True)
    
    ## private dependencies
    ctx.use_pkg("Control/StoreGate", version="StoreGate-*", private=True)
    ctx.use_pkg("Control/SGTools", version="SGTools-*", private=True)
    ctx.use_pkg("Control/AthenaKernel", version="AthenaKernel-*", private=True)
    ctx.use_pkg("Event/EventInfo", version="EventInfo-*", private=True)
    ctx.use_pkg("Event/EventInfoMgt", version="EventInfoMgt-*", private=True)
    ctx.use_pkg("External/AtlasPOOL", version="AtlasPOOL-*", private=True)
    ctx.use_pkg("External/AtlasROOT", version="AtlasROOT-*", private=True)
    ctx.use_pkg("Database/APR/CollectionBase", private=True)
    ctx.use_pkg("Database/AthenaPOOL/PoolSvc", version="PoolSvc-*", private=True)
    ctx.use_pkg("Database/AthenaPOOL/AthenaPoolUtilities", version="AthenaPoolUtilities-*", private=True)
    ctx.use_pkg("Database/IOVDbDataModel", version="IOVDbDataModel-*", private=True)
    ctx.use_pkg("Database/IOVDbMetaDataTools", version="IOVDbMetaDataTools-*", private=True)
    ctx.use_pkg("External/AtlasCORAL", version="AtlasCORAL-*", private=True)
    ctx.use_pkg("Database/CoraCool", version="CoraCool-*", private=True)
    ctx.use_pkg("DetectorDescription/GeoModel/GeoModelInterfaces", version="GeoModelInterfaces-*", private=True)
    
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):

    macro = ctx.hwaf_declare_macro
    
    ctx.hwaf_apply_tag("NEEDS_COOL_FACTORY")

    macro("POOL_Services_libset", "")
    macro("POOL_FileMgt_libset", "")
    macro("POOL_Collections_libset", "")

    macro("DOXYGEN_EXAMPLE_PATH", (
      {"default": ["../doc", "../cmt", "../share"]},
    ))

    macro("DOXYGEN_EXAMPLE_PATTERNS", (
      {"default": ["*.cxx", "*.html", "requirements", "*.py"]},
    ))

    macro("poolcondfile", (
      {"default": ""},
      {"CERN": "/afs/cern.ch/atlas/conditions/poolcond/catalogue/poolcond"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    ctx(
        features = "atlas_component",
        name     = "IOVDbSvc",
        target   = "IOVDbSvc",
        source   = ["src/*.cxx", "src/components/*.cxx"],
        use = [
            "COOL",
            "GaudiKernel",
            "StoreGate",
            "SGTools",
            "AthenaKernel",
            "EventInfo",
            "EventInfoMgt",
            "POOL",
            "ROOT",
            "PoolSvc",
            "AthenaPoolUtilities",
            "IOVDbDataModel",
            "IOVDbMetaDataTools",
            "CORAL",
            "CoraCool",
            "CollectionBase",
            "GeoModelInterfaces",
            ],
    )

    ctx(
        features = "atlas_install_headers",
        name     = "IOVDbSvc-install-headers",
    )
    
    if ctx.hwaf_enabled_tag('CERN'):
        ctx(
            features = "atlas_generic_install",
            name     = "IOVDbSvc-generic-install--runtime",
            target   = "IOVDbSvc-generic-install--runtime",
            source   = ["${poolcondfile}/*.xml"],
            install_prefix = ["share"],
        )
    
    ctx(
        features = "atlas_install_joboptions",
        name     = "IOVDbSvc-install-jobos",
        target   = "IOVDbSvc-install-jobos",
        source   = ["share/*.py", "share/*.txt"],
    )
    
    ctx(
        features = "atlas_install_python_modules",
        name     = "IOVDbSvc-install-py",
        target   = "IOVDbSvc-install-py",
        source   = ["python/*.py"],
    )
    return # build

## EOF ##
