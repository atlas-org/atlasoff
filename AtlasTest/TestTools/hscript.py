## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "AtlasTest/TestTools",
    "authors": ["Paolo Calafiura <Paolo.Calafiura@cern.ch>",
                "Sebastien Binet <binet@cern.ch>",
                ],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    ctx.use_pkg("Control/AthenaCommon", version="AthenaCommon-*", public=True)
    ctx.use_pkg("TestPolicy", version="TestPolicy-*", public=True)
    
    ## private dependencies
    ctx.use_pkg("External/GaudiInterface", version="GaudiInterface-*", private=True)
    
    ## runtime dependencies
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", runtime=True)
    ctx.use_pkg("Control/AthenaCommon", version="AthenaCommon-*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{whichGroup [{default [check]}]}}
    ctx.hwaf_declare_macro("whichGroup", (
      {"default": "check"},
    ))

    ctx.hwaf_macro_append("DOXYGEN_INPUT", (
      {"default": "../doc"},
    ))

    ctx.hwaf_macro_append("DOXYGEN_INPUT", (
      {"default": "../share"},
    ))

    ctx.hwaf_macro_append("DOXYGEN_FILE_PATTERNS", (
      {"default": "*.sh"},
    ))

    ctx.hwaf_macro_append("DOXYGEN_FILE_PATTERNS", (
      {"default": "*.txt"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    ctx(
        features = "atlas_library",
        name     = "TestTools",
        target   = "TestTools",
        source   = ["src/*.cxx"],
        use      = ["GaudiKernel", "boost-filesystem", "boost-system"],
    )

    ctx(
        features = "atlas_install_scripts",
        source   = ["share/runUnitTests.sh",
                    "share/post.sh",
                    ],
        )

    ctx(
        features = "atlas_install_python_modules",
        source   = ["python/*.py"],
        )

    ctx(
        features = "atlas_install_joboptions",
        source   = ["share/*.py"],
        )
    
    return # build

## EOF ##
