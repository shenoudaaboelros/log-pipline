
df = spark.read.text("hdfs://localhost:9000/user/bigdata/flume-logs/")

# عرض البيانات كما هي
df.show(truncate=False)


from pyspark.sql.functions import split

df_split = df.withColumn(
    "date",
    split(df["value"], " ").getItem(0)
).withColumn(
    "time",
    split(df["value"], " ").getItem(1)
).withColumn(
    "level",
    split(df["value"], " ").getItem(2)
)

# عرض البيانات بعد التقسيم
df_split.show()


# ==========================================
#  : عدّ عدد مرات ظهور كل Log Level
# ==========================================

log_counts = df_split.groupBy("level").count()

# عرض عدد مرات ظهور كل مستوى
log_counts.show()


# ==========================================
# 15: استخراج النتائج من Spark
# وتحويلها إلى Lists لاستخدامها في الرسم البياني
# ==========================================

pdf = log_counts.collect()

levels = [row["level"] for row in pdf]
counts = [row["count"] for row in pdf]
