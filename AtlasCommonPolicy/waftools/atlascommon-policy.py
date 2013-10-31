# -*- python -*-

## stdlib imports
import os
import os.path as osp
import re
import sys

## waf imports
import waflib.Errors
import waflib.Logs as msg
import waflib.Utils
import waflib.Configure
import waflib.Build
import waflib.Task
import waflib.Tools.ccroot
from waflib.Configure import conf
from waflib.TaskGen import feature, before_method, after_method, extension, after


### ---------------------------------------------------------------------------
@feature('cxx', 'c')
@after_method('apply_incpaths')
def _atlas_insert_blddir(self):
    self.env.prepend_value('INCPATHS', self.env.BUILD_INSTALL_AREA_INCDIR)
    self.env.prepend_value('INCPATHS', self.env.INSTALL_AREA_INCDIR)
    self.env.prepend_value('INCPATHS', '.')

    self.env.prepend_value('LIBPATH', self.env.BUILD_INSTALL_AREA_LIBDIR)
    return

### ---------------------------------------------------------------------------
@feature('hwaf_runtime_tsk', '*')
@before_method('process_rule')
def _atlas_insert_project_level_pythonpath(self):
    '''
    _atlas_insert_project_level_pythonpath adds ${INSTALL_AREA}/python into the
    ${PYTHONPATH} environment variable.
    '''
    if not self.env.HWAF_ENABLE_INSTALL_AREA:
        return
    _get = getattr(self, 'hwaf_get_install_path', None)
    if not _get: _get = getattr(self.bld, 'hwaf_get_install_path')
    pydir = _get('${INSTALL_AREA}/python')
    self.env.prepend_value('PYTHONPATH', pydir)
    return

### ---------------------------------------------------------------------------
@feature('hwaf_runtime_tsk', '*')
@before_method('process_rule')
def _atlas_insert_project_level_joboptpath(self):
    '''
    _atlas_insert_project_level_joboptpath adds ${INSTALL_AREA}/jobOptions into the
    ${JOBOPTSEARCHPATH} environment variable.
    '''
    if not self.env.HWAF_ENABLE_INSTALL_AREA:
        return
    _get = getattr(self, 'hwaf_get_install_path', None)
    if not _get: _get = getattr(self.bld, 'hwaf_get_install_path')
    d = _get('${INSTALL_AREA}/jobOptions')
    self.env.prepend_value('JOBOPTSEARCHPATH', d)
    return

### ---------------------------------------------------------------------------
@feature('hwaf_runtime_tsk', '*')
@before_method('process_rule')
def _atlas_insert_project_level_datapath(self):
    '''
    _atlas_insert_project_level_datapath adds ${INSTALL_AREA}/share into the
    ${DATAPATH} environment variable.
    '''
    if not self.env.HWAF_ENABLE_INSTALL_AREA:
        return
    _get = getattr(self, 'hwaf_get_install_path', None)
    if not _get: _get = getattr(self.bld, 'hwaf_get_install_path')
    d = _get('${INSTALL_AREA}/share')
    self.env.prepend_value('DATAPATH', d)
    return

### ---------------------------------------------------------------------------
@feature('hwaf_runtime_tsk', '*')
@before_method('process_rule')
def _atlas_insert_project_level_xmlpath(self):
    '''
    _atlas_insert_project_level_xmlpath adds ${INSTALL_AREA}/XML into the
    ${XMLPATH} environment variable.
    '''
    if not self.env.HWAF_ENABLE_INSTALL_AREA:
        return
    _get = getattr(self, 'hwaf_get_install_path', None)
    if not _get: _get = getattr(self.bld, 'hwaf_get_install_path')
    d = _get('${INSTALL_AREA}/XML')
    self.env.prepend_value('XMLPATH', d)
    return

