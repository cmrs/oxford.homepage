from AccessControl import ClassSecurityInfo
from zope.interface import implements

from plone.app.folder.folder import ATFolder

from Products.Archetypes.atapi import registerType
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

from oxford.homepage.config import PROJECTNAME
from oxford.homepage.interfaces.homepage import IHomePage

from schemata import HomePageSchema

class HomePage(ATFolder):
    """HomePage"""

    security = ClassSecurityInfo()

    implements(IHomePage)

    meta_type = 'HomePage'
    _at_rename_after_creation = True

    schema = HomePageSchema

    security.declarePublic('exclude_from_nav')
    def exclude_from_nav(self):
        return True

    security.declarePublic('canSetConstrainTypes')
    def canSetConstrainTypes(self):
        return False

registerType(HomePage, PROJECTNAME)

