## -*- python -*-
## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "AtlasTest/ControlTest",
    "authors": ["Paolo Calafiura <Paolo.Calafiura@cern.ch>"],


}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("AtlasPolicy", version="AtlasPolicy-*", public=True)
    ctx.use_pkg("Control/MinimalRunTime", version="MinimalRunTime-*", public=True)
    ctx.use_pkg("TestPolicy", version="TestPolicy-*", public=True)
    ctx.use_pkg("AtlasTest/TestTools", version="TestTools-*", public=True)
    ctx.use_pkg("Control/AthenaPython", version="AthenaPython-*", public=True)
    ctx.use_pkg("Control/AthenaExamples/AthExFortranAlgorithm", version="AthExFortranAlgorithm-*", public=True)
    ctx.use_pkg("Control/AthenaExamples/AthExStoreGateExample", version="AthExStoreGateExample-*", public=True)
    
    ## private dependencies
    ctx.use_pkg("External/GaudiInterface", version="GaudiInterface-*", private=True)
    ctx.use_pkg("Control/AthenaKernel", version="AthenaKernel-*", private=True)
    ctx.use_pkg("Control/AthContainers", version="AthContainers-*", private=True)
    ctx.use_pkg("Control/AthLinks", version="AthLinks-*", private=True)
    ctx.use_pkg("Control/DataModel", version="DataModel-*", private=True)
    ctx.use_pkg("Control/SGTools", version="SGTools-*", private=True)
    ctx.use_pkg("Control/StoreGate", version="StoreGate-*", private=True)
    ctx.use_pkg("Control/AthenaExamples/ToyConversion", version="ToyConversion-*", private=True)
    
    ## runtime dependencies
    ctx.use_pkg("Control/MinimalRunTime", version="MinimalRunTime-*", runtime=True)
    ctx.use_pkg("Control/AthenaPython", version="AthenaPython-*", runtime=True)
    ctx.use_pkg("Control/AthenaExamples/AthExFortranAlgorithm", version="AthExFortranAlgorithm-*", runtime=True)
    ctx.use_pkg("Control/AthenaExamples/AthExStoreGateExample", version="AthExStoreGateExample-*", runtime=True)
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    #### macro &{{SGGoptignore [{default []} {optimized [|Retrieved const handle to default object|of type EventInfo|object not modifiable when retrieved|requestRelease]}]}}
    ctx.hwaf_declare_macro("SGGoptignore", (
      {"default": ""},
      {"optimized": ["|Retrieved", "const", "handle", "to", "default", "object|of", "type", "EventInfo|object", "not", "modifiable", "when", "retrieved|requestRelease"]},
    ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ##### **** statement *hlib.ApplyPatternStmt (&{install_applications []})
    ##### **** statement *hlib.ApplyPatternStmt (&{install_xmls []})
    
    ctx(
        features = "atlas_install_joboptions",
        name     = "ControlTest-install-jobos",
        target   = "ControlTest-install-jobos",
        source   = ["share/*.py", "share/*.txt"],
    )
    
    ctx(
        features = "atlas_install_python_modules",
        name     = "ControlTest-install-py",
        target   = "ControlTest-install-py",
        source   = ["python/*.py"],
    )
    
    ctx(
        features = "atlas_athenarun_test",
        name     = "ControlTest-runtest-FortranAlgorithm",
        target   = "ControlTest-runtest-FortranAlgorithm",
        source   = [],
        use = ["ControlTest"],
        joboptions = ["AthExFortranAlgorithm/FortranAlgorithmOptions.py"],
        post_script = ["${TESTTOOLSROOT}/share/post.sh FortranAlgorithm $(q)^Py:ConfigurableDb +(WARNING|INFO|ERROR)|Py:Athena +INFO including file |Warning in .TEnvRec::ChangeValue.: duplicate entry|calling initialize_|ToolSvc.finalize.. +INFO| [A-Z]+ 2[0-9][0-9][0-9]$$|^Py:Athena +INFO|[Rr]oo[Ff]it|NIKHEF|DeprecationWarning: object.__new__|^ newobj =|^\\*+$$|drop-and-reload|^ *$$|we will keep the configuration around|ApplicationMgr +INFO$(q)"],
    )
    
    ctx(
        features = "atlas_athenarun_test",
        name     = "ControlTest-runtest-StoreGateGen",
        target   = "ControlTest-runtest-StoreGateGen",
        source   = [],
        use = ["ControlTest"],
        joboptions = ["AthExStoreGateExample/StoreGateExample_Gen_jobOptions.py"],
        post_script = ["${TESTTOOLSROOT}/share/post.sh StoreGateGen $(q)^Py:ConfigurableDb +(WARNING|INFO|ERROR)|Py:Athena +INFO including file |Warning in .TEnvRec::ChangeValue.: duplicate entry|ToolSvc.finalize.. +INFO|^WriteData +INFO in initialize$$| [A-Z]+ 2[0-9][0-9][0-9]$$$(SGGoptignore)|^Py:Athena +INFO|[Rr]oo[Ff]it|NIKHEF|DeprecationWarning: object.__new__|^ newobj =|^\\*+$$|drop-and-reload|^ *$$|we will keep the configuration around|object not modifiable when retrieved|Retrieved const handle to default|type EventInfo|^StoreGateSvc +DEBUG|^ of type|object modifiable when retrieved|ApplicationMgr +INFO$(q)"],
    )
    
    ctx(
        features = "atlas_unittest",
        name     = "ControlTest-test-CircularDep",
        target   = "ControlTest-test-CircularDep",
        source   = ["test/CircularDep_test.cxx"],
        use = ["MinimalRunTime", "TestPolicy", "TestTools", "AthenaPython", "GaudiKernel", "AthenaKernel", "AthContainers", "AthLinks", "DataModel", "SGTools", "StoreGate", "ToyConversion"],
        extrapatterns = ["^JobOptionsSvc +INFO"],
    )
    
    ctx(
        features = "atlas_unittest",
        name     = "ControlTest-test-ClearStore",
        target   = "ControlTest-test-ClearStore",
        source   = ["test/ClearStore_test.cxx"],
        use = ["MinimalRunTime", "TestPolicy", "TestTools", "AthenaPython", "GaudiKernel", "AthenaKernel", "AthContainers", "AthLinks", "DataModel", "SGTools", "StoreGate", "ToyConversion",
               "SGtests",
               ],
        extrapatterns = ["^JobOptionsSvc +INFO"],
    )
    
    ctx(
        features = "atlas_unittest",
        name     = "ControlTest-test-DataProxy",
        target   = "ControlTest-test-DataProxy",
        source   = ["test/DataProxy_test.cxx"],
        use = ["MinimalRunTime", "TestPolicy", "TestTools", "AthenaPython", "GaudiKernel", "AthenaKernel", "AthContainers", "AthLinks", "DataModel", "SGTools", "StoreGate", "ToyConversion"],
        extrapatterns = ["HistogramPersis.* +INFO|EventPersistenc.*INFO|^JobOptionsSvc +INFO"],
    )
    
    ctx(
        features = "atlas_unittest",
        name     = "ControlTest-test-ElementLink",
        target   = "ControlTest-test-ElementLink",
        source   = ["test/ElementLink_test.cxx"],
        use = ["MinimalRunTime", "TestPolicy", "TestTools", "AthenaPython", "GaudiKernel", "AthenaKernel", "AthContainers", "AthLinks", "DataModel", "SGTools", "StoreGate", "ToyConversion"],
        extrapatterns = ["^JobOptionsSvc +INFO"],
    )
    
    ctx(
        features = "atlas_unittest",
        name     = "ControlTest-test-ElementLinkVector",
        target   = "ControlTest-test-ElementLinkVector",
        source   = ["test/ElementLinkVector_test.cxx"],
        use = ["MinimalRunTime", "TestPolicy", "TestTools", "AthenaPython", "GaudiKernel", "AthenaKernel", "AthContainers", "AthLinks", "DataModel", "SGTools", "StoreGate", "ToyConversion"],
        extrapatterns = ["^JobOptionsSvc +INFO"],
    )
    
    ctx(
        features = "atlas_unittest",
        name     = "ControlTest-test-ProxyProviderSvc",
        target   = "ControlTest-test-ProxyProviderSvc",
        source   = ["test/ProxyProviderSvc_test.cxx"],
        use = ["MinimalRunTime", "TestPolicy", "TestTools", "AthenaPython", "GaudiKernel", "AthenaKernel", "AthContainers", "AthLinks", "DataModel", "SGTools", "StoreGate", "ToyConversion"],
        extrapatterns = ["$(PPSoptignore)^ClassIDSvc +DEBUG|Histogram.* (DEBUG|INFO)|DetectorStore +DEBUG|ToyConversionSvc +DEBUG|EventDataSvc +DEBUG|EventPersis.* +(DEBUG|INFO)|HistoryStore +DEBUG|^JobOptionsSvc +INFO|^DataProxy +VERBOSE"],
    )
    
    ctx(
        features = "atlas_unittest",
        name     = "ControlTest-test-SGDataLink",
        target   = "ControlTest-test-SGDataLink",
        source   = ["test/SGDataLink_test.cxx"],
        use = ["MinimalRunTime", "TestPolicy", "TestTools", "AthenaPython", "GaudiKernel", "AthenaKernel", "AthContainers", "AthLinks", "DataModel", "SGTools", "StoreGate", "ToyConversion"],
        extrapatterns = ["^JobOptionsSvc +INFO"],
    )
    
    ctx(
        features = "atlas_unittest",
        name     = "ControlTest-test-StoreGateSvcClient",
        target   = "ControlTest-test-StoreGateSvcClient",
        source   = ["test/StoreGateSvcClient_test.cxx"],
        use = ["MinimalRunTime", "TestPolicy", "TestTools", "AthenaPython", "GaudiKernel", "AthenaKernel", "AthContainers", "AthLinks", "DataModel", "SGTools", "StoreGate", "ToyConversion",
               "SGtests",
               ],
        extrapatterns = ["modifiable when retrieved|HistogramPersis.* +INFO|^JobOptionsSvc +INFO"],
    )
    return # build

## EOF ##
