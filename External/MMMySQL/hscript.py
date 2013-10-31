## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/MMMySQL",
    "authors": ["Julius Hrivnac <Julius.Hrivnac@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/JavaSDK", version="JavaSDK-01-*", public=True)
    ctx.use_pkg("External/AtlasExternalArea", version="AtlasExternalArea-00-*", public=True)
    ctx.use_pkg("External/Ant", version="Ant-00-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{MMMYSQL_VERSION [{default [5.0.5]}]}}
    ctx.hwaf_declare_macro("MMMYSQL_VERSION", (
      {"default": "5.0.5"},
    ))
    #### macro &{{MMMYSQL_HOME [{default [${JAVA_BASE}/mysql-connector/${MMMYSQL_VERSION}/share]}]}}
    ctx.hwaf_declare_macro("MMMYSQL_HOME", (
      {"default": "${JAVA_BASE}/mysql-connector/${MMMYSQL_VERSION}/share"},
    ))
    #### macro &{{MMMySQL.core [{default [${MMMYSQL_HOME}/mysql-connector-java-${MMMYSQL_VERSION}-bin.jar]}]}}
    ctx.hwaf_declare_macro("MMMySQL.core", (
      {"default": "${MMMYSQL_HOME}/mysql-connector-java-${MMMYSQL_VERSION}-bin.jar"},
    ))
    #### macro &{{MMMySQL_export_paths [{default [${MMMYSQL_HOME}]}]}}
    ctx.hwaf_declare_macro("MMMySQL_export_paths", (
      {"default": "${MMMYSQL_HOME}"},
    ))
    #### macro &{{MMMySQL_native_version [{default [${MMMYSQL_VERSION}]}]}}
    ctx.hwaf_declare_macro("MMMySQL_native_version", (
      {"default": "${MMMYSQL_VERSION}"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.DocumentStmt (&{installer [install_jars ${MMMySQL.core} install_dir="$(CMTINSTALLAREA)/share/lib]})
    ##### **** statement *hlib.ApplyPatternStmt (&{install_docs []})
    
    
    return # build

## EOF ##
