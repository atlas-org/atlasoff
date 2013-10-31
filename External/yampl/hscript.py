## -*- python -*-
## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/yampl",
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
    
    macro = ctx.hwaf_declare_macro
    
    macro("yampl_native_version", "1.0")
    macro("yampl_home", "${ATLAS_EXTERNAL}/yampl/${yampl_native_version}/${CMTCONFIG}")

    macro("yampl_bindir", "${yampl_home}/bin")
    macro("yampl_incdir", "${yampl_home}/include")
    macro("yampl_libdir", "${yampl_home}/lib")

    macro("INCLUDES_yampl", "${yampl_incdir}")
    macro("LIBPATH_yampl",  "${yampl_libdir}")
    macro("LIB_yampl",      "yampl")
    
    ctx.hwaf_path_remove("PATH", "${yampl_bin}")
    ctx.hwaf_path_append("PATH", "${yampl_bin}")

    macro("yampl_export_paths", "${yampl_home}")
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
