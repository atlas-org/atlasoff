## -*- python -*-

## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "AtlasCommonPolicy",
    "authors": ["David Quarrie"],
}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("LCG_Platforms", version="*", public=True)
    ctx.use_pkg("Tools/AtlasDoxygen", version="AtlasDoxygen-*", public=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):

    macro = ctx.hwaf_declare_macro
    
    ## load+export atlascommon policies
    ctx.hwaf_export_module("waftools/atlascommon-policy.py")

    ctx.hwaf_declare_tag(
        "static",
        content=["WithStatic"]
    )

    ctx.hwaf_declare_tag(
        "UnixStatic",
        content=["WithStatic"]
    )

    ## support for separate debug symbols
    ctx.hwaf_declare_tag("separate-debug", content=[])
    ctx.hwaf_apply_tag("separate-debug")

    ctx.hwaf_declare_macro("SEPARATEDEBUG", (
      {"default": ""},
      {("separate-debug", "target-opt", "target-linux"): "1"},
    ))

    ctx.hwaf_macro_append("CPPFLAGS", (
      {"default": ""},
      {("separate-debug", "target-opt", "target-linux"): "-g"},
    ))

    ctx.hwaf_macro_append("CFLAGS", (
      {"default": ""},
      {("separate-debug", "target-opt", "target-linux"): "-g"},
    ))

    ctx.hwaf_macro_append("FCFLAGS", (
      {"default": ""},
      {("separate-debug", "target-opt", "target-linux"): "-g"},
    ))

    ctx.hwaf_declare_macro("debuginfosuffix", ".debug")
    
    ctx.hwaf_macro_append("all_dependencies", (
      {"default": "checkreq"},
    ))

    # preprocessor ---
    ctx.hwaf_macro_append('DEFINES', (
        {'default':  ['DISABLE_ALLOC',
                      'HAVE_NEW_IOSTREAMS',
                      'ATHENA_VERSION=1',
                      '_GNU_SOURCE',
                      'GAUDI_V20_COMPAT',
                      'ATLAS_GAUDI_V21',
                      ]},
    ))

    # ctx.hwaf_macro_append('DEFINES', (
    #     {("slc6", "gcc43"): '__USE_XOPEN2K8'},
    # ))

    # ctx.hwaf_macro_append("DEFINES", (
    #     {"target-linux": ["__linux__", "__linux", "__USE_GNU", "linux"]},
    #     ))

    commonflags = ['-O2', '-fPIC',
                   '-pipe', '-ansi', '-Wall', '-W']
    
    ctx.hwaf_macro_append("CFLAGS", (
        {"default": commonflags},
        ))
    ctx.hwaf_macro_append("CXXFLAGS", (
        {"default": commonflags},
        ))

    ctx.hwaf_macro_append("CFLAGS", (
        {"target-x86_64": "-m64"},
        {"target-i686":   "-m32"},
    ))
    
    ctx.hwaf_macro_append("CXXFLAGS", (
        {"target-x86_64": "-m64"},
        {"target-i686":   "-m32"},
    ))

    ctx.hwaf_macro_append("CXXFLAGS", (
        {"gcc46": "-std=c++0x"},
        {"gcc47": "-std=c++11"},
        {"gcc48": "-std=c++11"},
    ))
    
    ### load-up toolchain
    ## override whatever previous projects did...
    macro("LCG_COMPILER_ROOT", (
        {"default": ""},
        {"target-lcg-compiler": "${gcc_home}"},
        {"target-clang":        "${clang_home}"},
        {"target-icc":          "${icc_home}"},
    ), override=True)
    
    macro("COMPILER_PATH", (
      {"default": "${gcc_home}/lib/gcc/x86_64-unknown-linux-gnu/${gcc_native_version}"},
    ), override=True)
    ctx.hwaf_declare_runtime_env("COMPILER_PATH")
    
    ctx.hwaf_path_prepend("PATH", (
      {"default": ""},
      {"target-lcg-compiler": "${gcc_home}/bin"},
      {"target-clang": "${gcc_home}/bin"},
      {"target-icc": "${gcc_home}/bin"},
    ))
    ctx.hwaf_path_prepend("PATH", (
      {"default": ""},
      {"target-clang": "${clang_home}/bin"},
    ))
    ctx.hwaf_path_prepend("LD_LIBRARY_PATH", (
      {"default": ""},
      {("target-lcg-compiler", "host-x86_64", "target-i686"): "${gcc_home}/lib64"},
      {("target-icc", "host-x86_64", "target-i686"): "${gcc_home}/lib64"},
      {"target-clang": "${clang_home}/lib"},
    ))

    ctx.hwaf_path_prepend("LD_LIBRARY_PATH", (
      {"default": ""},
      {"target-lcg-compiler": "${gcc_home}/${unixdirname}"},
      {"target-clang": "${gcc_home}/${unixdirname}"},
      {"target-icc": "${gcc_home}/${unixdirname}"},
    ))

    msg.debug("atlas: loading toolchain...")
    msg.debug("atlas: path=%s" % (ctx.env["LCG_COMPILER_ROOT"]))
    ctx.load('find_compiler')
    path = ctx.env['LCG_COMPILER_ROOT']
    ctx.find_toolchain(override=True, path=path, mandatory=True)
    ctx.msg("ATLAS C compiler", ctx.env['CC'])
    ctx.msg("ATLAS CXX compiler", ctx.env['CXX'])
    ctx.msg("ATLAS Fortran compiler", ctx.env['FC'])
    
    ctx.load('find_posixlibs')
    if not ctx.hwaf_enabled_tag("target-windows"):
        #ctx.find_posixlibs(override=True)
        ctx.hwaf_macro_append("LIB_dl", "dl")
        ctx.hwaf_macro_append("STLIB_bfd", "bfd")
        ctx.hwaf_macro_append("LIB_uuid", "uuid")
        ctx.hwaf_macro_append("LIB_pthread", "pthread")
        pass
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    return # build

## EOF ##
