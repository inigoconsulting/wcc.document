from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from wcc.document import MessageFactory as _
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from zope.interface import Interface


# Interface class; used to define content-type schema.

class IRelatedLinks(Interface):
    label = schema.TextLine(title=_(u'Title'))
    url = schema.TextLine(title=(u'URL'))
    description = schema.TextLine(title=_(u'Description'))

class IDocument(form.Schema, IImageScaleTraversable):
    """
    Description of the Example Type
    """


    document_owner = schema.Choice(
        title=_(u'Document Owner'),
        vocabulary='wcc.document.document_owner',
        required=False,
    )

    document_type = schema.Choice(
        title=_(u'Document Type'),
        vocabulary='wcc.document.document_type',
        required=False,
    )

    document_status = schema.TextLine(
        title=_(u'Document Status'),
        required=False,
    )

    form.widget(related_links=DataGridFieldFactory)
    related_links = schema.List(
        title=_(u'Related Links'),
        value_type=DictRow(schema=IRelatedLinks),
        required=False,
    )

    file = NamedBlobFile(title=_(u'File'),
        required=False
    )