### ---------------------------------------------------------------------------
@conf
def atlas_install_python_modules(ctx, **kw):
    # extract package name
    PACKAGE_NAME = osp.basename(ctx.hwaf_pkg_name())

    #source = waflib.Utils.to_list(source)
    pydir = ctx.path.find_dir('python')
    if not pydir:
        msg.error(
            '[%s] no such directory: [%s]' % (
                ctx.hwaf_pkg_name(),
                os.path.join(ctx.path.abspath(), 'python'),
                )
            )
        msg.error('cannot execute [atlas_install_python_modules]')
        return
    pyfiles = pydir.ant_glob(
        '**/*.py',
        dir=False,
        relative_trick=True,
        )
    ctx(
        features     = 'py',
        name         = 'py-%s' % PACKAGE_NAME,
        source       = pyfiles,
        install_path = '${INSTALL_AREA}/python/%s' % PACKAGE_NAME,
        )
    return

### ---------------------------------------------------------------------------
@conf
def atlas_install_scripts(ctx, **kw):
    # extract package name
    PACKAGE_NAME = osp.basename(ctx.hwaf_pkg_name())

    source = kw.get('source', 'scripts/*')
    
    source = waflib.Utils.to_list(source)
    _srcs = []
    for f in source:
        _srcs.extend(ctx.path.ant_glob(f, dir=False))
    source = _srcs[:]
    del _srcs
    
    ctx.install_files(
        '${INSTALL_AREA}/bin',
        source, 
        #relative_trick=True,
        chmod=waflib.Utils.O755,
        )
    return

### ---------------------------------------------------------------------------
@conf
def atlas_dictionary(ctx, **kw):

    kw = dict(kw)

    name = kw["name"]
    source = kw["source"]
    del kw["name"]
    del kw["source"]

    if 'selection_file' in kw:
        selection_file = kw["selection_file"]
        del kw["selection_file"]
    
        o = ctx.build_reflex_dict(
            name = name,
            source = source,
            selection_file = selection_file,
            **kw
            )

    else:
        linkdef = kw['rootcint_linkdef']
        del kw['rootcint_linkdef']

        o = ctx.build_rootcint_dict(
            name = name,
            source = source,
            rootcint_linkdef = linkdef,
            **kw
        )

    return o


### ---------------------------------------------------------------------------
@conf
def atlas_install_joboptions(ctx, **kw):
    # extract package name
    PACKAGE_NAME = osp.basename(ctx.hwaf_pkg_name())

    jobo_dir = ctx.path.find_dir('share')
    jobos = jobo_dir.ant_glob('**/*.py',  dir=False) + \
            jobo_dir.ant_glob('**/*.txt', dir=False)
    
    ctx.install_files(
        '${INSTALL_AREA}/jobOptions/%s' % PACKAGE_NAME,
        jobos,
        cwd=jobo_dir,
        relative_trick=True
        )
    return

### ---------------------------------------------------------------------------
@conf
def atlas_install_xmls(ctx, **kw):
    # extract package name
    PACKAGE_NAME = osp.basename(ctx.hwaf_pkg_name())

    source = kw['source']
    relative_trick = kw.get('relative_trick', True)
    cwd = kw.get('cwd', None)
    if cwd:
        cwd = waflib.Utils.to_list(cwd)[0]
        cwd = ctx.path.find_dir(cwd)
        
    source = waflib.Utils.to_list(source)
    _srcs = []
    for f in source:
        _srcs.extend(ctx.path.ant_glob(f, dir=False))
    source = _srcs[:]
    del _srcs

    ctx.install_files(
        '${INSTALL_AREA}/XML/%s' % PACKAGE_NAME,
        source, 
        relative_trick=relative_trick,
        cwd=cwd,
        postpone=False,
        )
    return

### ---------------------------------------------------------------------------
@conf
def atlas_install_data(ctx, **kw):
    # extract package name
    PACKAGE_NAME = osp.basename(ctx.hwaf_pkg_name())

    source = kw['source']
    relative_trick = kw.get('relative_trick', False)
    cwd = kw.get('cwd', None)
    if cwd:
        cwd = waflib.Utils.to_list(cwd)[0]
        cwd = ctx.path.find_dir(cwd)
        
    source = waflib.Utils.to_list(source)
    _srcs = []
    for f in source:
        _srcs.extend(ctx.path.ant_glob(f, dir=False))
    source = _srcs[:]
    del _srcs

    ctx.install_files(
        '${INSTALL_AREA}/share',
        source, 
        relative_trick=relative_trick,
        cwd=cwd,
        postpone=False,
        )
    return

