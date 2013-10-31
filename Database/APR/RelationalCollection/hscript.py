## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "Database/APR/RelationalCollection",
    "authors": ["Marcin Nowak"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    
    ## private dependencies
    ctx.use_pkg("External/AtlasCORAL", version="AtlasCORAL-*", private=True)
    ctx.use_pkg("Database/APR/CollectionBase", version="CollectionBase-*", private=True)
    ctx.use_pkg("Database/APR/PersistencySvc", version="PersistencySvc-*", private=True)
    ctx.use_pkg("External/AtlasReflex", version="AtlasReflex-*", private=True)
    ctx.use_pkg("Database/PersistentDataModel", version="PersistentDataModel-*", private=True)
    ctx.use_pkg("Database/APR/POOLCore", version="POOLCore-*", private=True)
    ctx.use_pkg("TestPolicy", version="TestPolicy-*", private=True)
    
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    ##### **** statement *hlib.PatternStmt (&{RelationalCollection_test_run use TestTools TestTools-* AtlasTest ; application <name>_test -suffix=_<name> ../tests/<name>/*.cpp application_suffix=" ; document athenarun_launcher <name>_utest -group=$(whichGroup) athenarun_exe="'../${CMTCONFIG}/<name>_test' athenarun_pre="'. ../cmt/setup.sh ; rm -f pool*.root *xml' athenarun_opt=" athenarun_out=" > <name>_test.log 2>&1' athenarun_post="'post.sh <name>_test $(q)<extrapatterns>$(q)'})
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{pool_plugin_library []})
    ##### **** statement *hlib.ApplyPatternStmt (&{RelationalCollection_test_run [name=WriteRead]})
    ##### **** statement *hlib.ApplyPatternStmt (&{RelationalCollection_test_run [name=WriteUpdate]})
    
    
    return # build

## EOF ##
