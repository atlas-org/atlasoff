## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasMagField",
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
    
    
    
    #### macro &{{AtlasMagField_native_version [{default [current]}]}}
    ctx.hwaf_declare_macro("AtlasMagField_native_version", (
      {"default": "current"},
    ))
    #### macro &{{ATLASMAGFIELD [{default [${SITEROOT}/atlas/project/magfield/CTB]} {BNL [${SITEROOT}/project/magfield/CTB]} {LBN [${SITEROOT}/local/project/magfield/CTB]}]}}
    ctx.hwaf_declare_macro("ATLASMAGFIELD", (
      {"default": "${SITEROOT}/atlas/project/magfield/CTB"},
      {"BNL": "${SITEROOT}/project/magfield/CTB"},
      {"LBN": "${SITEROOT}/local/project/magfield/CTB"},
    ))
    #### macro &{{AtlasMagField_export_paths [{default [${ATLASMAGFIELD}]}]}}
    ctx.hwaf_declare_macro("AtlasMagField_export_paths", (
      {"default": "${ATLASMAGFIELD}"},
    ))
    #### path_remove &{{DATAPATH [{default [/project/magfield/CTB]}]}}
    ctx.hwaf_path_remove("DATAPATH", (
      {"default": "/project/magfield/CTB"},
    ))
    #### path_append &{{DATAPATH [{default [${ATLASMAGFIELD}]}]}}
    ctx.hwaf_path_append("DATAPATH", (
      {"default": "${ATLASMAGFIELD}"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
