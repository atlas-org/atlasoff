## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasGdb",
    "authors": ["ATLAS Software Librarian <ATLAS-Software.Librarian@cern.ch>"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="*", public=True)
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-*", public=True)
    ctx.use_pkg("External/AtlasBzip2")
    ctx.use_pkg("External/AtlasPython")
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro

    macro("AtlasGdb_home", "${ATLAS_EXTERNAL}/gdb/${AtlasGdb_native_version}/${CMTCONFIG}")
    macro("AtlasGdb_native_version", "7.4.1")

    macro("AtlasGdb_incdir", "${AtlasGdb_home}/include")
    macro("AtlasGdb_libdir", "${AtlasGdb_home}/lib")

    macro("INCLUDES_AtlasGdb", "${AtlasGdb_incdir}")
    # FIXME lib,lib64 and static libs...
    macro("LIBPATH_AtlasGdb",  "${AtlasGdb_libdir}")
    macro("LIB_AtlasGdb",     (
        {"default": ["bfd", "iberty", "z"]},
    ))

    macro("AtlasGdb_export_paths", (
        {"default": ["${AtlasGdb_incdir}",
                     "${AtlasGdb_libdir}",
                     ]},
    ))

    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    ctx(
        name="AtlasGdb-install-py",
        features= "atlas_install_python_modules",
    )

    ctx(
        name="AtlasGdb-install-scripts",
        features= "atlas_install_scripts",
        source="share/atlasAddress2Line",
    )

    ctx(
        name="resolveAtlasAddr2Line",
        features= "atlas_application",
        source=   "app/resolveAtlasAddr2Line.cpp",
        use=      ["AtlasGdb"],
    )
    
    return # build

## EOF ##
