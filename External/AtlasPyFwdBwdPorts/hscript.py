## -*- python -*-
## automatically generated from a hscript
## do NOT edit.

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasPyFwdBwdPorts",
    "authors": ["Sebastien Binet <binet@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
    ctx.use_pkg("External/AtlasPython", version="AtlasPython-*", public=True)
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", public=True)
    
    ## private dependencies
    ctx.use_pkg("TestPolicy", version="TestPolicy-*", private=True)
    
    ## runtime dependencies
    ctx.use_pkg("Tools/PyCmt", version="PyCmt-*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    ##### **** statement *hlib.PatternStmt (&{pkg_autoconf_build include_dirs $(CMTINSTALLAREA)/$(CMTCONFIG)/include ; private ; macro_append constituents pkg_autoconf_build_<name> ; macro pkg_autoconf_build_<name>_dependencies  ; action pkg_autoconf_build_<name> $(AtlasPyFwdBwdPorts_root)/bin/autoconf-build.py --name=<name> --src-dir='<src_dir> --install-dir='$(CMTINSTALLAREA)/<install_dir> --configure-options='<configure_options>' ; end_private})
    #### macro_append &{{pkg_autoconf_ldflags [{default [${cpplinkflags} ${cmt_installarea_linkopts}]}]}}
    ctx.hwaf_macro_append("pkg_autoconf_ldflags", (
      {"default": ["${cpplinkflags}", "${cmt_installarea_linkopts}"]},
    ))
    #### macro &{{pkg_autoconf_libs [{default []}]}}
    ctx.hwaf_declare_macro("pkg_autoconf_libs", (
      {"default": ""},
    ))
    #### macro &{{pkg_autoconf_cc [{default [${cc}]}]}}
    ctx.hwaf_declare_macro("pkg_autoconf_cc", (
      {"default": "${cc}"},
    ))
    #### macro &{{pkg_autoconf_cflags [{default [${cflags} ${cppflags} ${cppdebugflags}]}]}}
    ctx.hwaf_declare_macro("pkg_autoconf_cflags", (
      {"default": ["${cflags}", "${cppflags}", "${cppdebugflags}"]},
    ))
    #### macro_remove &{{pkg_autoconf_cflags [{default [-Woverloaded-virtual]}]}}
    ctx.hwaf_macro_remove("pkg_autoconf_cflags", (
      {"default": "-Woverloaded-virtual"},
    ))
    #### macro_remove &{{pkg_autoconf_cflags [{default [-Wno-deprecated]}]}}
    ctx.hwaf_macro_remove("pkg_autoconf_cflags", (
      {"default": "-Wno-deprecated"},
    ))
    #### macro &{{pkg_autoconf_cxx [{default [${cpp}]}]}}
    ctx.hwaf_declare_macro("pkg_autoconf_cxx", (
      {"default": "${cpp}"},
    ))
    #### macro &{{pkg_autoconf_cxxflags [{default [${cppflags} ${cppdebugflags}]}]}}
    ctx.hwaf_declare_macro("pkg_autoconf_cxxflags", (
      {"default": ["${cppflags}", "${cppdebugflags}"]},
    ))
    #### macro &{{pkg_autoconf_fc [{default [${for}]}]}}
    ctx.hwaf_declare_macro("pkg_autoconf_fc", (
      {"default": "${for}"},
    ))
    #### macro &{{pkg_autoconf_fcflags [{default [${fflags}]}]}}
    ctx.hwaf_declare_macro("pkg_autoconf_fcflags", (
      {"default": "${fflags}"},
    ))
    #### macro &{{pkg_autoconf_cppflags [{default [${includes}]}]}}
    ctx.hwaf_declare_macro("pkg_autoconf_cppflags", (
      {"default": "${includes}"},
    ))
    #### macro_append &{{cc [{default [-fno-strict-aliasing]}]}}
    ctx.hwaf_macro_append("cc", (
      {"default": "-fno-strict-aliasing"},
    ))
    #### macro_remove &{{cflags [{default [-Wno-deprecated]}]}}
    ctx.hwaf_macro_remove("cflags", (
      {"default": "-Wno-deprecated"},
    ))
    #### macro_remove &{{cflags [{default [-Woverloaded-virtual]}]}}
    ctx.hwaf_macro_remove("cflags", (
      {"default": "-Woverloaded-virtual"},
    ))
    #### macro_append &{{make_pkgbuild_ordereddict_dependencies [{default [make_pkgbuild_collections]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_ordereddict_dependencies", (
      {"default": "make_pkgbuild_collections"},
    ))
    #### macro_append &{{make_pkgbuild_ordereddict_dependencies [{default [make_pkgbuild_collections]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_ordereddict_dependencies", (
      {"default": "make_pkgbuild_collections"},
    ))
    #### macro_append &{{make_pkgbuild_bunch_dependencies [{default [make_pkgbuild_collections]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_bunch_dependencies", (
      {"default": "make_pkgbuild_collections"},
    ))
    #### macro_append &{{make_pkgbuild_bunch_dependencies [{default [make_pkgbuild_distribute]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_bunch_dependencies", (
      {"default": "make_pkgbuild_distribute"},
    ))
    #### macro_append &{{make_pkgbuild_distribute_dependencies [{default [make_pkgbuild_collections]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_distribute_dependencies", (
      {"default": "make_pkgbuild_collections"},
    ))
    #### macro_append &{{make_pkgbuild_collections_dependencies [{default [make_pkgbuild_abc]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_collections_dependencies", (
      {"default": "make_pkgbuild_abc"},
    ))
    #### macro &{{iterutils_version [{default [0.1.6]}]}}
    ctx.hwaf_declare_macro("iterutils_version", (
      {"default": "0.1.6"},
    ))
    #### macro_append &{{make_pkgbuild_iterutils_dependencies [{default [make_pkgbuild_collections]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_iterutils_dependencies", (
      {"default": "make_pkgbuild_collections"},
    ))
    #### macro_append &{{make_pkgbuild_iterutils_dependencies [{default [make_pkgbuild_distribute]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_iterutils_dependencies", (
      {"default": "make_pkgbuild_distribute"},
    ))
    #### macro_append &{{make_pkgbuild_iterutils_dependencies [{default [make_pkgbuild_itertools]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_iterutils_dependencies", (
      {"default": "make_pkgbuild_itertools"},
    ))
    #### macro_append &{{make_pkgbuild_mercurial_dependencies [{default [make_pkgbuild_collections]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_mercurial_dependencies", (
      {"default": "make_pkgbuild_collections"},
    ))
    #### macro_append &{{make_pkgbuild_simplejson_dependencies [{default [make_pkgbuild_distribute]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_simplejson_dependencies", (
      {"default": "make_pkgbuild_distribute"},
    ))
    #### macro &{{pyflakes_version [{default [0.4.0]}]}}
    ctx.hwaf_declare_macro("pyflakes_version", (
      {"default": "0.4.0"},
    ))
    #### macro_append &{{make_pkgbuild_pyflakes_dependencies [{default [make_pkgbuild_collections]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_pyflakes_dependencies", (
      {"default": "make_pkgbuild_collections"},
    ))
    #### macro &{{argparse_version [{default [1.1]}]}}
    ctx.hwaf_declare_macro("argparse_version", (
      {"default": "1.1"},
    ))
    #### macro_append &{{make_pkgbuild_argparse_dependencies [{default [make_pkgbuild_collections]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_argparse_dependencies", (
      {"default": "make_pkgbuild_collections"},
    ))
    #### macro_append &{{make_pkgbuild_argparse_dependencies [{default [make_pkgbuild_distribute]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_argparse_dependencies", (
      {"default": "make_pkgbuild_distribute"},
    ))
    #### macro_append &{{make_pkgbuild_grin_dependencies [{default [make_pkgbuild_argparse]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_grin_dependencies", (
      {"default": "make_pkgbuild_argparse"},
    ))
    #### macro_append &{{make_pkgbuild_ruffus_dependencies [{default [make_pkgbuild_simplejson]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_ruffus_dependencies", (
      {"default": "make_pkgbuild_simplejson"},
    ))
    #### macro_append &{{make_pkgbuild_jsonpickle_dependencies [{default [make_pkgbuild_simplejson]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_jsonpickle_dependencies", (
      {"default": "make_pkgbuild_simplejson"},
    ))
    #### macro &{{hgsvn_version [{default [0.1.8]}]}}
    ctx.hwaf_declare_macro("hgsvn_version", (
      {"default": "0.1.8"},
    ))
    #### macro_append &{{make_pkgbuild_hgsvn_dependencies [{default [make_pkgbuild_distribute]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_hgsvn_dependencies", (
      {"default": "make_pkgbuild_distribute"},
    ))
    #### macro_append &{{make_pkgbuild_extensions_dependencies [{default [make_pkgbuild_collections]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_extensions_dependencies", (
      {"default": "make_pkgbuild_collections"},
    ))
    #### macro &{{affinity_version [{default [0.1.0]}]}}
    ctx.hwaf_declare_macro("affinity_version", (
      {"default": "0.1.0"},
    ))
    #### macro_append &{{make_pkgbuild_affinity_dependencies [{default [make_pkgbuild_distribute]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_affinity_dependencies", (
      {"default": "make_pkgbuild_distribute"},
    ))
    #### macro_append &{{make_pkgbuild_keyring_dependencies [{default [make_pkgbuild_distribute]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_keyring_dependencies", (
      {"default": "make_pkgbuild_distribute"},
    ))
    #### macro_append &{{make_pkgbuild_pyinotify_dependencies [{default [make_pkgbuild_distribute]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_pyinotify_dependencies", (
      {"default": "make_pkgbuild_distribute"},
    ))
    #### macro_append &{{make_pkgbuild_pyyaml_dependencies [{default [make_pkgbuild_distribute]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_pyyaml_dependencies", (
      {"default": "make_pkgbuild_distribute"},
    ))
    #### macro_append &{{make_pkgbuild_pycrypto_dependencies [{default [make_pkgbuild_distribute]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_pycrypto_dependencies", (
      {"default": "make_pkgbuild_distribute"},
    ))
    #### macro_append &{{make_pkgbuild_paramiko_dependencies [{default [make_pkgbuild_pycrypto]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_paramiko_dependencies", (
      {"default": "make_pkgbuild_pycrypto"},
    ))
    #### macro_append &{{make_pkgbuild_beaker_dependencies [{default [make_pkgbuild_distribute]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_beaker_dependencies", (
      {"default": "make_pkgbuild_distribute"},
    ))
    #### macro_append &{{make_pkgbuild_pip_dependencies [{default [make_pkgbuild_distribute]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_pip_dependencies", (
      {"default": "make_pkgbuild_distribute"},
    ))
    #### macro_append &{{make_pkgbuild_virtualenv_dependencies [{default [make_pkgbuild_pip]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_virtualenv_dependencies", (
      {"default": "make_pkgbuild_pip"},
    ))
    #### macro_append &{{make_pkgbuild_futures_dependencies [{default [make_pkgbuild_distribute]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_futures_dependencies", (
      {"default": "make_pkgbuild_distribute"},
    ))
    #### macro_append &{{make_pkgbuild_datadiff_dependencies [{default [make_pkgbuild_distribute]}]}}
    ctx.hwaf_macro_append("make_pkgbuild_datadiff_dependencies", (
      {"default": "make_pkgbuild_distribute"},
    ))
    #### alias &{{grin [{default [python -m grin]}]}}
    ctx.hwaf_declare_runtime_alias("grin", (
      {"default": ["python", "-m", "grin"]},
    ))
    #### alias &{{hgimportsvn [{default [python -m hgsvn.run.hgimportsvn]}]}}
    ctx.hwaf_declare_runtime_alias("hgimportsvn", (
      {"default": ["python", "-m", "hgsvn.run.hgimportsvn"]},
    ))
    #### alias &{{hgpullsvn [{default [python -m hgsvn.run.hgpullsvn]}]}}
    ctx.hwaf_declare_runtime_alias("hgpullsvn", (
      {"default": ["python", "-m", "hgsvn.run.hgpullsvn"]},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=ordereddict file=pkgbuild_ordereddict.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=nested_dict file=pkgbuild_nested_dict.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=bunch file=pkgbuild_bunch.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=distribute file=pkgbuild_distribute.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=abc file=pkgbuild_abc.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=collections file=pkgbuild_collections.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=itertools file=pkgbuild_itertools.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=iterutils file=pkgbuild_iterutils.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=mercurial file=pkgbuild_mercurial.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=simplejson file=pkgbuild_simplejson.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=pyflakes file=pkgbuild_pyflakes.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=argparse file=pkgbuild_argparse.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=grin file=pkgbuild_grin.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=ruffus file=pkgbuild_ruffus.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=jsonpickle file=pkgbuild_jsonpickle.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=hgsvn file=pkgbuild_hgsvn.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=extensions file=pkgbuild_extensions.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=affinity file=pkgbuild_affinity.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=keyring file=pkgbuild_keyring.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=pyinotify file=pkgbuild_pyinotify.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=pyyaml file=pkgbuild_pyyaml.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=pycrypto file=pkgbuild_pycrypto.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=paramiko file=pkgbuild_paramiko.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=beaker file=pkgbuild_beaker.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=pip file=pkgbuild_pip.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=virtualenv file=pkgbuild_virtualenv.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=futures file=pkgbuild_futures.py]})
    ##### **** statement *hlib.ApplyPatternStmt (&{make_pkgbuild [name=datadiff file=pkgbuild_datadiff.py]})
    
    ctx(
        features = "atlas_install_scripts",
        name     = "AtlasPyFwdBwdPorts-install-scripts",
        target   = "AtlasPyFwdBwdPorts-install-scripts",
        source   = ["scripts/*"],
    )
    return # build

## EOF ##
