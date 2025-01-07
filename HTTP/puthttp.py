import requests

# url = 'http://10.128.231.170:5008/ocr/truck'
# data = {
#     "qc_id":"901",
#     "image_path":"",
#     "lane_id":"3",
#     "truck_id":"F9096",
#     "occur_time":"2023-08-11 09:01:14 522"
# }
#
# response = requests.put(url, json=data)
#
# if response.status_code == 200:
#     print('PUT请求成功')
# else:
#     print('PUT请求失败')


url = 'http://10.128.231.170:5008/ocr/container'
data = {
	"qc_id": "901",
	"identified_cntr_list": [
	{
		"reference_id": "02310080010073502001",
		"cntr_no": "ZPMC0000211",
		"cntr_iso": "4500",
		"cntr_size": "40",
		"cntr_type": "40",
		"cntr_door_dir": "HB",
		"list_match_ind": "1",
		"manual_cfm_ind": "1",
		"seal_ind": "Y",
		"dg_codes": "1,2,3,4,5",
		"undg": "1",
		"imdg": "1",
		"image_path": "C:/XXX/YY",
		"check_image_path": "",
		"occur_time": "2023-08-11 08:59:17 522"
	}
  ]
}
# response = requests.put(url, json=data)
#
# if response.status_code == 200:
#     print('PUT请求成功')
# else:
#     print('PUT请求失败')


print(data['qc_id'])
print(data['identified_cntr_list'][0]['reference_id'])
