from plone.app.folder.folder import ATFolderSchema

from Products.Archetypes.atapi import AnnotationStorage
from Products.Archetypes.atapi import RichWidget
from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import TextField
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

HomePageSchema = ATFolderSchema.copy() + Schema((

    TextField(
        name='text',
        required=True,
        searchable=True,
        storage=AnnotationStorage(),
        validators=('isTidyHtml',),
        default_output_type='text/html',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label='Home Page Main Text',
            label_msgid='oxford.homepage_label_mainText',
            description='Text that appears in the main content area on the home page',
            description_msgid='oxford.homepage_help_mainText',
            i18n_domain='oxford.homepage',
            rows=25,
            allow_file_upload=False,
        ),
    ),

))

finalizeATCTSchema(HomePageSchema)

HomePageSchema['description'].schemata = 'default'
