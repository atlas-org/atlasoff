## -*- python -*-
## waf imports
import waflib.Logs as msg

PACKAGE = {
    "name":    "Trigger/TrigConfiguration/TriggerMenuCompiler",
    "authors": ["Ralf.Spiwoks@cern.ch"],
    "managers": ["Ralf.Spiwoks@cern.ch"],

}

### ---------------------------------------------------------------------------
def pkg_deps(ctx):
    
    ## public dependencies
    ctx.use_pkg("DetCommonPolicy", version="*", public=True)
    ctx.use_pkg("LCG_Interfaces/XercesC", version="v*", public=True)
    ctx.use_pkg("External/JavaSDK", version="*", public=True)
    
    ## no private dependencies
    ## no runtime dependencies
    return # pkg_deps


### ---------------------------------------------------------------------------
def options(ctx):
    
    return # options


### ---------------------------------------------------------------------------
def configure(ctx):
    
    ctx.hwaf_macro_remove("cppflags", (
      {"default": ""},
      {"target-darwin": "-pedantic"},
    ))

    # ctx.hwaf_declare_macro("application_suffix", (
    #   {"default": ""},
    # ))
    
    return # configure


### ---------------------------------------------------------------------------
def build(ctx):
    
    
    ctx(
        features = "atlas_library",
        name     = "TriggerMenuCompiler",
        target   = "TriggerMenuCompiler",
        source   = [
            "src/TMCTeeBuffer.cxx",
            "src/TMCUtilities.cxx",
            "src/TMCErrorHandler.cxx",
            "src/TMCLineNumberTag.cxx",
            "src/TMCDomParser.cxx",
            "src/TMCCommon.cxx",
            "src/TMCObject.cxx",
            "src/TMCConfiguration.cxx",
            "src/TMCNode.cxx",
            "src/TMCTree.cxx",
            "src/TMCDevice.cxx",
            "src/TMCNet.cxx",
            "src/TMCPlacedObject.cxx",
            "src/CentralTriggerProcessor.cxx",
            "src/PatternInTime.cxx",
            "src/TriggerInputSignal.cxx",
            "src/TriggerInputCable.cxx",
            "src/TriggerElement.cxx",
            "src/TriggerThreshold.cxx",
            "src/TriggerCondition.cxx",
            "src/TriggerCombination.cxx",
            "src/TriggerCombinationClique.cxx",
            "src/ContentAddressableMemory.cxx",
            "src/SumTermResult.cxx",
            "src/TriggerSumTerm.cxx",
            "src/TriggerItem.cxx",
            "src/TriggerMenu.cxx",
            "src/LookupTable.cxx",
            "src/SwitchMatrix.cxx",
            "src/CliquePlacement.cxx",
            "src/FirstFitPlacement.cxx",
            "src/RoutedPlacement.cxx",
            "src/TriggerMenuCompiler.cxx",
            "src/TriggerMenuComparison.cxx"],
        use = ["XercesC", "JavaSDK"],
    )
    
    ctx(
        features = "detcommon_generic_install",
        name     = "TriggerMenuCompiler-generic-install-TMC_XMLs-XML",
        target   = "TriggerMenuCompiler-generic-install-TMC_XMLs-XML",
        source   = ["data/*.dtd", "data/ctp.xml"],
    )
    
    ctx(
        features = "detcommon_install_headers",
        name     = "TriggerMenuCompiler-install-headers",
        target   = "TriggerMenuCompiler-install-headers",
        source   = [],
    )
    
    ctx(
        features = "atlas_library",
        name     = "TriggerMenuCompilerProxyImpl",
        target   = "TriggerMenuCompilerProxyImpl",
        source   = ["TriggerMenuCompilerProxyImpl.cxx"],
        use = ["TriggerMenuCompiler", "XercesC"],
    )
    
    ctx(
        features = "atlas_application",
        name     = "compareTriggerMenu",
        target   = "compareTriggerMenu",
        source   = ["src/test/compareTriggerMenu.cxx",],
        use = ["TriggerMenuCompiler",],
    )
    
    ctx(
        features = "atlas_application",
        name     = "copyTriggerMenu",
        target   = "copyTriggerMenu",
        source   = ["src/test/copyTriggerMenu.cxx",],
        use = ["TriggerMenuCompiler",],
    )
    
    ctx(
        features = "atlas_application",
        name     = "testBinPacking",
        target   = "testBinPacking",
        source   = ["src/test/testBinPacking.cxx",],
        use = ["TriggerMenuCompiler",],
    )
    
    ctx(
        features = "atlas_application",
        name     = "triggerMenuCompilerApp",
        target   = "triggerMenuCompilerApp",
        source   = ["src/test/triggerMenuCompilerApp.cxx",],
        use = ["TriggerMenuCompiler",],
    )
    return # build

## EOF ##
