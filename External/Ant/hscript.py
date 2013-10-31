## -*- python -*-
## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/Ant",
    "authors": ["Julius Hrivnac <Julius.Hrivnac@cern.ch>"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/JavaSDK", version="JavaSDK-01-*", public=True)
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-00-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):

    macro = ctx.hwaf_declare_macro
    
    macro("ANT_VERSION", (
      {"default": "1.7.0"},
    ))

    macro("ANT_HOME", "${JAVA_BASE}/Ant/${ANT_VERSION}/share")
    ctx.hwaf_declare_runtime_env("ANT_HOME")
    
    ctx.hwaf_path_remove("PATH", (
      {"default": "Ant"},
    ))

    ctx.hwaf_path_prepend("PATH", (
      {"default": "${ANT_HOME}/bin"},
      {"noJava": ""},
    ))

    macro("ANT_SITE", "CMT")
    ctx.hwaf_declare_runtime_env("ANT_SITE")
    
    ##### **** statement *hlib.MakeFragmentStmt (&{ant})
    ##### **** statement *hlib.PatternStmt (&{ant_jar_and_doc document ant jar ../ant/build.xml anttarget=jar ; document ant doc ../ant/build.xml anttarget=doc ; macro <package>.core ${<PACKAGE>ROOT}/lib/<package>.jar ; document installer install_jars ${<PACKAGE>ROOT}/lib/*.jar install_dir="$(CMTINSTALLAREA)/share/lib ; document installdoc install_docs ../doc})
    #### macro &{{Ant_export_paths [{default [${ANT_HOME}]}]}}
    ctx.hwaf_declare_macro("Ant_export_paths", (
      {"default": "${ANT_HOME}"},
    ))
    #### macro &{{Ant_native_version [{default [${ANT_VERSION}]}]}}
    ctx.hwaf_declare_macro("Ant_native_version", (
      {"default": "${ANT_VERSION}"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{install_docs []})
    
    
    return # build

## EOF ##
