## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "AtlasCxxPolicy",
    "authors": ["atlas collaboration"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("GaudiPolicy", version="v*", public=True)
    ctx.use_pkg("External/ExternalPolicy", version="ExternalPolicy-*", public=True)
    ctx.use_pkg("External/AtlasCompilers", version="AtlasCompilers-*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    ## FIXME: review mapping CMT -> hwaf
    
    #### macro &{{cpp_name [{default [${cpp_name}]} {host-mac106&gcc40 [gcc-4.0]}]}}
    ctx.hwaf_declare_macro("cpp_name", (
      {"default": "${cpp_name}"},
      {("host-mac106", "gcc40"): "gcc-4.0"},
    ))
    #### macro_append &{{shlibbuilder [{default []} {target-gcc&target-i686&host-x86_64 [-m32]} {target-gcc&target-i386&host-x86_64 [-m32]}]}}
    ctx.hwaf_macro_append("shlibbuilder", (
      {"default": ""},
      {("target-gcc", "target-i686", "host-x86_64"): "-m32"},
      {("target-gcc", "target-i386", "host-x86_64"): "-m32"},
    ))
    #### macro &{{cppflags [{default []} {target-darwin [-D_GNU_SOURCE -pthread -pipe -fPIC -W -Wall]} {target-unix [-D_GNU_SOURCE -pthread -pipe -ansi -fPIC -W -Wall]}]}}
    ctx.hwaf_declare_macro("cppflags", (
      {"default": ""},
      {"target-darwin": ["-D_GNU_SOURCE", "-pthread", "-pipe", "-fPIC", "-W", "-Wall"]},
      {"target-unix": ["-D_GNU_SOURCE", "-pthread", "-pipe", "-ansi", "-fPIC", "-W", "-Wall"]},
    ),override=True)
    #### macro_append &{{cppflags [{default [-pedantic -Wwrite-strings -Wpointer-arith -Woverloaded-virtual -Wno-long-long]}]}}
    ctx.hwaf_macro_append("cppflags", (
      {"default": ["-pedantic", "-Wwrite-strings", "-Wpointer-arith", "-Woverloaded-virtual", "-Wno-long-long"]},
    ))
    #### macro_append &{{cppflags [{default []} {errorConversion [-Werror=conversion]}]}}
    ctx.hwaf_macro_append("cppflags", (
      {"default": ""},
      {"errorConversion": "-Werror=conversion"},
    ))
    #### macro_append &{{cppflags [{default []} {target-unix&target-i686 [-march=pentium]}]}}
    ctx.hwaf_macro_append("cppflags", (
      {"default": ""},
      {("target-unix", "target-i686"): "-march=pentium"},
    ))
    #### macro_append &{{cppflags [{default []} {target-gcc&padded [-Wpadded]}]}}
    ctx.hwaf_macro_append("cppflags", (
      {"default": ""},
      {("target-gcc", "padded"): "-Wpadded"},
    ))
    #### macro_append &{{cppflags [{default []} {target-dbg&no-inline [-fno-inline -fno-default-inline]}]}}
    ctx.hwaf_macro_append("cppflags", (
      {"default": ""},
      {("target-dbg", "no-inline"): ["-fno-inline", "-fno-default-inline"]},
    ))
    #### macro_append &{{cppflags [{default []} {noWerror []} {applyWerror [-Werror]}]}}
    ctx.hwaf_macro_append("cppflags", (
      {"default": ""},
      {"noWerror": ""},
      {"applyWerror": "-Werror"},
    ))

    ctx.hwaf_macro_append("CXXFLAGS", (
      {"default":    ""},
      {"target-c11": "-std=c++11"},
    ))

    ctx.hwaf_macro_remove("CXXFLAGS", (
      {"default":    ""},
      {"target-icc": "-W"},
    ))

    ## FIXME
    ctx.hwaf_declare_macro("AtlasCxxPolicy_pp_cppflags", (
      {"default": ""},
      {"target-gcc40": ["-DHAVE_PRETTY_FUNCTION", "-DHAVE_LONG_LONG", "-DHAVE_BOOL", "-DHAVE_EXPLICIT", "-DHAVE_MUTABLE", "-DHAVE_SIGNED", "-DHAVE_TYPENAME", "-DHAVE_NEW_STYLE_CASTS", "-DHAVE_DYNAMIC_CAST", "-DHAVE_TYPEID", "-DHAVE_ANSI_TEMPLATE_INSTANTIATION", "-DHAVE_TEMPLATE_DEFAULT_ARGS", "-DHAVE_BROKEN_TEMPLATE_RESCOPE", "-DHAVE_TEMPLATE_NULL_ARGS", "-DHAVE_TEMPLATE_NULL_SPEC", "-DHAVE_TEMPLATE_PARTIAL_SPEC", "-DHAVE_MEMBER_TEMPLATES", "-DHAVE_ANSI_OPERATOR_ARROW", "-DHAVE_NAMESPACES", "-DHAVE_NAMESPACE_STD", "-DHAVE_NEW_IOSTREAMS", "-DHAVE_OSTREAM_CHAR_OVERLOAD", "-DHAVE_ITERATOR_TRAITS", "-DHAVE_ITERATOR", "-DHAVE_REVERSE_ITERATOR_STYLE", "-DHAVE_CXX_STDC_HEADERS"]},
      {"target-gcc41": ["-DHAVE_PRETTY_FUNCTION", "-DHAVE_LONG_LONG", "-DHAVE_BOOL", "-DHAVE_EXPLICIT", "-DHAVE_MUTABLE", "-DHAVE_SIGNED", "-DHAVE_TYPENAME", "-DHAVE_NEW_STYLE_CASTS", "-DHAVE_DYNAMIC_CAST", "-DHAVE_TYPEID", "-DHAVE_ANSI_TEMPLATE_INSTANTIATION", "-DHAVE_TEMPLATE_DEFAULT_ARGS", "-DHAVE_BROKEN_TEMPLATE_RESCOPE", "-DHAVE_TEMPLATE_NULL_ARGS", "-DHAVE_TEMPLATE_NULL_SPEC", "-DHAVE_TEMPLATE_PARTIAL_SPEC", "-DHAVE_MEMBER_TEMPLATES", "-DHAVE_ANSI_OPERATOR_ARROW", "-DHAVE_NAMESPACES", "-DHAVE_NAMESPACE_STD", "-DHAVE_NEW_IOSTREAMS", "-DHAVE_OSTREAM_CHAR_OVERLOAD", "-DHAVE_ITERATOR_TRAITS", "-DHAVE_ITERATOR", "-DHAVE_REVERSE_ITERATOR_STYLE", "-DHAVE_CXX_STDC_HEADERS"]},
      {"target-gcc42": ["-DHAVE_PRETTY_FUNCTION", "-DHAVE_LONG_LONG", "-DHAVE_BOOL", "-DHAVE_EXPLICIT", "-DHAVE_MUTABLE", "-DHAVE_SIGNED", "-DHAVE_TYPENAME", "-DHAVE_NEW_STYLE_CASTS", "-DHAVE_DYNAMIC_CAST", "-DHAVE_TYPEID", "-DHAVE_ANSI_TEMPLATE_INSTANTIATION", "-DHAVE_TEMPLATE_DEFAULT_ARGS", "-DHAVE_BROKEN_TEMPLATE_RESCOPE", "-DHAVE_TEMPLATE_NULL_ARGS", "-DHAVE_TEMPLATE_NULL_SPEC", "-DHAVE_TEMPLATE_PARTIAL_SPEC", "-DHAVE_MEMBER_TEMPLATES", "-DHAVE_ANSI_OPERATOR_ARROW", "-DHAVE_NAMESPACES", "-DHAVE_NAMESPACE_STD", "-DHAVE_NEW_IOSTREAMS", "-DHAVE_OSTREAM_CHAR_OVERLOAD", "-DHAVE_ITERATOR_TRAITS", "-DHAVE_ITERATOR", "-DHAVE_REVERSE_ITERATOR_STYLE", "-DHAVE_CXX_STDC_HEADERS"]},
      {"target-gcc43": ["-DHAVE_PRETTY_FUNCTION", "-DHAVE_LONG_LONG", "-DHAVE_BOOL", "-DHAVE_EXPLICIT", "-DHAVE_MUTABLE", "-DHAVE_SIGNED", "-DHAVE_TYPENAME", "-DHAVE_NEW_STYLE_CASTS", "-DHAVE_DYNAMIC_CAST", "-DHAVE_TYPEID", "-DHAVE_ANSI_TEMPLATE_INSTANTIATION", "-DHAVE_TEMPLATE_DEFAULT_ARGS", "-DHAVE_BROKEN_TEMPLATE_RESCOPE", "-DHAVE_TEMPLATE_NULL_ARGS", "-DHAVE_TEMPLATE_NULL_SPEC", "-DHAVE_TEMPLATE_PARTIAL_SPEC", "-DHAVE_MEMBER_TEMPLATES", "-DHAVE_ANSI_OPERATOR_ARROW", "-DHAVE_NAMESPACES", "-DHAVE_NAMESPACE_STD", "-DHAVE_NEW_IOSTREAMS", "-DHAVE_OSTREAM_CHAR_OVERLOAD", "-DHAVE_ITERATOR_TRAITS", "-DHAVE_ITERATOR", "-DHAVE_REVERSE_ITERATOR_STYLE", "-DHAVE_CXX_STDC_HEADERS"]},
      {"target-gcc4": ["-DHAVE_PRETTY_FUNCTION", "-DHAVE_LONG_LONG", "-DHAVE_BOOL", "-DHAVE_EXPLICIT", "-DHAVE_MUTABLE", "-DHAVE_SIGNED", "-DHAVE_TYPENAME", "-DHAVE_NEW_STYLE_CASTS", "-DHAVE_DYNAMIC_CAST", "-DHAVE_TYPEID", "-DHAVE_ANSI_TEMPLATE_INSTANTIATION", "-DHAVE_TEMPLATE_DEFAULT_ARGS", "-DHAVE_BROKEN_TEMPLATE_RESCOPE", "-DHAVE_TEMPLATE_NULL_ARGS", "-DHAVE_TEMPLATE_NULL_SPEC", "-DHAVE_TEMPLATE_PARTIAL_SPEC", "-DHAVE_MEMBER_TEMPLATES", "-DHAVE_ANSI_OPERATOR_ARROW", "-DHAVE_NAMESPACES", "-DHAVE_NAMESPACE_STD", "-DHAVE_NEW_IOSTREAMS", "-DHAVE_OSTREAM_CHAR_OVERLOAD", "-DHAVE_ITERATOR_TRAITS", "-DHAVE_ITERATOR", "-DHAVE_REVERSE_ITERATOR_STYLE", "-DHAVE_CXX_STDC_HEADERS"]},
      {"target-clang3": "-DHAVE_NEW_IOSTREAMS"},
    ))
    #### macro_append &{{AtlasCxxPolicy_pp_cppflags [{default []} {target-gcc&target-x86_64&host-x86_64 [-DHAVE_64_BITS]} {target-gcc&target-x86_64&host-darwin [-DHAVE_64_BITS]}]}}
    ctx.hwaf_macro_append("AtlasCxxPolicy_pp_cppflags", (
      {"default": ""},
      {("target-gcc", "target-x86_64", "host-x86_64"): "-DHAVE_64_BITS"},
      {("target-gcc", "target-x86_64", "host-darwin"): "-DHAVE_64_BITS"},
    ))
    #### macro_append &{{AtlasCxxPolicy_pp_cppflags [{default [-D__IDENTIFIER_64BIT__]}]}}
    ctx.hwaf_macro_append("AtlasCxxPolicy_pp_cppflags", (
      {"default": "-D__IDENTIFIER_64BIT__"},
    ))
    #### macro &{{q2 [{default []}]}}
    ctx.hwaf_declare_macro("q2", (
      {"default": ""},
    ))
    #### macro_append &{{AtlasCxxPolicy_pp_cppflags [{default [-DPACKAGE_VERSION=${q2}${version}${q2} -DPACKAGE_VERSION_UQ=${version}]}]}}
    ctx.hwaf_macro_append("AtlasCxxPolicy_pp_cppflags", (
      {"default": ["-DPACKAGE_VERSION=${q2}${version}${q2}", "-DPACKAGE_VERSION_UQ=${version}"]},
    ))
    #### macro_append &{{AtlasCxxPolicy_pp_cppflags [{default []} {target-opt [-DNDEBUG]}]}}
    ctx.hwaf_macro_append("AtlasCxxPolicy_pp_cppflags", (
      {"default": ""},
      {"target-opt": "-DNDEBUG"},
    ))
    #### macro_append &{{AtlasCxxPolicy_pp_cppflags [{default [${pp_cppflags}]}]}}
    ctx.hwaf_macro_append("AtlasCxxPolicy_pp_cppflags", (
      {"default": "${pp_cppflags}"},
    ))
    #### macro &{{cflags [{default [-fPIC]}]}}
    ctx.hwaf_declare_macro("cflags", (
      {"default": "-fPIC"},
    ),override=True)
    #### macro &{{clinkflags [{default [-fPIC]}]}}
    ctx.hwaf_declare_macro("clinkflags", (
      {"default": "-fPIC"},
    ))
    #### macro_append &{{cflags [{default []} {target-c11 [-std=c11]}]}}
    ctx.hwaf_macro_append("cflags", (
      {"default": ""},
      {"target-c11": "-std=c11"},
    ))
    #### tag &{Linux [cpp_native_dependencies]}
    ctx.hwaf_declare_tag(
        "Linux",
        content=["cpp_native_dependencies"]
    )
    #### tag &{Darwin [cpp_native_dependencies]}
    ctx.hwaf_declare_tag(
        "Darwin",
        content=["cpp_native_dependencies"]
    )
    ## FIXME
    ctx.hwaf_declare_tag("NICOS", content=[])
    
    #### macro &{{NICOS [{default [NICOS${NICOS_PROJECT_RELNAME}]}]}}
    ctx.hwaf_declare_macro("NICOS", (
      {"default": "NICOS${NICOS_PROJECT_RELNAME}"},
    ))
    #### apply_tag &{{$(NICOS) []}}
    ctx.hwaf_apply_tag("${NICOS}")
    #### macro &{{NICOS_TMP_A [{default [NICOS${NICOS_PROJECT_HOME}]}]}}
    ctx.hwaf_declare_macro("NICOS_TMP_A", (
      {"default": "NICOS${NICOS_PROJECT_HOME}"},
    ))
    #### macro &{{NICOS_TMP_B [{default [NICOS${NICOS_COPY_HOME}]}]}}
    ctx.hwaf_declare_macro("NICOS_TMP_B", (
      {"default": "NICOS${NICOS_COPY_HOME}"},
    ))
    #### macro &{{NICOS_TMP_C [{default [NICOS${NICOS_PROJECT_RELNAME_COPY}]}]}}
    ctx.hwaf_declare_macro("NICOS_TMP_C", (
      {"default": "NICOS${NICOS_PROJECT_RELNAME_COPY}"},
    ))
    #### apply_tag &{{$(NICOS_TMP_A) []}}
    ctx.hwaf_apply_tag("${NICOS_TMP_A}")
    #### apply_tag &{{$(NICOS_TMP_B) []}}
    ctx.hwaf_apply_tag("${NICOS_TMP_B}")
    #### apply_tag &{{$(NICOS_TMP_C) []}}
    ctx.hwaf_apply_tag("${NICOS_TMP_C}")
    ##### **** statement *hlib.TagExcludeStmt (&{NICOS [NICOSrel_nightly]})
    #### macro_append &{{cppflags [{default []} {NICOSrel_nightly [-fdebug-prefix-map=${NICOS_PROJECT_HOME}/${NICOS_PROJECT_RELNAME}=${NICOS_COPY_HOME}/${NICOS_PROJECT_RELNAME_COPY}]}]}}
    ctx.hwaf_macro_append("cppflags", (
      {"default": ""},
      {"NICOSrel_nightly": "-fdebug-prefix-map=${NICOS_PROJECT_HOME}/${NICOS_PROJECT_RELNAME}=${NICOS_COPY_HOME}/${NICOS_PROJECT_RELNAME_COPY}"},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    
    
    return # build

## EOF ##
