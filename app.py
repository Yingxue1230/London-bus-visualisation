import os
import pandas as pd
from pyproj import Transformer
import math
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 加载Excel文件
file_path = './data/bus-sequences-20231231.xlsx'
data = pd.read_excel(file_path)

# 选择Run为1的数据并创建副本
data_run_1 = data[data['Run'] == 1].copy()

# Definition of a converter from the UK National Grid Reference System (EPSG:27700) to WGS84 (EPSG:4326)
transformer = Transformer.from_crs("epsg:27700", "epsg:4326")

# Transform the coordinates
latitudes, longitudes = transformer.transform(data_run_1['Location_Easting'].values,
                                              data_run_1['Location_Northing'].values)

# 将转换后的坐标添加到DataFrame中
data_run_1['Latitude'] = latitudes
data_run_1['Longitude'] = longitudes

# 确保按照Route和Sequence进行排序
data_run_1 = data_run_1.sort_values(by=['Route', 'Sequence'])

# 确保Route列是字符串类型
data_run_1['Route'] = data_run_1['Route'].astype(str)

print(data_run_1)

# Loading passenger flow data for 2022-2023
passenger_flow_path = './data/2022-2023-annual-bus-stats.xlsx'
passenger_flow_data = pd.read_excel(passenger_flow_path, sheet_name='2022-2023')

# clean passenger flow data
passenger_flow_data_cleaned = passenger_flow_data.iloc[2:].reset_index(drop=True)
passenger_flow_data_cleaned.columns = ['Route', 'Usage recorded: 2022/23', 'Bus Km Operated: 2022/23']
passenger_flow_data_cleaned = passenger_flow_data_cleaned[['Route', 'Usage recorded: 2022/23']]
passenger_flow_data_cleaned = passenger_flow_data_cleaned.dropna()

# Make sure the Route column is of type String
passenger_flow_data_cleaned['Route'] = passenger_flow_data_cleaned['Route'].astype(str)

# 加载周六的客流量数据
saturday_data_path1 = './data/Saturday/Saturday 1-149.csv'
saturday_data1 = pd.read_csv(saturday_data_path1)

saturday_data_path2 = './data/Saturday/Saturday 150-299.csv'
saturday_data2 = pd.read_csv(saturday_data_path2)

saturday_data_path3 = './data/Saturday/Saturday 300-549.csv'
saturday_data3 = pd.read_csv(saturday_data_path3)

saturday_data_path4 = './data/Saturday/Saturday Letter Prefix Routes.csv'
saturday_data4 = pd.read_csv(saturday_data_path4)

# 加载周日的客流量数据
sunday_data_path1 = './data/Sunday/Sunday 1-149.csv'
sunday_data1 = pd.read_csv(sunday_data_path1)

sunday_data_path2 = './data/Sunday/Sunday 150-299.csv'
sunday_data2 = pd.read_csv(sunday_data_path2)

sunday_data_path3 = './data/Sunday/Sunday 300-549.csv'
sunday_data3 = pd.read_csv(sunday_data_path3)

sunday_data_path4 = './data/Sunday/Sunday Letter Prefix Routes.csv'
sunday_data4 = pd.read_csv(sunday_data_path4)

# 加载工作日的客流量数据
weekday_data_path1 = './data/Weekday/Weekday 1-149.csv'
weekday_data1 = pd.read_csv(weekday_data_path1)

weekday_data_path2 = './data/Weekday/Weekday 150-299.csv'
weekday_data2 = pd.read_csv(weekday_data_path2)

weekday_data_path3 = './data/Weekday/Weekday 300-549.csv'
weekday_data3 = pd.read_csv(weekday_data_path3)

weekday_data_path4 = './data/Weekday/Weekday Letter Prefix Routes.csv'
weekday_data4 = pd.read_csv(weekday_data_path4)

# Merge all datasets
saturday_data = pd.concat([saturday_data1, saturday_data2, saturday_data3, saturday_data4], ignore_index=True)
sunday_data = pd.concat([sunday_data1, sunday_data2, sunday_data3, sunday_data4], ignore_index=True)
weekday_data = pd.concat([weekday_data1, weekday_data2, weekday_data3, weekday_data4], ignore_index=True)

# Make sure the Route column is of type String
saturday_data['ROUTE'] = saturday_data['ROUTE'].astype(str)
sunday_data['ROUTE'] = sunday_data['ROUTE'].astype(str)
weekday_data['ROUTE'] = weekday_data['ROUTE'].astype(str)

#Convert STOPCODE to String
saturday_data['STOPCODE'] = saturday_data['STOPCODE'].astype(str)
sunday_data['STOPCODE'] = sunday_data['STOPCODE'].astype(str)
weekday_data['STOPCODE'] = weekday_data['STOPCODE'].astype(str)

data_run_1['Stop_Code_LBSL'] = data_run_1['Stop_Code_LBSL'].astype(str)

