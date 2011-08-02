from AccessControl import ClassSecurityInfo
from random import choice

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

    security.declarePublic('getRandomHomeImage')
    def getRandomHomeImage(self):
        """Returns a random image from the Home Page"""
        # TODO would be better to pass image portal type in as attribute and default to Image
        # would need to override the viewlet to pass in the new portal type
        images = self.getFolderContents()
        if not images:
            return
        random_image = choice(images).getObject().tag()
        return random_image

registerType(HomePage, PROJECTNAME)
