from five import grok
from plone.app.collection.interfaces import ICollection
from Products.ATContentTypes.interfaces import IATFolder

grok.templatedir('templates')


class DocumentListing(grok.View):
    grok.context(IATFolder)
    grok.name('documentlisting')
    grok.require('zope2.View')
    grok.template('documentlisting')


class DocumentListingCollection(DocumentListing):
    grok.context(ICollection)
