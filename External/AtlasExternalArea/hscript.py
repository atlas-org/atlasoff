## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasExternalArea",
    "authors": ["ATLAS Software Librarian <ATLAS-Software.Librarian@cern.ch>"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
    ctx.use_pkg("External/PlatformPolicy", version="PlatformPolicy-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    macro = ctx.hwaf_declare_macro

    macro("ATLAS_EXTERNAL", (
        {"default": "${SITEROOT}/atlas/offline/external"},
        {"BNL":     "${SITEROOT}/offline/externa"},
        {"LBNL":    "${SITEROOT}/local/offline/external"},
        {"EXTSITE": "${SITEROOT}/external"},
        ))
    ctx.hwaf_declare_runtime_env("ATLAS_EXTERNAL")
    
    macro("LCG_ROOT", (
      {"default": "${SITEROOT}/sw/lcg"},
      {"BNL": "${SITEROOT}/cernsw/lcg"},
    ))

    macro("LCG_EXTERNAL", "${LCG_ROOT}/external")
    macro("LCG_app_system", "${LCG_platform}")
    macro("LCG_ext_system", "${LCG_system}")

    macro("COMMON_PACKAGES", (
      {"default":    "${SITEROOT}/sw/packages"},
      {"BNL":        "${SITEROOT}/cernsw/packages"},
      {"EXTSITE":    "${SITEROOT}/packages"},
      {"STANDALONE": "${SITEROOT}/packages"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
