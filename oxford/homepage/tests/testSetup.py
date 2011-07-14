import unittest2 as unittest

from zope.component import getSiteManager

from plone.app.testing import PLONE_INTEGRATION_TESTING
from plone.app.testing import ploneSite
from plone.app.testing import applyProfile
from plone.browserlayer.utils import registered_layers

from Products.CMFCore.utils import getToolByName

from base import OXFORD_HOMEPAGE_INTEGRATION_TESTING

class TestReinstall(unittest.TestCase):
    """Ensure product can be reinstalled safely"""
    layer = OXFORD_HOMEPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testReinstall(self):
        portal_setup = getToolByName(self.portal, 'portal_setup')
        portal_setup.runAllImportStepsFromProfile('profile-oxford.homepage:default')
