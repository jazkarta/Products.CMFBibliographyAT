##################################################
#                                                #
#    Copyright (C), 2004, Raphael Ritz           #
#    <r.ritz@biologie.hu-berlin.de>              #
#                                                #
#    Humboldt University Berlin                  #
#                                                #
##################################################

import os, sys

if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from zope.component import getUtility

from Testing import ZopeTestCase

from Products.CMFPlone.tests import PloneTestCase

from bibliograph.rendering.interfaces import IBibliographyExporter
from bibliograph.rendering.utility import BibtexExport

from Products.CMFBibliographyAT.tests import setup

class TestCMFBibliographyATInstall(PloneTestCase.PloneTestCase):
    '''Test the CMFBibliographyAT installation'''

    def afterSetUp(self):
        pass

    # the individual tests

    def testSkinInstallation(self):
        st = self.portal.portal_skins
        self.failUnless('bibliography' in st.objectIds())

    def testToolInstalltion(self):
        root = self.portal
        self.failUnless('portal_bibliography' in root.objectIds())

    def testParserFolderInstallation(self):
        bibtool = self.portal.portal_bibliography
        self.failUnless('Parsers' in bibtool.objectIds())

    def testRendererFolderInstallation(self):
        pass
        # not used any longer
        #bibtool = self.portal.portal_bibliography
        #self.failUnless('Renderers' in bibtool.objectIds())

    def testBibtexParserInstallation(self):
        parsers = self.portal.portal_bibliography.Parsers
        self.failUnless('bibtex' in parsers.objectIds())

    def testMedlineParserInstallation(self):
        parsers = self.portal.portal_bibliography.Parsers
        self.failUnless('medline' in parsers.objectIds())

    def testBibtexRendererInstallation(self):
        util = getUtility(IBibliographyExporter, name='bibtex')
        self.failUnless(isinstance(util, BibtexExport))        
        

    def testBibFolderInstallation(self):
        ttool = self.portal.portal_types
        self.failUnless('BibliographyFolder' in ttool.objectIds())

    def testReferenceTypesInstallation(self):
        ttool = self.portal.portal_types
        # first check all listed in config
        from Products.CMFBibliographyAT.config import REFERENCE_TYPES
        for reftype in REFERENCE_TYPES:
            self.failUnless(reftype in ttool.objectIds(),
                            '%s not installed' % reftype)
        # to double check do also explicit tests
        reftypes = ['ArticleReference',
                    'BookReference',
                    'BookletReference',
                    'InbookReference',
                    'IncollectionReference',
                    'InproceedingsReference',
                    'ManualReference',
                    'MastersthesisReference',
                    'MiscReference',
                    'PhdthesisReference',
                    'PreprintReference',
                    'ProceedingsReference',
                    'TechreportReference',
                    'UnpublishedReference',
                    'WebpublishedReference',
                    ]
        for reftype in reftypes:
            self.failUnless(reftype in ttool.objectIds(),
                            '%s not installed' % reftype)


    def testCatalogExtensions(self):
        ctool = self.portal.portal_catalog

        newFieldIndexes = ['Authors', 'publication_year']
        newSchemaEntries = ['Authors', 'publication_year', 'Source']

        for idx in newFieldIndexes:
            self.failUnless(idx in ctool.indexes())

        for entry in newSchemaEntries:
            self.failUnless(entry in ctool.schema())

## rr: obsolte in CMF-2.0; custom tools must not be action providers
##     def testActionProvider(self):
##         atool = self.portal.portal_actions
##         self.failUnless('portal_bibliography' \
##                         in atool.listActionProviders())

    def testBibliographyViewAction(self):
        acttool = self.portal.portal_actions
        action_ids = [a.id for a in acttool.listActions()]
        self.failUnless('bibliography_search' in action_ids)

    # end of the individual tests

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestCMFBibliographyATInstall))
    return suite

if __name__ == '__main__':
    framework()