@app.route('/api/routes', methods=['GET'])
def get_routes():
    min_angle = request.args.get('min_angle', type=float, default=0)
    max_angle = request.args.get('max_angle', type=float, default=360)

    filtered_routes = []
    for route_id in data_run_1['Route'].unique():
        route_data = data_run_1[data_run_1['Route'] == route_id]
        start_point = route_data.iloc[0]
        end_point = route_data.iloc[-1]

        delta_lat = end_point['Latitude'] - start_point['Latitude']
        delta_lon = end_point['Longitude'] - start_point['Longitude']

        angle = math.degrees(math.atan2(delta_lon, delta_lat))
        if angle < 0:
            angle += 360

        if min_angle <= max_angle:
            if min_angle <= angle <= max_angle:
                filtered_routes.append(route_id)
        else:
            if angle >= min_angle or angle <= max_angle:
                filtered_routes.append(route_id)

    return jsonify(filtered_routes)


@app.route('/api/routes/<route_id>', methods=['GET'])
def get_route_data(route_id):
    route_data = data_run_1[data_run_1['Route'] == str(route_id)]
    if route_data.empty:
        return jsonify({'error': f'cannot find the route: {route_id}'}), 404

    route_points = route_data[['Latitude', 'Longitude', 'Stop_Name']].to_dict(orient='records')

    start_point = route_data.iloc[0]
    end_point = route_data.iloc[-1]

    delta_lat = end_point['Latitude'] - start_point['Latitude']
    delta_lon = end_point['Longitude'] - start_point['Longitude']

    angle = math.degrees(math.atan2(delta_lon, delta_lat))
    if angle < 0:
        angle += 360

    return jsonify({'route_id': route_id, 'points': route_points, 'angle': angle})


@app.route('/api/passenger_flow', methods=['GET'])
def get_passenger_flow_with_routes():
    min_angle = request.args.get('min_angle', type=float, default=0)
    max_angle = request.args.get('max_angle', type=float, default=360)

    filtered_routes = []
    for route_id in passenger_flow_data_cleaned['Route'].unique():
        if route_id in data_run_1['Route'].unique():
            route_data = data_run_1[data_run_1['Route'] == route_id]
            start_point = route_data.iloc[0]
            end_point = route_data.iloc[-1]

            delta_lat = end_point['Latitude'] - start_point['Latitude']
            delta_lon = end_point['Longitude'] - start_point['Longitude']

            angle = math.degrees(math.atan2(delta_lon, delta_lat))
            if angle < 0:
                angle += 360

            if min_angle <= max_angle:
                if min_angle <= angle <= max_angle:
                    usage_recorded = passenger_flow_data_cleaned[passenger_flow_data_cleaned['Route'] == route_id][
                        'Usage recorded: 2022/23'].values[0]
                    filtered_routes.append({
                        'route_id': route_id,
                        'usage_recorded': usage_recorded,
                        'angle': angle
                    })
            else:
                if angle >= min_angle or angle <= max_angle:
                    usage_recorded = passenger_flow_data_cleaned[passenger_flow_data_cleaned['Route'] == route_id][
                        'Usage recorded: 2022/23'].values[0]
                    filtered_routes.append({
                        'route_id': route_id,
                        'usage_recorded': usage_recorded,
                        'angle': angle
                    })

    return jsonify(filtered_routes)


@app.route('/api/passenger_flow/<route_id>', methods=['GET'])
def get_passenger_flow(route_id):
    route_data = passenger_flow_data_cleaned[passenger_flow_data_cleaned['Route'] == str(route_id)]
    if route_data.empty:
        return jsonify({'error': f'未找到线路 {route_id} 的客流量数据'}), 404

    usage_recorded = route_data['Usage recorded: 2022/23'].values[0]
    return jsonify({'route_id': route_id, 'Usage recorded: 2022/23': usage_recorded})


@app.route('/api/daily_passenger_flow', methods=['GET'])
def get_daily_passenger_flow():
    day_type = request.args.get('day_type', 'weekday')
    min_angle = request.args.get('min_angle', type=float, default=0)
    max_angle = request.args.get('max_angle', type=float, default=360)

    # 根据 day_type 获取相应的客流量数据
    if day_type == 'saturday':
        all_routes = saturday_data.groupby('ROUTE')['Boardings'].sum().reset_index()
    elif day_type == 'sunday':
        all_routes = sunday_data.groupby('ROUTE')['Boardings'].sum().reset_index()
    else:
        all_routes = weekday_data.groupby('ROUTE')['Boardings'].sum().reset_index()

    all_routes.columns = ['route_id', 'total_boardings']
    all_routes['route_id'] = all_routes['route_id'].astype(str).str.strip()

    filtered_routes = []
    for index, row in all_routes.iterrows():
        route_id = row['route_id']

        # 从 data_run_1 中获取该路线的起点和终点数据以计算角度
        route_data = data_run_1[data_run_1['Route'] == route_id]
        if route_data.empty:
            continue

        start_point = route_data.iloc[0]
        end_point = route_data.iloc[-1]

        delta_lat = end_point['Latitude'] - start_point['Latitude']
        delta_lon = end_point['Longitude'] - start_point['Longitude']

        angle = math.degrees(math.atan2(delta_lon, delta_lat))
        if angle < 0:
            angle += 360

        # 角度范围过滤
        if min_angle <= max_angle:
            if min_angle <= angle <= max_angle:
                filtered_routes.append({
                    'route_id': route_id,
                    'total_boardings': row['total_boardings'],
                    'angle': angle
                })
        else:
            if angle >= min_angle or angle <= max_angle:
                filtered_routes.append({
                    'route_id': route_id,
                    'total_boardings': row['total_boardings'],
                    'angle': angle
                })


    return jsonify(filtered_routes)

