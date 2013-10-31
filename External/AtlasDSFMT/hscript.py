## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasDSFMT",
    "authors": [
        "Michael Duehrssen michael.duehrssen@cern",
        "Paolo Calafiura pcalafiura@lbl",
        ],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-00-*", public=True)
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

    macro("AtlasDSFMT_home", "${ATLAS_EXTERNAL}/dSFMT")
    macro("AtlasDSFMT_native_version", "2.1")

    macro("AtlasDSFMT_incdir", "${AtlasDSFMT_home}/dSFMT-${AtlasDSFMT_native_version}/include")
    macro("AtlasDSFMT_libdir", "${AtlasDSFMT_home}/dSFMT-${AtlasDSFMT_native_version}/${HWAF_VARIANT}")

    macro("INCLUDES_AtlasDSFMT", "${AtlasDSFMT_incdir}")
    macro("LIBPATH_AtlasDSFMT",  "${AtlasDSFMT_libdir}")
    macro("LIB_AtlasDSFMT",      "dSFMT-sse2")

    # The code that uses dSFMT needs to make sure that dsfmt_t objects are alligned at
    # 128bit/16byte in memory
    # See Simulation/Tools/AtlasCLHEP_RandomGenerators for an example
    # -> " -msse2 " no longer needed as public flag
    # macro("CFLAGS_AtlasDSFMT",  "-msse2")
    # macro("CXXFLAGS_AtlasDSFMT", "-msse2")
    # macro("DEFINES_AtlasDSFMT", (["DHAVE_SSE2", "DSFMT_MEXP=19937"]))

    # Set the precsision of the dSFMT engine.
    # This is the parameter with which the external library is compiled
    macro("DEFINES_AtlasDSFMT", "DSFMT_MEXP=19937")

    macro("AtlasDSFMT_export_paths", (
        {"default": ["${AtlasDSFMT_incdir}",
                     "${AtlasDSFMT_libdir}",
                     ]},
    ))
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
