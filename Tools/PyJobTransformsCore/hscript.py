## -*- python -*-
## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "Tools/PyJobTransformsCore",
    "authors": ["Alvin Tan <clat@hep.ph.bham.ac.uk>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{trfs_dir [{default [../scripts]}]}}
    ctx.hwaf_declare_macro("trfs_dir", (
      {"default": "../scripts"},
    ))
    #### macro &{{expand_files_cmd [{default [expand_files.py]}]}}
    ctx.hwaf_declare_macro("expand_files_cmd", (
      {"default": "expand_files.py"},
    ))
    ##### **** statement *hlib.PatternStmt (&{declare_jobtransforms private ; apply_pattern generic_declare_for_link kind=trfs_exe files='-s=${trfs_dir} <trfs> prefix=share/bin ; apply_pattern generic_declare_for_link kind=trfs_pyt files='-s=${trfs_dir} <trfs> prefix=python/<package> ; apply_pattern generic_declare_for_link kind=trfs_jop files='-s=../share <jo> prefix=jobOptions/<package> ; macro <package>_jobtransforms `${expand_files_cmd} -r=$(<PACKAGE>ROOT) -d=<package> -s=${trfs_dir} <trfs>` ; apply_pattern install_python_init ; macro_append <package>_python_init_dependencies install_trfs_pyt ; end_private ; macro_append all_jobtransforms ${<package>_jobtransforms}})
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    ctx(
        features = "atlas_generic_install",
        name     = "PyJobTransformsCore-generic-install-trf-runtime",
        target   = "PyJobTransformsCore-generic-install-trf-runtime",
        source   = ["share/*.db"],
        install_prefix = ["share"],
    )
    
    ctx(
        features = "atlas_install_python_modules",
        name     = "PyJobTransformsCore-install-py",
        target   = "PyJobTransformsCore-install-py",
        source   = ["python/*.py"],
    )
    
    ctx(
        features = "atlas_install_scripts",
        name     = "PyJobTransformsCore-install-scripts",
        target   = "PyJobTransformsCore-install-scripts",
        source   = ["scripts/*"],
    )
    return # build

## EOF ##
