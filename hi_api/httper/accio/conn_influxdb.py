from influxdb import InfluxDBClient


class ConnectInfluxDB:
    """
    连接influxdb数据库
    """

    def __init__(self):
        self.influx_client = InfluxDBClient('10.39.32.50', 31273, '', '', 'influxdb')
        self.make = False
        for database in self.influx_client.get_list_database():
            if "influxdb" not in database["name"]:
                self.make = True
            else:
                # 写入前删除数据
                self.influx_client.drop_measurement("locust")
                self.make = False
        if self.make:
            self.influx_client.create_database("influxdb")

    def post_dump_data(self, data, measurement):
        """

        @param data:返回的list
        @param measurement:
        """
        if isinstance(data, list):
            for key in data:
                json_body = [
                    {
                        "measurement": measurement,
                        "fields": key,
                    }
                ]
                self.influx_client.write_points(json_body)

    def post_dump_data(self, data, table):
        """

        @param data:
        @param measurement: 表名
        """
        if isinstance(data, list):
            for key in data:
                json_body = [
                    {
                        "measurement": table,
                        "fields": key,
                    }
                ]
                self.influx_client.write_points(json_body)

# if __name__ == '__main__':
#     pass