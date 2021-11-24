import requests



url = 'https://api.clashroyale.com/v1/players/%2328PV8Y8QC'



token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjkxNDgzZTJlLTVkOTQtNGQ0Mi1hMzRjLTUwMzcxNmE1NWM5YyIsImlhdCI6MTYzNzc1NzYxOSwic3ViIjoiZGV2ZWxvcGVyLzQzZjAzMjgyLThhMjQtYjg0Mi01ZGVkLTBkMzA5N2RiYTZmMiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxOTMuMTU2LjE1Mi4yNTQiXSwidHlwZSI6ImNsaWVudCJ9XX0.lIHPj586MdbaQn2W7Rrj85MF__sD9QJwCFSfdoO0EjeVN5m7j3h5Wjl2raI-NXTqYlhuh-fiun275s-SIoU5Lg"



headers = {

"authorization" : "Bearer " + token,

"accept": "application/json"

}



x = requests.get(url, data = {}, headers=headers)



print(x.text)