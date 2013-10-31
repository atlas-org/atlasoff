## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "Tools/CodeCheck",
    "authors": ["Albrand Solveig <albrand@isn.in2p3.fr>"],


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
    
    macro = ctx.hwaf_declare_macro
    
    #### macro &{{use_JavaSDK [{default []} {CodeCheck [JavaSDK JavaSDK-01-* External]}]}}
    macro("use_JavaSDK", (
      {"default": ""},
      {"CodeCheck": ["JavaSDK", "JavaSDK-01-*", "External"]},
    ))
    #### macro &{{RELATIVE_CODECHECK_OUTPUT_DIRECTORY [{default []} {CodeCheck [/CodeCheck]}]}}
    macro("RELATIVE_CODECHECK_OUTPUT_DIRECTORY", (
      {"default": ""},
      {"CodeCheck": "/CodeCheck"},
    ))
    #### macro &{{RULECHECKER [{default []} {CodeCheck [/rulechecker]}]}}
    macro("RULECHECKER", (
      {"default": ""},
      {"CodeCheck": "/rulechecker"},
    ))
    #### macro &{{CODECHECK_STRATEGY [{default []} {CodeCheck [package]}]}}
    macro("CODECHECK_STRATEGY", (
      {"default": ""},
      {"CodeCheck": "package"},
    ))
    #### macro &{{RULECHECKER_SUFFIX [{default []} {CodeCheck [/]}]}}
    macro("RULECHECKER_SUFFIX", (
      {"default": ""},
      {"CodeCheck": "/"},
    ))
    #### macro &{{CODECHECK_RELEASE_OUTPUT_DIRECTORY [{default []} {CodeCheck [/afs/cern.ch/user/a/albrand/www/CodeCheck]}]}}
    macro("CODECHECK_RELEASE_OUTPUT_DIRECTORY", (
      {"default": ""},
      {"CodeCheck": "/afs/cern.ch/user/a/albrand/www/CodeCheck"},
    ))
    #### macro &{{SELECTED_RULES [{default []} {CodeCheck [all]}]}}
    macro("SELECTED_RULES", (
      {"default": ""},
      {"CodeCheck": "all"},
    ))
    #### macro &{{CCTMP [{default []} {CodeCheck [/CCTMP]}]}}
    macro("CCTMP", (
      {"default": ""},
      {"CodeCheck": "/CCTMP"},
    ))
    #### macro &{{DOTI [{default []} {CodeCheck [/DOTI]}]}}
    macro("DOTI", (
      {"default": ""},
      {"CodeCheck": "/DOTI"},
    ))
    #### macro &{{IRST_DIR [{default [CERN&CodeCheck /afs/cern.ch/user/a/albrand/public/IRST2.5]}]}}
    macro("IRST_DIR", (
      {"default": ["CERN&CodeCheck", "/afs/cern.ch/user/a/albrand/public/IRST2.5"]},
    ))
    #### macro &{{IRST_CONFIG_DIR [{default []} {CodeCheck [${IRST_DIR}/userConfig/ATLAS]}]}}
    macro("IRST_CONFIG_DIR", (
      {"default": ""},
      {"CodeCheck": "${IRST_DIR}/userConfig/ATLAS"},
    ))
    ##### **** statement *hlib.SetStmt (&{{atlas_checker_command [{default []} {CodeCheck [java -classpath ${IRST_DIR} rules.ATLAS.ATLASRuleChecker]}]}})
    ##### **** statement *hlib.SetStmt (&{{atlas_patch_command [{default []} {CodeCheck [${IRST_DIR}/patch/patch4atlas.prl]}]}})
    ##### **** statement *hlib.PatternStmt (&{rulechecker -global tag target_<package>rchk CodeCheck ; document rulechecker <package>rchk -target_tag $(src)*.cxx -group=rulechecker})
    #### macro &{{rulechecker_header_fragment [{default []} {CodeCheck []}]}}
    macro("rulechecker_header_fragment", (
      {"default": ""},
      {"CodeCheck": ""},
    ))
    #### macro &{{rulechecker_fragment [{default []} {CodeCheck []}]}}
    macro("rulechecker_fragment", (
      {"default": ""},
      {"CodeCheck": ""},
    ))
    #### macro &{{rulechecker_trailer_fragment [{default []} {CodeCheck []}]}}
    macro("rulechecker_trailer_fragment", (
      {"default": ""},
      {"CodeCheck": ""},
    ))
    ##### **** statement *hlib.MakeFragmentStmt (&{rulechecker_header})
    ##### **** statement *hlib.MakeFragmentStmt (&{rulechecker})
    ##### **** statement *hlib.MakeFragmentStmt (&{rulechecker_trailer})
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
