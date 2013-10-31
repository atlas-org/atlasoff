## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "Database/APR/XMLCatalog",
    "authors": ["Marcin Nowak"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("Database/APR/FileCatalog", version="FileCatalog-*", public=True)
    
    ## private dependencies
    ctx.use_pkg("External/AtlasCORAL", version="AtlasCORAL-*", private=True)
    ctx.use_pkg("External/AtlasReflex", version="AtlasReflex-*", private=True)
    ctx.use_pkg("External/AtlasXercesC", version="AtlasXercesC-*", private=True)
    ctx.use_pkg("External/AtlasCppUnit", version="AtlasCppUnit-*", private=True)
    ctx.use_pkg("Database/PersistentDataModel", version="PersistentDataModel-*", private=True)
    ctx.use_pkg("TestPolicy", version="TestPolicy-*", private=True)
    
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    ##### **** statement *hlib.PatternStmt (&{APR_test use TestTools TestTools-* AtlasTest ; apply_pattern CppUnit name=<name> files=../test/<name>_test.cxx})
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{pool_plugin_library []})
    ##### **** statement *hlib.ApplyPatternStmt (&{install_runtime []})
    ##### **** statement *hlib.ApplyPatternStmt (&{APR_test [name=XMLFunctionality]})
    ##### **** statement *hlib.ApplyPatternStmt (&{APR_test [name=XMLmetaTest]})
    
    
    return # build

## EOF ##