### -----------------------------------------------------------------------------
@conf
def atlas_install_headers(ctx, **kw):
    # extract package name
    PACKAGE_NAME = osp.basename(ctx.hwaf_pkg_name())

    incdir = kw.get('incdir', None)
    relative_trick = kw.get('relative_trick', True)
    cwd = kw.get('cwd', None)
    
    inc_node = None
    if not incdir:
        inc_node = ctx.path.find_dir(PACKAGE_NAME)
        if not inc_node:
            return
    else:
        if isinstance(incdir, str):
            inc_node = ctx.path.find_dir(incdir)
        else:
            inc_node = incdir
            pass
        pass
    
    if isinstance(cwd, str):
        cwd = ctx.path.find_dir(cwd)
        
    if not inc_node:
        ctx.fatal('no such directory [%s] (pkg=%s)' % (incdir, ctx.hwaf_pkg_name()))
        pass
    
    includes = inc_node.ant_glob('**/*', dir=False)
    ctx.install_files(
        '${INSTALL_AREA}/include', includes, 
        relative_trick=relative_trick,
        cwd=cwd,
        postpone=False,
        )

    incpath = waflib.Utils.subst_vars('${INSTALL_AREA}/include',ctx.env)
    ctx.env.append_unique('INCLUDES_%s' % PACKAGE_NAME,
                           [incpath,inc_node.parent.abspath()])
    
    # msg.info("--> [%s] %s: %r" %(PACKAGE_NAME,incpath,
    #                              ctx.env.get_flat('INCLUDES_%s'%PACKAGE_NAME)))
    return
    
### -----------------------------------------------------------------------------
@conf
def atlas_generic_install(ctx, **kw):
    # extract package name
    PACKAGE_NAME = osp.basename(ctx.hwaf_pkg_name())

    source = waflib.Utils.to_list(kw['source'])
    source = [ctx.hwaf_subst_vars(s) for s in source]
    prefix = kw.get('install_prefix', 'share/'+PACKAGE_NAME)
    relative_trick = kw.get('relative_trick', True)
    cwd = kw.get('cwd', None)

    do_dbg = kw.get('name', '') == "xxxx"
    if do_dbg:
        print ">>>>>>",source
        
    srcs = []
    for s in source:
        pp = ctx.path
        idx = 0
        if osp.isabs(s):
            pp = ctx.root
            ### drop leading '/'
            ### does NOT work: ctx.root.ant_glob("/usr/include/*.h")
            ### this DOES:     ctx.root.ant_glob("usr/include/*.h")
            idx = 1
        if do_dbg:
            print ">>>>>> <<",s
        if '*' in s:
            src = pp.ant_glob(s[idx:], dir=False)
        else:
            src = [pp.find_or_declare(s)]
            if not src and pp == ctx.path:
                pp = ctx.path.get_bld()
                pp.mkdir()
                if '*' in s: src = pp.ant_glob(s, dir=False)
                else:        src = [pp.find_or_declare(s)]
        if do_dbg:
            print ("*** [%s] ==> %s" % (s, src))
        srcs.extend(src)
        pass
    source = srcs    
    if do_dbg:
        print "::: sources:",source
    if not source:
        ctx.fatal('[%s] [atlas_generic_install] got no file to install [source=%s]' %
                  (ctx.hwaf_pkg_name(),
                   kw['source'],)
                  )
    del kw['source']

    try:
        ctx.install_files(
            '${INSTALL_AREA}/%s' % prefix,
            source, 
            relative_trick=relative_trick,
            cwd=cwd,
            #postpone=False,
            )
    except Exception, err:
        print ">>>>",err
        raise
    return

