## -*- python -*-
## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "taginfo",
    "authors": ["Fulachier <jerome.fulachier@isn.in2p3.fr>", "Albrand <albrand@isn.in2p3.fr>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/JavaSDK", version="JavaSDK-01-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
        
    ##### **** statement *hlib.MakeFragmentStmt (&{java_header})

    macro = ctx.hwaf_declare_macro
    
    macro("javacomp", (
      {"default": ["javac", "-J-Xmx32m", "-J-XX:ReservedCodeCacheSize=128m", "-classpath", "${src}:${CLASSPATH}"]},
    ))

    macro("jar", (
      {"default": ["jar", "-J-Xmx32m", "-J-XX:ReservedCodeCacheSize=128m"]},
    ))

    ctx.hwaf_path_append("CLASSPATH", "${INSTALL_AREA}/share/lib/taginfo.jar")
    
    ctx.hwaf_declare_runtime_alias("taginfo", (
      {"default": ["java", "-Xms64m", "-Xmx384m", "-Dhttp_proxy=${http_proxy}", "-cp", "${INSTALL_AREA}/lib/taginfo.jar", "taginfo"]},
      {"STANDALONE": ["java", "-Xms64m", "-Xmx384m", "-Dhttp_proxy=${http_proxy}", "-cp", "${taginfo_cmtpath}/InstallArea/share/lib/taginfo.jar"]},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    ctx(
        #features = "atlas_application javac",
        features = "javac jar",
        name     = "taginfo",
        #source   = ["taginfo.java"],
        srcdir = "src",
        outdir = "${INSTALL_AREA}/lib",
        classpath = ["src", "classes"],
    )
    return # build

## EOF ##
