## -*- python -*-
## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "Database/ConnectionManagement/AtlasAuthentication",
    "authors": ["RD Schaffer <R.D.Schaffer@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):

    macro = ctx.hwaf_declare_macro
    
    macro("AtlasAuthentication_native_version", "v16")
    macro("AtlasAuthentication_home", "${ATLAS_EXTERNAL}/AtlasAuth/${AtlasAuthentication_native_version}")

    macro("AtlasAuthentication_export_paths", "${AtlasAuthentication_home}")

    ctx.hwaf_path_remove("CORAL_AUTH_PATH", (
      {"default": "AtlasAuthentication"},
    ))

    ctx.hwaf_path_append("CORAL_AUTH_PATH", (
      {"default": "${AtlasAuthentication_cmtpath}/${cmt_installarea_prefix}/XML/AtlasAuthentication"},
    ))

    ctx.hwaf_path_remove("CORAL_DBLOOKUP_PATH", (
      {"default": "AtlasAuthentication"},
    ))

    # ctx.hwaf_path_append("CORAL_DBLOOKUP_PATH", (
    #   {"default": "${AtlasAuthentication_cmtpath}/${cmt_installarea_prefix}/XML/AtlasAuthentication"},
    # ))
    ctx.hwaf_path_append("CORAL_DBLOOKUP_PATH","${INSTALL_AREA}/XML/AtlasAuthentication")
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):

    ctx(
        features = "atlas_generic_install",
        name     = "AtlasAuthentication-generic-install",
        source   = ["${AtlasAuthentication_home}/authentication.xml"],
        install_prefix = ["XML/AtlasAuthentication"],
        relative_trick = False,
    )
    
    ctx(
        features = "atlas_install_data",
        name     = "AtlasAuthentication-install-data",
        source   = ["data/dbreplica.config"],
    )
    
    ctx(
        features = "atlas_install_scripts",
        name     = "AtlasAuthentication-install-scripts",
        target   = "AtlasAuthentication-install-scripts",
        source   = ["scripts/setupLocalDBReplica_CERN.sh"],
    )
    
    ctx(
        features = "atlas_install_xmls",
        name     = "AtlasAuthentication-install-xmls",
        target   = "AtlasAuthentication-install-xmls",
        source   = ["xml/*"],
    )
    return # build

## EOF ##