### ---------------------------------------------------------------------------
@conf
def atlas_install_runtime_extras(ctx, **kw):
    kw['install_prefix'] = 'share'
    kw['features'] = ['atlas_generic_install'] + waflib.Utils.to_list(kw.get('features', []))
    return ctx(**kw)

### ---------------------------------------------------------------------------
@conf
def atlas_library(ctx, **kw):
    # extract package name
    PACKAGE_NAME = osp.basename(ctx.hwaf_pkg_name())

    kw = dict(kw)
    name = kw['name']
    source = kw["source"]
    del kw['name']
    del kw['source']
    
    linkflags = kw.get('linkflags', [])
    linkflags = ctx.env.SHLINKFLAGS + linkflags
    kw['linkflags'] = linkflags
    
    src_node = ctx.path.find_dir('src')

    srcs = ctx._cmt_get_srcs_lst(source)
    includes = waflib.Utils.to_list(kw.get('includes', []))
    includes.insert(0, ctx.path.abspath())
    kw['includes'] = includes + [src_node]

    export_incs = None
    kw['export_includes'] = waflib.Utils.to_list(
        kw.get('export_includes', [])
        )[:]
    if not kw['export_includes']:
        inc_node = ctx.path.find_dir(PACKAGE_NAME)
        if inc_node:
            export_incs = '.'
            kw['export_includes'].append(export_incs)
    else:
        export_incs = kw['export_includes']
        #msg.info('%s: exports: %r' % (name, kw['export_includes']))
        pass

    kw['includes'].extend(kw['export_includes'])
    
    kw['use'] = waflib.Utils.to_list(kw.get('use', [])) + ['dl']
    
    defines = waflib.Utils.to_list(kw.get('defines', []))
    kw['defines'] = defines + ctx._get_pkg_version_defines()

    kw['features'] = waflib.Utils.to_list(kw.get('features', [])) + [
        'cxx', 'cxxshlib', 'symlink_tsk',
        ]
    kw['target'] = kw.get('target', name)
    
    #msg.info ("==> atlas_library(%s, '%s', %r)..." % (name, srcs, kw.keys()))
    o = ctx(
        name            = name,
        source          = srcs,
        install_path    = '${INSTALL_AREA}/lib',
        libpath = ctx.env.LD_LIBRARY_PATH + [ctx.path.get_bld().abspath()],
        **kw
        )
    o.reentrant = True
    # for use-exports
    # FIXME: also propagate uses ?
    ctx.env['LIB_%s' % name] = [name]
    ctx.env.append_unique('LIBPATH_%s'%name, ctx.path.get_bld().abspath())
    #msg.info('--> libpath[%s]: %s' % (name, ctx.env['LIBPATH_%s'%name]))
    #msg.info('--> incpath[%s]: %s' % (name, export_incs))
    if export_incs:
        export_incs = waflib.Utils.to_list(export_incs)[0]
        if export_incs == '.':
            ctx.atlas_install_headers()
            pass
        pass
    
    return o

