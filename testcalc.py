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
filepath = "Test.xlsx"
fileUrl = uno.systemPathToFileUrl(os.path.realpath(filepath))
uno_args = (
    createProp("Minimized", False),
)
document = desktop.loadComponentFromURL(
    fileUrl, "_default", 0, uno_args)

oSheet = document.CurrentController.getActiveSheet()
oCell = oSheet.getCellRangeByName("A1")
oCell.setValue(123)

uno_args = (
    createProp("FilterName", "calc_pdf_Export"),
    createProp("Overwrite", True),
)
newpath = filepath[:-len("xlsx")] + "pdf"
fileUrl = uno.systemPathToFileUrl(os.path.realpath(newpath))
try:
    document.storeToURL(fileUrl, uno_args)  # Export
except ErrorCodeIOException:
    raise
try:
    document.close(True)
except CloseVetoException:
    raise

