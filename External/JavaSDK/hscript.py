## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/JavaSDK",
    "authors": ["Julius Hrivnac <Julius.Hrivnac@cern.ch@cern.ch>",
                "Chriatian Arnault <arnault@lal.in2p3.fr>",
                ],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/CERNJavaInstallation", version="CERNJavaInstallation-01-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("JDK_ARCH", (
      {"default": "ia32"},
      {"64": "amd64"},
      {"Darwin": "Darwin"},
    ))

    macro("JDK_HOME", "${JAVA_BASE}/JDK/1.6.0/${JDK_ARCH}")
    ctx.hwaf_declare_runtime_env("JDK_HOME")

    macro("JAVA_HOME", (
        {"default":       "${JDK_HOME}"},
        {"target-mac106": ""},
    ))
    ctx.hwaf_declare_runtime_env("JAVA_HOME")

    macro("_JAVA_OPTIONS", (
        {"default": ["-Xms64m","-Xmx128m"]},
    ))
    ctx.hwaf_declare_runtime_env("_JAVA_OPTIONS")
    
    ctx.hwaf_path_remove("PATH", (
      {"default": "/JDK"},
    ))

    ctx.hwaf_path_append("PATH", (
      {"default": "${JDK_HOME}/jre/bin"},
      {"noJava": ""},
    ))

    ctx.hwaf_path_append("PATH", (
      {"default": "${JDK_HOME}/bin"},
      {"noJava": ""},
    ))

    macro("JavaSDK_export_paths", (
      {"default": "${JDK_HOME}"},
    ))

    macro("JavaSDK_native_version", (
      {"default": "1.6.0"},
    ))

    macro("JavaSDK_platform", (
      {"default": ""},
      {"PACK": "${JDK_ARCH}"},
    ))

    macro("INCLUDES_JavaSDK", (
      {"target-linux":  ["${JDK_HOME}/include", "${JDK_HOME}/include/linux"]},
    ))


    # now load java tools
    #import os
    #os.environ['JAVA_HOME'] = ctx.env.get_flat("JAVA_HOME")
    #ctx.load("java")
    ctx.load("find_java")
    ctx.find_java(path_list=ctx.hwaf_subst_vars("${JDK_HOME}/bin"))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{install_docs []})
    
    
    return # build

## EOF ##
