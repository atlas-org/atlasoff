## -*- python -*-
## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasQt4",
    "authors": ["Sebastien Binet <binet@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
    ctx.use_pkg("LCG_Interfaces/Qt", version="*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    macro = ctx.hwaf_declare_macro
    
    macro("AtlasQt4_native_version", "${Qt_native_version}")
    macro("AtlasQt4_home",           "${Qt_home}")

    macro("Qt4_native_version",      "${AtlasQt4_native_version}")
    macro("Qt4_home",                "${AtlasQt4_home}")

    ctx.hwaf_path_remove("DYLD_LIBRARY_PATH", (
      {"default": "/qt/4"},
    ))

    ctx.hwaf_path_prepend("DYLD_LIBRARY_PATH", (
      {"default": "${AtlasQt4_home}/lib"},
    ))

    ctx.hwaf_path_remove("PATH", (
      {"default": "/qt/4"},
    ))

    ctx.hwaf_path_prepend("PATH", (
      {"default": "${AtlasQt4_home}/bin"},
    ))

    macro("LIBPATH_AtlasQt4", "${AtlasQt4_home}/lib")

    ctx.hwaf_macro_append("AtlasQt4_CPPFLAGS", (
      {"default": ""},
      {("target-gcc47", "debug"): "-fpermissive"},
      {("target-gcc48", "debug"): "-fpermissive"},
    ))

    ctx.hwaf_macro_append("LIB_AtlasQt4",         "QtCore")
    ctx.hwaf_macro_append("LIB_AtlasQt4-Gui",     "QtCore QtGui")
    ctx.hwaf_macro_append("LIB_AtlasQt4-Network", "QtCore QtNetwork")
    ctx.hwaf_macro_append("LIB_AtlasQt4-OpenGL",  "QtCore QtOpenGL")
    ctx.hwaf_macro_append("LIB_AtlasQt4-Sql",     "QtCore QtSql")
    ctx.hwaf_macro_append("LIB_AtlasQt4-Svg",     "QtCore QtSvg")
    ctx.hwaf_macro_append("LIB_AtlasQt4-Xml",     "QtCore QtXml")

    ctx.hwaf_declare_macro("AtlasQt4_export_paths", "${AtlasQt4_home}")
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    return # build

## EOF ##
