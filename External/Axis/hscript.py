## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/Axis",
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
    
    
    
    #### set &{{AXIS_VERSION [{default [1.4]}]}}
    ctx.hwaf_declare_macro("AXIS_VERSION", (
      {"default": "1.4"},
    ))
    ctx.hwaf_declare_runtime_env("AXIS_VERSION")
    #### set &{{AXIS_HOME [{default [${JAVA_BASE}/axis/${AXIS_VERSION}/share]}]}}
    ctx.hwaf_declare_macro("AXIS_HOME", (
      {"default": "${JAVA_BASE}/axis/${AXIS_VERSION}/share"},
    ))
    ctx.hwaf_declare_runtime_env("AXIS_HOME")
    #### macro &{{AXIS.core [{default [${AXIS_HOME}/lib/axis.jar]}]}}
    ctx.hwaf_declare_macro("AXIS.core", (
      {"default": "${AXIS_HOME}/lib/axis.jar"},
    ))
    #### macro &{{AXIS.ant [{default [${AXIS_HOME}/lib/axis-ant.jar]}]}}
    ctx.hwaf_declare_macro("AXIS.ant", (
      {"default": "${AXIS_HOME}/lib/axis-ant.jar"},
    ))
    #### macro &{{AXIS.jaxrpc [{default [${AXIS_HOME}/lib/jaxrpc.jar]}]}}
    ctx.hwaf_declare_macro("AXIS.jaxrpc", (
      {"default": "${AXIS_HOME}/lib/jaxrpc.jar"},
    ))
    #### macro &{{AXIS.logging [{default [${AXIS_HOME}/lib/commons-logging-1.0.4.jar]}]}}
    ctx.hwaf_declare_macro("AXIS.logging", (
      {"default": "${AXIS_HOME}/lib/commons-logging-1.0.4.jar"},
    ))
    #### macro &{{AXIS.discovery [{default [${AXIS_HOME}/lib/commons-discovery-0.2.jar]}]}}
    ctx.hwaf_declare_macro("AXIS.discovery", (
      {"default": "${AXIS_HOME}/lib/commons-discovery-0.2.jar"},
    ))
    #### macro &{{AXIS.saaj [{default [${AXIS_HOME}/lib/saaj.jar]}]}}
    ctx.hwaf_declare_macro("AXIS.saaj", (
      {"default": "${AXIS_HOME}/lib/saaj.jar"},
    ))
    #### macro &{{AXIS.wsdl4j [{default [${AXIS_HOME}/lib/wsdl4j-1.5.1.jar]}]}}
    ctx.hwaf_declare_macro("AXIS.wsdl4j", (
      {"default": "${AXIS_HOME}/lib/wsdl4j-1.5.1.jar"},
    ))
    #### macro &{{AXIS.log4j [{default [${AXIS_HOME}/lib/log4j-1.2.8.jar]}]}}
    ctx.hwaf_declare_macro("AXIS.log4j", (
      {"default": "${AXIS_HOME}/lib/log4j-1.2.8.jar"},
    ))
    #### macro &{{Axis_export_paths [{default [${AXIS_HOME}]}]}}
    ctx.hwaf_declare_macro("Axis_export_paths", (
      {"default": "${AXIS_HOME}"},
    ))
    #### macro &{{Axis_native_version [{default [${AXIS_VERSION}]}]}}
    ctx.hwaf_declare_macro("Axis_native_version", (
      {"default": "${AXIS_VERSION}"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.DocumentStmt (&{installer [install_jars ${AXIS.core} ${AXIS.ant} ${AXIS.jaxrpc} ${AXIS.logging} ${AXIS.discovery} ${AXIS.saaj} ${AXIS.wsdl4j} ${AXIS.log4j} install_dir="$(CMTINSTALLAREA)/share/lib]})
    ##### **** statement *hlib.ApplyPatternStmt (&{install_docs []})
    
    
    return # build

## EOF ##
