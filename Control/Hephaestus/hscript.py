## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "Control/Hephaestus",
    "authors": ["Wim Lavrijsen <WLavrijsen@lbl.gov>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    ctx.use_pkg("External/AtlasLibUnwind", version="AtlasLibUnwind-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{python_extension_fragment [{default []} {Linux [python_extension -dependencies -header=python_extension_header]}]}}
    ctx.hwaf_declare_macro("python_extension_fragment", (
      {"default": ""},
      {"Linux": ["python_extension", "-dependencies", "-header=python_extension_header"]},
    ))
    ##### **** statement *hlib.MakeFragmentStmt (&{$(python_extension_fragment)})
    #### macro_append &{{MemoryTracker_dependencies [{default [install_includes]}]}}
    ctx.hwaf_macro_append("MemoryTracker_dependencies", (
      {"default": "install_includes"},
    ))
    #### macro_append &{{MemoryTracker_linkopts [{default [-lpthread ${AtlasLibUnwind_linkopts}]} {use_bfd [-aarchive -L/usr/local/lib -L/usr/lib -lbfd -liberty -lpthread]}]}}
    ctx.hwaf_macro_append("MemoryTracker_linkopts", (
      {"default": ["-lpthread", "${AtlasLibUnwind_linkopts}"]},
      {"use_bfd": ["-aarchive", "-L/usr/local/lib", "-L/usr/lib", "-lbfd", "-liberty", "-lpthread"]},
    ))
    #### macro_append &{{cflags [{default []} {use_bfd [-DHEPHAESTUS_USE_BFD]}]}}
    ctx.hwaf_macro_append("cflags", (
      {"default": ""},
      {"use_bfd": "-DHEPHAESTUS_USE_BFD"},
    ))
    #### macro_append &{{cppflags [{default [-fuse-cxa-atexit]}]}}
    ctx.hwaf_macro_append("cppflags", (
      {"default": "-fuse-cxa-atexit"},
    ))
    #### macro_append &{{cflags [{default [-O3 -Wno-deprecated-declarations -Wno-format-security]}]}}
    ctx.hwaf_macro_append("cflags", (
      {"default": ["-O3", "-Wno-deprecated-declarations", "-Wno-format-security"]},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.DocumentStmt (&{python_extension [MemoryTracker files="*.c HashTable.c]})
    
    ctx(
        features = "atlas_install_python_modules",
        name     = "Hephaestus-install-py",
        target   = "Hephaestus-install-py",
        source   = ["python/*.py"],
    )
    
    ctx(
        features = "atlas_application",
        name     = "hephprof",
        target   = "hephprof",
        source   = ["src/HephProf/HephProf.cxx"],
    )
    return # build

## EOF ##
