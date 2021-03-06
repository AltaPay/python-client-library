

#!/usr/bin/python

"""

Klarna test script: capture and update an existing order.

"""

import sys

# Update this with real path and uncomment before use, please
# sys.path.append('/absolute_path_to/python-client-library')


#sdk path check
sdkPathExists = False
for path in sys.path:
    if path.endswith("/python-client-library"):
        sdkPathExists=True
if sdkPathExists is False:
    print "Path to python-client-library does not exist, update your environment variable, or put sys.path.append('/absolute_path_to/python-cliend-library') before including altapay sdk modules"
    sys.exit()

from altapay import API, UpdateOrder, Transaction

api = API(mode='test',account='shop api', password='testpassword',  url='http://gateway.dev.earth.pensio.com/merchant/')


# CAPTURE: ======================================================================

paymentId = "117" # PUT A PAYMENT ID FROM A PREVIOUSLY CREATED ORDER HERE

transaction = Transaction.find(paymentId, api)

capture = transaction.capture()

if capture.error_code == 0 and capture.result == 'Success':
    print ("Successful capture!")
else:
    print "capture Error code: " + str(capture.error_code)
    print "capture Error message: " + capture.error_message
    print "capture Result: " + capture.result
    print "capture Merchant error message: " + capture.merchant_error_message

# UPDATE ORDER: ==================================================================

update_order = UpdateOrder(api = api)

orderLines = [
    {
        'description': 'description 01',
        'itemId': 'id 01',
        'quantity': -1,
        'unitPrice': 1.1
    },
    {
        'description': 'new item',
        'itemId': 'new id',
        'quantity': 1,
        'unitPrice': 1.1
    }
]

update_order.update(paymentId, orderLines)

if update_order.success:
    print ("Successful update order!")
else:
    print "update order Error code: " + str(update_order.error_code)
    print "update order Error message: " + update_order.error_message