### ---------------------------------------------------------------------------
@conf
def atlas_component(ctx, **kw):
    kw = dict(kw)
    do_genmap = kw.get('do_genmap', True)
    do_genconf= kw.get('do_genconf', True)
    do_gencliddb= kw.get('do_gencliddb', True)
    
    name = kw['name']
    source = kw["source"]
    del kw['name']
    del kw['source']

    #msg.info('=========== %s ============' % name)
    #msg.info("::: %s" % ctx.path.abspath())
    src_node = ctx.path.find_dir('src')
    bld_node = src_node.get_bld()

    srcs = ctx._cmt_get_srcs_lst(source)
    includes = waflib.Utils.to_list(kw.get('includes', []))
    includes.insert(0, ctx.path.abspath())
    includes.insert(1, ctx.path.get_bld().abspath())
    #includes.insert(1, ctx.path.abspath()+'/'+PACKAGE_NAME)
    kw['includes'] = includes + [src_node]

    linkflags = waflib.Utils.to_list(kw.get('linkflags', []))
    linkflags = ctx.env.SHLINKFLAGS + linkflags
    kw['linkflags'] = linkflags

    defines = waflib.Utils.to_list(kw.get('defines', []))
    kw['defines'] = defines + ctx._get_pkg_version_defines()

    kw['depends_on'] = waflib.Utils.to_list(kw.get('use', [])) + \
                       waflib.Utils.to_list(kw.get('depends_on', []))
    #print("---> depends: %s" % kw['depends_on'])
    
    # extract package name
    PACKAGE_NAME = osp.basename(ctx.hwaf_pkg_name())

    # schedule the requested features
    features = ['cxx', 'cxxshlib',]
    features.append('symlink_tsk')
    if do_genmap:
        features.append('gen_map')
    if do_genconf:
        features.append('gen_conf')
        #features.append('py')
    if do_gencliddb:
        features.append('gen_cliddb')

    kw['features'] = waflib.Utils.to_list(kw.get('features',[])) + features
    kw['target'] = kw.get('target', name)
    kw['use'] = waflib.Utils.to_list(kw.get('use', [])) + ["Reflex"]
    
    lib = ctx(
        name=name,
        source=srcs,
        **kw)
    lib.name = 'complib-%s' % name
    lib.reentrant = True
    lib.install_path = '${INSTALL_AREA}/lib'
    lib.libpath = ctx.env.LD_LIBRARY_PATH + [ctx.path.get_bld().abspath()]
    lib_name = "lib%s.so" % (lib.target,) # FIXME !!
    lib.env['GENCONF_LIBNAME'] = lib.target
    lib.env['PACKAGE_NAME'] = PACKAGE_NAME
    
    return lib

### ---------------------------------------------------------------------------
@conf
def atlas_dual_use_library(ctx, **kw):
    
    # extract package name
    PACKAGE_NAME = osp.basename(ctx.hwaf_pkg_name())

    name = kw['name']
    source = kw['source']
    
    srcs = ctx._cmt_get_srcs_lst(source)
    link_libname = name
    link_kw = dict(kw)
    link_kw['name'] = link_libname
    link_kw['source'] = srcs
    _ = link_kw.pop('target', None)
    link_o = ctx.atlas_library(**link_kw)

    comp_kw = dict(kw)
    comp_libname = name + "Comps"
    comp_kw['name'] = comp_libname
    comp_uses = waflib.Utils.to_list(comp_kw.get('use', [])) + ["Reflex"]
    comp_kw['use'] = [link_libname] + comp_uses
    src_dir = ctx.path.find_dir('src')
    if not src_dir:
        ctx.fatal("no 'src' directory in package [%s]!" % ctx.hwaf_pkg_name())
        pass
    comp_dir = src_dir.find_dir('components')
    if not comp_dir:
        ctx.fatal("no 'src/components' directory in package [%s]!" %
                   ctx.hwaf_pkg_name())
        pass

    pydir = ctx.path.find_dir('python')
    if not pydir:
        pydir = ctx.path.find_or_declare('python')
        pydir.mkdir()
        pydir.make_node('__init__.py')
        pass
    pyredirect = pydir.make_node(name+'Conf.py')
    pyredirect.write(
'''## redirect %s.%sConf to %s.%sConf
from %s.%sConf import *
## EOF ##
''' % (PACKAGE_NAME, comp_libname,
       PACKAGE_NAME, link_libname,
       PACKAGE_NAME, comp_libname)
        )

    comp_srcs = comp_dir.ant_glob("*.cxx")
    comp_kw['source'] = srcs + comp_srcs
    _ = comp_kw.pop('target', None)
    comp_o = ctx.atlas_component(**comp_kw)
    return

### ---------------------------------------------------------------------------
@conf
def atlas_tpcnv(ctx, **kw):
    kw['features'] = ['atlas_library', 'gen_map'] + waflib.Utils.to_list(kw.get('features', []))
    return ctx(**kw)

