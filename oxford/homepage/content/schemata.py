from plone.app.folder.folder import ATFolderSchema

from Products.Archetypes import atapi
from Products.ATContentTypes.configuration import zconf
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.validation import V_REQUIRED

HomePageSchema = ATFolderSchema.copy() + atapi.Schema((

    atapi.TextField(
        name='mainText',
        required=True,
        searchable=True,
        storage=atapi.AnnotationStorage(),
        validators=('isTidyHtml',),
        default_output_type='text/html',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=atapi.RichWidget(
            label='Home Page Main Text',
            label_msgid='KebleContent_label_mainText',
            description='Text that appears in the main content area on the home page',
            description_msgid='KebleContent_help_mainText',
            i18n_domain='KebleContent',
            rows=25,
            allow_file_upload=False,
        ),
    ),

    atapi.ReferenceField(
        name = 'mainTextLink',
        storage = atapi.AnnotationStorage(),
        multiValued=0,
        required=0,
        relationship='HomePageMainTextLink',
        vocabulary_display_path_bound=999999,
        widget=ReferenceBrowserWidget(
            default_search_index = 'Title',
            force_close_on_insert = True, 
            label='Main Text More Info Link',
            label_msgid='KebleContent_label_mainTextLink',
            description='Choose an item to link to underneath the home page main text',
            description_msgid='KebleContent_help_mainTextLink',
        ),
    ),

    atapi.TextField(
        name='featureItem',
        required=True,
        searchable=True,
        storage=atapi.AnnotationStorage(),
        validators=('isTidyHtml',),
        default_output_type='text/html',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=atapi.RichWidget(
            label="Home Page Feature Item Text",
            label_msgid='KebleContent_label_featureItem',
            description='Text that appears in the feature content area on the home page',
            description_msgid='KebleContent_help_featureItem',
            i18n_domain='KebleContent',
            rows=25,
            allow_file_upload=False,
        ),
    ),

    atapi.ReferenceField(
        name = 'featureItemLink',
        storage = atapi.AnnotationStorage(),
        multiValued=0,
        required=0,
        relationship='HomePageFeatureItemLink',
        vocabulary_display_path_bound=999999,
        widget=ReferenceBrowserWidget(
            default_search_index = 'Title',
            force_close_on_insert = True, 
            label='Feature Item More Info Link',
            label_msgid='KebleContent_label_featureItemLink',
            description='Choose an item to link to underneath the home page feature item text',
            description_msgid='KebleContent_help_featureItemLink',
        ),
    ),

    atapi.ImageField(
        name='featureImage',
        languageIndependent=True,
        storage=atapi.AnnotationStorage(),
        swallowResizeExceptions=zconf.swallowImageResizeExceptions.enable,
        pil_quality=zconf.pil_config.quality,
        pil_resize_algo=zconf.pil_config.resize_algo,
        max_size=zconf.ATImage.max_image_dimension,
        sizes= {
            'large'   : (768, 768),
            'preview' : (400, 400),
            'mini'    : (200, 200),
            'thumb'   : (128, 128),
            'tile'    :  (64, 64),
            'icon'    :  (32, 32),
            'listing' :  (16, 16),
        },
        validators=(('isNonEmptyFile', V_REQUIRED),
                    ('checkImageMaxSize', V_REQUIRED)),
        widget=atapi.ImageWidget(
            label='Feature Image',
            label_msgid='KebleContent_label_featureImage',
            description='The feature image that appears in the bottom right corner of the home page. Please upload an image with the following dimensions: width 465px, height: variable.',
            description_msgid='KebleContent_help_featureImage',
            i18n_domain='KebleContent',
            show_content_type = False,
        ),
    ),

))

HomePageSchema['description'].schemata = 'default'
