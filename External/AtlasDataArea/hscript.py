## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasDataArea",
    "authors": ["ATLAS Software Librarian <ATLAS-Software.Librarian@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-00-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{AtlasDataArea_native_version [{default [v16]}]}}
    ctx.hwaf_declare_macro("AtlasDataArea_native_version", (
      {"default": "v16"},
    ))
    #### set &{{ATLASTESTDATA [{default [${SITEROOT}/atlas/offline/ReleaseData/${AtlasDataArea_native_version}/testfile]} {BNL [${SITEROOT}/offline/ReleaseData/${AtlasDataArea_native_version}/testfile]} {LBNL [${SITEROOT}/local/offline/ReleaseData/${AtlasDataArea_native_version}/testfile]}]}}
    ctx.hwaf_declare_macro("ATLASTESTDATA", (
      {"default": "${SITEROOT}/atlas/offline/ReleaseData/${AtlasDataArea_native_version}/testfile"},
      {"BNL": "${SITEROOT}/offline/ReleaseData/${AtlasDataArea_native_version}/testfile"},
      {"LBNL": "${SITEROOT}/local/offline/ReleaseData/${AtlasDataArea_native_version}/testfile"},
    ))
    ctx.hwaf_declare_runtime_env("ATLASTESTDATA")
    #### set &{{ATLASCALDATA [{default [${SITEROOT}/atlas/offline/ReleaseData/${AtlasDataArea_native_version}]} {BNL [${SITEROOT}/offline/ReleaseData/${AtlasDataArea_native_version}]} {LBNL [${SITEROOT}/local/offline/ReleaseData/${AtlasDataArea_native_version}]}]}}
    ctx.hwaf_declare_macro("ATLASCALDATA", (
      {"default": "${SITEROOT}/atlas/offline/ReleaseData/${AtlasDataArea_native_version}"},
      {"BNL": "${SITEROOT}/offline/ReleaseData/${AtlasDataArea_native_version}"},
      {"LBNL": "${SITEROOT}/local/offline/ReleaseData/${AtlasDataArea_native_version}"},
    ))
    ctx.hwaf_declare_runtime_env("ATLASCALDATA")
    #### macro &{{AtlasDataArea_export_paths [{default [${ATLASCALDATA}]}]}}
    ctx.hwaf_declare_macro("AtlasDataArea_export_paths", (
      {"default": "${ATLASCALDATA}"},
    ))
    #### macro &{{AtlasDataArea_platform [{default []} {PACK [noarch]}]}}
    ctx.hwaf_declare_macro("AtlasDataArea_platform", (
      {"default": ""},
      {"PACK": "noarch"},
    ))
    #### path_remove &{{DATAPATH [{default [/offline/ReleaseData]}]}}
    ctx.hwaf_path_remove("DATAPATH", (
      {"default": "/offline/ReleaseData"},
    ))
    #### path_append &{{DATAPATH [{default [${ATLASCALDATA}]}]}}
    ctx.hwaf_path_append("DATAPATH", (
      {"default": "${ATLASCALDATA}"},
    ))
    #### path_append &{{DATAPATH [{default [${ATLASTESTDATA}]}]}}
    ctx.hwaf_path_append("DATAPATH", (
      {"default": "${ATLASTESTDATA}"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
