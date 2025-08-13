data = {
    'stream_group01': {
        'stream_group01-EndpointSet-1 - Flow Group 0001': {
            'Tx Frames': '219874',
            'Rx Frames': '1978866',
            'Loss %': '',
            'Frames Delta': '1758992',
            'Tx Frame Rate': '1000.000',
            'Rx Frame Rate': '9000.000'
        }
    },
    'stream_group02': {
        'stream_group02-EndpointSet-1 - Flow Group 0001': {
            'Tx Frames': '209257',
            'Rx Frames': '1255542',
            'Loss %': '',
            'Frames Delta': '1046285',
            'Tx Frame Rate': '1000.000',
            'Rx Frame Rate': '6000.000'
        }
    }
}

for main_key in data:
    for inner_key in data[main_key]:
        tx_rate = data[main_key][inner_key]['Tx Frame Rate']
        rx_rate = data[main_key][inner_key]['Rx Frame Rate']
        print(f"Transmitted rate is {tx_rate} and Received rate is {rx_rate} on {inner_key} of {main_key}")