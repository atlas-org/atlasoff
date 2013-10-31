## -*- python -*-
## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "Control/HeapMon",
    "authors": ["Mous Tatarkhanov <tmmous@berkeley.edu>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    ctx.use_pkg("External/AtlasTCMalloc", version="AtlasTCMalloc-*", public=True)
    
    ## private dependencies
    ctx.use_pkg("External/AtlasROOT", version="AtlasROOT-*", private=True)
    
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{python_extension_fragment [{default []} {Linux [python_extension -dependencies -header=python_extension_header]} {Darwin [python_extension -dependencies -header=python_extension_header]}]}}
    ctx.hwaf_declare_macro("python_extension_fragment", (
      {"default": ""},
      {"Linux": ["python_extension", "-dependencies", "-header=python_extension_header"]},
      {"Darwin": ["python_extension", "-dependencies", "-header=python_extension_header"]},
    ))
    ##### **** statement *hlib.MakeFragmentStmt (&{$(python_extension_fragment)})
    #### macro_append &{{MemoryMarker_dependencies [{default [install_includes]}]}}
    ctx.hwaf_macro_append("MemoryMarker_dependencies", (
      {"default": "install_includes"},
    ))
    #### macro_append &{{MemoryMarker_linkopts [{default []} {use_bfd [-aarchive -L/usr/local/lib -L/usr/lib -lbfd -liberty]}]}}
    ctx.hwaf_macro_append("MemoryMarker_linkopts", (
      {"default": ""},
      {"use_bfd": ["-aarchive", "-L/usr/local/lib", "-L/usr/lib", "-lbfd", "-liberty"]},
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
    #### macro_append &{{cflags [{default [-O3]}]}}
    ctx.hwaf_macro_append("cflags", (
      {"default": "-O3"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.DocumentStmt (&{python_extension [MemoryMarker files="*.c MemoryMarker.c]})
    
    ctx(
        features = "atlas_install_python_modules",
        name     = "HeapMon-install-py",
        target   = "HeapMon-install-py",
        source   = ["python/*.py"],
    )
    
    ctx(
        features = "atlas_application",
        name     = "MemoryScanner",
        target   = "MemoryScanner",
        source   = ["src/MemoryScanner.cxx"],
        use      = ["ROOT"],
    )
    return # build

## EOF ##
