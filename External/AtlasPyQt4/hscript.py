## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasPyQt4",
    "authors": ["Sebastien Binet <binet@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
    ctx.use_pkg("LCG_Interfaces/pygraphics", version="v*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    ctx.use_pkg("External/AtlasQt4", version="AtlasQt4-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{PyQt4_native_version [{default [${pyqt_config_version}]}]}}
    ctx.hwaf_declare_macro("PyQt4_native_version", (
      {"default": "${pyqt_config_version}"},
    ))
    #### macro &{{PyQt4_home [{default [${pygraphics_home}]}]}}
    ctx.hwaf_declare_macro("PyQt4_home", (
      {"default": "${pygraphics_home}"},
    ))
    #### macro &{{pyqt4_ext_pylib [{default [${pygraphics_home}/lib/python${Python_version}/site-packages]}]}}
    ctx.hwaf_declare_macro("pyqt4_ext_pylib", (
      {"default": "${pygraphics_home}/lib/python${Python_version}/site-packages"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    ctx(
        features = "atlas_generic_install",
        name     = "AtlasPyQt4-generic-install-pygraphics_binaries-binaries",
        target   = "AtlasPyQt4-generic-install-pygraphics_binaries-binaries",
        source   = ["'-s=$(pygraphics_home)/bin *"],
        install_prefix = ["$(CMTCONFIG)/bin"],
    )
    
    ctx(
        features = "atlas_generic_install",
        name     = "AtlasPyQt4-generic-install-pygraphics_pymodule-python_modules",
        target   = "AtlasPyQt4-generic-install-pygraphics_pymodule-python_modules",
        source   = ["'-s=$(pyqt4_ext_pylib) * *.py *.so"],
        install_prefix = ["$(CMTCONFIG)/lib/python$(Python_version)"],
    )
    return # build

## EOF ##
