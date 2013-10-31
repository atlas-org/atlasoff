## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasInlineAssistant",
    "authors": ["ravitillo@lbl.gov"],


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
    
    
    
    #### macro &{{inlineassistant_native_version [{default [1.0]}]}}
    ctx.hwaf_declare_macro("inlineassistant_native_version", (
      {"default": "1.0"},
    ))
    #### macro &{{inlineassistant_home [{default [${ATLAS_EXTERNAL}/InlineAssistant/${inlineassistant_native_version}/${CMTCONFIG}]}]}}
    ctx.hwaf_declare_macro("inlineassistant_home", (
      {"default": "${ATLAS_EXTERNAL}/InlineAssistant/${inlineassistant_native_version}/${CMTCONFIG}"},
    ))
    #### macro &{{inlineassistant_libs [{default [${inlineassistant_home}/lib]}]}}
    ctx.hwaf_declare_macro("inlineassistant_libs", (
      {"default": "${inlineassistant_home}/lib"},
    ))
    #### macro &{{inlineassistant_bin [{default [${inlineassistant_home}/bin]}]}}
    ctx.hwaf_declare_macro("inlineassistant_bin", (
      {"default": "${inlineassistant_home}/bin"},
    ))
    #### path_remove &{{LD_LIBRARY_PATH [{default [${inlineassistant_libs}]}]}}
    ctx.hwaf_path_remove("LD_LIBRARY_PATH", (
      {"default": "${inlineassistant_libs}"},
    ))
    #### path_append &{{LD_LIBRARY_PATH [{default [${inlineassistant_libs}]}]}}
    ctx.hwaf_path_append("LD_LIBRARY_PATH", (
      {"default": "${inlineassistant_libs}"},
    ))
    #### path_remove &{{PATH [{default [${inlineassistant_bin}]}]}}
    ctx.hwaf_path_remove("PATH", (
      {"default": "${inlineassistant_bin}"},
    ))
    #### path_append &{{PATH [{default [${inlineassistant_bin}]}]}}
    ctx.hwaf_path_append("PATH", (
      {"default": "${inlineassistant_bin}"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
