## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasDBRelease",
    "authors": [],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
    ## FIXME
    #ctx.use_pkg("DBRelease", version="", public=True)
    #ctx.use_pkg("$(useDBRelease_use)", version="", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{AtlasDBRelease_default_version [{default [23.2.1]}]}}
    ctx.hwaf_declare_macro("AtlasDBRelease_default_version", (
      {"default": "23.2.1"},
    ))
    #### macro &{{printenvdefault [{default [${AtlasDBRelease_root}/cmt/printenvdefault]}]}}
    ctx.hwaf_declare_macro("printenvdefault", (
      {"default": "${AtlasDBRelease_root}/cmt/printenvdefault"},
    ))
    #### macro &{{AtlasDBRelease_native_version [{default [`${printenvdefault} DBRELEASE_OVERRIDE current`]} {PACK [${AtlasDBRelease_default_version}]}]}}
    ctx.hwaf_declare_macro("AtlasDBRelease_native_version", (
      {"default": ["`${printenvdefault}", "DBRELEASE_OVERRIDE", "current`"]},
      {"PACK": "${AtlasDBRelease_default_version}"},
    ))
    ##### **** statement *hlib.SetStmt (&{{DBRELEASE_REQUESTED [{default [${AtlasDBRelease_native_version}]} {useDBRelease [${AtlasDBRelease_native_version}]} {noDBRelease []} {CERN []}]}})
    ##### **** statement *hlib.SetStmt (&{{DBRELEASE_REQUIRED [{default [${AtlasDBRelease_default_version}]} {useDBRelease [${AtlasDBRelease_default_version}]} {noDBRelease []} {CERN []}]}})
    #### macro &{{AtlasDBRelease_default_base [{default [${SITEROOT}]} {BNL [/afs/usatlas/project/database]}]}}
    ctx.hwaf_declare_macro("AtlasDBRelease_default_base", (
      {"default": "${SITEROOT}"},
      {"BNL": "/afs/usatlas/project/database"},
    ))
    #### macro &{{AtlasDBRelease_base [{default [`${printenvdefault} ATLAS_DB_AREA ${AtlasDBRelease_default_base}`]}]}}
    ctx.hwaf_declare_macro("AtlasDBRelease_base", (
      {"default": ["`${printenvdefault}", "ATLAS_DB_AREA", "${AtlasDBRelease_default_base}`"]},
    ))
    #### macro &{{AtlasDBRelease_home [{default [${AtlasDBRelease_base}/DBRelease/${AtlasDBRelease_native_version}]}]}}
    ctx.hwaf_declare_macro("AtlasDBRelease_home", (
      {"default": "${AtlasDBRelease_base}/DBRelease/${AtlasDBRelease_native_version}"},
    ))
    #### macro &{{useDBRelease_statement [{default [DBRelease ${AtlasDBRelease_native_version} ${AtlasDBRelease_base}]}]}}
    ctx.hwaf_declare_macro("useDBRelease_statement", (
      {"default": ["DBRelease", "${AtlasDBRelease_native_version}", "${AtlasDBRelease_base}"]},
    ))
    #### macro &{{useDBRelease_use [{default []} {useDBRelease [${useDBRelease_statement}]} {noDBRelease []} {STANDALONE [${useDBRelease_statement}]} {BNL [${useDBRelease_statement}]}]}}
    ctx.hwaf_declare_macro("useDBRelease_use", (
      {"default": ""},
      {"useDBRelease": "${useDBRelease_statement}"},
      {"noDBRelease": ""},
      {"STANDALONE": "${useDBRelease_statement}"},
      {"BNL": "${useDBRelease_statement}"},
    ))
    #### macro &{{AtlasDBRelease_requires [{default [http://atlas.web.cern.ch/Atlas/GROUPS/DATABASE/pacman4/DBRelease:DBRelease-${AtlasDBRelease_default_version}]}]}}
    ctx.hwaf_declare_macro("AtlasDBRelease_requires", (
      {"default": "http://atlas.web.cern.ch/Atlas/GROUPS/DATABASE/pacman4/DBRelease:DBRelease-${AtlasDBRelease_default_version}"},
    ))
    #### macro &{{AtlasDBRelease_TestConfiguration [{default [../test/AtlasDBRelease_TestConfiguration.xml]}]}}
    ctx.hwaf_declare_macro("AtlasDBRelease_TestConfiguration", (
      {"default": "../test/AtlasDBRelease_TestConfiguration.xml"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{declare_scripts [files="*.sh]})
    ##### **** statement *hlib.ApplyPatternStmt (&{declare_runtime_extras [extras="../test/AtlasDBRelease_TestConfiguration.xml]})
    
    
    return # build

## EOF ##
