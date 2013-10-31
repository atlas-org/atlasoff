## -*- python -*-
## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "Trigger/TrigConfiguration/TrigDb",
    "authors": ["David.Berge@cern.ch,Joerg.Stelzer@cern.ch"],
    "managers": ["David.Berge@cern.ch,Joerg.Stelzer@cern.ch"],

}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("DetCommonPolicy", version="*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    ctx(
        features = "detcommon_generic_install",
        name     = "TrigDb-generic-install-DB_scripts-scripts",
        target   = "TrigDb-generic-install-DB_scripts-scripts",
        source   = ["share/EmptyDB",
                    "share/EmptyDBOracle",
                    "share/get_triggerDBfiles",
                    "share/DBstartup",
                    ],
        install_prefix = ["share/bin"],
    )
    
    ctx(
        features = "detcommon_generic_install",
        name     = "TrigDb-generic-install-sql_scripts-sql",
        target   = "TrigDb-generic-install-sql_scripts-sql",
        source   = ["share/sql/*.sql"],
        install_prefix = ["share/bin/sql"],
    )
    return # build

## EOF ##
