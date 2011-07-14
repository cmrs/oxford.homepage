import unittest2 as unittest

from zope.component import getSiteManager

from plone.app.testing import PLONE_INTEGRATION_TESTING
from plone.app.testing import ploneSite
from plone.app.testing import applyProfile
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.browserlayer.utils import registered_layers

from Products.CMFCore.utils import getToolByName

from base import OXFORD_HOMEPAGE_INTEGRATION_TESTING

class TestContentType(unittest.TestCase):
    """Ensure product is properly installed"""
    layer =  OXFORD_HOMEPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testAddType(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('HomePage', 'hp1')
        hp1 = getattr(self.portal, 'hp1')
        assert 'hp1' in self.portal.objectIds()
