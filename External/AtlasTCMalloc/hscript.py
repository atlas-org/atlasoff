## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasTCMalloc",
    "authors": ["Paolo Calafiura"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    

    macro("TCMalloc_native_version", (
      {"default": "google-perftools-0.99.2c"},
    ))

    macro("AtlasTCMalloc_native_version", (
      {"default": "${TCMalloc_native_version}"},
    ))

    macro("TCMalloc_home", (
      {"default": "${ATLAS_EXTERNAL}/tcmalloc/${TCMalloc_native_version}"},
    ))

    macro("tcmdir", (
      {"default": ""},
      {("target-icc", "x86_64"): "${TCMalloc_home}/x86_64-slc5-gcc43-opt/lib"},
      {("target-icc", "i686"): "${TCMalloc_home}/i686-slc5-gcc43-opt/lib"},
      {"Linux": "${TCMalloc_home}/${CMTCONFIG}/lib"},
    ))

    macro("TCMALLOCDIR", "${tcmdir}")
    ctx.hwaf_declare_runtime_env("TCMALLOCDIR")
    
    macro("AtlasTCMalloc_follow_symlinks", (
      {"default": ""},
      {"64": "yes"},
    ))

    macro("AtlasTCMalloc_export_paths", (
      {"default": "${tcmdir}"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
