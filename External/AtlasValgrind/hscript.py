## -*- python -*-
## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasValgrind",
    "authors": ["Sebastien Binet <binet@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Settings", version="v*", public=True)
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
    
    macro("AtlasValgrind_native_version", "3.8.0")

    macro("AtlasValgrind_version", (
      {"default": "3.8"},
      {"WIN32":    "38"},
    ))

    macro("AtlasValgrind_basesystem", (
      {"default": "${LCG_basesystem}"},
      {("host-i686", "host-slc5", "target-gcc41"): "i686-slc5-gcc41"},
      {("host-i686", "host-slc5", "target-gcc43"): "i686-slc5-gcc43"},
      {("host-i686", "host-slc5", "target-gcc44"): "i686-slc5-gcc44"},
      {("host-i686", "host-slc5", "target-gcc45"): "i686-slc5-gcc45"},
      {("host-x86_64", "host-slc5", "target-gcc41"): "x86_64-slc5-gcc41"},
      {("host-x86_64", "host-slc5", "target-gcc43"): "x86_64-slc5-gcc43"},
      {("host-x86_64", "host-slc5", "target-gcc44"): "x86_64-slc5-gcc44"},
      {("host-x86_64", "host-slc5", "target-gcc45"): "x86_64-slc5-gcc45"},
    ))

    macro("AtlasValgrind_system", (
      {"default": "${AtlasValgrind_basesystem}-opt"},
      {"target-opt": "${AtlasValgrind_basesystem}-opt"},
      {"target-dbg": "${AtlasValgrind_basesystem}-opt"},
    ))

    macro("AtlasValgrind_home", 
          "${LCG_external}/valgrind/${AtlasValgrind_native_version}/${AtlasValgrind_system}"
    )

    macro("AtlasValgrind_bindir", "${AtlasValgrind_home}/bin")
    macro("AtlasValgrind_incdir", "${AtlasValgrind_home}/include")
    macro("AtlasValgrind_libdir", "${AtlasValgrind_home}/lib/valgrind")

    macro("AtlasValgrind_export_paths", "${AtlasValgrind_home}")
    
    ctx.hwaf_path_remove("LD_LIBRARY_PATH", (
      {"default": "/valgrind/"},
      {"WIN32": "\\valgrind"},
    ))

    ctx.hwaf_path_prepend("LD_LIBRARY_PATH", (
      {"default": "${AtlasValgrind_libdir}"},
      {"WIN32":   ""},
    ))

    ctx.hwaf_path_remove("PATH", (
      {"default": "/valgrind/"},
      {"WIN32":   "\\valgrind"},
    ))

    ctx.hwaf_path_prepend("PATH", "${AtlasValgrind_bindir}")
    
    macro("LIB_valgrind",      (
        {"build_Valgrind_tool": "coregrind"},
    ))
    macro("LIBPATH_valgrind",  "${AtlasValgrind_libdir}")
    macro("INCLUDES_valgrind", "${AtlasValgrind_incdir}")
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{declare_runtime [files="*.supp]})
    
    
    return # build

## EOF ##
