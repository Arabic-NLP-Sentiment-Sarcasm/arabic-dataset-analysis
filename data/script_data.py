#Source of Data and data descreption
import pandas as pd

print("\nDatasets: ArSarcasm & Arabic Sentiment Tweets")

#ArSarcasm Dataset
df = pd.read_csv("./ArSarcasm_sample.csv")
print("\nArSarcasm Dataset")
print("Task: Arabic sarcasm detection")
print("Source: https://github.com/iabufarha/ArSarcasm")


print("===Sample of Data====")
print(df.head(5))
print("---")
print(df["sarcasm"].value_counts())

print("__________________________")
#Arabic Sentiment Tweets Dataset
df = pd.read_csv(
    "./Sentiment_tweets_sample.txt",
    sep="\t",                
    names=["sentence", "sentiment"], 
    encoding="utf-8"
)
print("\nASTD: Arabic Sentiment Tweets Dataset")

print("Task: Arabic Sentiment Tweets")
print("Source: https://github.com/mahmoudnabil/ASTD")

print("=== Sample of Data ===")
print(df.head(5))
print("---")
print(df["sentiment"].value_counts())