### ---------------------------------------------------------------------------
@conf
def atlas_pyext(ctx, **kw):
    return

### ---------------------------------------------------------------------------
@conf
def atlas_unittest(ctx, **kw):
    features = waflib.Utils.to_list(kw.get('features', []))
    if not 'hwaf_utest' in features:
        features.append('hwaf_utest')
        pass
    if not 'atlas_application' in features:
        features.append('atlas_application')
        pass
    kw['features'] = features

    use = waflib.Utils.to_list(kw.get('use', []))
    if not 'TestTools' in use:
        use.append('TestTools')
        pass
    kw['use'] = use
    
    return ctx(**kw)

### ---------------------------------------------------------------------------
@conf
def atlas_athenarun_test(ctx, **kw):
    features = waflib.Utils.to_list(kw.get('features', []))
    if not 'hwaf_utest' in features:
        features.append('hwaf_utest')
        pass
    kw['features'] = features
    
    return ctx(**kw)

### ---------------------------------------------------------------------------
@conf
def atlas_application(ctx, **kw):
    kw = dict(kw)

    name = kw['name']
    source = kw["source"]
    del kw['name']
    del kw['source']

    kw['features'] = waflib.Utils.to_list(
        kw.get('features', '')) + [
        'cxx', 'cxxprogram', 'symlink_tsk',
        ]
    
    kw['use'] = waflib.Utils.to_list(kw.get('use', []))

    pkg_node = ctx.path.get_src()
    src_node = ctx.path.find_dir('src')

    srcs = ctx._cmt_get_srcs_lst(source)
    linkflags = waflib.Utils.to_list(kw.get('linkflags', []))
    linkflags = ctx.env.SHLINKFLAGS + linkflags
    kw['linkflags'] = linkflags

    defines = waflib.Utils.to_list(kw.get('defines', []))
    kw['defines'] = defines + ctx._get_pkg_version_defines()
    
    includes = waflib.Utils.to_list(kw.get('includes', []))
    includes.insert(0, ctx.path.abspath())
    #includes.insert(1, ctx.path.abspath()+'/'+PACKAGE_NAME)
    kw['includes'] = includes + [src_node]

    # extract package name
    PACKAGE_NAME = ctx._get_pkg_name()

    exe = ctx(
        name=name,
        source=srcs,
        **kw)
    exe.install_path = '${INSTALL_AREA}/bin'
    exe.libpath = ctx.env.LD_LIBRARY_PATH + [ctx.path.get_bld().abspath()]
    exe.target = name+'.exe'
    
    return exe

### ----------------------------------------------------------------------------
@feature('gen_conf')
@after('symlink_tsk')
def schedule_gen_conf(self):
    lnk_task = getattr(self, 'link_task', None)
    if not lnk_task:
        return
    for n in lnk_task.outputs:
        gen_conf_hook(self, n)
    pass

@after('symlink_tsk')
def gen_conf_hook(self, node):
    "Bind the .dsomap file extension to the creation of a genconf task"
    dso = self.env['GENCONF_LIBNAME']
    bld_node = node.get_bld().parent
    pkg_name = bld_node.name # FIXME!!
    genconf_dir_node = bld_node.make_node('genConf').make_node(pkg_name)
    self.env['GENCONF_OUTPUTDIR'] = genconf_dir_node.abspath()
    genconf_node = genconf_dir_node.make_node('%sConf.py' % dso)
    initpy_node = genconf_dir_node.make_node('__init__.py')
    confdb_node = genconf_dir_node.make_node('%s_confDb.py' % dso)
    tsk = self.create_task('gen_conf',
                           node,
                           [genconf_node,genconf_dir_node,initpy_node,confdb_node])
    # schedule the merge of confdb.py files
    merge_confdb_hook(self, confdb_node).set_run_after(tsk)

    # schedule the installation of py-files
    src_node = self.path.get_src()
    py_dir = src_node.find_dir('python')
    py_files = [genconf_node, confdb_node]
    if not py_dir:
        py_files.append(initpy_node)
    PACKAGE_NAME = self.env['PACKAGE_NAME']
    self.bld(
        features='py',
        name    ='py-genconf-%s' % PACKAGE_NAME,
        source  = py_files,
        install_path = '${INSTALL_AREA}/python/%s' % PACKAGE_NAME,
        )

    # add ${INSTALL_AREA}/python to PYTHONPATH if not there already
    pypath = waflib.Utils.subst_vars('${INSTALL_AREA}/python', self.env)
    if not pypath in self.env.get_flat('PYTHONPATH'):
        self.env.prepend_value('PYTHONPATH', pypath)
        pass
    
    return

