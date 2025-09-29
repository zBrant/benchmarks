TUNE=base
LABEL=primeiro-teste-m64
NUMBER=523
NAME=xalancbmk_r
SOURCES= AIXPlatformUtils.cpp CSetDefs.cpp Win32PlatformUtils.cpp \
	 Win32MsgLoader.cpp Win32TransService.cpp Win32TransService2.cpp \
	 SunCCDefs.cpp SolarisPlatformUtils.cpp GCCDefs.cpp \
	 LinuxPlatformUtils.cpp MIPSproDefs.cpp IRIXPlatformUtils.cpp \
	 HPCCDefs.cpp HPPlatformUtils.cpp ASCIIRangeFactory.cpp AVT.cpp \
	 AVTPart.cpp AVTPartSimple.cpp AVTPartXPath.cpp AbstractDOMParser.cpp \
	 AbstractNumericFacetValidator.cpp AbstractNumericValidator.cpp \
	 AbstractStringValidator.cpp AllContentModel.cpp \
	 AnySimpleTypeDatatypeValidator.cpp AnyURIDatatypeValidator.cpp \
	 AttrImpl.cpp AttrMapImpl.cpp AttrNSImpl.cpp AttributeListImpl.cpp \
	 AttributesImpl.cpp BMPattern.cpp Base64.cpp \
	 Base64BinaryDatatypeValidator.cpp BinFileInputStream.cpp \
	 BinFileOutputStream.cpp BinInputStream.cpp BinMemInputStream.cpp \
	 BinMemOutputStream.cpp BinOutputStream.cpp BitSet.cpp \
	 BlockRangeFactory.cpp BooleanDatatypeValidator.cpp CDATASectionImpl.cpp \
	 CMAny.cpp CMBinaryOp.cpp CMUnaryOp.cpp CharToken.cpp \
	 CharacterDataImpl.cpp ChildNode.cpp ClosureToken.cpp CommentImpl.cpp \
	 ComplexTypeInfo.cpp ConcatToken.cpp ConditionToken.cpp Constants.cpp \
	 ContentLeafNameTypeVector.cpp ContentSpecNode.cpp CountersTable.cpp \
	 DFAContentModel.cpp DGXMLScanner.cpp DOMAttrImpl.cpp DOMAttrMapImpl.cpp \
	 DOMAttrNSImpl.cpp DOMBuilderImpl.cpp DOMCDATASectionImpl.cpp \
	 DOMCharacterDataImpl.cpp DOMChildNode.cpp DOMCommentImpl.cpp \
	 DOMConfigurationImpl.cpp DOMDeepNodeListImpl.cpp \
	 DOMDocumentFragmentImpl.cpp DOMDocumentImpl.cpp DOMDocumentTypeImpl.cpp \
	 DOMElementImpl.cpp DOMElementNSImpl.cpp DOMEntityImpl.cpp \
	 DOMEntityReferenceImpl.cpp DOMErrorImpl.cpp DOMException.cpp \
	 DOMImplementationImpl.cpp DOMImplementationRegistry.cpp \
	 DOMLocatorImpl.cpp DOMNamedNodeMapImpl.cpp DOMNodeIDMap.cpp \
	 DOMNodeImpl.cpp DOMNodeIteratorImpl.cpp DOMNodeListImpl.cpp \
	 DOMNodeVector.cpp DOMNormalizer.cpp DOMNotationImpl.cpp \
	 DOMParentNode.cpp DOMParser.cpp DOMProcessingInstructionImpl.cpp \
	 DOMRangeException.cpp DOMRangeImpl.cpp DOMServices.cpp DOMString.cpp \
	 DOMStringHelper.cpp DOMStringPool.cpp DOMStringPrintWriter.cpp \
	 DOMSupport.cpp DOMSupportDefault.cpp DOMSupportException.cpp \
	 DOMSupportInit.cpp DOMTextImpl.cpp DOMTreeWalkerImpl.cpp \
	 DOMTypeInfoImpl.cpp DOMWriterImpl.cpp DOMXPathException.cpp DOM_Attr.cpp \
	 DOM_CDATASection.cpp DOM_CharacterData.cpp DOM_Comment.cpp \
	 DOM_DOMException.cpp DOM_DOMImplementation.cpp DOM_Document.cpp \
	 DOM_DocumentFragment.cpp DOM_DocumentType.cpp DOM_Element.cpp \
	 DOM_Entity.cpp DOM_EntityReference.cpp DOM_NamedNodeMap.cpp DOM_Node.cpp \
	 DOM_NodeFilter.cpp DOM_NodeIterator.cpp DOM_NodeList.cpp \
	 DOM_Notation.cpp DOM_ProcessingInstruction.cpp DOM_Range.cpp \
	 DOM_RangeException.cpp DOM_Text.cpp DOM_TreeWalker.cpp DOM_XMLDecl.cpp \
	 DStringPool.cpp DTDAttDef.cpp DTDAttDefList.cpp DTDElementDecl.cpp \
	 DTDEntityDecl.cpp DTDGrammar.cpp DTDScanner.cpp DTDValidator.cpp \
	 DatatypeValidator.cpp DatatypeValidatorFactory.cpp \
	 DateDatatypeValidator.cpp DateTimeDatatypeValidator.cpp \
	 DateTimeValidator.cpp DayDatatypeValidator.cpp \
	 DecimalDatatypeValidator.cpp DeepNodeListImpl.cpp \
	 DefaultPanicHandler.cpp DocumentFragmentImpl.cpp DocumentImpl.cpp \
	 DocumentTypeImpl.cpp DomMemDebug.cpp DoubleDatatypeValidator.cpp \
	 DoubleSupport.cpp Dummy.cpp DurationDatatypeValidator.cpp \
	 ENTITYDatatypeValidator.cpp ElemApplyImport.cpp ElemApplyTemplates.cpp \
	 ElemAttribute.cpp ElemAttributeSet.cpp ElemCallTemplate.cpp \
	 ElemChoose.cpp ElemComment.cpp ElemCopy.cpp ElemCopyOf.cpp \
	 ElemDecimalFormat.cpp ElemElement.cpp ElemEmpty.cpp \
	 ElemExtensionCall.cpp ElemFallback.cpp ElemForEach.cpp \
	 ElemForwardCompatible.cpp ElemIf.cpp ElemLiteralResult.cpp \
	 ElemMessage.cpp ElemNumber.cpp ElemOtherwise.cpp ElemPI.cpp \
	 ElemParam.cpp ElemSort.cpp ElemStack.cpp ElemTemplate.cpp \
	 ElemTemplateElement.cpp ElemText.cpp ElemTextLiteral.cpp ElemUse.cpp \
	 ElemValueOf.cpp ElemVariable.cpp ElemWhen.cpp ElemWithParam.cpp \
	 ElementDefinitionImpl.cpp ElementImpl.cpp ElementNSImpl.cpp \
	 ElementPrefixResolverProxy.cpp EncodingValidator.cpp EntityImpl.cpp \
	 EntityReferenceImpl.cpp ExecutionContext.cpp \
	 ExtensionFunctionHandler.cpp ExtensionNSHandler.cpp FieldActivator.cpp \
	 FieldValueMap.cpp FileHandleImpl.cpp FloatDatatypeValidator.cpp \
	 FormatterListener.cpp FormatterStringLengthCounter.cpp \
	 FormatterToDOM.cpp FormatterToDeprecatedXercesDOM.cpp \
	 FormatterToHTML.cpp FormatterToNull.cpp FormatterToSourceTree.cpp \
	 FormatterToText.cpp FormatterToXML.cpp FormatterToXercesDOM.cpp \
	 FormatterTreeWalker.cpp Function.cpp FunctionConcat.cpp \
	 FunctionContains.cpp FunctionCurrent.cpp FunctionDifference.cpp \
	 FunctionDistinct.cpp FunctionDocument.cpp FunctionElementAvailable.cpp \
	 FunctionEvaluate.cpp FunctionFormatNumber.cpp \
	 FunctionFunctionAvailable.cpp FunctionGenerateID.cpp \
	 FunctionHasSameNodes.cpp FunctionID.cpp FunctionIntersection.cpp \
	 FunctionKey.cpp FunctionLang.cpp FunctionNamespaceURI.cpp \
	 FunctionNodeSet.cpp FunctionNormalizeSpace.cpp FunctionStartsWith.cpp \
	 FunctionString.cpp FunctionSubstring.cpp FunctionSubstringAfter.cpp \
	 FunctionSubstringBefore.cpp FunctionSystemProperty.cpp \
	 FunctionTranslate.cpp FunctionUnparsedEntityURI.cpp \
	 GeneralAttributeCheck.cpp GenerateEvent.cpp Grammar.cpp \
	 GrammarResolver.cpp HashPtr.cpp HashXMLCh.cpp HeaderDummy.cpp HexBin.cpp \
	 HexBinaryDatatypeValidator.cpp ICUResHandler.cpp IC_Field.cpp IC_Key.cpp \
	 IC_KeyRef.cpp IC_Selector.cpp IC_Unique.cpp IDDatatypeValidator.cpp \
	 IDREFDatatypeValidator.cpp IGXMLScanner.cpp IGXMLScanner2.cpp \
	 IconvTransService.cpp IdentityConstraint.cpp \
	 IdentityConstraintHandler.cpp InMemHandler.cpp InMemMsgLoader.cpp \
	 InputSource.cpp KVStringPair.cpp KeyTable.cpp ListDatatypeValidator.cpp \
	 LocalFileFormatTarget.cpp LocalFileInputSource.cpp Match.cpp \
	 MemBufFormatTarget.cpp MemBufInputSource.cpp MemoryManagerArrayImpl.cpp \
	 MemoryManagerImpl.cpp MixedContentModel.cpp ModifierToken.cpp \
	 MonthDatatypeValidator.cpp MonthDayDatatypeValidator.cpp \
	 MsgFileOutputStream.cpp MutableNodeRefList.cpp Mutexes.cpp \
	 NCNameDatatypeValidator.cpp NLSHandler.cpp NOTATIONDatatypeValidator.cpp \
	 NameDatatypeValidator.cpp NamedNodeMapAttributeList.cpp \
	 NamedNodeMapImpl.cpp NamespaceScope.cpp NamespacesHandler.cpp \
	 NodeIDMap.cpp NodeImpl.cpp NodeIteratorImpl.cpp NodeListImpl.cpp \
	 NodeNameTreeWalker.cpp NodeRefList.cpp NodeRefListBase.cpp \
	 NodeSortKey.cpp NodeSorter.cpp NodeVector.cpp NotationImpl.cpp \
	 NullPrintWriter.cpp Op.cpp OpFactory.cpp OutputContextStack.cpp \
	 PSVIAttribute.cpp PSVIAttributeList.cpp PSVIElement.cpp PSVIItem.cpp \
	 PanicHandler.cpp ParenToken.cpp ParentNode.cpp ParserForXMLSchema.cpp \
	 PlatformSupportInit.cpp PlatformUtils.cpp PrefixResolver.cpp \
	 PrintWriter.cpp ProblemListener.cpp ProblemListenerDefault.cpp \
	 ProcessingInstructionImpl.cpp QName.cpp QNameDatatypeValidator.cpp \
	 RangeFactory.cpp RangeImpl.cpp RangeToken.cpp RangeTokenMap.cpp \
	 ReaderMgr.cpp RefCountedImpl.cpp RegularExpression.cpp RegxParser.cpp \
	 RegxUtil.cpp Resettable.cpp ResultNamespacesStack.cpp SAX2Handler.cpp \
	 SAX2XMLFilterImpl.cpp SAX2XMLReaderImpl.cpp SAXException.cpp \
	 SAXParseException.cpp SAXParser.cpp SGXMLScanner.cpp SchemaAttDef.cpp \
	 SchemaAttDefList.cpp SchemaElementDecl.cpp SchemaGrammar.cpp \
	 SchemaInfo.cpp SchemaSymbols.cpp SchemaValidator.cpp SelectionEvent.cpp \
	 SimpleContentModel.cpp StdBinInputStream.cpp StdInInputSource.cpp \
	 StdOutFormatTarget.cpp StringDatatypeValidator.cpp StringPool.cpp \
	 StringToken.cpp StringTokenizer.cpp Stylesheet.cpp \
	 StylesheetConstructionContext.cpp \
	 StylesheetConstructionContextDefault.cpp StylesheetExecutionContext.cpp \
	 StylesheetExecutionContextDefault.cpp StylesheetHandler.cpp \
	 StylesheetRoot.cpp SubstitutionGroupComparator.cpp \
	 SynchronizedStringPool.cpp TextImpl.cpp TimeDatatypeValidator.cpp \
	 Token.cpp TokenFactory.cpp TopLevelArg.cpp TraceListener.cpp \
	 TraceListenerDefault.cpp TracerEvent.cpp TransService.cpp \
	 TraverseSchema.cpp TreeWalker.cpp TreeWalkerImpl.cpp URISupport.cpp \
	 URLInputSource.cpp UnicodeRangeFactory.cpp UnionDatatypeValidator.cpp \
	 UnionToken.cpp ValidationContextImpl.cpp ValueStore.cpp \
	 ValueStoreCache.cpp VariablesStack.cpp VecAttrListImpl.cpp \
	 VecAttributesImpl.cpp WFXMLScanner.cpp Wrapper4DOMInputSource.cpp \
	 Wrapper4InputSource.cpp Writer.cpp XBoolean.cpp \
	 XML256TableTranscoder.cpp XML256TableTranscoder390.cpp \
	 XML88591Transcoder.cpp XML88591Transcoder390.cpp XMLASCIITranscoder.cpp \
	 XMLASCIITranscoder390.cpp XMLAbstractDoubleFloat.cpp XMLAttDef.cpp \
	 XMLAttDefList.cpp XMLAttr.cpp XMLBigDecimal.cpp XMLBigInteger.cpp \
	 XMLBuffer.cpp XMLBufferMgr.cpp XMLCanRepGroup.cpp XMLChTranscoder.cpp \
	 XMLChar.cpp XMLContentModel.cpp XMLDTDDescription.cpp \
	 XMLDTDDescriptionImpl.cpp XMLDateTime.cpp XMLDeclImpl.cpp XMLDouble.cpp \
	 XMLEBCDICTranscoder.cpp XMLEBCDICTranscoder390.cpp XMLElementDecl.cpp \
	 XMLEntityDecl.cpp XMLException.cpp XMLFloat.cpp XMLFormatter.cpp \
	 XMLGrammarDescription.cpp XMLGrammarPoolImpl.cpp \
	 XMLIBM1047Transcoder.cpp XMLIBM1047Transcoder390.cpp \
	 XMLIBM1140Transcoder.cpp XMLIBM1140Transcoder390.cpp XMLInitializer.cpp \
	 XMLMsgLoader.cpp XMLNotationDecl.cpp XMLNumber.cpp XMLParserLiaison.cpp \
	 XMLRangeFactory.cpp XMLReader.cpp XMLRecognizer.cpp XMLRefInfo.cpp \
	 XMLRegisterCleanup.cpp XMLScanner.cpp XMLScannerResolver.cpp \
	 XMLSchemaDescription.cpp XMLSchemaDescriptionImpl.cpp XMLString.cpp \
	 XMLStringTokenizer.cpp XMLSupportException.cpp XMLSupportInit.cpp \
	 XMLUCSTranscoder.cpp XMLURL.cpp XMLUTF16Transcoder.cpp \
	 XMLUTF8Transcoder.cpp XMLUTF8Transcoder390.cpp XMLUni.cpp \
	 XMLUniCharacter.cpp XMLUri.cpp XMLValidator.cpp XMLWin1252Transcoder.cpp \
	 XMLWin1252Transcoder390.cpp XMemory.cpp XNodeSet.cpp \
	 XNodeSetAllocator.cpp XNodeSetBase.cpp XNodeSetNodeProxy.cpp \
	 XNodeSetNodeProxyAllocator.cpp XNodeSetResultTreeFragProxy.cpp XNull.cpp \
	 XNumber.cpp XNumberAllocator.cpp XNumberBase.cpp XObject.cpp \
	 XObjectFactory.cpp XObjectFactoryDefault.cpp \
	 XObjectResultTreeFragProxy.cpp XObjectResultTreeFragProxyBase.cpp \
	 XObjectResultTreeFragProxyText.cpp XObjectTypeCallback.cpp XPath.cpp \
	 XPathAllocator.cpp XPathCAPI.cpp XPathConstructionContext.cpp \
	 XPathConstructionContextDefault.cpp XPathEnvSupport.cpp \
	 XPathEnvSupportDefault.cpp XPathEvaluator.cpp XPathExecutionContext.cpp \
	 XPathExecutionContextDefault.cpp XPathExpression.cpp XPathFactory.cpp \
	 XPathFactoryBlock.cpp XPathFactoryDefault.cpp XPathFunctionTable.cpp \
	 XPathInit.cpp XPathMatcher.cpp XPathMatcherStack.cpp \
	 XPathParserException.cpp XPathProcessor.cpp XPathProcessorImpl.cpp \
	 XPathSymbols.cpp XProtoType.cpp XResultTreeFrag.cpp \
	 XResultTreeFragAllocator.cpp XSAXMLScanner.cpp XSAnnotation.cpp \
	 XSAttributeDeclaration.cpp XSAttributeGroupDefinition.cpp \
	 XSAttributeUse.cpp XSComplexTypeDefinition.cpp XSDDOMParser.cpp \
	 XSDElementNSImpl.cpp XSDErrorReporter.cpp XSDLocator.cpp \
	 XSElementDeclaration.cpp XSFacet.cpp XSIDCDefinition.cpp \
	 XSLException.cpp XSLTEngineImpl.cpp XSLTInit.cpp XSLTInputSource.cpp \
	 XSLTProcessor.cpp XSLTProcessorEnvSupport.cpp \
	 XSLTProcessorEnvSupportDefault.cpp XSLTProcessorException.cpp \
	 XSLTResultTarget.cpp XSModel.cpp XSModelGroup.cpp \
	 XSModelGroupDefinition.cpp XSMultiValueFacet.cpp XSNamespaceItem.cpp \
	 XSNotationDeclaration.cpp XSObject.cpp XSObjectFactory.cpp \
	 XSParticle.cpp XSSimpleTypeDefinition.cpp XSTypeDefinition.cpp \
	 XSValue.cpp XSWildcard.cpp XSerializeEngine.cpp XSpan.cpp XString.cpp \
	 XStringAdapter.cpp XStringAdapterAllocator.cpp XStringAllocator.cpp \
	 XStringBase.cpp XStringCached.cpp XStringCachedAllocator.cpp \
	 XStringReference.cpp XStringReferenceAllocator.cpp \
	 XTemplateSerializer.cpp XToken.cpp XTokenNumberAdapter.cpp \
	 XTokenNumberAdapterAllocator.cpp XTokenStringAdapter.cpp \
	 XTokenStringAdapterAllocator.cpp XUnknown.cpp XUtil.cpp \
	 XalanAVTAllocator.cpp XalanAVTPartSimpleAllocator.cpp \
	 XalanAVTPartXPathAllocator.cpp XalanAttr.cpp XalanBitmap.cpp \
	 XalanCAPI.cpp XalanCDataSection.cpp XalanCharacterData.cpp \
	 XalanComment.cpp XalanCompiledStylesheetDefault.cpp \
	 XalanDOMException.cpp XalanDOMImplementation.cpp XalanDOMInit.cpp \
	 XalanDOMString.cpp XalanDOMStringAllocator.cpp XalanDOMStringCache.cpp \
	 XalanDOMStringHashTable.cpp XalanDOMStringPool.cpp \
	 XalanDOMStringReusableAllocator.cpp XalanDecimalFormatSymbols.cpp \
	 XalanDefaultDocumentBuilder.cpp XalanDefaultParsedSource.cpp \
	 XalanDiagnosticMemoryManager.cpp XalanDocument.cpp \
	 XalanDocumentFragment.cpp XalanDocumentFragmentNodeRefListBaseProxy.cpp \
	 XalanDocumentPrefixResolver.cpp XalanDocumentType.cpp \
	 XalanEXSLTCommon.cpp XalanEXSLTDateTime.cpp XalanEXSLTDynamic.cpp \
	 XalanEXSLTMath.cpp XalanEXSLTSet.cpp XalanEXSLTString.cpp \
	 XalanElemApplyTemplatesAllocator.cpp XalanElemAttributeAllocator.cpp \
	 XalanElemAttributeSetAllocator.cpp XalanElemCallTemplateAllocator.cpp \
	 XalanElemElementAllocator.cpp XalanElemEmptyAllocator.cpp \
	 XalanElemLiteralResultAllocator.cpp XalanElemTemplateAllocator.cpp \
	 XalanElemTextAllocator.cpp XalanElemTextLiteralAllocator.cpp \
	 XalanElemValueOfAllocator.cpp XalanElemVariableAllocator.cpp \
	 XalanElement.cpp XalanEmptyNamedNodeMap.cpp \
	 XalanEncodingPropertyCache.cpp XalanEntity.cpp XalanEntityReference.cpp \
	 XalanExe.cpp XalanExtensions.cpp XalanFStreamOutputStream.cpp \
	 XalanFileOutputStream.cpp XalanFileUtility.cpp \
	 XalanHTMLElementsProperties.cpp XalanICUMessageLoader.cpp \
	 XalanInMemoryMessageLoader.cpp XalanMatchPatternData.cpp \
	 XalanMatchPatternDataAllocator.cpp XalanMemoryManagement.cpp \
	 XalanMemoryManagerDefault.cpp XalanMessageLoader.cpp XalanMsgLib.cpp \
	 XalanNLSMessageLoader.cpp XalanNamedNodeMap.cpp XalanNamespacesStack.cpp \
	 XalanNode.cpp XalanNodeList.cpp XalanNodeListDummy.cpp \
	 XalanNodeListSurrogate.cpp XalanNotation.cpp XalanNullOutputStream.cpp \
	 XalanNumberFormat.cpp XalanNumberingResourceBundle.cpp \
	 XalanOutputStream.cpp XalanOutputStreamPrintWriter.cpp \
	 XalanParsedSource.cpp XalanParsedURI.cpp XalanProcessingInstruction.cpp \
	 XalanQName.cpp XalanQNameByReference.cpp XalanQNameByValue.cpp \
	 XalanQNameByValueAllocator.cpp XalanReferenceCountedObject.cpp \
	 XalanSimplePrefixResolver.cpp XalanSourceTreeAttr.cpp \
	 XalanSourceTreeAttrNS.cpp XalanSourceTreeAttributeAllocator.cpp \
	 XalanSourceTreeAttributeNSAllocator.cpp XalanSourceTreeComment.cpp \
	 XalanSourceTreeCommentAllocator.cpp XalanSourceTreeContentHandler.cpp \
	 XalanSourceTreeDOMSupport.cpp XalanSourceTreeDocument.cpp \
	 XalanSourceTreeDocumentAllocator.cpp XalanSourceTreeDocumentFragment.cpp \
	 XalanSourceTreeDocumentFragmentAllocator.cpp XalanSourceTreeElement.cpp \
	 XalanSourceTreeElementA.cpp XalanSourceTreeElementAAllocator.cpp \
	 XalanSourceTreeElementANS.cpp XalanSourceTreeElementANSAllocator.cpp \
	 XalanSourceTreeElementNA.cpp XalanSourceTreeElementNAAllocator.cpp \
	 XalanSourceTreeElementNANS.cpp XalanSourceTreeElementNANSAllocator.cpp \
	 XalanSourceTreeHelper.cpp XalanSourceTreeInit.cpp \
	 XalanSourceTreeParserLiaison.cpp \
	 XalanSourceTreeProcessingInstruction.cpp \
	 XalanSourceTreeProcessingInstructionAllocator.cpp \
	 XalanSourceTreeText.cpp XalanSourceTreeTextAllocator.cpp \
	 XalanSourceTreeTextIWS.cpp XalanSourceTreeTextIWSAllocator.cpp \
	 XalanSourceTreeWrapperParsedSource.cpp XalanSpaceNodeTester.cpp \
	 XalanStdOutputStream.cpp XalanText.cpp \
	 XalanToXercesTranscoderWrapper.cpp XalanTranscodingServices.cpp \
	 XalanTransformer.cpp XalanTransformerOutputStream.cpp \
	 XalanTransformerProblemListener.cpp XalanUTF16Transcoder.cpp \
	 XalanUTF16Writer.cpp XalanUTF8Writer.cpp XalanXMLChar.cpp \
	 XalanXMLFileReporter.cpp XalanXMLSerializerBase.cpp \
	 XalanXMLSerializerFactory.cpp XalanXPathException.cpp \
	 XercesAttGroupInfo.cpp XercesAttrBridge.cpp XercesAttrWrapper.cpp \
	 XercesAttrWrapperAllocator.cpp XercesAttributeBridgeAllocator.cpp \
	 XercesBridgeHelper.cpp XercesBridgeNavigator.cpp \
	 XercesCDATASectionBridge.cpp XercesCDATASectionWrapper.cpp \
	 XercesCommentBridge.cpp XercesCommentWrapper.cpp XercesDOMException.cpp \
	 XercesDOMFormatterWalker.cpp XercesDOMImplementationBridge.cpp \
	 XercesDOMImplementationWrapper.cpp XercesDOMParsedSource.cpp \
	 XercesDOMParser.cpp XercesDOMSupport.cpp XercesDOMWalker.cpp \
	 XercesDOMWrapperException.cpp XercesDOMWrapperParsedSource.cpp \
	 XercesDOM_NodeHack.cpp XercesDocumentBridge.cpp \
	 XercesDocumentFragmentBridge.cpp XercesDocumentTypeBridge.cpp \
	 XercesDocumentTypeWrapper.cpp XercesDocumentWrapper.cpp \
	 XercesElementBridge.cpp XercesElementBridgeAllocator.cpp \
	 XercesElementWildcard.cpp XercesElementWrapper.cpp \
	 XercesElementWrapperAllocator.cpp XercesEntityBridge.cpp \
	 XercesEntityReferenceBridge.cpp XercesEntityReferenceWrapper.cpp \
	 XercesEntityWrapper.cpp XercesGroupInfo.cpp \
	 XercesLiaisonXalanDOMStringPool.cpp XercesNamedNodeMapAttributeList.cpp \
	 XercesNamedNodeMapBridge.cpp XercesNamedNodeMapWrapper.cpp \
	 XercesNodeListBridge.cpp XercesNodeListWrapper.cpp \
	 XercesNotationBridge.cpp XercesNotationWrapper.cpp \
	 XercesParserLiaison.cpp XercesProcessingInstructionBridge.cpp \
	 XercesProcessingInstructionWrapper.cpp XercesTextBridge.cpp \
	 XercesTextBridgeAllocator.cpp XercesTextWrapper.cpp \
	 XercesTextWrapperAllocator.cpp XercesToXalanNodeMap.cpp \
	 XercesTreeWalker.cpp XercesWrapperHelper.cpp XercesWrapperNavigator.cpp \
	 XercesWrapperNavigatorAllocator.cpp XercesWrapperToXalanNodeMap.cpp \
	 XercesXPath.cpp YearDatatypeValidator.cpp YearMonthDatatypeValidator.cpp
