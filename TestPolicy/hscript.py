## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "TestPolicy",
    "authors": ["Alexander Undrus <undrus@bnl.gov>",
                "Jean-Francois Laporte <laport@hep.saclay.cea.fr>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-01-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    ## FIXME
    
    ##### **** statement *hlib.PatternStmt (&{CppUnit private ; use AtlasCppUnit AtlasCppUnit-* External -no_auto_imports ; use StoreGate StoreGate-* Control -no_auto_imports ; document CppUnitLauncher <name>CppUnitTest -group=CppUnit cppunitrun_exe="'<name>CppUnit.exe' cppunitrun_opt="<options> cppunitrun_out=" > <name>.log 2>&1' cppunitrun_log=" <name>.log' ; application <name>CppUnit <files> -suffix=_<name> -import=CppUnit -import=TestPolicy -import=TestTools <imports> -group=CppUnit ; macro_append <name>CppUnitTest_dependencies <name>CppUnit ; end_private})
    ##### **** statement *hlib.MakeFragmentStmt (&{CppUnitLauncher})
    ##### **** statement *hlib.PatternStmt (&{ctest -global document ctest myctest -group=ctest})
    ##### **** statement *hlib.MakeFragmentStmt (&{ctest})
    ##### **** statement *hlib.MakeFragmentStmt (&{athenarun_launcher_header})
    ##### **** statement *hlib.MakeFragmentStmt (&{athenarun_launcher})
    ##### **** statement *hlib.PatternStmt (&{athenarun_test document athenarun_launcher <name>_test -group=check athenarun_exe="'athena.py' athenarun_opt="<options> athenarun_pre="'logfile=<name>.log; . <pre_script>' athenarun_out=" > <name>.log 2>&1' athenarun_post="'sh <post_script>'})
    ##### **** statement *hlib.MakeFragmentStmt (&{athenacreate_launcher})
    ##### **** statement *hlib.PatternStmt (&{athenacreate_descr document athenacreate_launcher <name>_test -group=descr athenacreate_exe="'athena.py' athenacreate_opt="<options> athenacreate_pre="'logfile=<name>.log; . <pre_script>' athenacreate_out=" > <name>.log 2>&1' athenacreate_post="'sh <post_script>'})
    ##### **** statement *hlib.PatternStmt (&{validate_xml private ; action <package>_validateXML python ${TestPolicy_root}/python/validateXML.py $(<package>_root)/test/<package>_TestConfiguration.xml ; macro_append all_dependencies <package>_validateXML AtlasHLT_scripts  ; end_private})
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
