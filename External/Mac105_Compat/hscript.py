## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/Mac105_Compat",
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
    
    #### macro &{{Mac105_Compat_native_version [{default [1.0.0]}]}}
    macro("Mac105_Compat_native_version", (
      {"default": "1.0.0"},
    ))

    macro("Mac105_Compat_platform", (
      {"default": "NotSupported"},
      {"i386-mac105-gcc40-dbg": "i386-mac105-gcc40"},
      {"i386-mac105-gcc40-opt": "i386-mac105-gcc40"},
    ))

    macro("Mac105_Compat_base", (
      {"default": "${ATLAS_EXTERNAL}/mac105compat/${Mac105_Compat_native_version}"},
    ))

    macro("Mac105_Compat_home", (
      {"default": "${Mac105_Compat_base}/${Mac105_Compat_platform}"},
    ))

    macro("Mac105_Compat_home_install", (
      {"default": "${Mac105_Compat_root}/${CMTCONFIG}"},
    ))

    macro("Mac105_Compat_bin", (
      {"default": ""},
      {("host-mac106", "target-mac105"): "${Mac105_Compat_home_install}/bin"},
    ))

    macro("Mac105_Compat_lib", (
      {"default": ""},
      {("host-mac106", "target-mac105"): "${Mac105_Compat_home_install}/lib"},
    ))

    ctx.hwaf_path_remove("PATH", (
      {"default": "/mac105compat/"},
    ))

    ctx.hwaf_path_prepend("PATH", (
      {"default": ""},
      {("host-mac106", "target-mac105"): "${Mac105_Compat_bin}"},
    ))

    ctx.hwaf_path_remove("LD_LIBRARY_PATH", (
      {"default": "/mac105compat/"},
    ))

    ctx.hwaf_path_prepend("LD_LIBRARY_PATH", (
      {"default": ""},
      {("host-mac106", "target-mac105"): "${Mac105_Compat_lib}"},
    ))

    ctx.hwaf_path_remove("DYLD_LIBRARY_PATH", (
      {"default": "/mac105compat/"},
    ))

    ctx.hwaf_path_prepend("DYLD_LIBRARY_PATH", (
      {"default": ""},
      {("host-mac106", "target-mac105"): "${Mac105_Compat_lib}"},
    ))

    macro("Mac105_Compat_export_paths", (
      {"default": ""},
      {"i386-mac105-gcc40-dbg": "${Mac105_Compat_home}"},
      {"i386-mac105-gcc40-opt": "${Mac105_Compat_home}"},
    ))

    macro("Mac105_Compat_install_cmd", (
      {"default": ["${library_install_command}", "${Mac105_Compat_home}", "${Mac105_Compat_home_install}"]},
    ))

    ctx.hwaf_macro_append("all_dependencies", (
      {"default": ""},
      {"i386-mac105-gcc40-dbg": "Mac105_Compat_install_action"},
      {"i386-mac105-gcc40-opt": "Mac105_Compat_install_action"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
