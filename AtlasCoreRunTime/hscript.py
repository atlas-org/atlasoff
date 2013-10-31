## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "AtlasCoreRunTime",
    "authors": ["David Quarrie <David.Quarrie@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("Control/MinimalRunTime", version="MinimalRunTime-*", public=True)
    ctx.use_pkg("External/Ant", version="", public=True)
    ctx.use_pkg("External/AtlasAIDA", version="AtlasAIDA-*", public=True)
    ctx.use_pkg("External/AtlasBoost", version="AtlasBoost-*", public=True)
    ctx.use_pkg("External/AtlasCLHEP", version="AtlasCLHEP-*", public=True)
    ctx.use_pkg("External/AtlasCOOL", version="AtlasCOOL-*", public=True)
    ctx.use_pkg("External/AtlasCORAL", version="AtlasCORAL-*", public=True)
    ctx.use_pkg("External/AtlasCppUnit", version="AtlasCppUnit-*", public=True)
    ctx.use_pkg("External/AtlasDBRelease", version="AtlasDBRelease-*", public=True)
    ctx.use_pkg("External/AtlasDataArea", version="AtlasDataArea-*", public=True)
    ctx.use_pkg("External/AtlasExpat", version="AtlasExpat-*", public=True)
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-*", public=True)
    ctx.use_pkg("External/AtlasGSL", version="AtlasGSL-*", public=True)
    ctx.use_pkg("External/AtlasMagField", version="AtlasMagField-*", public=True)
    ctx.use_pkg("External/AtlasMatplotlib", version="AtlasMatplotlib-*", public=True)
    ctx.use_pkg("External/AtlasMKL", version="AtlasMKL-*", public=True)
    ctx.use_pkg("External/AtlasOracle", version="AtlasOracle-*", public=True)
    ctx.use_pkg("External/AtlasPOOL", version="AtlasPOOL-*", public=True)
    ctx.use_pkg("External/AtlasPyROOT", version="AtlasPyROOT-*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    ctx.use_pkg("External/AtlasRELAX", version="AtlasRELAX-*", public=True)
    ctx.use_pkg("External/AtlasROOT", version="AtlasROOT-*", public=True)
    ctx.use_pkg("External/AtlasReflex", version="AtlasReflex-*", public=True)
    ctx.use_pkg("External/AtlasSQLite", version="AtlasSQLite-*", public=True)
    ctx.use_pkg("External/AtlasValgrind", version="AtlasValgrind-*", public=True)
    ctx.use_pkg("External/Axis", version="", public=True)
    ctx.use_pkg("External/CERNJavaInstallation", version="", public=True)
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
    ctx.use_pkg("External/GaudiInterface", version="GaudiInterface-*", public=True)
    ctx.use_pkg("External/JavaSDK", version="", public=True)
    ctx.use_pkg("External/MMMySQL", version="", public=True)
    ctx.use_pkg("External/MySQL", version="MySQL-*", public=True)
    ## FIXME: should this be External/pyAMI ??
    #ctx.use_pkg("Database/Bookkeeping/AMIClients/pyAMI", version="pyAMI-*", public=True)
    ## FIXME
    #ctx.use_pkg("External/SLC4_Compat", version="SLC4_Compat-*", public=True)
    #ctx.use_pkg("External/SLC5_Compat", version="SLC5_Compat-*", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("Control/MinimalRunTime", version="MinimalRunTime-*", runtime=True)
    ctx.use_pkg("External/AtlasAIDA", version="AtlasAIDA-*", runtime=True)
    ctx.use_pkg("External/AtlasBoost", version="AtlasBoost-*", runtime=True)
    ctx.use_pkg("External/AtlasCLHEP", version="AtlasCLHEP-*", runtime=True)
    ctx.use_pkg("External/AtlasCOOL", version="AtlasCOOL-*", runtime=True)
    ctx.use_pkg("External/AtlasCORAL", version="AtlasCORAL-*", runtime=True)
    ctx.use_pkg("External/AtlasCppUnit", version="AtlasCppUnit-*", runtime=True)
    ctx.use_pkg("External/AtlasDBRelease", version="AtlasDBRelease-*", runtime=True)
    ctx.use_pkg("External/AtlasDataArea", version="AtlasDataArea-*", runtime=True)
    ctx.use_pkg("External/AtlasExpat", version="AtlasExpat-*", runtime=True)
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-*", runtime=True)
    ctx.use_pkg("External/AtlasGSL", version="AtlasGSL-*", runtime=True)
    ctx.use_pkg("External/AtlasMagField", version="AtlasMagField-*", runtime=True)
    ctx.use_pkg("External/AtlasMatplotlib", version="AtlasMatplotlib-*", runtime=True)
    ctx.use_pkg("External/AtlasMKL", version="AtlasMKL-*", runtime=True)
    ctx.use_pkg("External/AtlasOracle", version="AtlasOracle-*", runtime=True)
    ctx.use_pkg("External/AtlasPOOL", version="AtlasPOOL-*", runtime=True)
    ctx.use_pkg("External/AtlasPyROOT", version="AtlasPyROOT-*", runtime=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", runtime=True)
    ctx.use_pkg("External/AtlasRELAX", version="AtlasRELAX-*", runtime=True)
    ctx.use_pkg("External/AtlasROOT", version="AtlasROOT-*", runtime=True)
    ctx.use_pkg("External/AtlasReflex", version="AtlasReflex-*", runtime=True)
    ctx.use_pkg("External/AtlasSQLite", version="AtlasSQLite-*", runtime=True)
    ctx.use_pkg("External/AtlasValgrind", version="AtlasValgrind-*", runtime=True)
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", runtime=True)
    ctx.use_pkg("External/GaudiInterface", version="GaudiInterface-*", runtime=True)
    ctx.use_pkg("External/MySQL", version="MySQL-*", runtime=True)
    ## FIXME: should this be External/pyAMI ??
    #ctx.use_pkg("Database/Bookkeeping/AMIClients/pyAMI", version="pyAMI-*", runtime=True)
    ## FIXME
    #ctx.use_pkg("External/SLC4_Compat", version="SLC4_Compat-*", runtime=True)
    #ctx.use_pkg("External/SLC5_Compat", version="SLC5_Compat-*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{use_Ant [{default [Ant Ant-* External -no_auto_imports]} {noJava []}]}}
    ctx.hwaf_declare_macro("use_Ant", (
      {"default": ["Ant", "Ant-*", "External", "-no_auto_imports"]},
      {"noJava": ""},
    ))
    #### macro &{{use_Axis [{default [Axis Axis-* External -no_auto_imports]} {noJava []}]}}
    ctx.hwaf_declare_macro("use_Axis", (
      {"default": ["Axis", "Axis-*", "External", "-no_auto_imports"]},
      {"noJava": ""},
    ))
    #### macro &{{use_CERNJava [{default [CERNJavaInstallation CERNJavaInstallation-* External -no_auto_imports]} {noJava []}]}}
    ctx.hwaf_declare_macro("use_CERNJava", (
      {"default": ["CERNJavaInstallation", "CERNJavaInstallation-*", "External", "-no_auto_imports"]},
      {"noJava": ""},
    ))
    #### macro &{{use_JavaSDK [{default [JavaSDK JavaSDK-* External -no_auto_imports]} {noJava []}]}}
    ctx.hwaf_declare_macro("use_JavaSDK", (
      {"default": ["JavaSDK", "JavaSDK-*", "External", "-no_auto_imports"]},
      {"noJava": ""},
    ))
    #### macro &{{use_MMMySQL [{default [MMMySQL MMMySQL-* External -no_auto_imports]} {noJava []}]}}
    ctx.hwaf_declare_macro("use_MMMySQL", (
      {"default": ["MMMySQL", "MMMySQL-*", "External", "-no_auto_imports"]},
      {"noJava": ""},
    ))
    #### macro &{{atlascore_path [{default []} {slim [${EXTERNALPOLICYROOT}/cmt/cmt_slim_path]}]}}
    ctx.hwaf_declare_macro("atlascore_path", (
      {"default": ""},
      {"slim": "${EXTERNALPOLICYROOT}/cmt/cmt_slim_path"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
