## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "External/AtlasReflex",
    "authors": ["RD Schaffer <R.D.Schaffer@cern.ch>",
                "Kyle Cranmer <cranmer@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
    ctx.use_pkg("LCG_Interfaces/Reflex", version="v*", public=True)
    ctx.use_pkg("External/AtlasRELAX", version="AtlasRELAX-00-*", public=True)
    
    ## no private dependencies
    ## runtime dependencies
    ctx.use_pkg("External/AtlasRELAX", version="AtlasRELAX-00-*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    
    
    #### macro &{{athena_genreflex_wrapper_cmd [{default [python ${AtlasReflex_root}/cmt/athena_genreflex_wrapper.py]}]}}
    ctx.hwaf_declare_macro("athena_genreflex_wrapper_cmd", (
      {"default": ["python", "${AtlasReflex_root}/cmt/athena_genreflex_wrapper.py"]},
    ))
    #### macro_prepend &{{genreflex_cmd [{default []} {gcc43 [GCCXML_USER_FLAGS=-D__GNUC_MINOR__=2]}]}}
    ctx.hwaf_macro_prepend("genreflex_cmd", (
      {"default": ""},
      {"gcc43": "GCCXML_USER_FLAGS=-D__GNUC_MINOR__=2"},
    ))
    #### macro &{{merge_dict_rootmap_cmd [{default [${GaudiPolicy_root}/scripts/merge_files.py]}]}}
    ctx.hwaf_declare_macro("merge_dict_rootmap_cmd", (
      {"default": "${GaudiPolicy_root}/scripts/merge_files.py"},
    ),override=True)
    ##### **** statement *hlib.MakeFragmentStmt (&{reflex_dict})
    ##### **** statement *hlib.MakeFragmentStmt (&{merge_dict_rootmap})
    ##### **** statement *hlib.MakeFragmentStmt (&{DataLink_selection.xml})
    ##### **** statement *hlib.MakeFragmentStmt (&{ElementLink_selection.xml})
    ##### **** statement *hlib.MakeFragmentStmt (&{ElementLinkVector_selection.xml})
    ##### **** statement *hlib.MakeFragmentStmt (&{Navigable_selection.xml})
    ##### **** statement *hlib.MakeFragmentStmt (&{NavigableDict.h})
    ##### **** statement *hlib.MakeFragmentStmt (&{ElementLinkDict.h})
    ##### **** statement *hlib.MakeFragmentStmt (&{DataLinkDict.h})
    ##### **** statement *hlib.SetStmt (&{{GCCXML_USER_FLAGS [{default []} {target-darwin&target-x86_64 [-m64]}]}})
    ##### **** statement *hlib.PatternStmt (&{lcgdict private ; use Reflex v* LCG_Interfaces ; macro gcc_user_flags  target-darwin&target-x86_64 -m64 ; macro dict_dir $(bin)dict ; macro_append <dict>Gen_dependencies install_includes ; document reflex_dict <dict>Gen <headerfiles> dictionary=<dict> ; library <dict>Dict -suffix=_<dict> <extralibfiles> -s=$(dict_dir)/<dict> *.cpp ; macro cppdebugflags $(cppdebugflags) target_<dict>Dict -O2 -DNDEBUG ; macro_append lib_<dict>Dict_cppflags  HIVE&&gcc47  gcc47 -std=c++03 ; macro_append <dict>Dict_pp_cppflags -I. -ftemplate-depth-125 ; macro_append <dict>Dict_pp_cppflags  separate-debug&target-opt&target-linux -g ; macro_append <dict>Dict_dependencies <dict>Gen ; macro_append <dict>Dict_dependencies $(<package>_library_dependencies) ; macro reflex_dict<dict>_clean_target <dict>Dictclean ; macro reflex_dict<dict>_selection_file ../<package>/<selectionfile> ; macro reflex_dict<dict>_navigables <navigables> ; macro reflex_dict<dict>_data_links <dataLinks> ; macro reflex_dict<dict>_element_links <elementLinks> ; macro reflex_dict<dict>_element_link_vectors <elementLinkVectors> ; macro reflex_dict<dict>_opt_rootmap --rootmap=<dict>Dict.dsomap --rootmap-lib=$(libprefix)<dict>Dict.$(shlibsuffix) ; macro reflex_dict<dict>_options <options> --select=$(dict_dir)/<dict>_selection.xml -DNDEBUG $(reflex_dict<dict>_opt_rootmap) ; macro_append reflex_dict<dict>_options --gccxmlpath=$(GCCXML_home)/bin ; macro_append reflex_dict<dict>_options --fail_on_warnings ; macro_append reflex_dict<dict>_options --fail_on_warnings $(reflex_dict_options_cppflags) ; macro_append reflex_dict<dict>_options  x86_64&&32 --gccxmlopt=--gccxml-cxxflags --gccxmlopt=-m32 ; macro <dict>Dict_shlibflags $(componentshr_linkopts) $(use_linkopts) $(Reflex_linkopts) $(<package>_extra_shlibflags) ; apply_pattern generic_declare_for_link files='$(dict_dir)/<dict>/<dict>Dict.dsomap prefix=$(tag)/lib name=<dict>Dict_ kind=<dict>dictrootmap ; macro_append install_<dict>Dict_<dict>dictrootmap_dependencies <dict>Gen ; apply_pattern optdebug_library name='<dict>Dict ; macro_append check_install_<dict>Dict_<dict>dictrootmap_dependencies <dict>Gen ; apply_pattern merge_dict_dsomap dict=<dict> headerfiles=<headerfiles> ; end_private})
    ##### **** statement *hlib.PatternStmt (&{merge_dict_dsomap private ; macro run_merge_dict_cmd do_real_merge_dict_dsomap rootmap_merge do_real_merge_dict_dsomap no_rootmap do_null_merge_dict_dsomap ; apply_pattern $(run_merge_dict_cmd) dict=<dict> headerfiles=<headerfiles> ; end_private})
    ##### **** statement *hlib.PatternStmt (&{do_real_merge_dict_dsomap document merge_dict_rootmap <dict>DictMerge <headerfiles> dictionary=<dict> ; macro_append <dict>DictMerge_dependencies <dict>Dict})
    ##### **** statement *hlib.PatternStmt (&{do_null_merge_dict_dsomap private ; macro dummy_for_<dict>DictMerge <dict> ; macro dummy_for_<headerfiles>DictHeaders <headerfiles> ; end_private})
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
