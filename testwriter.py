import os
import uno
from com.sun.star.beans import PropertyValue
def createProp(name, value):
    prop = PropertyValue()
    prop.Name = name
    prop.Value = value
    return prop

localContext = uno.getComponentContext()
resolver = localContext.ServiceManager.createInstanceWithContext(
    "com.sun.star.bridge.UnoUrlResolver", localContext)
ctx = resolver.resolve(
    "uno:socket,host=localhost,port=2002;urp;"
    "StarOffice.ComponentContext")
smgr = ctx.ServiceManager
desktop = smgr.createInstanceWithContext(
    "com.sun.star.frame.Desktop", ctx)
dispatcher = smgr.createInstanceWithContext(
    "com.sun.star.frame.DispatchHelper", ctx)
filepath = "Test.docx"
fileUrl = uno.systemPathToFileUrl(os.path.realpath(filepath))
uno_args = (
    createProp("Minimized", True),
)
document = desktop.loadComponentFromURL(
    fileUrl, "_default", 0, uno_args)
uno_args = (
    createProp("FilterName", "writer_pdf_Export"),
    createProp("Overwrite", True),
)
newpath = filepath[:-len("docx")] + "pdf"
fileUrl = uno.systemPathToFileUrl(os.path.realpath(newpath))
try:
    document.storeToURL(fileUrl, uno_args)  # Export
except ErrorCodeIOException:
    raise
try:
    document.close(True)
except CloseVetoException:
    raise

