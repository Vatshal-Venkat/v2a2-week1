from pyspark.sql import functions as F

train_df = spark.table("workspace.default.silver_cmapss_train")
test_df = spark.table("workspace.default.silver_cmapss_test")
rul_df = spark.table("workspace.default.silver_cmapss_rul")

print("Train rows:", train_df.count())
print("Test rows:", test_df.count())
print("RUL rows:", rul_df.count())

train_df.printSchema()