===================================================================
Using JSON API to create, retrieve, update and delete WCC Documents
===================================================================

Implementation is using plone.jasonapi.routes

https://github.com/ramonski/plone.jsonapi.routes

Testing can be done using Advanced REST Client for Chrome
https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo

Retrieving WCC Documents
========================

Return a list of all wcc.document added to a site in JSON format
----------------------------------------------------------------

http://10.1.1.4:8080/Plone/@@API/plone/api/1.0/wccdocuments

Return JSON details of specific wcc.document
--------------------------------------------

For each wcc.document in the list above, there is a uid api link, which
will return JSON values for specific document. This uid will also be
used for updating and delete calls.

http://10.1.1.4:8080/Plone/@@API/plone/api/1.0/wccdocuments/ab94a476a46d47869710ee9a61067149

Adding/Creating WCC Document
============================

First we need to know the uid of folder to create the document. Add a
normal Plone folder, can call it Documents

Return a list of all folders and find the uid for Documents folder:

http://10.1.1.4:8080/Plone/@@API/plone/api/1.0/folders

This uid will be used as the reference container when adding
wcc.documents

In Advanced REST Client:

1. URL to post is link to API with create and uid of folder at the end

eg.

http://10.1.1.4:8080/Plone/@@API/plone/api/1.0/wccdocuments/create/409f6df1028c490da8ca20c031f634f0

Method is POST (radio button)

Payload in RAW JSON:

{ "title" : "Example Document",
  "description" : "Description of Document",
  "document_type" : "Advocacy report", //Choice list 
  "effective": "1969-12-31T00:00:00+00:00", //Publishing Date
  "document_owner": "Assembly", //Choice list
  "file" : { "data" : "base64", //base64 encoded file
             "content-type": "mimetype", // application/pdf
             "size" : "bytes", // bytes eg. 1024
           },
 }

Working test example:

{ "title" : "Example Document",
  "description" : "Description of Document",
  "document_type" : "Advocacy report",
  "effective": "1969-12-31T00:00:00+00:00", 
  "document_owner": "Assembly",
}


Known Bugs
==========

- currently doesn't support dexterity behaviours,
  wcc title, description using behaviours.
  https://github.com/ramonski/plone.jsonapi.routes/issues/9

- file doesn't work well with NamedBlobFiles
  https://github.com/ramonski/plone.jsonapi.routes/issues/10

- security is not enabled yet (http auth)

Needs Testing
=============

Language should work when uploading in correct language folder structure
eg. sitename/de/Document as it using uids when referencing parent
folder not tested yet.