class gen_conf(waflib.Task.Task):
    vars = ['GENCONF', 'DEFINES', 'INCLUDES', 'GENCONF_CONFIGURABLE_MODULE']
    color= 'BLUE'
    ext_in  = ['.bin', '.so']
    ext_out = ['.py']
    shell = False
    reentrant = True
    after = ['cxxshlib', 'cxxprogram', 'symlink_tsk', 'gen_map']
    depends_on = ['genconf', 'complib-GaudiCoreSvc']
    
    def run(self):
        import os
        cmd = '${GENCONF} -p ${PACKAGE_NAME} -i %s -o ${GENCONF_OUTPUTDIR} --configurable-module ${GENCONF_CONFIGURABLE_MODULE}' % (
            self.inputs[0].name,
            )
        cmd = waflib.Utils.subst_vars(cmd, self.env)

        bld_node = self.inputs[0].parent.get_bld()
    
        o = self.outputs[0].change_ext('.genconf.log')
        fout_node = bld_node.find_or_declare(o.name)
        fout = open(fout_node.abspath(), 'w')
        env = self.generator.bld._get_env_for_subproc()
        rc = self.generator.bld.exec_command(
            cmd,
            stdout=fout,
            stderr=fout,
            env=env
            )
        if rc != 0:
            msg.error("** error running [%s]" % cmd)
            msg.error(fout_node.read())
        return rc
    
### ---------------------------------------------------------------------------
g_confdb_merger = None
@feature('merge_confdb')
def schedule_merge_confdb(self):
    pass

@extension('_confDb.py')
def merge_confdb_hook(self, node):
    global g_confdb_merger
    if g_confdb_merger is None:
        import os
        bld_area = os.path.basename(self.env['BUILD_INSTALL_AREA'])
        bld_node = self.bld.bldnode.find_dir(bld_area)
        py_node = bld_node.make_node('python')
        py_node.mkdir()
        out_node = py_node.make_node(
            'project_%s_merged_confDb.py' %
            self.bld.hwaf_project_name().replace('-', '_')
            )
        g_confdb_merger = self.create_task('merge_confdb', node, out_node)
        self.bld.install_files(
            '${INSTALL_AREA}/python',
            out_node,
            relative_trick=False
            )
    else:
        g_confdb_merger.inputs.append(node)
    return g_confdb_merger

class merge_confdb(waflib.Task.Task):
    color='PINK'
    ext_in = ['_confDb.py']
    #ext_out= ['.py']
    after = ['merge_dsomap',]
    run_str = 'cat ${SRC} > ${TGT}'
    reentrant = False
    
    def runnable_status(self):
        status = waflib.Task.Task.runnable_status(self)
        if status == waflib.Task.ASK_LATER:
            return status
        
        import os
        for in_node in self.inputs:
            try:
                os.stat(in_node.abspath())
            except:
                msg.debug("::missing input [%s]" % in_node.abspath())
                return waflib.Task.ASK_LATER
        return waflib.Task.RUN_ME
    

### utils


### ---------------------------------------------------------------------------
import waflib.Build
waflib.Build.BuildContext.atlas_component = atlas_component
waflib.Build.BuildContext.atlas_library = atlas_library
waflib.Build.BuildContext.atlas_application = atlas_application

waflib.Build.BuildContext.atlas_install_headers = atlas_install_headers

