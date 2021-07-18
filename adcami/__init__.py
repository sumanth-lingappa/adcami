import boto3

CITRIX_AWS_PRODUCTS = {
    'Citrix ADC VPX - Customer Licensed': '63425ded-82f0-4b54-8cdd-6ec8b94bd4f8',
    'Citrix ADC VPX Express - 20 Mbps': 'daf08ece-57d1-4c0a-826a-b8d9449e3930',

    'Citrix ADC VPX Standard Edition - 10 Mbps': '85bb75fd-34a4-4395-bb19-04b71b20cf3e',
    'Citrix ADC VPX Standard Edition - 200 Mbps': 'dd84ff86-4cea-4c4b-8811-726d079324c7',
    'Citrix ADC VPX Standard Edition - 1000 Mbps': '8328715f-8ad4-4121-af6f-77466a6fd325',
    'Citrix ADC VPX Standard Edition - 3Gbps': 'ecde3c83-e3df-4310-931c-be7164f3c504',
    'Citrix ADC VPX Standard Edition - 5Gbps': '5b010f6b-96e4-4f67-bd66-07022dd5dfec',

    'Citrix ADC VPX Premium Edition - 10 Mbps': '0f7c03e9-ccf7-4b68-815f-0696e1e5770f',
    'Citrix ADC VPX Premium Edition - 200 Mbps': 'a277a667-7f08-44c9-9787-59424b2c50fa',
    'Citrix ADC VPX Premium Edition - 1000 Mbps': '198e217b-a775-4322-8bfe-ab1ea7d598f4',
    'Citrix ADC VPX Premium Edition - 3Gbps': '302979c1-fe98-4344-8a11-c26c88f55e01',
    'Citrix ADC VPX Premium Edition - 5Gbps': '755645a9-d61f-4350-bb91-a6ef204debb3',

    'Citrix ADC VPX Advanced Edition - 10 Mbps': '9ff329b9-3273-4ab0-a7db-d1bd714d4bb3',
    'Citrix ADC VPX Advanced Edition - 200 Mbps': 'fff7ca8f-96a9-4ea7-afa1-279b0d23fe3c',
    'Citrix ADC VPX Advanced Edition - 1000 Mbps': '4e123cf4-fe4c-4afd-a11e-b4280a522de5',
    'Citrix ADC VPX Advanced Edition - 3Gbps': 'd0ebd087-5a71-47e4-8eb0-8bbac8593b43',
    'Citrix ADC VPX Advanced Edition - 5Gbps': 'f67de268-1a70-477e-b135-bf789a9e1d76',
}


# List all regions
AWS_REGIONS = [region['RegionName'] for region in boto3.client('ec2').describe_regions()['Regions']]