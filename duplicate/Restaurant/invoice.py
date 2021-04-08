import os

from tempfile import NamedTemporaryFile

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
# choose english as language
os.environ["INVOICE_LANG"] = "en"

client = Client('Table 1') 
provider = Provider('Restaurant', bank_account='2600420569', bank_code='2010')
creator = Creator('Team 5')
invoice = Invoice(client, provider, creator)
invoice_number = 1
data = ((1, 60,"dosa"), (2, 10,"Idly"), (3, 70,"Fried Rice"), (4, 60,"Noodles"))
invoice.currency_locale = 'en_IN'
invoice.currency = "INR"
invoice.number = invoice_number
for item in data:
    invoice.add_item(Item(item[0], item[1], description=item[2], tax=14))

pdf = SimpleInvoice(invoice)
pdf.gen("invoice.pdf", generate_qr_code=True)