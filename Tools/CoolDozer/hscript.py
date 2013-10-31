## -*- python -*-
## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "Tools/CoolDozer",
    "authors": ["Krzysztof Daniel Ciba <Krzysztof.Ciba@NOSPAMgmail.com>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/sqlalchemy", version="sqlalchemy-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    ctx.hwaf_declare_macro("CoolDozer_TestConfiguration", (
      {"default": "../test/CoolDozer_TestConfiguration.xml"},
    ))

    ctx.hwaf_declare_macro("DOXYGEN_IMAGE_PATH", (
      {"default": "../doc/images"},
    ))

    ctx.hwaf_declare_macro("DOXYGEN_EXAMPLE_PATH", (
      {"default": ""},
      {"Doxygen": ["../doc", "../cmt", "../share", "../doc"]},
    ), override=True)

    ctx.hwaf_declare_macro("DOXYGEN_EXAMPLE_PATTERNS", (
      {"default": ""},
      {"Doxygen": ["*.cxx", "*.html", "requirements", "*.py", "*.css"]},
    ), override=True)
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    ctx(
        features = "atlas_install_joboptions",
        name     = "CoolDozer-install-jobos",
        target   = "CoolDozer-install-jobos",
        source   = ["share/*.py", "share/*.txt"],
    )
    
    ctx(
        features = "atlas_install_python_modules",
        name     = "CoolDozer-install-py",
        target   = "CoolDozer-install-py",
        source   = ["python/*.py"],
    )
    
    ctx(
        features = "atlas_install_scripts",
        name     = "CoolDozer-install-scripts",
        target   = "CoolDozer-install-scripts",
        source   = ["scripts/*"],
    )
    
    ctx(
        features = "atlas_install_xmls",
        name     = "CoolDozer-install-xmls",
        target   = "CoolDozer-install-xmls",
        source   = ["xml/*"],
    )
    return # build

## EOF ##
