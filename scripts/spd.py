from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("SimpleTaxiTripCount") \
        .getOrCreate()

    df = spark.read.csv("hdfs://namenode//spd/input/taxi.csv", header=True, inferSchema=True)

    trip_count = df.count()

    result = spark.createDataFrame([(trip_count,)], ["TotalTrips"])
    result.write.mode("overwrite").csv("hdfs://namenode//spd/output/simple_trip_count")

    spark.stop()

if __name__ == "__main__":
    main()
