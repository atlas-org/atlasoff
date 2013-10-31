## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/SLC5_Compat",
    "authors": ["David Quarrie <David.Quarrie@cern.ch>"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-*", public=True)
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
    
    macro("SLC5_Compat_native_version", (
      {"default": "1.0.2"},
    ))

    macro("SLC5_Compat_platform", (
      {"default": "NotSupported"},
      {"i686-slc5-gcc43": "i686-slc5-gcc43"},
      {"x86_64-slc5-gcc43": "x86_64-slc5-gcc43"},
    ))

    macro("SLC5_Compat_base", (
      {"default": "${ATLAS_EXTERNAL}/slc5compat/${SLC5_Compat_native_version}"},
    ))

    macro("SLC5_Compat_home", (
      {"default": "${SLC5_Compat_base}/${SLC5_Compat_platform}"},
    ))

    macro("SLC5_Compat_home_install", (
      {"default": "${SLC5_Compat_root}/${CMTCONFIG}/slc5compat"},
    ))

    macro("SLC5_Compat_bin", (
      {"default": ""},
      {("host-slc5", "i686-slc5-gcc43"): "${SLC5_Compat_home_install}/bin"},
      {("host-slc5", "x86_64-slc5-gcc43"): "${SLC5_Compat_home_install}/bin"},
    ))

    macro("SLC5_Compat_lib", (
      {"default": ""},
      {("host-slc5", "i686-slc5-gcc43"): "${SLC5_Compat_home_install}/lib"},
      {("host-slc5", "x86_64-slc5-gcc43"): "${SLC5_Compat_home_install}/lib"},
    ))

    ctx.hwaf_path_remove("PATH", (
      {"default": "/slc4compat/"},
    ))

    ctx.hwaf_path_prepend("PATH", (
      {"default": ""},
      {("host-slc5", "i686-slc5-gcc43"): "${SLC5_Compat_bin}"},
      {("host-slc5", "x86_64-slc5-gcc43"): "${SLC5_Compat_bin}"},
    ))

    ctx.hwaf_path_remove("LD_LIBRARY_PATH", (
      {"default": "/slc4compat/"},
    ))

    ctx.hwaf_path_prepend("LD_LIBRARY_PATH", (
      {"default": ""},
      {("host-slc5", "i686-slc5-gcc43"): "${SLC5_Compat_lib}"},
      {("host-slc5", "x86_64-slc5-gcc43"): "${SLC5_Compat_lib}"},
    ))

    macro("SLC5_Compat_export_paths", (
      {"default": ""},
      {"i686-slc5-gcc43": "${SLC5_Compat_home}"},
      {"x86_64-slc5-gcc43": "${SLC5_Compat_home}"},
    ))

    macro("SLC5_Compat_install_cmd", (
      {"default": ["${library_install_command}", "${SLC5_Compat_home}", "${SLC5_Compat_home_install}"]},
    ))

    ctx.hwaf_macro_append("all_dependencies", (
      {"default": ""},
      {"i686-slc5-gcc43": "SLC5_Compat_install_action"},
      {"x86_64-slc5-gcc43": "SLC5_Compat_install_action"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
