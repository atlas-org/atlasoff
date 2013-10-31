## -*- python -*-
## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "Tools/PyJobTransforms",
    "authors": [],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    ctx.use_pkg("External/AtlasPyFwdBwdPorts", version="*", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", runtime=True)
    ctx.use_pkg("External/AtlasPyFwdBwdPorts", version="*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    ## load+export atlascommon policies
    ctx.hwaf_export_module("waftools/pyjobtransforms-features.py")

    macro = ctx.hwaf_declare_macro
    
    macro("tfs_dir", "../scripts")

    macro("PyJobTransforms_TestConfiguration", "test/PyJobTransforms_TestConfiguration.xml")
    ctx.hwaf_macro_append("makeTrfSignatures_dependencies", (
      {"default": ["install_tfs_jop", "install_python_modules"]},
    ))

    ctx.hwaf_macro_append("all_dependencies", (
      {"default": "makeTrfSignatures"},
    ))

    ctx.hwaf_macro_append("check_install_json_dependencies", (
      {"default": "makeTrfSignatures"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    ctx(
        features = "atlas_install_runtime_extras",
        name     = "PyJobTransforms-install-runtime-extras",
        source   = ["test/PyJobTransforms_TestConfiguration.xml"],
    )

    o = ctx(
        features = "make_trf_signatures",
        name     = "PyJobTransforms-make-trf-signatures",
        #rule     = "scripts/makeTrfSignatures.py --output ${TGT}",
        #source   = "scripts/makeTrfSignatures.py",
        target   = "PyJobTransformsSignatures.json",
        update_outputs = True,
        )

    ## FIXME
    if 0:
        ctx(
        features = "atlas_generic_install",
        name     = "PyJobTransforms-generic-install--json",
        target   = "PyJobTransforms-generic-install--json",
        source   = ["share/PyJobTransformsSignatures.json"],
        install_prefix = ["share/JobTransforms"],
        use      = ["PyJobTransforms-make-trf-signatures"],
        after    = [o, "PyJobTransforms-make-trf-signatures"],
    )
    
    ctx(
        features = "atlas_generic_install",
        name     = "PyJobTransforms-generic-install--test",
        target   = "PyJobTransforms-generic-install--test",
        source   = ["test/test_*.py"],
        install_prefix = ["share/JobTransforms/test"],
    )

    ctx(
        features = "atlas_generic_install",
        name     = "PyJobTransforms-generic-install-trf-runtime",
        target   = "PyJobTransforms-generic-install-trf-runtime",
        source   = ["share/*.db"],
        install_prefix = ["share"],
    )
    
    ctx(
        features = "atlas_install_python_modules",
        name     = "PyJobTransforms-install-py",
        target   = "PyJobTransforms-install-py",
        source   = ["python/*.py"],
    )
    
    ctx(
        features = "atlas_install_scripts",
        name     = "PyJobTransforms-install-scripts",
        target   = "PyJobTransforms-install-scripts",
        source   = ["scripts/*"],
    )
    
    ctx(
        features = "atlas_install_trfs",
        name     = "PyJobTransforms-install-trfs",
        target   = "PyJobTransforms-install-trfs",
        source   = [],
        trf_jo = ["'*.py"],
        trf_tfs = ["'*_tf.py"],
    )
    return # build

## EOF ##
