# TaipeiTransportation
Query estimation arrival time of bus and YouBike availability
查詢新北市公車到站時間以及 YouBike 站點可借可停資訊

GetRouteID.py
輸入公車路線名稱，取得後端的 RouteID。舉例而言，輸入 "57" 路線公車，輸出為 "RouteID: 16468"。

GetRouteAllStops.py
輸入 RouteID，取得所有停靠站的 StopID。舉例而言，輸入 "16468"，輸出為所有停靠站資料。

GetBusETA.py
輸入 RouteID 以及該路線某站的 StopID，取得所有停靠站的預估到站時間。
舉例而言，輸入 "RouteID: 16468 StopID: 167762"，輸出為南山高中站的預估到站時間或開班狀態。