@app.route('/api/daily_passenger_flow/<route_id>', methods=['GET'])
def get_daily_passenger_flow_by_route(route_id):
    day_type = request.args.get('day_type', 'weekday')
    hour = request.args.get('hour', type=int)
    minute = request.args.get('minute', type=int)

    # 检查是否使用了默认时间
    default_time = False
    if hour is None or minute is None:
        hour = 0
        minute = 0
        default_time = True

    # 生成时间字符串
    start_time = f"{hour}:{minute:02d}:00"

    # 根据 day_type 获取相应的客流量数据
    if day_type == 'saturday':
        route_data = saturday_data[saturday_data['ROUTE'] == str(route_id)]
    elif day_type == 'sunday':
        route_data = sunday_data[sunday_data['ROUTE'] == str(route_id)]
    else:
        route_data = weekday_data[weekday_data['ROUTE'] == str(route_id)]

    if route_data.empty:
        return jsonify({'error': f'未找到线路 {route_id} 的客流量数据'}), 404

    # 按时间点汇总所有站点的上客量
    time_grouped_boardings = route_data.groupby('QHr')['Boardings'].sum()
    print(time_grouped_boardings.to_string())

    # 找到最大和最小上客量的时间点
    max_boardings = time_grouped_boardings.max()
    min_boardings = time_grouped_boardings.min()

    # 获取当前时间点的上客量总和
    total_boardings = time_grouped_boardings.get(start_time, 0)

    return jsonify({
        'route_id': route_id,
        'total_boardings': total_boardings,
        'max_boardings': max_boardings,
        'min_boardings': min_boardings,
        'time': start_time,
        'day_type': day_type,
        'default_time': default_time
    })

@app.route('/api/stop_passenger_flow/<route_id>', methods=['GET'])
def get_stop_passenger_flow(route_id):
    day_type = request.args.get('day_type', 'weekday')
    hour = request.args.get('hour', type=int)
    minute = request.args.get('minute', type=int)

    # check if it uses default time
    default_time = False
    if hour is None or minute is None:
        hour = 0
        minute = 0
        default_time = True

    # Generate Time String
    start_time = f"{hour}:{minute:02d}:00"

    # Get the corresponding dataset according to day_type
    if day_type == 'saturday':
        route_data = saturday_data[saturday_data['ROUTE'] == str(route_id)]
    elif day_type == 'sunday':
        route_data = sunday_data[sunday_data['ROUTE'] == str(route_id)]
    else:
        route_data = weekday_data[weekday_data['ROUTE'] == str(route_id)]

    if route_data.empty:
        return jsonify({'error': f'Cannot find passenger flow data for {route_id} '}), 404

    # Filter out data at a specified point in time
    stop_data_at_time = route_data[route_data['QHr'] == start_time]

    # Get all related stops from data_run_1
    route_stops = data_run_1[data_run_1['Route'] == str(route_id)][['Stop_Code_LBSL', 'Stop_Name', 'Latitude', 'Longitude']]

    # Merge stop_data_at_time with route_stops, based on STOPCODE and Stop_Code_LBSL,
    # to ensure that all sites are retained
    merged_data = pd.merge(route_stops, stop_data_at_time, left_on='Stop_Code_LBSL', right_on='STOPCODE', how='left')

    # Fill missing Boardings and Load data to 0
    merged_data['Boardings'] = merged_data['Boardings'].apply(lambda x: 'NaN' if pd.isna(x) else x)
    merged_data['Load'] = merged_data['Load'].apply(lambda x: 'NaN' if pd.isna(x) else x)

    # Get Boardings, Load and Latitude/Longitude data for each stop
    stops_info = merged_data[['Stop_Name', 'Boardings', 'Load', 'Latitude', 'Longitude']].to_dict(orient='records')

    # # 计算当前线路的最大和最小的 Boardings 和 Load
    # max_boardings = merged_data['Boardings'].max()
    # min_boardings = merged_data['Boardings'].min()
    # max_load = merged_data['Load'].max()
    #min_load = merged_data['Load'].min()

    # Calculate the maximum and minimum Boardings and Load for the line at all points in time
    max_boardings = route_data['Boardings'].max()
    min_boardings = route_data['Boardings'].min()
    max_load = route_data['Load'].max()
    min_load = route_data['Load'].min()

    return jsonify({
        'route_id': route_id,
        'stops': stops_info,
        'max_boardings': max_boardings,
        'min_boardings': min_boardings,
        'max_load': max_load,
        'min_load': min_load,
        'time': start_time,
        'day_type': day_type,
        'default_time': default_time
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