EXEBASE=cpuxalan_r
NEED_MATH=
BENCHLANG=CXX

BENCH_CXXFLAGS   = -DAPP_NO_THREADS -DXALAN_INMEM_MSG_LOADER -I. -Ixercesc -Ixercesc/dom -Ixercesc/dom/impl -Ixercesc/sax -Ixercesc/util/MsgLoaders/InMemory -Ixercesc/util/Transcoders/Iconv -Ixalanc/include -DPROJ_XMLPARSER -DPROJ_XMLUTIL -DPROJ_PARSERS -DPROJ_SAX4C -DPROJ_SAX2 -DPROJ_DOM -DPROJ_VALIDATORS -DXML_USE_INMEM_MESSAGELOADER -DSPEC_AUTO_SUPPRESS_OPENMP
CC               = $(SPECLANG)gcc     -std=c99   -m64
CC_VERSION_OPTION = -v
CXX              = $(SPECLANG)g++     -std=c++03 -m64
CXX_VERSION_OPTION = -v
EXTRA_COPTIMIZE  = -fno-strict-aliasing -fgnu89-inline
EXTRA_PORTABILITY = -DSPEC_LP64
FC               = $(SPECLANG)gfortran           -m64
FC_VERSION_OPTION = -v
OPTIMIZE         = -g -O3 -march=native -fno-unsafe-math-optimizations  -fno-tree-loop-vectorize
OS               = unix
PORTABILITY      = -DSPEC_LINUX
SPECLANG         = /usr/bin/
absolutely_no_locking = 0
abstol           = 
action           = build
allow_label_override = 0
backup_config    = 1
baseexe          = cpuxalan_r
basepeak         = 1
benchdir         = benchspec
benchmark        = 523.xalancbmk_r
binary           = 
bindir           = exe
builddir         = build
bundleaction     = 
bundlename       = 
calctol          = 0
changedhash      = 0
check_version    = 0
clean_between_builds = no
command_add_redirect = 1
commanderrfile   = speccmds.err
commandexe       = cpuxalan_r_base.primeiro-teste-m64
commandfile      = speccmds.cmd
commandoutfile   = speccmds.out
commandstdoutfile = speccmds.stdout
comparedir       = compare
compareerrfile   = compare.err
comparefile      = compare.cmd
compareoutfile   = compare.out
comparestdoutfile = compare.stdout
compile_error    = 0
compwhite        = 
configdir        = config
configfile       = my-first-run.cfg
configpath       = /home/kratos/cpu2017/config/my-first-run.cfg
copies           = 1
current_range    = 
datadir          = data
default_size     = ref
default_submit   = $command
delay            = 0
deletebinaries   = 0
deletework       = 0
dependent_workloads = 0
device           = 
difflines        = 10
dirprot          = 511
discard_power_samples = 0
enable_monitor   = 1
endian           = 12345678
env_vars         = 0
expand_notes     = 0
expid            = 
exthash_bits     = 256
failflags        = 0
fake             = 1
feedback         = 1
flag_url_base    = https://www.spec.org/auto/cpu2017/Docs/benchmarks/flags/
floatcompare     = 
force_monitor    = 0
from_runcpu      = 2
fw_bios          = virtualbox
hostname         = watter
http_proxy       = 
http_timeout     = 30
hw_avail         = Ago-2025
hw_cpu_max_mhz   = 4100
hw_cpu_name      = AMD Ryzen 7 5700X3D
hw_cpu_nominal_mhz = 3000
hw_disk          = 1 TB SSD NVMe
hw_memory001     = 16 GB (1 x 16 GB DDR4-3200)
hw_memory002     = 'N GB (N x N GB nRxn PC4-nnnnX-X)'
hw_model         = 'Test Build'
hw_nchips        = 1
hw_ncores        = 8
hw_ncpuorder     = 1-9 chips
hw_nthreadspercore = 2
hw_ocache        = None
hw_other         = None
hw_pcache        = 64 KB I + 64 KB D on chip per core
hw_scache        = 512 KB I+D on chip per core
hw_tcache        = 96 MB I+D on chip
hw_vendor        = My Test
idle_current_range = 
idledelay        = 10
idleduration     = 60
ignore_errors    = 1
ignore_sigint    = 0
ignorecase       = 
info_wrap_columns = 50
inputdir         = input
inputgenerrfile  = inputgen.err
inputgenfile     = inputgen.cmd
inputgenoutfile  = inputgen.out
inputgenstdoutfile = inputgen.stdout
iteration        = -1
iterations       = 1
keeptmp          = 0
label            = primeiro-teste-m64
license_num      = 2017
line_width       = 1020
link_input_files = 1
locking          = 1
log              = CPU2017
log_line_width   = 1020
log_timestamp    = 0
logfile          = /home/kratos/cpu2017/tmp/CPU2017.008/templogs/preenv.intrate.008.2
logname          = /home/kratos/cpu2017/tmp/CPU2017.008/templogs/preenv.intrate.008.2
lognum           = 008.2
mail_reports     = all
mailcompress     = 0
mailmethod       = smtp
mailport         = 25
mailserver       = 127.0.0.1
mailto           = 
make             = specmake
make_no_clobber  = 0
makefile_template = Makefile.YYYtArGeTYYYspec
makeflags        = --jobs=8
max_average_uncertainty = 1
max_hum_limit    = 0
max_report_runs  = 3
max_unknown_uncertainty = 1
mean_anyway      = 1
meter_connect_timeout = 30
meter_errors_default = 5
meter_errors_percentage = 5
min_report_runs  = 2
min_temp_limit   = 20
minimize_builddirs = 0
minimize_rundirs = 0
name             = xalancbmk_r
nansupport       = 
need_math        = 
no_input_handler = close
no_monitor       = 
noratios         = 0
note_preenv      = 1
notes_plat_sysinfo_000 = 
notes_plat_sysinfo_005 =  Sysinfo program /home/kratos/cpu2017/bin/sysinfo
notes_plat_sysinfo_010 =  Rev: r6365 of 2019-08-21 295195f888a3d7edb1e6e46a485a0011
notes_plat_sysinfo_015 =  running on watter Sat Sep 27 22:21:18 2025
notes_plat_sysinfo_020 = 
notes_plat_sysinfo_025 =  SUT (System Under Test) info as seen by some common utilities.
notes_plat_sysinfo_030 =  For more information on this section, see
notes_plat_sysinfo_035 =     https://www.spec.org/cpu2017/Docs/config.html\#sysinfo
notes_plat_sysinfo_040 = 
notes_plat_sysinfo_045 =  From /proc/cpuinfo
notes_plat_sysinfo_050 =     model name : AMD Ryzen 7 5700X3D 8-Core Processor
notes_plat_sysinfo_055 =        1  "physical id"s (chips)
notes_plat_sysinfo_060 =        8 "processors"
notes_plat_sysinfo_065 =     cores, siblings (Caution: counting these is hw and system dependent. The following
notes_plat_sysinfo_070 =     excerpts from /proc/cpuinfo might not be reliable.  Use with caution.)
notes_plat_sysinfo_075 =        cpu cores : 8
notes_plat_sysinfo_080 =        siblings  : 8
notes_plat_sysinfo_085 =        physical 0: cores 0 1 2 3 4 5 6 7
notes_plat_sysinfo_090 = 
notes_plat_sysinfo_095 =  From lscpu:
notes_plat_sysinfo_100 =       Architecture:                         x86_64
notes_plat_sysinfo_105 =       CPU op-mode(s):                       32-bit, 64-bit
notes_plat_sysinfo_110 =       Address sizes:                        48 bits physical, 48 bits virtual
notes_plat_sysinfo_115 =       Byte Order:                           Little Endian
notes_plat_sysinfo_120 =       CPU(s):                               8
notes_plat_sysinfo_125 =       On-line CPU(s) list:                  0-7
notes_plat_sysinfo_130 =       Vendor ID:                            AuthenticAMD
notes_plat_sysinfo_135 =       Model name:                           AMD Ryzen 7 5700X3D 8-Core Processor
notes_plat_sysinfo_140 =       CPU family:                           25
notes_plat_sysinfo_145 =       Model:                                33
notes_plat_sysinfo_150 =       Thread(s) per core:                   1
notes_plat_sysinfo_155 =       Core(s) per socket:                   8
notes_plat_sysinfo_160 =       Socket(s):                            1
notes_plat_sysinfo_165 =       Stepping:                             2
notes_plat_sysinfo_170 =       BogoMIPS:                             6000.00
notes_plat_sysinfo_175 =       Flags:                                fpu vme de pse tsc msr pae mce cx8 apic sep
notes_plat_sysinfo_180 =       mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt
notes_plat_sysinfo_185 =       rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid tsc_known_freq
notes_plat_sysinfo_190 =       pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c
notes_plat_sysinfo_195 =       rdrand hypervisor lahf_lm cmp_legacy cr8_legacy abm sse4a misalignsse 3dnowprefetch
notes_plat_sysinfo_200 =       vmmcall fsgsbase bmi1 avx2 bmi2 invpcid rdseed adx clflushopt sha_ni arat debug_swap
notes_plat_sysinfo_205 =       Hypervisor vendor:                    KVM
notes_plat_sysinfo_210 =       Virtualization type:                  full
notes_plat_sysinfo_215 =       L1d cache:                            256 KiB (8 instances)
notes_plat_sysinfo_220 =       L1i cache:                            256 KiB (8 instances)
notes_plat_sysinfo_225 =       L2 cache:                             4 MiB (8 instances)
notes_plat_sysinfo_230 =       L3 cache:                             768 MiB (8 instances)
notes_plat_sysinfo_235 =       NUMA node(s):                         1
notes_plat_sysinfo_240 =       NUMA node0 CPU(s):                    0-7
notes_plat_sysinfo_245 =       Vulnerability Gather data sampling:   Not affected
notes_plat_sysinfo_250 =       Vulnerability Itlb multihit:          Not affected
notes_plat_sysinfo_255 =       Vulnerability L1tf:                   Not affected
notes_plat_sysinfo_260 =       Vulnerability Mds:                    Not affected
notes_plat_sysinfo_265 =       Vulnerability Meltdown:               Not affected
notes_plat_sysinfo_270 =       Vulnerability Mmio stale data:        Not affected
notes_plat_sysinfo_275 =       Vulnerability Reg file data sampling: Not affected
notes_plat_sysinfo_280 =       Vulnerability Retbleed:               Not affected
notes_plat_sysinfo_285 =       Vulnerability Spec rstack overflow:   Vulnerable: Safe RET, no microcode
notes_plat_sysinfo_290 =       Vulnerability Spec store bypass:      Not affected
notes_plat_sysinfo_295 =       Vulnerability Spectre v1:             Mitigation; usercopy/swapgs barriers and
notes_plat_sysinfo_300 =       __user pointer sanitization
notes_plat_sysinfo_305 =       Vulnerability Spectre v2:             Mitigation; Retpolines; STIBP disabled; RSB
notes_plat_sysinfo_310 =       filling; PBRSB-eIBRS Not affected; BHI Not affected
notes_plat_sysinfo_315 =       Vulnerability Srbds:                  Not affected
notes_plat_sysinfo_320 =       Vulnerability Tsx async abort:        Not affected
notes_plat_sysinfo_325 = 
notes_plat_sysinfo_330 =  /proc/cpuinfo cache data
notes_plat_sysinfo_335 =     cache size : 512 KB
notes_plat_sysinfo_340 = 
notes_plat_sysinfo_345 =  From numactl --hardware  WARNING: a numactl 'node' might or might not correspond to a
notes_plat_sysinfo_350 =  physical chip.
notes_plat_sysinfo_355 = 
notes_plat_sysinfo_360 =  From /proc/meminfo
notes_plat_sysinfo_365 =     MemTotal:       16376184 kB
notes_plat_sysinfo_370 =     HugePages_Total:       0
notes_plat_sysinfo_375 =     Hugepagesize:       2048 kB
notes_plat_sysinfo_380 = 
notes_plat_sysinfo_385 =  /usr/bin/lsb_release -d
notes_plat_sysinfo_390 =     Ubuntu 22.04.5 LTS
notes_plat_sysinfo_395 = 
notes_plat_sysinfo_400 =  From /etc/*release* /etc/*version*
notes_plat_sysinfo_405 =     debian_version: bookworm/sid
notes_plat_sysinfo_410 =     os-release:
notes_plat_sysinfo_415 =        PRETTY_NAME="Ubuntu 22.04.5 LTS"
notes_plat_sysinfo_420 =        NAME="Ubuntu"
notes_plat_sysinfo_425 =        VERSION_ID="22.04"
notes_plat_sysinfo_430 =        VERSION="22.04.5 LTS (Jammy Jellyfish)"
notes_plat_sysinfo_435 =        VERSION_CODENAME=jammy
notes_plat_sysinfo_440 =        ID=ubuntu
notes_plat_sysinfo_445 =        ID_LIKE=debian
notes_plat_sysinfo_450 =        HOME_URL="https://www.ubuntu.com/"
notes_plat_sysinfo_455 = 
notes_plat_sysinfo_460 =  uname -a:
notes_plat_sysinfo_465 =     Linux watter 6.8.0-79-generic \#79~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Fri Aug 15
notes_plat_sysinfo_470 =     16:54:53 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
notes_plat_sysinfo_475 = 
notes_plat_sysinfo_480 =  Kernel self-reported vulnerability status:
notes_plat_sysinfo_485 = 
notes_plat_sysinfo_490 =  gather_data_sampling:                     Not affected
notes_plat_sysinfo_495 =  itlb_multihit:                            Not affected
notes_plat_sysinfo_500 =  CVE-2018-3620 (L1 Terminal Fault):        Not affected
notes_plat_sysinfo_505 =  Microarchitectural Data Sampling:         Not affected
notes_plat_sysinfo_510 =  CVE-2017-5754 (Meltdown):                 Not affected
notes_plat_sysinfo_515 =  mmio_stale_data:                          Not affected
notes_plat_sysinfo_520 =  reg_file_data_sampling:                   Not affected
notes_plat_sysinfo_525 =  retbleed:                                 Not affected
notes_plat_sysinfo_530 =  spec_rstack_overflow:                     Vulnerable: Safe RET, no microcode
notes_plat_sysinfo_535 =  CVE-2018-3639 (Speculative Store Bypass): Not affected
notes_plat_sysinfo_540 =  CVE-2017-5753 (Spectre variant 1):        Mitigation: usercopy/swapgs barriers and __user
notes_plat_sysinfo_545 =                                            pointer sanitization
notes_plat_sysinfo_550 =  CVE-2017-5715 (Spectre variant 2):        Mitigation: Retpolines; STIBP: disabled; RSB
notes_plat_sysinfo_555 =                                            filling; PBRSB-eIBRS: Not affected; BHI: Not
notes_plat_sysinfo_560 =                                            affected
notes_plat_sysinfo_565 =  srbds:                                    Not affected
notes_plat_sysinfo_570 =  tsx_async_abort:                          Not affected
notes_plat_sysinfo_575 = 
notes_plat_sysinfo_580 =  run-level 5 Sep 14 23:57
notes_plat_sysinfo_585 = 
notes_plat_sysinfo_590 =  SPEC is set to: /home/kratos/cpu2017
notes_plat_sysinfo_595 =     Filesystem     Type  Size  Used Avail Use% Mounted on
notes_plat_sysinfo_600 =     /dev/sda3      ext4   78G   31G   44G  41% /
notes_plat_sysinfo_605 = 
notes_plat_sysinfo_610 =  From /sys/devices/virtual/dmi/id
notes_plat_sysinfo_615 =      BIOS:    innotek GmbH VirtualBox 12/01/2006
notes_plat_sysinfo_620 =      Vendor:  innotek GmbH
notes_plat_sysinfo_625 =      Product: VirtualBox
notes_plat_sysinfo_630 =      Product Family: Virtual Machine
notes_plat_sysinfo_635 = 
notes_plat_sysinfo_640 =  Cannot run dmidecode; consider saying (as root)
notes_plat_sysinfo_645 =     chmod +s /usr/sbin/dmidecode
notes_plat_sysinfo_650 = 
notes_plat_sysinfo_655 =  (End of data from sysinfo program)
notes_wrap_columns = 0
notes_wrap_indent =   
num              = 523
obiwan           = 
os_exe_ext       = 
output_format    = txt,html,cfg,pdf,csv
output_root      = 
outputdir        = output
parallel_test    = 0
parallel_test_submit = 0
parallel_test_workloads = 
path             = /home/kratos/cpu2017/benchspec/CPU/523.xalancbmk_r
plain_train      = 1
platform         = 
power            = 0
preENV_LD_LIBRARY_PATH = %{gcc_dir}/lib64/:%{gcc_dir}/lib/:/lib64
preenv           = 0
prefix           = 
prepared_by      = Watta
ranks            = 1
rawhash_bits     = 256
rebuild          = 1
reftime          = reftime
reltol           = 
reportable       = 0
resultdir        = result
review           = 0
run              = all
runcpu           = /home/kratos/cpu2017/bin/harness/runcpu --configfile my-first-run.cfg --action build --fake --noreportable --nopower --runmode rate --tune base --size refrate intrate --nopreenv --note-preenv --logfile /home/kratos/cpu2017/tmp/CPU2017.008/templogs/preenv.intrate.008.2 --lognum 008.2 --from_runcpu 2
rundir           = run
runmode          = rate
safe_eval        = 1
save_build_files = 
section_specifier_fatal = 1
setprocgroup     = 1
setup_error      = 0
sigint           = 2
size             = refrate
size_class       = ref
skipabstol       = 
skipobiwan       = 
skipreltol       = 
skiptol          = 
smarttune        = base
specdiff         = specdiff
specrun          = specinvoke
srcalt           = 
srcdir           = src
srcsource        = /home/kratos/cpu2017/benchspec/CPU/523.xalancbmk_r/src
stagger          = 10
strict_rundir_verify = 1
sw_avail         = Ago-2025
sw_base_ptrsize  = 64-bit
sw_compiler001   = C/C++/Fortran: Version 11.4.0 of GCC, the
sw_compiler002   = GNU Compiler Collection
sw_file          = ext4
sw_os001         = Ubuntu 22.04.5 LTS
sw_os002         = 6.8.0-79-generic
sw_other         = None
sw_peak_ptrsize  = Not Applicable
sw_state         = 
sysinfo_hash_bits = 256
sysinfo_program  = specperl /home/kratos/cpu2017/bin/sysinfo
sysinfo_program_hash = sysinfo:SHA:1b187da62efa5d65f0e989c214b6a257d16a31d3cf135973c9043da741052207
table            = 1
teeout           = 1
test_date        = Sep-2025
test_sponsor     = My Test
tester           = My Test
threads          = 1
top              = /home/kratos/cpu2017
train_single_thread = 0
train_with       = train
tune             = base
uid              = 1000
unbuffer         = 1
uncertainty_exception = 5
update           = 0
update_url       = http://www.spec.org/auto/cpu2017/updates/
use_submit_for_compare = 0
use_submit_for_speed = 0
username         = kratos
verbose          = 5
verify_binaries  = 1
version          = 1.000503
voltage_range    = 
worklist         = list
OUTPUT_RMFILES   = train-allbooks.out
